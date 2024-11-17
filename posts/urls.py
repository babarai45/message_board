from django.urls import path
from .views import Homeposts ,homeview
urlpatterns = [
    path('post/',homeview.as_view(),name='posts'),
    path('post2/',Homeposts.as_view(), name='postpage2')

]
