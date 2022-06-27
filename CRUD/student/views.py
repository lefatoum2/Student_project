from django.shortcuts import render, redirect
from .forms import StudForm
from .models import Stud
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='acces')
def create_stud(request):
    form = StudForm()
    if request.method == "POST":
        form = StudForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Created successful!")
                return redirect('/show_stud')
            except:
                message = "Something we are wrong!"
                form = StudForm()
            return render(request, 'create.html', {'message': message, 'form': form})
    else:
        form = StudForm()
    return render(request, 'create.html', {'form': form})


@login_required(login_url='acces')
def show_stud(request):
    stud = Stud.objects.order_by('-id');
    return render(request, 'index.html', {'stud': stud})


@login_required(login_url='acces')
def edit_stud(request, id):
    stud = Stud.objects.get(id=id)
    return render(request, 'edit.html', {'stud': stud})


@login_required(login_url='acces')
def update_stud(request, id):
    stud = Stud.objects.get(id=id)
    if request.method == "POST":
        form = StudForm(request.POST, request.FILES, instance=stud)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful!')
            return redirect("/show_stud")
        message = 'Something we are wrong!'
        return render(request, 'edit.html', {'message': message, 'stud': form})
    else:
        form = Stud.objects.get(id=id)
        stud = StudForm(instance=form)
        content = {'stud': stud, 'id': id}
        return render(request, 'edit.html', content)


@login_required(login_url='acces')
def delete_stud(request, id):
    stud = Stud.objects.get(id=id)
    stud.delete()
    messages.success(request, 'Deleted successful!')
    return redirect("/show_stud")
