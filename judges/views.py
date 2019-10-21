from django.shortcuts import render, get_object_or_404
from .models import Problem,Example
from . import views
# Create your views here.


def judge(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    examples = get_object_or_404(Example, problem=problem_id)
    context = {
        'problem':problem,
        'examples':examples,
    }
    problem_test = {
        'id': 1,
        'subject': '외국어',
        'category': '문법',
        'q_date': '2009년 06월',
        'q_org': '평가원',
        'q_num': 21,
        'correct_rate': 0.75,
        'header': '(A), (B), (C)의 각 네모 안에서 어법에 맞는 표현으로 가장 적절한 것은?',
        'content': 'The most useful thing I brought out of my childhood was confidence in reading. Not long ago, I went on a weekend self-exploratory workshop, in the hope of getting a clue about how to live. One of the exercises we were given (A) to make a list of the ten most important events of our lives. Number one was: \"I was born,\" and you could put (B) you liked after that. Without even thinking about it, my hand wrote at number two: \"I learned to read.\" wouldn\'nt be a sequence that occurs to many people, I imagine. But I knew what I meant to say. Being born was something (C) to me, but my own life began when I first made out the meaning of a sentence.',
        'examples': {
            '1': '(A): was , (B): however , (C): done',
            '2': '(A): was , (B): whaterver , (C): done',
            '3': '(A): was , (B): whatever , (C): doing',
            '4': '(A): were , (B): however , (C): doing',
            '5': '(A): were , (B): however , (C): done',
        },
    }
    return render(request, 'judges/judge.html', context)


def result(request, problem_id):
    return render(request, 'judges/result.html', )