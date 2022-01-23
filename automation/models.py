from django.db import models


class Project(models.Model):
    name = models.CharField(
        'название',
        max_length=50
    )
    start_date = models.DateField(
        'дата начала проекта',
        db_index=True,
    )
    end_date = models.DateField(
        'дата окончания проекта',
        db_index=True,
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f'{self.name} [{self.start_date} - {self.end_date}]'


class Category(models.Model):
    name = models.CharField(
        'название',
        max_length=50
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    far_east = models.BooleanField('Дальний восток', default=False)
    category = models.ForeignKey(
        Category,
        verbose_name='категория',
        related_name='students',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    email = models.EmailField('Email')
    tg_username = models.CharField('Телеграм ник', max_length=255)
    tg_chat_id = models.CharField('Телеграм chat_id', max_length=255)
    discord_username = models.CharField('Discort ник', max_length=255, default='example#1234')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'





class ProjectManager(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=50
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=50
    )
    start_at = models.CharField(
        verbose_name='Созвон ОТ',
        max_length=50,
        blank=True,
    )
    end_at = models.CharField(
        verbose_name='Созвон ДО',
        max_length=50,
        blank=True,
    )

    class Meta:
        verbose_name = 'ПМ'
        verbose_name_plural = 'ПМы'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Command(models.Model):
    project = models.ForeignKey(
        Project,
        verbose_name='проект',
        related_name='commands',
        null=True,
        on_delete=models.SET_NULL,
    )
    command_name = models.CharField(
        'Название команды',
        max_length=50,
        blank=True,
        null=True,
    )
    meeting_time = models.CharField(
        verbose_name='Время созвона',
        max_length=50,
        blank=True,
    )

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return f'{self.command_name} {self.project.name}'


class ParticipantProject(models.Model):
    project_manager = models.ForeignKey(
        ProjectManager,
        verbose_name='ПМ',
        related_name='participants_project',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    student = models.ForeignKey(
        Student,
        verbose_name='ученик',
        related_name='participants_project',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    command = models.ForeignKey(
        Command,
        verbose_name='команда',
        related_name='participants_project',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    meeting_time = models.CharField(
        verbose_name='Время созвона',
        max_length=50,
        blank=True,
    )

    class Meta:
        verbose_name = 'Участник проекта'
        verbose_name_plural = 'Участники проекта'

    def __str__(self):
        return f'{self.student}'
