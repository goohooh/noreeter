from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView
from users.views import LoginView, LogoutView, SignupView, ProfileView, TownSetView
from users.api.search_town import TownListAPIView
from activities.views import ActivityListView, ActivityDetailView, ActivityCreateView
from activities.views.comments import ActivityCommentCreateView
from activities.api import ParticipateAPIView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),

    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^profile/(?P<slug>\w+)/$', ProfileView.as_view(), name="profile"),

    url(r'^api/participate/$', ParticipateAPIView.as_view(), name="api-participate"),
    url(r'^api/towns/$', TownListAPIView.as_view(), name="api-towns"),
    url(r'^town/set/$', TownSetView.as_view(), name="towns"),

    url(r'^activities/$', ActivityListView.as_view(), name="activities"),
    url(r'^activities/(?P<pk>\d+)/$', ActivityDetailView.as_view(), name="activity"),
    url(r'^activities/new/$', ActivityCreateView.as_view(), name="create-activity"),
    url(r'^activities/(?P<pk>\d+)/comment/$', ActivityCommentCreateView.as_view(), name="activity-comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
