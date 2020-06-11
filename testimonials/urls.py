from django.urls import path
from . import views


app_name = 'testimonials'
urlpatterns = [
              path('',views.all_testimonials, name='all_testimonials'),
              path('<int:test_id>/',views.detail, name='detail' ),
]
