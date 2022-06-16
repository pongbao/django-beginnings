# Http404 was replaced by get_object_or_404()
from django.shortcuts import render, get_object_or_404

# HttpResponse was replaced by HttpResponseRedirect
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# class-based views
# https://docs.djangoproject.com/en/4.0/topics/class-based-views/

# Create your views here.
# def index(request):
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     latest_question_list = Question.objects.all()
#     template = 'polls/index.html'
#     # used in the html
#     context = {'latest_question_list': latest_question_list}
#     return render(request, template, context)
class IndexView(generic.ListView):
    # the ListView generic view uses a default template called <app name>/<model name>_list.html
    template_name = 'polls/index.html'
    # the default variable to return the object list is <lowercaseModel_list>
    context_object_name = 'latest_question_list'

    # determines the list of objects that you want to display
    def get_queryset(self):
        # return the last five published questions
        # lte = less than or equal
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]

# def detail(request, question_id):
    # # try:
    # #     question = Question.objects.get(pk = question_id)
    # # except Question.DoesNotExist:
    # #     raise Http404("Question does not exist!")
    # question = get_object_or_404(Question, pk = question_id)
    # template = 'polls/detail.html'
    # context = {'question': question}
    # return render(request, template, context)

class DetailView(generic.DetailView):
    # a variable is automatically provided by using the lowercase version of the model name
    model = Question
    # by default, the DetailView generic view uses a template called <app name>/<model name>_detail.html
    template_name = 'polls/detail.html'

    # determines the list of objects that you want to display    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte = timezone.now())


# def results(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     template = 'polls/results.html'
#     context = {'question': question}
#     return render(request, template, context)
class ResultsView (generic.DetailView):
    # a variable is automatically provided by using the lowercase version of the model name
    model = Question
    # by default, the DetailView generic view uses a template called <app name>/<model name>_detail.html
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        # request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.
        # request.GET can also be used
        # 'choice' is linked to the html input tag's value attribute
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        template = 'polls/detail.html'
        context = {'question': question, 'error_message': "You didn't select a choice."}
        return render(request, template, context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.
        # helps avoid having to hardcode a URL in the view function
        #  given the name of the view that we want to pass control to and the variable portion of the URL pattern that points to that view, i.e., reversing from polls/results/ back to polls/question_id/
        return HttpResponseRedirect(reverse('polls:results', args = (question_id,)))