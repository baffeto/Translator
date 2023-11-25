from django.shortcuts import render
from googletrans import Translator

def index(request):
    if request.method == 'POST':
        lang = request.POST.get('lang', None)
        txt = request.POST.get('txt', None)
        
        translator = Translator()
        translate = translator.translate(txt, dest=lang)
        
        return render(request, 'main/index.html', {'result': translate.text})
    
    return render(request, 'main/index.html')
