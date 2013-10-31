from django.conf.urls import patterns, include  # , url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# amitu.com/smarturls
from smarturls import surl


urlpatterns = patterns('',
    surl('/', include('principal.urls', namespace="principal")),
    surl('/agenda/', include('agenda.urls', namespace="agenda")),
    surl('/developers/', include('developers.urls', namespace="developers")),
    surl('/recover_password/', include('recover_password.urls', namespace="recover_password")),
    surl('admin/', include(admin.site.urls)),

    surl('/validate/', 'principal.views.validate'),

    surl('/agenda/append_agenda/', 'agenda.views.append_agenda'),
    surl('/agenda/save_agenda/', 'agenda.views.save_agenda'),
    surl('/agenda/search_agenda/', 'agenda.views.search_agenda'),
    surl('/agenda/delete_agenda/', 'agenda.views.delete_agenda'),
)

urlpatterns += staticfiles_urlpatterns()
