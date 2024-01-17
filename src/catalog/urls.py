from django.urls import path

from catalog.views import CategoryListView, GoodsByCategoryView, GoodCreateView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories_list'),
    path('categories/<int:pk>', GoodsByCategoryView.as_view(), name='goods_by_category'),
    path('add/', GoodCreateView.as_view(), name='add_good'),
]