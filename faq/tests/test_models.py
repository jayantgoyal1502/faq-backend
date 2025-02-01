import pytest
from faq.models import FAQ
from googletrans import Translator

@pytest.mark.django_db
def test_faq_model_translation():
    # Create FAQ in English
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework for Python."
    )

    # Check if translations are generated
    translator = Translator()
    assert faq.question_hi == translator.translate(faq.question, src='en', dest='hi').text
    assert faq.question_bn == translator.translate(faq.question, src='en', dest='bn').text
