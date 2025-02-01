from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG editor support
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Automatically translate question into Hindi & Bengali before saving"""
        translator = Translator()

        if not self.question_hi:
            try:
                self.question_hi = translator.translate(self.question, src='en', dest='hi').text
            except:
                self.question_hi = self.question  # Fallback to English

        if not self.question_bn:
            try:
                self.question_bn = translator.translate(self.question, src='en', dest='bn').text
            except:
                self.question_bn = self.question  # Fallback to English

        super().save(*args, **kwargs)

    def get_translated_question(self, lang):
        """Retrieve translated question based on the requested language"""
        if lang == "hi":
            return self.question_hi or self.question
        elif lang == "bn":
            return self.question_bn or self.question
        return self.question  # Default: English


    def __str__(self):
        return self.question
