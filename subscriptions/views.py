from django.shortcuts import render

def service_view(request):
    """Displays an overview of what ArtBiz offers"""
    return render(request, 'services.html')
    
   