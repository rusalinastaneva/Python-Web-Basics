from django.contrib import admin

# Register your models here.
from pets.models import Pet, Like, Comment


class LikeInLine(admin.TabularInline):
    model = Like


class PetAdmin(admin.ModelAdmin):
    # fields = ('type', 'name')
    list_display = ('id', 'type', 'name', 'age')
    list_filter = ('type', 'age')
    inlines = [
        LikeInLine,
    ]


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
admin.site.register(Comment)