from django.shortcuts import redirect, render
from django.utils.timezone import now


from .models import Question, Student, Ranking
from .forms import StudentForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            student = Student.objects.get(email = email)
            
        except Student.DoesNotExist:            
            form = StudentForm(request.POST)
            if form.is_valid():
                student = form.save()
                request.session['student_id'] = student.id
                return redirect('game/1')
            context = {'form': form}
            return render (request, 'quiz/index.html', form)
        else:
            request.session['student_id'] = student.id
            return redirect('game/1')

    return render (request, 'quiz/index.html')

def game(request, id):
    student_id = request.session['student_id']
    try:
        name = Student.objects.get(id = student_id).name
        question = Question.objects.filter(available=True).order_by('id')[id - 1]
    except IndexError:
        return redirect('/ranking')
    else:
        context = {'id' : id, 'question': question, 'name': name}
        if request.method == 'POST':
            userAnswer = int(request.POST['chosen'])
            if userAnswer == question.answer:
                try:
                    first_answer = Ranking.objects.filter(question=question).order_by('created')[0]
                except IndexError:
                    score = 100
                else:
                    timestampFirstAnswer = first_answer.created
                    timeDifference = now() - timestampFirstAnswer
                    score = 100 - int(timeDifference.total_seconds())
                    score = max(score, 1)

                Ranking(student_id=student_id, question=question, score=score).save()


                return redirect (f'game/{id + 1}')
            context['user_answer'] = userAnswer
    
    
    #return HttpResponse("Hello World")
    return render (request, 'quiz/game.html', context)

def ranking(request):
    #return HttpResponse("Hello World")
    return render (request, 'quiz/ranking.html')