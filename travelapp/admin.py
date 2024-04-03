from django.contrib import admin
from . models import Place  #dbname
from . models import Team
# # Register your models here.
admin.site.register(Place)
admin.site.register(Team)