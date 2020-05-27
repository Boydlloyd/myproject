from django.shortcuts import render,redirect,get_object_or_404
from .forms import ComputerForm, ComputerSearchForm,OperatingSystemForm
from .models import Computer,ComputerHistory
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
import csv

success_message='Record Successfully Saved...'
# Create your views here.

def home(request):
    title='Home Page'
    body='This is Home Page'
    context={
        "title":title,
        "body":body,
    }
    return render(request, "home.html",context)

def createComputer(request):
    title='Add Computer'
    form=ComputerForm(request.POST or None)
    if form.is_valid():
        #computer = form.save(commit=False)
        form.save()
        #form.save_m2m()
        messages.success(request, success_message)
        return redirect('/computerlist')
    context={
        "title":title,
        "from":form,
    }
    return render(request,"createcomputer.html",context)


def computerList(request):
    title='List of Computers'
    computers=Computer.objects.all()
    form=ComputerSearchForm(request.POST or None)
    context={
        'title':title,
        'computers':computers,
        'form':form,
    }
    if request.method=='POST':
        computers = Computer.objects.all().filter(computer_name__icontains=form['computer_name'].value())
        context = {
        'title': title,
        'computers': computers,
        'form': form,
        }
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Computer_List.csv"'
            writer = csv.writer(response)
            writer.writerow(['COMPUTER NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
            computer = computers
            for row in computer:
                writer.writerow([row.computer_name, row.IP_address, row.MAC_address, row.operating_system, row.users_name,row.location, row.purchase_date, row.timestamp])
            return response
    return render(request, "computerlist1.html", context)


def updateComputer(request, id=None):
    computer = get_object_or_404(Computer, id=id)
    form = ComputerForm(request.POST or None, instance=computer)  
    form.fields['computer_name'].disabled = True
    # OR #form.fields['computer_name'].widget.attrs['readonly'] = True
    #form.fields['users_name'].widget.attrs['hidden'] = True

    if form.is_valid():
        #computer = form.save(commit=False)
        computer.save()
        #form.save_m2m()
        messages.success(request, success_message)
        return redirect('/computerlist')
    context = {
     "title": 'Edit ' + str(computer.computer_name),
     "instance": computer,
     "form": form,
    }
    return render(request, "updatecomputer.html", context)


def deleteComputer(request, id=None):
    computerList=get_object_or_404(Computer,id=id)
    computerList.delete()
    return redirect('/computerlist')


def computerHistory(request):
    title = 'Computer History'
    computers = ComputerHistory.objects.all()
    form = ComputerSearchForm(request.POST or None)
    context = {
       "title": title,
       "computers": computers,
    }
    if request.method=='POST':
        computers = ComputerHistory.objects.all().filter(computer_name__icontains=form['computer_name'].value(),users_name__icontains=form['users_name'].value())
        context = {
        'title': title,
        'computers': computers,
        'form': form,
        }
    return render(request, "computerhistory.html",context)


def computerHistory1(request):
    title = 'Computer History'
    computers = ComputerHistory.objects.all()
    form = ComputerSearchForm(request.POST or None)
    context = {
       "title": title,
       "computers": computers,
    }

    paginator = Paginator(computers, 2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'computerhistory.html', {'page_obj': page_obj})


def settings(request):
    title = 'Add Operating system'
    form = OperatingSystemForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, success_message)
        return redirect('/computerlist')
    context = {
        "title": title,
        "form": form,
        }
    return render(request, "settings.html",context)



