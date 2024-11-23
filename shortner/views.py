"""
This module defines views and utility functions for a URL shortener application.
It provides functionality to shorten URLs, retrieve original URLs, update, delete, and track URL statistics.
"""

import json
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortenedURL
from .serializers import ShortURLSerializer
from .utils import generate_short_code
from django.shortcuts import render


class ShortenURLView(APIView):
    """
    API view to handle URL shortening, retrieval, updating, and deletion.
    """

    def post(self, request):
        """Create a new shortened URL."""
        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(shortCode=generate_short_code())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, short_code):
        """Retrieve the original URL from the short code."""
        short_url = get_object_or_404(ShortenedURL, shortCode=short_code)
        short_url.accessCount += 1  # Increment access count
        short_url.save()
        return Response(ShortURLSerializer(short_url).data)

    def put(self, request, short_code):
        """Update an existing shortened URL."""
        short_url = get_object_or_404(ShortenedURL, shortCode=short_code)
        serializer = ShortURLSerializer(short_url, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, short_code):
        """Delete a shortened URL."""
        short_url = get_object_or_404(ShortenedURL, shortCode=short_code)
        short_url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShortURLStatsView(APIView):
    """
    API view to retrieve statistics for a shortened URL.
    """

    def get(self, request, short_code):
        """Retrieve statistics for the given short code."""
        short_url = get_object_or_404(ShortenedURL, shortCode=short_code)
        return Response(ShortURLSerializer(short_url).data)

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def create_short_url(request):
    """
    Function-based view to handle URL shortening through a POST request.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            url = data.get('url')
            if not url:
                return JsonResponse({'error': 'URL is required'}, status=400)

            # Generate the short code
            short_code = generate_short_code()

            # Create the ShortenedURL object
            short_url = ShortenedURL.objects.create(url=url, shortCode=short_code)

            # Prepare the response data
            response_data = {
                'id': short_url.id,
                'url': short_url.url,
                'shortCode': short_url.shortCode,
                'createdAt': short_url.createdAt.isoformat(),
                'updatedAt': short_url.updatedAt.isoformat()
            }

            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON body'}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def redirect_url(request, short_code):
    """
    Redirect to the original URL based on the short code.
    """
    shortened_url = get_object_or_404(ShortenedURL, shortCode=short_code)
    return HttpResponseRedirect(shortened_url.url)
