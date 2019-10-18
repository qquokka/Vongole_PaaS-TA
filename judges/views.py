from django.shortcuts import render, get_object_or_404
from .models import Problem
# Create your views here.

def judge(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    return render(request, 'judges/judge.html', {'problem':problem})