from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'translated_question', 'answer', 'created_at']

    def get_translated_question(self, obj):
        """Fetch translated question based on query parameter (?lang=)"""
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'en')
        return obj.get_translated_question(lang)
