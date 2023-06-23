from django.shortcuts import render
from django import forms

# Create your views here.
def fun(request):
    return render(request,"base.html")


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from transportapp.models import Question, Answer, Like

from django.shortcuts import render, redirect

from django.contrib.auth import login



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            
            return redirect('post_question')
        
        
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


     



class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields="__all__"

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields="__all__"
@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = QuestionForm()
    return render(request, 'post_question.html', {'form': form})

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answer_set.all()
    return render(request, 'question_detail.html', {'question': question, 'answers': answers})

@login_required
def post_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'post_answer.html', {'form': form, 'question': question})

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    user = request.user

   
    like, created = Like.objects.get_or_create(user=user, answer=answer)

    if not created:
       
        like.delete()

    return redirect('question_detail', question_id=answer.question.id)




from django.contrib.auth.decorators import login_required

@login_required
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})

@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answer_set.all()
    return render(request, 'question_detail.html', {'question': question, 'answers': answers})
