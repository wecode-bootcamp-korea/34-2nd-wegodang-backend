from django.urls import path

from products.views import SliderView

urlpatterns = [
    path('/sliders', SliderView.as_view())
]