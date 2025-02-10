from django.contrib import admin
from .models import Person, Skill, Category, PersonSkill, SkillCategory

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  
    search_fields = ("name",)  

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(PersonSkill)
class PersonSkillAdmin(admin.ModelAdmin):
    list_display = ("id", "person", "skill")  
    search_fields = ("person__name", "skill__name")

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "skill", "category")
    search_fields = ("skill__name", "category__name")
