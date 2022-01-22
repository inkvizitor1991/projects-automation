from django.db import models


class Trello(models.Model):
    project = models.OneToOneField(
        'automation.Project',
        verbose_name='проект',
        related_name='trello',
        null=True,
        on_delete=models.SET_NULL,
    )
    url = models.URLField(
        'trello workspace url'
    )

    class Meta:
        verbose_name = 'Trello'
        verbose_name_plural = 'Trelloes'

    def __str__(self):
        return f'{self.project.name} [{self.project.start_date} - {self.project.end_date}]'


class Discord(models.Model):
    project = models.OneToOneField(
        'automation.Project',
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
