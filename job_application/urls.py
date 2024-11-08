from django.urls import path
from varname import nameof
from . import views

urlpatterns = [
    path('', views.index, name=nameof(views.index)),
    path(f'{nameof(views.about)}/', views.about, name=nameof(views.about)),
]
