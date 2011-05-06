from django.conf.urls.defaults import patterns
from django.views.generic import DetailView, ListView
from UKElectionData.election.models import Party, Constituency_2010, Candidate_2010

urlpatterns = patterns('election.views',
    # party information
    #(r'^party/$', 'partyIndex'),
    (r'^party/$',
        ListView.as_view(
            queryset = Party.objects.order_by('name'),
            context_object_name = 'parties',
            template_name = 'election/party/index.html')),
    (r'^party/(?P<party_id>\d+)/$', 'partyDetail'),
    
    # constituency information
    # (r'^constituency/$', 'constituencyIndex'),
    (r'^constituency/$',
        ListView.as_view(
            queryset = Constituency_2010.objects.order_by('name'),
            context_object_name = 'constituencies',
            template_name = 'election/constituency/index.html')),
    (r'^constituency/(?P<constituency_id>\d+)/$', 'constituencyDetail'),
    
    # candidate 2010 information
    (r'^candidate/$',
        ListView.as_view(
            queryset = Candidate_2010.objects.order_by('name'),
            context_object_name = 'candidates',
            template_name = 'election/candidate/index.html')),
    # (r'^candidate/$', 'candidate2010Index'),
)
