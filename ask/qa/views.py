from django.http import HttpResponse, HttpResponseRedirect, Http404

# for test with inittest25 import start
from django.contrib.auth.models import User
from django.db.models import Max
from models import Question
from models import Answer
from forms import AskForm
from forms import AnswerForm
from forms import LoginForm
from forms import SignupForm
from django.contrib.auth import login, logout
# import finish

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator


def test(request, *args, **kwargs):
    return HttpResponse('OK')


@require_GET
def inittest25(request, *args, **kwargs):
    # copy from test site
    res = Question.objects.all().aggregate(Max('rating'))
    max_rating = res['rating__max'] or 0
    user, _ = User.objects.get_or_create(username='test', password='test')
    for i in range(30):
        question = Question.objects.create(title='question ' + str(i), text='text ' + str(i),
                                           author=user, rating=max_rating + i)
    question = Question.objects.create(title='question last', text='text', author=user)
    question, _ = Question.objects.get_or_create(pk=3141592, title='question about pi',
                                                 text='what is the last digit?', author=user)
    question.answer_set.all().delete()
    for i in range(10):
        answer = Answer.objects.create(text='answer ' + str(i), question=question, author=user)

    return HttpResponse("Init for test done.")


@require_GET
def index(request, *args, **kwargs):

    try:
        page = int(request.GET.get("page"))
    except (ValueError, TypeError):
        page = 1

    questions = Question.objects.new()
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(
        request, 'list.html',
        {'title': 'Lastest question', 'paginator': paginator,
         'questions': page.object_list, 'page': page,
         'user': request.user, 'session': request.session})


@require_GET
def popular(request, *args, **kwargs):

    try:
        page = int(request.GET.get("page"))
    except (ValueError, TypeError):
        page = 1

    questions = Question.objects.popular()

    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(
        request, 'list.html',
        {'title': 'Popular question', 'paginator': paginator,
         'questions': page.object_list, 'page': page,
         'user': request.user, 'session': request.session})


def question(request, pk_question):
    gs = get_object_or_404(Question, id=pk_question)
    answers = gs.answer_set.all()
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            _ = form.save()
            redirect_url = gs.get_absolute_url()
            return HttpResponseRedirect(redirect_url)
    else:
        form = AnswerForm(initial={'question': str(pk_question)})

    return render(
        request, 'question.html',
        {'question': gs, 'form': form, 'answers': answers,
         'user': request.user, 'session': request.session})


def ask(request):
    if request.method == "POST":
        try:
            form = AskForm(request.POST)
            if form.is_valid():
                post = form.save()
                redirect_url = post.get_absolute_url()
                print 'redirect to: ', redirect_url
                return HttpResponseRedirect(redirect_url)
        except Exception as error_message:
            print error_message
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


def question_detail(request, pk_question):
    qs = get_object_or_404(Question, id=pk_question)
    answers = qs.answer_set.all()
    form = AnswerForm(initial={'question': str(pk_question)})
    return render(request, 'question.html', {
        'question': qs, 'answers': answers,
        'form': form, 'user': request.user, 'session': request.session
    })


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    form = SignupForm()
    return render(request, 'signup.html', {'form': form,
                                           'user': request.user,
                                           'session': request.session})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    form = LoginForm()
    return render(request, 'login.html', {'form': form,
                                          'user': request.user,
                                          'session': request.session})

@require_GET
def user_logout(request):
    logout(request)
    redirect_url = request.GET.get('continue', '/')
    return HttpResponseRedirect(redirect_url)
