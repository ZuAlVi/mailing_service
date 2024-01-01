from django.conf import settings
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, View, UpdateView
from django.utils.crypto import get_random_string

from users.forms import UserRegisterForm, UserForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:code')
    template_name = 'users/register.html'

    def form_valid(self, form):
        code = get_random_string(12)
        new_user = form.save()
        new_user.code = code
        new_user.save()
        send_mail(
            recipient_list=[new_user.email],
            message=f'Для подтверждения email введите код {new_user.code}',
            subject='Регистрация на сервисе',
            from_email=settings.DEFAULT_FROM_EMAIL,
        )

        client_group = Group.objects.get(name='Клиент')
        client_group.user_set.add(new_user)

        return super().form_valid(form)


class CodeView(View):
    model = User
    template_name = 'users/code.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        code = request.POST.get('code')
        user = User.objects.filter(code=code).first()

        if user is not None and user.code == code:
            user.is_active = True
            user.save()
            return redirect(reverse('users:login'))


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user
