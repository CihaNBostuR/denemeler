from django.urls import path

from .views import person_create_view,load_yayinevi

urlpatterns = [
    path('add/', person_create_view, name='person_add'),
    # path('<int:pk>/', person_update_view, name='person_change'),
    path('ajax/load-yayinevi/', load_yayinevi, name='ajax_load_yayinevi'), # AJAX
]