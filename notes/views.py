# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Note
from django.contrib.auth.decorators import login_required
from . import forms

def my_note(request, slug):
    notes = Note.obNects.all().order_by('-date')
    return render(request,'notes/notes.html', { 'notes': notes })

def note_page(request, slug):
    note = Note.objects.get(slug=slug)
    return render(request,'notes/note_page.html', { 'note': note })

@login_required(login_url="/users/login/")
def note_new(request):
    if request.method == 'POST':
        form = forms.NoteUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            newNote = form.save(commit=False)
            newNote.author = request.user
            newNote.save()
            return redirect('users:notes')
    else:
        form = forms.NoteUpdateForm()
    return render(request, 'notes/note_new.html', { 'form': form })