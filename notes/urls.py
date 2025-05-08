from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.my_note, name="my-note"),
    path('new-note/', views.note_new, name="new-note"),
    path('<slug:slug>', views.note_page, name="page"),
]