from django.urls import path
from . import views
urlpatterns=[
    path("",views.Home,name="Home"),
    path("delete_rec/<id>/",views.delete_res,name="Delete function"),
    path("update_rec/<id>/",views.update_res,name="Update function"),
    path("login",views.login_pg,name="login page"),
    path("register",views.register_pg,name="register page"),
    path("logout",views.logout_pg,name="logout page")



]

# for media file
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)