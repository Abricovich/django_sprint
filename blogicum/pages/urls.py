from django.urls import path
from .views import about, rules


app_name = 'pages'

# Здесь будут три адреса - второй с детальной информацией публиукации, третий будет с категориями
urlpatterns = [
    path('about/', about, name='about'),
    path('rules/', rules, name='rules') 
]