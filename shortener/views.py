from django.shortcuts import render, redirect
from .models import URLMapping
from random import choices
from string import ascii_letters, digits
from django.http import Http404
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'shortener/home.html')

def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        
        # Generate a random short code
        length = 4
        chars = ascii_letters + digits
        while True:
            short_code = ''.join(choices(chars, k=length))
            # Check if code already exists
            if not URLMapping.objects.filter(short_url=short_code).exists():
                break
        
        # Create and save URL mapping with the generated short code
        url = URLMapping(original_url=long_url, short_url=short_code)
        url.save()
        
        returnD = {
            "id": str(url.id),
            "url": url.original_url,
            "short_url": url.short_url,
            "created_at": url.created_at.isoformat(),
        }
        return render(request, 'shortener/home.html', returnD)
    return render(request, 'shortener/home.html')


def redirect_url(request, short_code):
    try:
        url = URLMapping.objects.get(short_url=short_code)
        url.access_count += 1
        url.save()
        return redirect(url.original_url)
    except URLMapping.DoesNotExist:
        raise Http404("Short URL not found")

def delete_url(request, short_code):
    try:
        url = URLMapping.objects.get(short_url=short_code)
        url.delete()
        messages.success(request, f'URL with short code "{short_code}" has been successfully deleted.')
        return redirect('home')
    except URLMapping.DoesNotExist:
        raise Http404("Short URL not found")
