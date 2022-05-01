from django.shortcuts import render
from . models import Question, Choice
# Create your views here.
def index(request):
    return render(request,"index.html")

def vote(request):
    ques=Question.objects.all()
    ch=Choice.objects.all()
    return render(request,"vote.html",{"question":ques,"choice":ch})

def display(request):
    ch=request.GET["your_choice"]
    print(ch)
    x=Choice.objects.get(choice_text=ch)
    x.vote+=1
    x.save()
    return render(request,"display.html",{"question":x.choice_text,"result":x.vote})