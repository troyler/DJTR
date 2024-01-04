from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse
from django.views import generic

#Each view is responsible for doing one of two things:
# 1.) returning an HttpResponse object containing the content for the requested page
# 2.) or raising an exception such as Http404. The rest is up to you.


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"  #use this to redefine the autodefined variable 'question_list'

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    template_name = "polls/detail.html"
    model = Question


class ResultsView(generic.DetailView):
    template_name = "polls/results.html"
    model = Question


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

"""def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    return render(request, "polls/detail.html", {"question" : question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question" : question})
"""

def vote(request, question_id):   #at detail page, the vote form is submitted as a post request, calling the url with the polls:vote and the question.id and posting the request object containing the choice id
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])   #visit the question entry in the database and use the contents of the input to gather the info
        #from the html page <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    except (KeyError, Choice.DoesNotExist):
        #redisplaying the voting form if an error occurs
        return render(
            request,    
            "poll/detail.html",   
            {"question" : question, 
             "error_message" : "You didn't select a choice.",
             },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #Always return an HttpRespnseRedirect after successfully dealing with post data 
        #prevents data from being posted twice if a user hits the back button 

        return HttpResponseRedirect(reverse("polls:results", args = (question.id,)))
        
