from django.urls import path
from . import views

urlpatterns = [
	path('', views.index2, name="index2"),
	path('cdetails/<int:post_id>', views.post_detail, name="post_detail"),
	path('cdetails/<int:contact_id>/edit', views.post_edit, name="post_edit"),
	path('deleteContact/<int:contact_id>', views.post_delete, name="post_delete"),
	path('addContact/', views.post_add, name="post_add"),
]