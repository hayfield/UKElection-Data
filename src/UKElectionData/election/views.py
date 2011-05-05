# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from UKElectionData.election.models import Party, Candidate_2010, Constituency

# display all of the parties
def partyIndex(request):
    parties = Party.objects.all().order_by('party_name')
    return render_to_response('election/party/index.html', {'parties': parties})

def partyDetail(request, party_id):
    return HttpResponse("You're looking at party %s." % party_id)