
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('home/', views.home,name='home'),
    path('createcomputer/', views.createComputer,name='createcomputer'),
    path('computerlist/', views.computerList,name='computerlist'),
    path('updatecomputer/<int:id>', views.updateComputer,name='updatecomputer'),
    path('deletecomputer/<int:id>', views.deleteComputer,name='deletecomputer'),
    path('computerhistory/', views.computerHistory,name='computerhistory'),
    path('settings/', views.settings,name='settings'),
    url(r'^accounts/', include('registration.backends.default.urls')),

]
