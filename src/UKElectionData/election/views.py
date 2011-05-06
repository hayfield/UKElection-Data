# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from UKElectionData.election.models import Party, Candidate_2010, Constituency_2010

# display all of the parties
def partyIndex(request):
    parties = Party.objects.all().order_by('name')
    return render_to_response('election/party/index.html', {'parties': parties})

# display info about a specific party
def partyDetail(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    return render_to_response('election/party/party.html', {'party': party})

# display all of the constituencies
def constituencyIndex(request):
    constituencies = Constituency_2010.objects.all().order_by('name')
    return render_to_response('election/constituency/index.html', {'constituencies': constituencies})

# display info about a specific constituency
def constituencyDetail(request, constituency_id):
    constituency = get_object_or_404(Constituency_2010, pk=constituency_id)
    return render_to_response('election/constituency/constituency.html', {'constituency': constituency})

# display all of the 2010 candidates
def candidate2010Index(request):
    candidates = Candidate_2010.objects.all().order_by('name')
    return render_to_response('election/candidate/index.html', {'candidates': candidates})