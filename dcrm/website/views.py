from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddRecordForm
from .models import Record

def home(request):
    records = Record.objects.all()
    return render(request, 'home.html', {'records': records})

def customer_record(request, pk):
    record = Record.objects.get(id=pk)
    return render(request, 'record.html', {'record': record})

def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added successfully.")
                return redirect('home')
        return render(request, 'add-record.html', {'form': form})
    else:
        messages.success("You must be logged In...")
        return redirect(request, 'home')
    
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=record)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record edited successfully.")
                return redirect('home')
        return render(request, 'update-record.html', {'form': form})
    else:
        messages.success("You must be logged In...")
        return redirect(request, 'home')