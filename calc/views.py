from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def add(request):
    num1 = request.POST["num1"]
    num2 = request.POST["num2"]
    res = int(num1) + int(num2)

    return render(request, 'results.html', {'results':res})