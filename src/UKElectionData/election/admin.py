from UKElectionData.election.models import Candidate_2010, Constituency_2010, Party
from django.contrib import admin

class CandidateInline(admin.StackedInline):
    model = Candidate_2010
    extra = 3

class PartyAdmin(admin.ModelAdmin):
    inlines = [CandidateInline]
    
class ConstituencyAdmin(admin.ModelAdmin):
    inlines = [CandidateInline]

admin.site.register(Candidate_2010)
admin.site.register(Constituency_2010, ConstituencyAdmin)
admin.site.register(Party, PartyAdmin)
