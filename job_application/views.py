from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import ApplicationForm
from .models import JobAppForm
from varname import nameof


def index(request: HttpRequest) -> HttpResponse:
    if request.method == nameof(request.POST):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name: str = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            start_date = form.cleaned_data["start_date"]
            occupation = form.cleaned_data["occupation"]
            JobAppForm.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                start_date=start_date,
                occupation=occupation)
            messages.success(request, "Application submitted successfully!")
    return render(request, "index.html")
