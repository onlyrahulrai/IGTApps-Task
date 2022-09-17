from django.shortcuts import render,redirect,get_object_or_404
from base.forms import IdentityCardForm, RegisterForm, UpdateProfileImageForm
from django.contrib import messages 
from django.contrib.auth import login
from base.models import Profile
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required(login_url='register')
def identity(request):
    if request.user.profile.front_img and request.user.profile.back_img:
        return redirect("recognize")

    form = IdentityCardForm()
    if request.method == "POST":
        profile = get_object_or_404(Profile,user=request.user)
        form = IdentityCardForm(request.POST,request.FILES,instance=profile)

        if form.is_valid():
            form.save()

            messages.success(request,f"{request.user.name} your Identity Card uploded successfully!")

            return redirect('/recognize')

    context = {"form":form}
    return render(request,'identity.html',context)

@login_required(login_url='register')
def recognize(request):
    profile = request.user.profile
    if not profile.front_img and not profile.back_img:
        return redirect('identity')

    if profile.front_img and profile.back_img and profile.self_image:
        return redirect("details")
        
    form = UpdateProfileImageForm()
    if request.method == "POST":

        profile = get_object_or_404(Profile,user=request.user)

        form = UpdateProfileImageForm(request.POST,request.FILES,instance=profile)

        if form.is_valid():
            form.save()

            messages.success(request,f"{request.user.name} your profile updated successfully!")

            return redirect('details')
        
    context = {
        "form":form
    }
    return render(request,'recognize.html',context)

@login_required(login_url='register')
def details(request):
    profile = request.user.profile
    if not profile.front_img  and not profile.back_img:
        return redirect('identity')
    elif not profile.self_image:
        return redirect('recognize')
    return render(request,'details.html')

def register(request):
    form = RegisterForm()

    if request.user.is_authenticated:
        return redirect('identity')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            if user is not None:
                name = form.cleaned_data.get('name')

                messages.success(request,f'Account was created for {name}')

                login(request,user)

                return redirect('/')
    context = {
        "form":form
    }
    return render(request,"register.html",context)