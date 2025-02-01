from django.contrib import admin
from .models import FAQ
from django.utils.translation import gettext_lazy as _

class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "created_at")  # Show question & date in list
    search_fields = ("question", "question_hi", "question_bn")  # Search by question
    list_filter = ("created_at",)  # Filter by creation date
    ordering = ("-created_at",)  # Show latest first

    fieldsets = (
        (_("FAQ Details"), {"fields": ("question", "answer")}),
        (_("Translations"), {"fields": ("question_hi", "question_bn")}),
    )

admin.site.register(FAQ, FAQAdmin)