"""Define url patterns for pizzas"""

from django.urls import path

from . import views


app_name = 'pizzas'
urlpatterns = [
	# Home page.
	path('', views.index, name='index'),
	# Page that shows all the pizzas.
	path('pizza_names/', views.pizzas, name='pizza_names'),
	# Detail page for a single topic.
	path('pizza_names/<int:pizza_id/', views.pizza, name='pizza'),
]