from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def home_view(request):
    context = { 
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
