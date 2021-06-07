from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

def polls_page(request):
    poll = Poll.objects.all()
    return render(request,'polls_page.html',{'poll':poll})


def questions_page(request,poll_id):
    form = AnswerForm()
    poll = Poll.objects.get(id=poll_id)
    question = poll.quest.all()
    if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                user_answer = form.cleaned_data.get('user_answer')
                for quest in question:
                    print(quest.answer,user_answer)
                    if quest.answer == user_answer:
                        return HttpResponse('Correct!')
                    elif quest.answer != user_answer:
                        return HttpResponse('Not correct')

    return render(request,'questions_page.html',{'form':form, 'question':question})