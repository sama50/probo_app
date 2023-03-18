from django.contrib import admin
from app.models import Myuser , Context , User_context
# Register your models here.


@admin.register(Myuser)
class MyuserAdmin(admin.ModelAdmin):
    list_display = ('id','number','curr_amount','added_amount')

@admin.register(Context)
class ContextAdmin(admin.ModelAdmin):
    list_display = ('id','title','middle_line','yes_amount','no_amount','chance_win','date','done')


@admin.register(User_context)
class User_contextAdmin(admin.ModelAdmin):
    list_display = ('id','user','context')


