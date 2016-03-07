"""
***Application url's***
"""

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls import include, patterns, url

urlpatterns = [
	
	#localhost:8000/constellation
	url(r'^$', views.index, name='index'),	
 
	#localhost:8000/constellation/login 
	url(r'^login/$', views.Login, name='Login'),
	
	#localhost:8000/constellation/logout 
	url(r'^logout/$', views.Logout, name='Logout'),
	
	#localhost:8000/constellation/register
	url(r'^register/$', views.Register, name='Register'),
	
	#localhost:8000/constellation/munster
	url(r'^munster/$', views.Munster, name='Munster'),

	#localhost:8000/constellation/leinster
	url(r'^leinster/$', views.Leinster, name='Leinster'),

	#localhost:8000/constellation/connacht
	url(r'^connacht/$', views.Connacht, name='Connacht'),

	#localhost:8000/constellation/ulster
	url(r'^ulster/$', views.Ulster, name='Ulster'),

    #localhost:8000/constellation/?/checkin/
    url(r'^(?P<qr_code>[0-999999999]+)/checkin/$', views.Checkin, name='Checkin'),

    #localhost:8000/constellation/?/getticket/
    # url(r'^(\w+)/getticket/$', views.GetTicket, name='GetTicket'),

    #localhost:8000/constellation/generateticket/?
    url(r'^generateticket/(?P<event_id>[0-999999999]+)$', views.GenerateTicket, name='GenerateTicket'),

    #
    url(r'^account/$', views.Account, name='Account'),
    
    #localhost:8000/constellation/reset/password_reset/
    url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset_password_reset1'),
    
    url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
      
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
