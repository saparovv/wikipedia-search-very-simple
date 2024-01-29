from django.shortcuts import render
import wikipedia
from django.http import HttpResponse


def home(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        try:
            result = wikipedia.summary(search)
        except:
            return HttpResponse("Wrong input for search")

        return render(request, 'index.html', {'result': result})

    return render(request, 'index.html')