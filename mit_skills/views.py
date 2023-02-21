from django.shortcuts import redirect
from . import views

def index_redirect(request):
    return redirect('/skillsapp/')