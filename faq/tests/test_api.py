import pytest
from rest_framework import status
from django.urls import reverse
from faq.models import FAQ  # Add this import

@pytest.mark.django_db
def test_faq_list_api(client):
    # Create a FAQ
    FAQ.objects.create(
        question="What is Django?",
        question_hi="डिजैंगो क्या है?",
        question_bn="ডিজেঙ্গো কি?",
        answer="Django is a web framework for Python."
    )

    # Test fetching FAQs in English
    url = reverse("faq-list")
    response = client.get(url, {"lang": "en"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0

    # Test fetching FAQs in Hindi
    response = client.get(url, {"lang": "hi"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0

    # Test fetching FAQs in Bengali
    response = client.get(url, {"lang": "bn"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
