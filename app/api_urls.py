"""putra perkasa abadi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from api.views.divisi import DivisiViews


# handler404 = 'app.views.custom_default_view.page_not_found'
# handler400 = 'app.views.custom_default_view.page_not_found'
# handler500 = 'app.views.custom_default_view.page_not_found'

app_name = 'api'

urlpatterns = [

    # Main URL
    # url(r'^$', do_login, name='signin_default'),
    # url(r'^signin/$', do_login, name='signin'),
    # url(r'^signout/$', do_logout, name='signout'),
    # url(r'^forget_password/$', show_forget_password, name='forget_password'),
    # url(r'^reset_password/$', do_reset_password, name='do_reset_password'),
    # url(r'^activation/$', user_activation, name='user_activation'),

    url(r'^divisi/$', DivisiViews.as_view(), name='test'),

]
