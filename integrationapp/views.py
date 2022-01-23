from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.conf import settings

from integrationapp.models import Trello
from integrationapp.models import TrelloBoard
from automation.models import Project
from automation.models import ProjectManager

import requests
from environs import Env

from .utils.trello_lib import create_workspace
from .utils.trello_lib import create_board
from .utils.trello_lib import invite_member_to_board_via_email
from .utils.trello_lib import BOARD_BG_COLOURS



TRELLO_API_KEY = settings.TRELLO_API_KEY
TRELLO_SERVER_TOKEN = settings.TRELLO_SERVER_TOKEN


def create_trello(project):
    workspace_name = f'Проект "{project.name}" [{project.start_date} - {project.end_date}]'
    workspace = create_workspace(workspace_name)

    trello = Trello.objects.create(
        project=project,
        workspace_id=workspace['id'],
        url=workspace['url']
    )

    return trello


def create_trello_boards(trello):
    project_managers = ProjectManager.objects.all()
    for index, project_manager in enumerate(project_managers):
        project_manager.board_bg_colour = BOARD_BG_COLOURS[index]

    trello_boards = []

    commands = trello.project.commands.all()
    for command in commands:
        command_members = command.participants_project.all()
        command_member = command_members.first()

        command_members_names = [member.student.first_name for member in command_members]
        formatted_command_members_names = ', '.join(command_members_names)
        command_project_manager = command_member.project_manager
        meeting_time = command_member.meeting_time

        board_name = f'[{meeting_time}] {formatted_command_members_names}'
        board_bg_colour = list(
            filter(
                lambda pm: pm.id == command_project_manager.id,
                project_managers
            )
        )[0].board_bg_colour
        board = create_board(trello.workspace_id, board_name, board_bg_colour)

        trello_boards.append(board)

        TrelloBoard.objects.create(
            trello=trello,
            board_id=board['id'],
            command=command
        )

    return trello_boards


def invite_project_members_to_trello_boards_via_emails(trello):
    boards = trello.boards.all()

    invitations = []
    for board in boards:
        command_members = board.command.participants_project.all()

        command_invitations = []
        for member in command_members:
            member_email = member.student.email
            member_invitation = invite_member_to_board_via_email(
                board.board_id,
                member_email
            )

            command_invitations.append(member_invitation)

        invitations.append(command_invitations)

    return invitations


def handle_trello_create_request(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    is_invite_command_members = bool(request.GET.get('send_email'))

    try:
        trello = Trello.objects.get(project=project)

        if is_invite_command_members:
            invite_project_members_to_trello_boards_via_emails(trello)

        return render(request, template_name='trello.html', context={
            'created_now': False,
            'trello': trello,
            'sent_email': is_invite_command_members,
        })

    except Trello.DoesNotExist as err:
        trello = create_trello(project)
        trello_boards = create_trello_boards(trello)
        print(trello_boards)

        if is_invite_command_members:
            invite_project_members_to_trello_boards_via_emails(trello)

        return render(request, template_name='trello.html', context={
            'created_now': True,
            'trello': trello,
            'sent_email': is_invite_command_members,
        })


def create_discord(request):
    print('Discord created')

    return render(request, template_name='discord.html', context={
        # 'discord': discord,
    })
