tim = {
    '18:00 - 18:30': {
        'team': ['Ivan - @Ivan', 'Petia - @Petia', 'Katia - @Katia'],
        'discord': 'https://discord.gg/FwVcqfZU4Q'
    },
    '18:30 - 19:00': {
        'team': ['Vasia - @Vasia', 'Petra - @Petaa', 'Kolia - @Kolia'],
        'discord': 'https://discord.gg/FwVcqfZU4Q'
    },
    '19:00 - 19:30': {
        'team': ['Inga - @Inga', 'Dasha - @Dasha', 'Klava - @Klava'],
        'discord': 'https://discord.gg/FwVcqfZU4Q'
    },
    '19:30 - 20:00': {
        'team': ['Ilia - @Ilia', 'Petia - @Petia', 'Katia - @Katia'],
        'discord': 'https://discord.gg/FwVcqfZU4Q'
    },
}

def get_teams():
    text = ''
    teams = list(tim)
    for team in teams:
        a =[man for man in tim[team]['team']]
        b = [c + '\n' for c in a]
        t = f'{b[0]}{b[1]}{b[2]}'
        massege = f'\nСозвон: {team}\n' \
        '  Команда:\n' \
        f'{t} \n' \
        f'  Дискорд: {tim[team]["discord"]} \n'
        text += massege
    return text









        # [
        #     InlineKeyboardButton("✅  Да", callback_data=str(ONE)),
        #     InlineKeyboardButton("❌  Нет", callback_data=str(THREE)),
        # ]