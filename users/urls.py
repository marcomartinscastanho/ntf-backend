from django.urls import path

from users import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", views.UserList.as_view(), name="user-list"),
    path("<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
]
