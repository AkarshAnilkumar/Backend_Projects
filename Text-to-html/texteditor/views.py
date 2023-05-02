from django.shortcuts import render
from .models import Editor
from .forms import Editorform


def index(request):
    form = Editorform()
    return render(request, 'index.html', {'form': form})
