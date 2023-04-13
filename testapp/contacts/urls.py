from django.urls import path
from .views import ContactView, ContactUpdateView, ContactDeleteView, ContactCreateView

urlpatterns = [
    path('', ContactView.as_view(), name='contact_list'),
    path('add/', ContactCreateView.as_view(), name='contact_new'),
    path('<int:pk>/edit/', ContactUpdateView.as_view(), name='contact_edit'),
    path('<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
]



