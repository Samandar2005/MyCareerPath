from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Count
from .models import DailyPlan

def dashboard(request):
    plans = DailyPlan.objects.all()
    
    # Statistika
    total_days = plans.count()
    completed_days = plans.filter(status='completed').count()
    in_progress_days = plans.filter(status='in_progress').count()
    total_hours = plans.aggregate(Sum('time_spent'))['time_spent__sum'] or 0
    
    progress_percent = 0
    if total_days > 0:
        progress_percent = int((completed_days / total_days) * 100)

    context = {
        'plans': plans,
        'total_days': total_days,
        'completed_days': completed_days,
        'in_progress_days': in_progress_days,
        'progress_percent': progress_percent,
        'total_hours': round(total_hours, 1)
    }
    return render(request, 'dashboard.html', context)

def day_detail(request, day_id):
    day = get_object_or_404(DailyPlan, day_number=day_id)
    
    if request.method == "POST":
        day.status = request.POST.get('status')
        day.notes = request.POST.get('notes')
        day.time_spent = request.POST.get('time_spent')
        day.save()
        return redirect('dashboard')
        
    return render(request, 'day_detail.html', {'day': day})