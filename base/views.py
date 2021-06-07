from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Results


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('results')


class SignupPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('results')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignupPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('results')
        return super(SignupPage, self).get(*args, **kwargs)


class ResultsList(LoginRequiredMixin, ListView):
    model = Results   
    context_object_name = 'results'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results'] = context['results'].filter(user=self.request.user)
        context['count'] = context['results'].filter(verdict=0).count()


        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['results'] = context['results'].filter(title__icontains = search_input)

        context['search_input'] = search_input
        return context