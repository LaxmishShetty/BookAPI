from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('books', views.BooksView)
router.register('genre',views.GenreView)
router.register('readers',views.ReadersView)


urlpatterns = [
    path('', include(router.urls))

]