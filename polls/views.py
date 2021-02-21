from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question, Thought

from .forms import ThoughtsForm

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class ThoughtsView(generic.ListView):
    # model = Thought  # Each generic Detail view needs to know what model it will be acting upon
    template_name = 'polls/thoughts.html'  # reference the html file
    context_object_name = 'latest_thought_list'

    def get_queryset(self):
        """Return the published Thoughts in order of produced. only include last 10"""
        return Thought.objects.filter(date_posted__lte=timezone.now()).order_by('-date_posted')[:10]

        # return Question.objects.order_by('-pub_date')[:5]
    # return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


def thoughtsSubmit(request):
    form = ThoughtsForm(request.POST or None)

    if (request.method == 'POST'):# if its a post request, post request = someone clicking submit; receiving data
        if form.is_valid():
            form.save() #saves to database
            form = ThoughtsForm()  # rerender the form, deleting the text from it.
            context = {
            'form': form
            }
            return HttpResponseRedirect('/polls/thoughts/list')  #when you go to results page, displays result

    else:
        form = ThoughtsForm()
        context = {
        'form': form
        }
        return render(request, "polls/thoughtsSubmission.html", context)
    # render loads template, redners, pass it to httpresponse




'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

    #return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''
