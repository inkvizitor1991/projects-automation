import time

import discord
from environs import Env


env = Env()
env.read_env()

DISCORD_BOT_TOKEN = env.str('DISCORD_BOT_TOKEN')


class DiscordClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.guild_id = None
        self.private_category_id = None
        self.text_channel_id = None
        self.guild_member = None

    # Функция отрабатывает все вызовы и в конце закрывает соединение с Discord сервером
    async def on_ready(self):
        print('Logged on as', self.user)

        # Создание сервера
        guild_name = 'Девман. Проект {project_name}. {project_month}'
        guild = await self.create_guild(guild_name)
        self.guild_id = guild.id
        print(guild)

        # Получаем объект созданного сервера для дальнейшей работы
        guild = self.get_guild(self.guild_id)

        # Создание приватной категории
        private_category_name = 'Команда 1'
        private_category = await guild.create_category(
            private_category_name,
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True)
            }
        )
        self.private_category_id = private_category.id
        print(private_category)

        # Создание текстового канала на сервере
        text_channel_name = 'чат-команды'
        text_channel = await guild.create_text_channel(text_channel_name, category=private_category)
        self.text_channel_id = text_channel.id
        print(text_channel)

        # Создание приглашения на текстовый канал
        text_channel_invite = await text_channel.create_invite()
        self.text_channel_invite = text_channel_invite
        print(text_channel_invite)

        # Время чтобы перейти по сгенерированной ссылке, чтобы добавился доступ в приватный чат
        time.sleep(30)
        await guild.fetch_members(limit=150).flatten()

        # Получение участника по нику
        member_nickname = 'RimProg#2389'
        guild_member = guild.get_member_named(member_nickname)
        self.guild_member = guild_member
        print(guild_member)

        # Установка прав пользования секретным чатом для участника сервера
        permissions = await private_category.set_permissions(
            guild_member,
            read_messages=True,
            send_messages=True
        )

        # Закрываем клиент соединение
        await self.close()


def main():
    # Устанавливаем клиенту Discord все доступные права и запускаем
    intents = discord.Intents.all()
    client = DiscordClient(intents=intents)
    client.run(DISCORD_BOT_TOKEN)


if __name__ == '__main__':
    main()
