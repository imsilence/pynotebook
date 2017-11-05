#encoding: utf-8


from django.conf.urls import url

from .views import RegisterView, ActiveView, \
                    LoginView, LogoutView, \
                    ResetPasswordView, ResetPasswordConfirmView, \
                    ModifyPasswordView, ChangePasswordView, \
                    UserExtBaseView, UserExtAvatarView

app_name = 'account'


urlpatterns = [
    url(r'^register/', RegisterView.as_view(), name="register"),
    url(r'^active/', ActiveView.as_view(), name="active"),
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^modify_password/', ModifyPasswordView.as_view(), name="modify_password"),
    url(r'^reset_password/', ResetPasswordView.as_view(), name="reset_password"),
    url(r'^reset_password_confirm/', ResetPasswordConfirmView.as_view(), name="reset_password_confirm"),
    url(r'^change_password/', ChangePasswordView.as_view(), name="change_password"),
    url(r'^user_ext_base/', UserExtBaseView.as_view(), name="user_ext_base"),
    url(r'^user_ext_avatar/', UserExtAvatarView.as_view(), name="user_ext_avatar"),
       
]

