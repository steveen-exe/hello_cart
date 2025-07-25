from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer 
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages


def show_account(request):
    context = {}
    if request.method == 'POST':
        if 'register' in request.POST:
            context['register'] = True
            # Registration form processing
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')

            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken. Try a different one.")
            else:
                try:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email
                    )

                    Customer.objects.create(
                        user=user,
                        phone=phone,
                        address=address
                    )

                    messages.success(request, "User registration completed ")
                except Exception as e:
                    messages.error(request, f"Registration failed: {str(e)}")

        elif 'login' in request.POST:
            context['register'] = False
            # Login form processing
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('product_index')
            
            else:
                messages.error(request, "Invalid credentials. Please try again.")

    # Render page for GET or anvalid credentials. Please try again.fter form submission
    return render(request, 'account.html' ,context)
 

def sign_out(request):
    logout(request)
    return redirect('account')  # or wherever your login page is