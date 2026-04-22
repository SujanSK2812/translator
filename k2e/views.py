from django.shortcuts import render
# Create your views here.
from googletrans import Translator

def home(request):
    translated_text = ""

    if request.method == "POST":
        english_text = request.POST.get("text")
        translator = Translator()
        result = translator.translate(english_text, src='en', dest='kn')
        translated_text = result.text

    return render(request, "home.html", {"translated_text": translated_text})
