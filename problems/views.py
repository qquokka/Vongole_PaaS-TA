from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'problems/index.html')


def subject(request):
    return render(request, 'problems/subject.html')


def category(request):
    print(request.GET)
    subject = request.GET.get('subject')
    context = {
        'subject': subject,
    }
    return render(request, 'problems/category.html', context)

