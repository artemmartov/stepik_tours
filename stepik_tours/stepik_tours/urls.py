from django.urls import path

from tours.views import DepartureView, MainView, TourView


urlpatterns = [
    path('', MainView),
    path('/departure/<str:departure>/', DepartureView),
    path('/tour/<int:id>', TourView),
]
