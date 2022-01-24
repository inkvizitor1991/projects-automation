from django.db import models
from automation.models import Project


class Trello(models.Model):
    project = models.OneToOneField(
        Project,
        verbose_name='проект',
        related_name='trello',
        null=True,
        on_delete=models.CASCADE,
    )
    workspace_id = models.CharField(
        'workspace id',
        max_length=50
    )
    url = models.URLField(
        'trello workspace url'
    )

    class Meta:
        verbose_name = 'Trello workspace'
        verbose_name_plural = 'Trello  workspaces'

    def __str__(self):
        return f'{self.project.name} [{self.project.start_date} - {self.project.end_date}]'


class TrelloBoard(models.Model):
    trello = models.ForeignKey(
        Trello,
        verbose_name='trello',
        related_name='boards',
        null=True,
        on_delete=models.CASCADE,
    )
    board_id = models.CharField(
        'board id',
        max_length=50
    )
    command = models.OneToOneField(
        'automation.Command',
        verbose_name='команда',
        related_name='trello_board',
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Trello board'
        verbose_name_plural = 'Trello boards'

    def __str__(self):
        return f'{self.trello.project.name} \
                 [{self.trello.project.start_date} - {self.trello.project.end_date}] \
                 {self.command.command_name}'


class Discord(models.Model):
    project = models.OneToOneField(
        Project,
        verbose_name='проект',
        related_name='discord',
        null=True,
        on_delete=models.SET_NULL,
    )
    url = models.URLField(
        'discord server url'
    )

    class Meta:
        verbose_name = 'Discord'
        verbose_name_plural = 'Discords'

    def __str__(self):
        return f'{self.project.name} [{self.project.start_date} - {self.project.end_date}]'
