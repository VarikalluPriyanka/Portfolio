from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  About,Education,Internship,Project, Certification, Category, Skills


# Home


admin.site.register(About)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Internship)
admin.site.register(Project)

# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]
