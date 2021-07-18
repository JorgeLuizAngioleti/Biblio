from django.contrib import admin
from .models import Biblioteca, Usuario, Emprestar
# Register your models here.
admin.site.register(Biblioteca)
admin.site.register(Usuario)
admin.site.register(Emprestar)