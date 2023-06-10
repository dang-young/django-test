from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wait/", views.get_post_wait),
    path("order/", views.get_post_order),
    #path("parameter/",views.get_post),
    #path("parameter/",CustomerView.as_view()),
    #path("<int:cid>/", views.detail, name = "detail"),
]
