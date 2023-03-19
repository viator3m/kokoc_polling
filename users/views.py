from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import CreationForm, EditColorForm, EditStyleForm

User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('polls:index')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect(self.success_url)


def users_list(request):
    users = sorted(User.objects.all(), key=lambda user: -user.success_rate)
    template = 'users/users_list.html'
    context = {'users': users}
    return render(request, template, context)


def profile(request):
    template = 'users/profile.html'
    return render(request, template)


def color(request):
    form = EditColorForm()
    context = {'form': form}
    user = User.objects.get(id=request.user.id)
    color = request.POST.get('color')
    template = 'users/color.html'
    if request.POST and color:
        if user.money >= 5:
            user.background_color = color
            user.money -= 5
            user.save()
            return redirect(reverse('users:profile'))
        context = {'error': 'Недостаточно средств для изменения цвета.'}
    return render(request, template, context)


def style(request):
    form = EditStyleForm()
    context = {'form': form}
    user = User.objects.get(id=request.user.id)
    style = request.POST.get('styles')
    template = 'users/style.html'
    if request.POST and style:
        if user.money >= 5:
            user.background_style = style
            user.money -= 5
            user.save()
            return redirect(reverse('users:profile'))
        context = {'error': 'Недостаточно средств для изменения цвета.'}
    return render(request, template, context)
