from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entryPage, name="entry_page"),
    path("search", views.search, name="search"),
    path("new_page", views.newPage, name="new_page"),
    path("edit_page", views.editPage, name="edit_page"),
    path("save_page", views.savePage, name="save_page"),
    path("random_page", views.randomPage, name="random_page")
]
