from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings

from django.contrib import messages
from django.urls import reverse_lazy
from .models import Results, CSV
from django.http import HttpResponse
from django.utils.dateparse import parse_date

import csv


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('results')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('results')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'base/login.html', context)


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
        context['count'] = context['results'].filter(verdict='Wrong').count()


        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['results'] = context['results'].filter(search_query__icontains = search_input)

        context['search_input'] = search_input
        return context


class UploadTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'base/upload_objects.html'

@login_required
def csv_upload_view( request):

    if request.method == 'POST':
        csv_file_name = request.FILES.get('file').name
        csv_file = request.FILES.get('file')
        obj, created = CSV.objects.get_or_create(file_name=csv_file_name)

        if created:
            obj.csv_file = csv_file
            obj.save()
            with open(obj.csv_file.path, 'r') as f:
                reader = csv.reader(f)
                reader.__next__()
                for row in reader:
                    data = "".join(row)
                    data = data.split(';')
                    data.pop()
        
                    contributor_id = data[0]
                    search_query = data[5]
                    link_query = data[6]
                    user_answer = data[7]
                    correct_answer = data[8]
                    verdict = data[9]

                    try:
                        result_obj = Results.objects.get(name__iexact=search_query)
                    except Results.DoesNotExist:
                        result_obj = None

                    if result_obj is not None:
                        result_obj = Results.objects.get_or_create(contributor_id= contributor_id, search_query= search_query, link_query= link_query,
                        user_answer=user_answer, correct_answer=correct_answer, verdict=verdict) 
                        
                        result_obj.add(result_obj)
                        result_obj.save()
                return JsonResponse({'ex': False})
        else:
            return JsonResponse({'ex': True})

    return HttpResponse()