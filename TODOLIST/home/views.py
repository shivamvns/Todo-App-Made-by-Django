from django.shortcuts import render, HttpResponse
from home.models import Tasks
# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Tasks(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}
    return render(request, 'index.html', context)

def tasks(request):
    allTasks = Tasks.objects.all()
    context = {'tasks': allTasks}
    print(allTasks)
    return render(request, 'tasks.html', context)