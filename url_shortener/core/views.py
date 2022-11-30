from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone

from rest_framework import status, generics, response

from .serializers import ShortenURLSerializer
from .models import ShortenedURL
from .settings import TTL

class ShortenURLView(generics.CreateAPIView):
    serializer_class = ShortenURLSerializer
    


class RedirectView(generics.RetrieveAPIView):
    
    def retrieve(self, request, *args, **kwargs):
        slug = kwargs.get('slug', None)
        
        try:
            shortened_url = ShortenedURL.objects.get(slug=slug)
            
            if (timezone.now() - shortened_url.created_at).days > TTL:
                return response.Response(status=status.HTTP_404_NOT_FOUND)
            
            return HttpResponseRedirect(shortened_url.url)
        
        except Exception:
            return response.Response(status=status.HTTP_404_NOT_FOUND)