import openai
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

openai.api_key = "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"

def chatview(request):    

    if not request.user.is_authenticated:
        messages.info(request, "You need to log in to access the Chatbot!")
        return redirect('login')

    if request.method == "POST":
        user_input = request.POST.get('user_input', '')

        #check if the users inpuit exists
        if user_input:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful financial advice chatbot."},
                    {"role": "user", "content": user_input}
                ]
            )

            #extract the bot response
            bot_response = response['choices'][0]['message']['content'].strip()
            #return response as JSOn
            return JsonResponse({'response': bot_response}) 
    
    #render the chat template for get requests
    return render(request, 'chatbot/chat.html')

def feedbackview(request):
    if request.method == 'POST':
        # Handle POST request
        # Process user input, save feedback, etc.
        return HttpResponse("Feedback sent!")
    else:
        return render(request, 'chatbot/feedback.html')
    
def aboutview(request):
    return render(request, 'chatbot/about.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()  # Instantiate a blank form
    
    return render(request, 'chatbot/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Attempting login for: {username}")  # Debug log

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(f"User '{username}' authenticated successfully.")  # Debug log
            login(request, user)
            return redirect('chatbot')  # Redirect to chatbot after successful login
        else:
            print("Authentication failed.")  # Debug log
            messages.error(request, 'Invalid username or password.')
            return render(request, 'chatbot/login.html', {'error': 'Invalid credentials'})

    return render(request, 'chatbot/login.html')







