from django.urls import path
from . import views


urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.testapp_list),
   # path('about/', views.about),
]

