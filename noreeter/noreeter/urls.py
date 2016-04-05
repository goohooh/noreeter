from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView
from users.views import LoginView, LogoutView, SignupView, ProfileView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),

    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^profile/$', ProfileView.as_view(), name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
