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


    async def on_ready(self):
        print('Logged on as', self.user)

        # Создание сервера
        guild_name = 'Девман. Проект {project_name}. {project_month}'
        guild = client.create_guild(guild_name)
        self.guild_id = guild.id

        # Создание приватной категории
        private_category_name = 'Команда 1'
        private_category = await guild.create_category(
            'test_private_category2',
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True)
            }
        )
        self.private_category_id = private_category.id

        # Создание текстового канала на сервере
        text_channel_name = 'чат-команды'
        text_channel = await guild.create_text_channel(text_channel_name, category=category)
        self.text_channel_id = text_channel.id

        # Получение участника по нику
        guild_member = guild.get_member_named('RimProg#2389')
        self.guild_member = guild_member

        # Создание приглашения на текстовый канал
        text_channel_invite = await text_channel.create_invite()
        self.text_channel_invite = text_channel_invite

        # Установка прав пользования секретным чатом для участника сервера
        permissions = await category.set_permissions(
            guild_member,
            read_messages=True,
            send_messages=False
        )


def main():
    # Устанавливаем клиенту Discord все доступные права и запускаем
    intents = discord.Intents.all()
    client = DiscordClient(intents=intents)
    client.run(DISCORD_BOT_TOKEN)


if __name__ == '__main__':
    main()
