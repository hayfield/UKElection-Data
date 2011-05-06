from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView
from UKElectionData.election.models import Party, Constituency_2010, Candidate_2010

urlpatterns = patterns('',
    # party information
    # full party listing
    url(r'^party/$',
        ListView.as_view(
            queryset = Party.objects.order_by('name'),
            context_object_name = 'parties',
            template_name = 'election/party/list.html'),
        name = 'party-list'),
                    
    # specific party info   
    url(r'^party/(?P<pk>\d+)/$',
        DetailView.as_view(
            model = Party,
            template_name = 'election/party/party.html'),
        name = 'party-detail'),
    
    # constituency information
    # full constituency listing
    url(r'^constituency/$',
        ListView.as_view(
            queryset = Constituency_2010.objects.order_by('name'),
            context_object_name = 'constituencies',
            template_name = 'election/constituency/list.html'),
        name = 'constituency-2010-list'),
    
    # specific constituency info
    url(r'^constituency/(?P<pk>\d+)/$',
        DetailView.as_view(
            model = Constituency_2010,
            context_object_name = 'constituency',
            template_name = 'election/constituency/constituency.html'),
        name = 'constituency-2010-detail'),
    
    # candidate 2010 information
    # full candidate listing
    url(r'^candidate/$',
        ListView.as_view(
            queryset = Candidate_2010.objects.order_by('name'),
            context_object_name = 'candidates',
            template_name = 'election/candidate/list.html'),
        name = 'candidate-2010-list'),
)
