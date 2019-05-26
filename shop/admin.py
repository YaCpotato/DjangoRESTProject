from django.contrib import admin

from .models import TsunList
from .models import User


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('password', 'name', 'id')
    ordering = ('-id',)

class TsunListModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','tsuntype','link','memo','exp','created_at')
    ordering = ('-created_at',)


admin.site.register(User, UserModelAdmin)
admin.site.register(TsunList, TsunListModelAdmin)
