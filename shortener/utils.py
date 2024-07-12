import string
import random
from .models import URLMapping

def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choices(characters, k=length))
        if not URLMapping.objects.filter(short_url=short_url).exists():
            return short_url
