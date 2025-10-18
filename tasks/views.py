from django.shortcuts import get_object_or_404, render, redirect
from .models import Task


# List all tasks
def task_list(request):
    tasks = Task.objects.filter(is_completed=False).order_by("-created_at")
    return render(request, "tasks/list.html", {"tasks": tasks})


# Add a new task
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        if title:  # title is required
            Task.objects.create(title=title, description=description)
        return redirect("tasks:task_list")
    return render(request, "tasks/add.html")


# Mark a task as complete
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect("tasks:task_list")
