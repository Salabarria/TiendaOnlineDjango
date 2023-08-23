from django.contrib import admin

# Register your models here.
from projects.models import Project,Album,Track

# class ProjectAdmin(admin.ModelAdmin):
#     list_display=("title","description","created","datecompleted","important","user")  # muesta estos campos en el panel de control del modelo cliente
#     search_fields=("title","important","user")                            # realiza una busqueda pro nombre en el campo que se implementada
#     list_filter=("title","important","user","created")


admin.site.register([Project,Album,Track]) 