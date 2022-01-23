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
from scripts.add_commands_to_db import *


def create_teams(request):
    if Project.objects.all():
        return render(request, 'automation/teams.html')
    else:
        tim = 'Тим'
        kate = 'Катя'
        second_project = 'week_2'
        first_project = 'week_1'

        create_groups(tim, junior_groups_for_tim_week_2, second_project)
        create_groups(tim, junior_groups_for_tim_week_1, first_project)
        create_groups(kate, junior_groups_for_kate_week_2, second_project)
        create_groups(kate, junior_groups_for_kate_week_1, first_project)
        create_groups(tim, beginner_groups_for_tim_week_2, second_project)
        create_groups(tim, beginner_groups_for_tim_week_1, first_project)
        create_groups(kate, beginner_groups_for_kate_week_2, second_project)
        create_groups(kate, beginner_groups_for_kate_week_1, first_project)

        return render(request, 'automation/teams.html')


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