from django.contrib import admin
from django.urls import path
from app.views import home , money_panel , win , panel ,index , otp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('money-panel', money_panel,name='money_panel'),
    path('win/<str:choine>/<int:id>/', win,name='win'),
    path('panel/', panel,name='panel'),
    path('login/', index,name='index'),
    path('login/otp/', otp,name='otp'),
]
