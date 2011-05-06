# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from UKElectionData.election.models import Party, Candidate_2010, Constituency_2010

# display all of the parties
def partyIndex(request):
    parties = Party.objects.all().order_by('name')
    return render_to_response('election/party/index.html', {'parties': parties})

def partyDetail(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    return render_to_response('election/party/party.html', {'party': party})