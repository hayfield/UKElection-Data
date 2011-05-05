# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from UKElectionData.election.models import Party, Candidate_2010, Constituency

# display all of the parties
def partyIndex(request):
    parties = Party.objects.all().order_by('party_name')
    t = loader.get_template('election/party/index.html')
    c = Context({
        'parties': parties
    })
    return HttpResponse(t.render(c))

def partyDetail(request, party_id):
    return HttpResponse("You're looking at party %s." % party_id)