from django.shortcuts import render,redirect
from .forms import *
from django.contrib  import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .models import *
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
def home(request):
    return render(request,'pages/index.html')

def register(request):
    if request.method == 'POST':
        form = mailerRegister(request.POST)
        if form.is_valid() == True:
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = form.save(commit = True)
            #user = form.save()  try this later!!!
            return redirect('/')
    else:
        form = mailerRegister()
    return render(request, 'pages/register.html',{'form':form})

    

@login_required(login_url='/')
def showGoals(request,id):
    goals = dailyGoal.objects.select_related().filter(mailer_id = id)
    totalMonth =  0
    tatalYear = 0
    globtotal = 0
    for goal in goals:
        globtotal = globtotal + goal.goal
        if str(goal.Year) == str(datetime.now().strftime("%Y")):
            tatalYear = tatalYear + goal.goal                     
        if str(goal.Month) == str(datetime.now().strftime("%B")) and str(goal.Year) == str(datetime.now().strftime("%Y")):
            totalMonth = totalMonth + goal.goal
        
    return render(request,'pages/goals.html',{'goalsList':goals,'total':totalMonth,'tatalYear':tatalYear,'globtotal':globtotal})


@login_required(login_url='/login')
def addGoal(request,id):
    form = Goal()
    if request.method == "POST":
        form = Goal(request.POST)
        newGoal = dailyGoal.objects.create(goal = request.POST["goal"],dayOfMonth = request.POST["dayOfMonth"],Day = request.POST["Day"],Month = request.POST["Month"],Year = request.POST["Year"],mailer_id = id)
        newGoal.save()
        return redirect('/')
    return render(request,'pages/addgoals.html',{'addgoals':form,'dayofMonth': datetime.now().strftime("%b"),'day': datetime.now().strftime("%A"),'month': datetime.now().strftime("%B"),'year': datetime.now().strftime("%Y")})



@login_required(login_url='/login')
def editGoal(request,id):
    existantGoal = dailyGoal.objects.get(id=id)
    form = Goal(request.POST or None , instance=existantGoal)    
    if form.is_valid():        
        form.save()
        return redirect('/')
    return render(request,'pages/editgoal.html',{'editgoal':existantGoal,'form':form})

@login_required(login_url='/')
def deleteGoal(request,id):   
        dailyGoal.objects.filter(id= id).delete()
        return redirect('/')