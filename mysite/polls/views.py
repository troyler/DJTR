from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.http import Http404

#Each view is responsible for doing one of two things:
# 1.) returning an HttpResponse object containing the content for the requested page
# 2.) or raising an exception such as Http404. The rest is up to you.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

#t’s a very common idiom to load a template, fill a context
# and return an HttpResponse object with the result of the 
# rendered template. Django provides a shortcut. Here’s the full 
# index() view, rewritten using the render functionality:





#from django.shortcuts import render
#def index(request):
#    latest_question_list = Question.objects.order_by("-pub_date")[:5]
#    context = {"latest_question_list": latest_question_list}
#    return render(request, "polls/index.html", context)
# Render takes the object as its first argument, a template name 
# as the second argument, and a dictionary as its third (optional) arg
#returns an HTTpRespnse of the givene template rendered with the content

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    return render(request, "polls/detail.html", {"question" : question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)