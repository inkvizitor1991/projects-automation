from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .form import RegisterUserForm, LoginUserForm
from .models import *
from .utils import DataMixin
from integrationapp.views import *
from scripts import form_groups
from scripts.form_groups import form_gorups
    # from automation.models import Project, Category, Student, ProjectManager, \
    #     Command, ParticipantProject


def create_teams(request):
    # from form_groups import form_gorups
    # from automation.models import Project, Category, Student, ProjectManager, \
    #     Command, ParticipantProject

    students = Student.objects.filter(category__name='Джуниор')
    students_new = Student.objects.filter(category__name='Новичек')
    students_new_3 = Student.objects.filter(category__name='Новичек +3')

    students_junior = []
    new_students = []

    for student in students:
        students_junior.append(student.id)

    for student in students_new:
        new_students.append(student.id)

    for student in students_new_3:
        new_students.append(student.id)

    def create_groups(pm_name, groups, project_name):
        for commands in groups:
            project = Project.objects.filter(name=project_name).first()
            command = Command(command_name=commands, project=project)
            command.save()
            for students in groups[commands]:
                pm = ProjectManager.objects.filter(first_name=pm_name).first()
                student = Student.objects.filter(id=students).first()
                participants = ParticipantProject.objects.create(
                    student=student,
                    project_manager=pm,
                    command=command
                )

    junior = form_gorups(students_junior)
    new_students = form_gorups(new_students)
    print(junior)
    print(new_students)
    junior_groups_for_tim_week_2 = junior['groups_for_tim_week_2']
    junior_groups_for_tim_week_1 = junior['groups_for_tim_week_1']
    junior_groups_for_kate_week_2 = junior['groups_for_kate_week_2']
    junior_groups_for_kate_week_1 = junior['groups_for_kate_week_1']

    beginner_groups_for_tim_week_2 = new_students['groups_for_tim_week_2']
    beginner_groups_for_tim_week_1 = new_students['groups_for_tim_week_1']
    beginner_groups_for_kate_week_2 = new_students['groups_for_kate_week_2']
    beginner_groups_for_kate_week_1 = new_students['groups_for_kate_week_1']

    tim = 'Тим'
    kate = 'Катя'
    second_project = 'week_2'
    first_project = 'week_1'

    created_groups_junior_for_tim_week_2 = create_groups(tim,
                                                         junior_groups_for_tim_week_2,
                                                         second_project)
    created_groups_junior_for_tim_week_1 = create_groups(tim,
                                                         junior_groups_for_tim_week_1,
                                                         first_project)
    created_groups_junior_for_kate_week_2 = create_groups(kate,
                                                          junior_groups_for_kate_week_2,
                                                          second_project)
    created_groups_junior_for_kate_week_1 = create_groups(kate,
                                                          junior_groups_for_kate_week_1,
                                                          first_project)

    created_groups_beginner_for_tim_week_2 = create_groups(tim,
                                                           beginner_groups_for_tim_week_2,
                                                           second_project)
    created_groups_beginner_for_tim_week_1 = create_groups(tim,
                                                           beginner_groups_for_tim_week_1,
                                                           first_project)
    created_groups_beginner_for_kate_week_2 = create_groups(kate,
                                                            beginner_groups_for_kate_week_2,
                                                            second_project)
    created_groups_beginner_for_kate_week_1 = create_groups(kate,
                                                            beginner_groups_for_kate_week_1,
                                                            first_project)


    project = Project.objects.last()
    projects = []
    pm = ProjectManager.objects.all()[0]
    print(pm)
    # for pm in pms:
    #     participants = ParticipantProject.objects.filter(
    #         project_manager__first_name=pm)

    participants = ParticipantProject.objects.filter(
        project_manager__first_name=pm)
    for participant in participants:
        #print(participant.command)
        if participant.command:
            projects.append(participant.command.command_name)
            print(participant)
    unique_projects = list(set(projects))
    print(f'{unique_projects}')


    context = {
        # 'title': 'Inicio',
        # 'menu': menu,
    }
    return render(request, 'automation/teams.html', context=context)


class Home(DataMixin, ListView):
    model = Student
    template_name = 'automation/index.html'
    context_object_name = 'users'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'automation/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'automation/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))
    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def page_no_found(request, exception):
    return HttpResponseNotFound('Upssss....')