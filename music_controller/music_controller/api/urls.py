# Example ------
# from django.urls import path

# from .views import main
# from .views import home
# from .views import about

# urlpatterns = [
#     path("",main),
#     path("home",home),
#     path("about",about),
# ]
# ----------------
from django.urls import path

from .views import RoomView

urlpatterns = [
    path("home",RoomView.as_view()),
]