
from django.contrib import admin
from django.urls import path
from .views import book_create,book_delete,book_view,book_update,registration,login_view
from .views import Books,BookCreate,BookUpdate,BookDetail,BookDelete
urlpatterns = [
    path("create",book_create,name="create"),
    path("delete/<int:id>",book_delete,name="delete"),
    path("view/<int:id>",book_view,name="detail"),
    path("edit/<int:pk>",book_update,name="edit"),
    path("registration",registration,name="registration"),
    path("login",login_view,name="logsin"),
    path("clslist",Books.as_view(),name="clslist"),
    path("clscreate",BookCreate.as_view(),name="clscreate"),
    path("clsupdate/<int:pk>",BookUpdate.as_view(),name="clsupdate"),
    path("clsdetail/<int:pk>",BookDetail.as_view(),name="clsdetail"),
    path("clsdelete/<int:pk>",BookDelete.as_view(),name="clsdelete")
]
