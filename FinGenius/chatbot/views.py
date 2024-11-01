import openai
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

openai.api_key = "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"

def chatview(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input', '')

        #check if the users input exists
        if user_input:
            #call Chatgpt openai 
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages = [
                    {"role": "system", "content": "You are a helpful financial advice chatbot."},
                    {"role": "user", "content": user_input}
                ]
            )

            #extract the bot's response
            bot_response = response['choices'][0]['message']['content'].strip()

            #return response as JSON
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


