from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Question

from django.template import loader

def add_question(request):
    if request.method == 'GET':
        return render(request, 'polls/add_question.html')
    else:
        qt = request.POST['question']
        dt = request.POST['datenow']
        print(qt,dt)
        qs = Question.objects.create(question_text=qt,pub_date=dt)
        return redirect('questions.html')

def addjs(request):
    if request.method == 'GET':
        return render(request, 'polls/add_js.html')
    else:
        qt = request.POST['fquestion']
        dt = request.POST['fdatenow']
        print(qt,dt)
        qs = Question.objects.create(question_text=qt,pub_date=dt)
        return redirect('questions.html')

def add_smoke(request):
    if request.method == 'GET':
        return render(request, 'polls/motai.html')
    else:
        qt = request.POST['mquestion']
        dt = request.POST['mdatenow']
        print(qt,dt)
        qs = Question.objects.create(question_text=qt,pub_date=dt)
        return redirect('questions.html')


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # templates = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list, }
    return render(request, 'polls/index.html', context)


def questions(request):
    latest_question_list = Question.objects.all()
    print(latest_question_list)
    # templates = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list, }
    return render(request, 'polls/questions.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(results, question_id):
    response = "You are looking at question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
