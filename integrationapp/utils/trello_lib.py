import json

import requests
from environs import Env


env = Env()
env.read_env()

TRELLO_API_KEY = env.str('TRELLO_API_KEY')
TRELLO_SERVER_TOKEN = env.str('TRELLO_SERVER_TOKEN')

BOARD_BG_COLOURS = ['blue', 'orange', 'green', 'red', 'purple', 'pink', 'lime', 'sky', 'grey']


def create_workspace(workspace_name):
    url = "https://api.trello.com/1/organizations"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_SERVER_TOKEN,
        'displayName': workspace_name
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=query
    )

    return response.json()


def create_board(organization_id, board_name, bg_color):
    url = "https://api.trello.com/1/boards/"

    query = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_SERVER_TOKEN,
        'idOrganization': organization_id,
        'name': board_name,
        'prefs_background': bg_color
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )

    return response.json()


def invite_member_to_board_via_email(board_id, member_email):
    url = f"https://api.trello.com/1/boards/{board_id}/members"

    query = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_SERVER_TOKEN,
        'email': member_email
    }

    response = requests.request(
        "PUT",
        url,
        params=query
    )

    return response


def main():
    workspace_name = 'Проект "{project_name}" [{project_start_date}-{project_end_date}]'
    workspace = create_workspace(workspace_name)
    print(workspace)

    board_name = '[{время начала созвона}] {Имена участников через запятую}'
    board = create_board(workspace['id'], 'test_board', BOARD_BG_COLOURS[5])
    print(board)
    print(board['shortUrl'])

    board_id = board['id']
    member_email = 'test@test.com'
    member_invitation = invite_member_to_board_via_email(board_id, member_email)
    print(member_invitation)
    print(member_invitation.text)
    print(member_invitation.url)


if __name__ == '__main__':
    main()
