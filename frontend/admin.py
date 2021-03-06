from django.contrib import admin
from .models import *

admin.site.site_header = "Rhixecompany Admin"
admin.site.site_title = "Rhixecompany Admin Area"
admin.site.index_title = "Welcome to the Rhixecompany Admin area"

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3
  
class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [(None, {'fields': ['question_text']}),
               ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
