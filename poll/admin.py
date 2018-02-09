from django.contrib import admin

from .models import Choice, Question,Private


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('qid','question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date'] #用来过滤
    search_fields = ['question_text']#用来搜索
    list_per_page = 50 #控制分页

admin.site.register(Question, QuestionAdmin)
admin.site.register(Private)