from django.urls import path
from . import views


app_name = 'poetry'
urlpatterns = [
              path('',views.all_poetry, name='all_poetry'),
              path('<int:test_id>/',views.detailp, name='detailp' ),
]
