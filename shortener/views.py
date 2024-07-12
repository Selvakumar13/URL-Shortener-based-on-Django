from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import URLMapping
from .utils import generate_short_url  # Import the function

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        custom_domain = request.POST.get('custom_domain', '')

        short_url = generate_short_url()
        if custom_domain:
            full_short_url = f"{custom_domain}/{short_url}"
        else:
            full_short_url = request.build_absolute_uri('/') + short_url

        url_mapping = URLMapping.objects.create(original_url=original_url, short_url=short_url, full_short_url=full_short_url)
        return render(request, 'shortener/result.html', {'short_url': full_short_url})

    return render(request, 'shortener/index.html')

def redirect_to_original(request, short_url):
    try:
        # Extract the short URL part if it contains a custom domain
        short_url = short_url.split('/')[-1]
        url_mapping = URLMapping.objects.get(short_url=short_url)
        return redirect(url_mapping.original_url)
    except URLMapping.DoesNotExist:
        return render(request, 'shortener/not_found.html')
