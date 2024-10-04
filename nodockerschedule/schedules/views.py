from django.shortcuts import render, redirect
from .models import Schedule, Event
from .forms import ScheduleForm, EventForm, PasswordForm
from django.contrib import messages

def home_view(request):
    if request.method == 'POST':
        # Обработка создания нового расписания
        schedule_form = ScheduleForm(request.POST)
        if schedule_form.is_valid():
            schedule = schedule_form.save()
            messages.success(request, 'Расписание успешно создано!')
            return redirect('home')
    else:
        schedule_form = ScheduleForm()

    schedules = Schedule.objects.all()
    return render(request, 'schedules/home.html', {
        'schedules': schedules,
        'schedule_form': schedule_form
    })

def create_event_view(request, schedule_id):
    schedule = Schedule.objects.get(id=schedule_id)
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.schedule = schedule
            event.save()
            messages.success(request, 'Событие успешно добавлено!')
            return redirect('home')
    else:
        event_form = EventForm()

    return render(request, 'schedules/create_event.html', {
        'event_form': event_form,
        'schedule': schedule,
    })

def open_schedule(request):
    if request.method == 'POST':
        password_form = PasswordForm(request.POST)
        if password_form.is_valid():
            password = password_form.cleaned_data['password']
            try:
                # Предполагается, что у вас есть поле password в модели Schedule
                schedule = Schedule.objects.get(password=password)
                messages.success(request, 'Расписание успешно открыто!')
                events = Event.objects.filter(schedule=schedule)
                return render(request, 'schedules/open_schedule.html', {
                    'schedule': schedule,
                    'events': events,
                    'password_form': password_form
                })
            except Schedule.DoesNotExist:
                messages.error(request, 'Неверный пароль! Попробуйте снова.')
    else:
        password_form = PasswordForm()

    return render(request, 'schedules/open_schedule.html', {
        'password_form': password_form,
    })

def some_view(request):
    if request.method == 'POST':
        password_form = PasswordForm(request.POST)
        if password_form.is_valid():
            # Обработка пароля
            messages.success(request, 'Пароль принят!')
            return redirect('home')
    else:
        password_form = PasswordForm()

    return render(request, 'your_template.html', {
        'password_form': password_form,
    })