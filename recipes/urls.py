from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeListCreate.as_view()),
    path('<int:pk>/', views.RecipeDetail.as_view()),

    path('api/recipes/', views.RecipeListCreate.as_view(), name='recipe-list-create'),
    path('api/recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe-detail'),

   # path('recipes/', recipe_list, name='recipe_list'),
   # path('recipes/<int:pk>/', recipe_detail, name='recipe_detail'),
]
