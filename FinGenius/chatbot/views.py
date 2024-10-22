from django.shortcuts import render
from django.http import HttpResponse

def chatview(request):
    if request.method == 'POST':
        # Handle POST request
        # Process user input, get response from chatbot, etc.
        return HttpResponse("Chat response")
    else:
        # Handle GET request
        return render(request, 'chatbot/chat.html')


