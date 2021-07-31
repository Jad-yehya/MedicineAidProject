from django.urls import path

from .views import HomePageView, AboutPageView, BlogDetailView, BlogCreateView, BlogUpdateView, FormPageView, \
    BlogDeleteView, NavBarView, AddressView, MedicineListPageView, SearchView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('medicine_list/', MedicineListPageView.as_view(), name='medicine_list'),
    path('search/', SearchView.as_view(), name='search_results'),
    path('navbar/', NavBarView.as_view(), name='nav'),
    path('form/', FormPageView.as_view(), name='form'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    # MAPBOX ADDRESS VIEW
    path('post/new/', AddressView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'),
]
