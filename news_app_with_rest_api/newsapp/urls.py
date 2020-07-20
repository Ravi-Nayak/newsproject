from django.urls import path,include
from .views import Index, bbc,india,signup_view,logout_view

urlpatterns = [
    path('alg/', Index, name='Index'),
    path('bbc/', bbc, name='BBC'),
    path('',india,name='IND'),
    path('logout/', logout_view),
    path('signup/', signup_view),
    path('accounts/', include('django.contrib.auth.urls')),

]