from django.urls import path

from . import views

app_name = "web"
urlpatterns = [
    path("", views.index, name="index"),
    path("airports/", views.airport_list, name="airport_list"),
    path("airports/add/", views.airport_create, name="airport_create"),
    path("airports/edit/<int:pk>/", views.airport_update, name="airport_update"),
    path("airports/delete/<int:pk>/", views.airport_delete, name="airport_delete"),
    path("add-route/", views.add_route, name="add_route"),
    path("nth-node/", views.find_nth_node, name="nth_node"),
    path("longest/", views.longest_route, name="longest"),
    path("shortest/", views.shortest_path, name="shortest"),
]
