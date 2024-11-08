from django.contrib import messages
from django.core.mail import EmailMessage
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
            message_body = f"""\
Dear {first_name} {last_name},

Your application for the position has been received.
You submitted the following details:
First name: {first_name}
Last name: {last_name}
Email: {email}
Possible start date: {start_date}
Occupation: {occupation}
We will get back to you soon.

Thank you!
"""
            email_message = EmailMessage(subject="Job Application Confirmation",
                                         body=message_body,
                                         to=[email])
            email_message.send()
            messages.success(request, "Application submitted successfully!")
    return render(request, "index.html")
