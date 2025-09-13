from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from question.models import Question


@login_required(login_url='/auth/login')
def index(request):
    questions = Question.objects.prefetch_related('variants').all().order_by('-created_at')
    return render(request, 'index.html', {'questions': questions})