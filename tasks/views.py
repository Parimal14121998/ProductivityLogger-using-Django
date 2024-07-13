from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Task, WorkSession
from .forms import TaskForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_start_session(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if task.completed:
        return redirect('task_detail', pk=task.pk)  # Prevent starting new session if task is completed
    if request.method == 'POST':
        # Check if there's an existing active session and end it
        active_sessions = task.work_sessions.filter(end_time__isnull=True)
        if active_sessions.exists():
            for session in active_sessions:
                session.end_time = timezone.now()
                session.save()
        WorkSession.objects.create(task=task, start_time=timezone.now())
        return redirect('task_detail', pk=task.pk)
    return render(request, 'tasks/task_start_session.html', {'task': task})


@login_required
def task_end_session(request, pk, session_pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    session = get_object_or_404(WorkSession, pk=session_pk, task=task)
    if request.method == 'POST':
        session.end_time = timezone.now()
        session.save()
        return redirect('task_detail', pk=task.pk)
    return render(request, 'tasks/task_end_session.html', {'task': task, 'session': session})

@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        # Check if there's an active session and end it
        active_sessions = task.work_sessions.filter(end_time__isnull=True)
        if active_sessions.exists():
            for session in active_sessions:
                session.end_time = timezone.now()
                session.save()
        task.completed = True
        task.end_time = timezone.now()  # Automatically capture the end time
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_complete.html', {'task': task})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

