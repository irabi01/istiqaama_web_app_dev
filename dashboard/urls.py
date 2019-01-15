from django.conf.urls import url
from . import views
# from .views import GeneratePdf

urlpatterns = [
    url(r'^$', views.login_view, name = 'login_view' ),
    url(r'^all_members/details/pdf/', views.generate_view, name = 'generate_view'),
    url(r'^single_member/(?P<id>\d+)/details/pdf/', views.generate_single_view, name = 'generate_single_view'),
    url(r'^logout/', views.logout_view, name = 'logout_view' ),
    url(r'^user/login/', views.login_view, name = 'login_view' ),
    url(r'^home/', views.home_view, name = 'home_view'),
    url(r'^profile/', views.user_profile, name = 'user_profile'),
    url(r'^setting/', views.home_setting, name = 'home_setting'),
    url(r'^add_member/', views.add_view, name = 'add_view'),
    url(r'^dependant/', views.add_dependant, name = 'add_dependant'),
    url(r'^member_list/', views.list_view, name = 'list_view'),
    url(r'^view/(?P<id>\d+)/detail/', views.detail_view, name = 'detail_view'),
    url(r'^delete/(?P<id>\d+)/detail/delete', views.delete_detail_view, name = 'delete_detail_view'),
]
