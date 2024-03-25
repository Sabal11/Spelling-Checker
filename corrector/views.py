from django.shortcuts import render
from .spelling_checker import spell_checker_function

def spell_check(request):
    if request.method == 'POST':
        text_to_check = request.POST.get('text_to_check', '')
        corrected_text = spell_checker_function(text_to_check)

        return render(request, 'result.html', {'text_to_check': text_to_check, 'corrected_text': corrected_text})

    return render(request, 'home.html')



    