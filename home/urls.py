from tkinter.font import names

from django.urls import path

from .views import home, drama, fantastika, jahon_kinolari, jangari, komediya, uzbek_kinolari

urlpatterns = [
    path('', home, name='home'),
    path('drama/', drama, name='drama'),
    path('fantastika/', fantastika, name='fantastika'),
    path('jahon_kinolari/', jahon_kinolari, name='jahon_kinolari'),
    path('jangari/', jangari, name='jangari'),
    path('komediya/', komediya, name='komediya'),
    path('uzbek_kinolari/', uzbek_kinolari, name='uzbek_kinolari'),
]