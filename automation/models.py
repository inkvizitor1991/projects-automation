from django.conf import settings
from django.db import models




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
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
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

    def __str__(self):
        return f"{self.first_name} {self.last_name} Категория:{self.category.name} Дальний восток-{self.far_east}"

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    # telegram_user_name = models.CharField('Телеграм ник', max_length=255)
    # telegram_chat_id = models.CharField('Телеграм chat_id', max_length=255)
    # devman_user_name = models.CharField('Devman ник', max_length=255)



class ProjectManager(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=50
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=50
    )
    start_at = models.DateTimeField(
        verbose_name='Созвон ОТ',
        db_index=True,
    )
    end_at = models.DateTimeField(
        verbose_name='Созвон ДО',
        db_index=True,
    )

    class Meta:
        verbose_name = 'ПМ'
        verbose_name_plural = 'ПМы'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Command(models.Model):
    command_name = models.CharField(
        'Название команды',
        max_length=50,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return f'{self.command_name}'  # со временем тут будет дата созвона


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
    meeting_time = models.DateTimeField(
        verbose_name='Время созвона',
        db_index=True,
    )

    class Meta:
        verbose_name = 'Участник проекта'
        verbose_name_plural = 'Участники проекта'

    def __str__(self):
        return f'{self.student}'
