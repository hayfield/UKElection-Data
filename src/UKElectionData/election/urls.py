from django.conf.urls.defaults import patterns
from django.views.generic import DetailView, ListView
from UKElectionData.election.models import Party, Constituency_2010, Candidate_2010

urlpatterns = patterns('election.views',
    # party information
    # full party listing
    (r'^party/$',
        ListView.as_view(
            queryset = Party.objects.order_by('name'),
            context_object_name = 'parties',
            template_name = 'election/party/index.html')),
                    
    # specific party info   
    (r'^party/(?P<pk>\d+)/$',
        DetailView.as_view(
            model = Party,
            template_name = 'election/party/party.html')),
    
    # constituency information
    # full constituency listing
    (r'^constituency/$',
        ListView.as_view(
            queryset = Constituency_2010.objects.order_by('name'),
            context_object_name = 'constituencies',
            template_name = 'election/constituency/index.html')),
    
    # specific constituency info
    (r'^constituency/(?P<pk>\d+)/$',
        DetailView.as_view(
            model = Constituency_2010,
            context_object_name = 'constituency',
            template_name = 'election/constituency/constituency.html')),
    
    # candidate 2010 information
    # full candidate listing
    (r'^candidate/$',
        ListView.as_view(
            queryset = Candidate_2010.objects.order_by('name'),
            context_object_name = 'candidates',
            template_name = 'election/candidate/index.html')),
)
