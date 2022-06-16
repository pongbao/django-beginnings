from django.contrib import admin

# added imports
from .models import Question, Choice

# Register your models here.
# StackedInline
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

# TabularInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # Change the display fields
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Add Filter for pub_date
    list_filter = ['pub_date']
    # Add search field
    search_fields = ['question_text']
    # Others
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_per_page
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.date_hierarchy
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display

# models will show up in the admin interface once registered
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

