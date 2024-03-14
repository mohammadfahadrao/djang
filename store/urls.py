from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    # path("<int:question_id>", views.show, name="show"),
    # path("<int:question_id>/single",views.show_single_obj, name="singleObj")
]