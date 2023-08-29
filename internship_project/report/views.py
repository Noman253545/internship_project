from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django import forms

from .models import Intern
from django.http import HttpResponseRedirect
from .forms import WorkSubmissionForm

# Create your views here.
def home_page(request):
    # return HttpResponse("<b>Hello Interns</b>")
    return render(request, 'home.html') # templates auto search

def work_submission(request):
    print('in work submission function')
    if request.method == 'POST':
        form = WorkSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')  # Redirect after successful submission
    else:
        form = WorkSubmissionForm()
    interns = Intern.objects.all()
    print('interns list ', interns)
    return render(request, 'home.html', {'form': form, 'interns': interns})

def success(request):
    return render(request, 'success.html')