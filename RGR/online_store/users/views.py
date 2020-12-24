from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

class UserRegistrationView(CreateView):
    template_name = 'users/user/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('catalog:product_list')                  #URL действие после удачной регистрации

    def form_valid(self, form):
        result = super(UserRegistrationView, self).form_valid(form)     #super - вызываем метод класса-родителя, form_valid - выполняет проверку всех полей формы
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])                   #проверяет идентификационные данные и возвращает объект User, если они корректны
        login(self.request, user)                                       #сохраняет текущего пользователя в сессии
        return result