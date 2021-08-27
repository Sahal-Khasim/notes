from app.models import Notes
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render

# Create your views here.


def notes(request):
    if request.method == 'POST':
        event = request.POST['event']
        notes = request.POST['notes']

        note = Notes(
            event=event,
            notes=notes,

        )
        note.save()

    
    note = Notes.objects.all()
    data = {
        'note' : note,
    }
    return render(request, 'notes/home.html', data)