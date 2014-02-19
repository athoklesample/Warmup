from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Warmup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', 'Login.views.main'),
    url(r'^user/login','Login.views.main'),
    url(r'^user/add','Login.views.main'),
    url(r'^TESTAPI/resetFixture','Login.views.main'),
    url(r'^TESTAPI/unitTests', 'Login.views.main')
)
