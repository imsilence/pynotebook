#encoding: utf-8


from django.conf.urls import url

from .views import RegisterView, ActiveView, LoginView, LogoutView, \
                    PasswordResetView, PasswordResetConfirmView, PasswordModifyView,\
                    UserExtView, UserAvatarView,\
                    UserAddressListView, UserAddressCreateView, UserAddressDeleteView, UserAddressUpdateView

app_name = 'account'

urlpatterns = [
    url(r'^register/', RegisterView.as_view(), name="register"),
    url(r'^active/', ActiveView.as_view(), name="active"),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^password_reset/', PasswordResetView.as_view(), name="password_reset"),
    url(r'^password_reset_confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password_modify/', PasswordModifyView.as_view(), name='password_modify'),
    url(r'^user_ext/', UserExtView.as_view(), name='user_ext'),
    url(r'^user_avatar/', UserAvatarView.as_view(), name='user_avatar'),
    url(r'^user_address/$', UserAddressListView.as_view(), name='user_addresses'),
    url(r'^user_address/create/$', UserAddressCreateView.as_view(), name='create_user_address'),
    url(r'^user_address/(?P<pk>\d+)/delete/$', UserAddressDeleteView.as_view(), name='delete_user_address'),
    url(r'^user_address/(?P<pk>\d+)/$', UserAddressUpdateView.as_view(), name='update_user_address'),
]
