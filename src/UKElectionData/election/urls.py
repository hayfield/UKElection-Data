from django.conf.urls.defaults import patterns

urlpatterns = patterns('election.views',
    # party information
    (r'^party/$', 'partyIndex'),
    (r'^party/(?P<party_id>\d+)/$', 'partyDetail'),
    
    # constituency information
    (r'^constituency/$', 'constituencyIndex'),
    (r'^constituency/(?P<constituency_id>\d+)/$', 'constituencyDetail'),
    
    # candidate 2010 information
    (r'^candidate/$', 'candidate2010Index'),
)
