from django.contrib import admin
from.models import Problem,Subject,Category,Example

class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "subject_name",
    ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "category_name",
        "subject",
    ]


class ProblemAdmin(admin.ModelAdmin):
    list_display = [
        "id", 
        "subject", 
        "category", 
        "q_date", 
        "q_org", 
        "q_num", 
        "correct_rate", 
        "header", 
        "content"
    ]

class ExampleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "problem",
        "content_type",
        "example_1",
        "example_2",
        "example_3",
        "example_4",
        "example_5",
    ]

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Example, ExampleAdmin)