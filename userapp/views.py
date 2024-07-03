from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import render, redirect, get_object_or_404
from .form import InfoForm,PortfolioForm,UserRegistrationForm,UserLoginForm,ProjectForm
from .models import Info,Portfolio,Project
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


from django.core.paginator import Paginator, EmptyPage

# Create your views here.
def list(request,profile_id=None):
    if profile_id:
        det=Info.objects.get(id=profile_id)
    else:
        det = Info.objects.all()
    # paginator=Paginator(det,1)  # to set how many objects need to be set on a page
    # page_number=request.GET.get('page') # retrieves page number from parameter 'page'
    # try:
    #     page=paginator.get_page(page_number)  # attempts to retrieve the requested page from the Paginator.
    #
    # except EmptyPage:                 # If the requested page number is invalid (e.g., beyond the total number of pages), an EmptyPage exception is caught.
    #     page=paginator.page(page_number.num_pages)        #In case of an EmptyPage exception, it retrieves the last available page instead (assuming page_number is an integer or convertible to one).
    return render(request,'list.html',{'det':det})

def Createbook(request):
    info=Info.objects.all()
    if request.method=='POST':
        form=InfoForm(request.POST,files=request.FILES)
        print(form)
        if form.is_valid():
            new_info=form.save()
            return redirect('list_id',profile_id=new_info.id)
    else:
        form=InfoForm()

    return render(request,'info.html',{'form':form,'info':info})

def UpdateProfile(request,profile_id):
    det = get_object_or_404(Info,id=profile_id)
    if request.method=='POST':
        form = InfoForm(request.POST,request.FILES,instance=det)
        if form.is_valid():
            new_info=form.save()

            return redirect('list_id',profile_id=new_info.id)
    else:
        form=InfoForm(instance=det)

    return render(request,'update.html',{'form':form})

def UpdatePortfolio(request,profile_id):
    det1 = get_object_or_404(Portfolio,id=profile_id)
    if request.method=='POST':
        form_b = PortfolioForm(request.POST,request.FILES,instance=det1,prefix='form_b')
        if form_b.is_valid():
            new_info=form_b.save()

            return redirect('index_id',profile_id=new_info.id)
    else:
        form_b=PortfolioForm(instance=det1,prefix='form_b')

    return render(request,'update_port.html',{'form_b':form_b})

def UpdateProject(request,profile_id):
    det1 = get_object_or_404(Project,id=profile_id)
    if request.method=='POST':
        form_c = ProjectForm(request.POST,request.FILES,instance=det1,prefix='form_c')
        if form_c.is_valid():
            new_info=form_c.save()

            return redirect('indexi_id',profile_id=new_info.id)
    else:
        form_c=ProjectForm(instance=det1,prefix='form_c')

    return render(request,'update_project.html',{'form_c':form_c})

def DeleteProfile(request,profile_id):
    det=Info.objects.get(id=profile_id)
    if request.method=='POST':
        det.delete()
        return redirect('create')

    return render(request,'delete.html',{'profile_id':profile_id})

def CreatePortfolio(request):
    port=Portfolio.objects.all()
    if request.method=='POST':
        form=PortfolioForm(request.POST,files=request.FILES)
        print(form)
        if form.is_valid():
            new_info=form.save()
            return redirect('index_id',profile_id=new_info.id)
    else:
        form=PortfolioForm()

    return render(request,'portfolio.html',{'form':form,'port':port})

def Index(request,profile_id=None):
    if profile_id:
        det1 = get_object_or_404(Portfolio, id=profile_id)
    else:
        det1=Portfolio.objects.all()
    return render(request, 'index2.html', {'det1': det1})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('login')  # Redirect to a success page.
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('create')  # Redirect to a success page.
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('create')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    auth.logout(request)
    return redirect('login')

# views.py
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'info.html')

def IndexI(request, profile_id=None):
    if profile_id:
        try:
            det1 = Project.objects.get(id=profile_id)
        except Project.DoesNotExist:
            det1 = None
    else:
        det1 = None
    return render(request, 'index.html', {'det1': det1})

def CreateProject(request):
    det1=Project.objects.all()
    if request.method=='POST':
        form_3=ProjectForm(request.POST,files=request.FILES)
        print(form_3)
        if form_3.is_valid():
            new_info=form_3.save()
            return redirect('indexi_id',profile_id=new_info.id)
    else:
        form_3=ProjectForm()

    return render(request,'project.html',{'form_3':form_3,'det1':det1})

from userapp.models import Info # replace with your actual model
def dlt(request):
    if request.method=='POST':
        Portfolio.objects.all().delete()
        return redirect('create')

    return render(request,'delete.html')

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import UserIDForm
from .models import UserID

@login_required
def add_user_id(request):
    if request.method == 'POST':
        form = UserIDForm(request.POST)
        if form.is_valid():
            user_id = form.save(commit=False)
            user_id.user = request.user
            user_id.save()
            return redirect('some-view-name')  # Redirect to a success page or another view
    else:
        form = UserIDForm()
    return render(request, 'add_user_id.html', {'form': form})
