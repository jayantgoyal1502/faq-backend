from django.shortcuts import render
from rest_framework import generics
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all().order_by('-created_at')
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        """Pass request context to serializer to fetch translations"""
        return {'request': self.request}

class FAQDetailView(generics.RetrieveAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class FAQListView(APIView):
    """Fetch all FAQs with caching"""
    def get(self, request):
        lang = request.GET.get("lang", "en")
        cache_key = f"faqs_{lang}"
        cached_faqs = cache.get(cache_key)

        if cached_faqs:
            return Response(cached_faqs)  # Return cached data

        faqs = FAQ.objects.all().order_by("-created_at")
        serializer = FAQSerializer(faqs, many=True, context={"request": request})
        cache.set(cache_key, serializer.data, timeout=300)  # Store in cache for 5 min

        return Response(serializer.data)