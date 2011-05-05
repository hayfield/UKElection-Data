from django.db import models

# Create your models here.
# a party
class Party(models.Model):
    party_id = models.IntegerField(primary_key=True)
    party_name = models.CharField(max_length=255)
    party_votes_2010 = models.IntegerField()
    party_votes_fought_2010 = models.IntegerField()
    party_candidates_2010 = models.IntegerField()
    party_seats_2010 = models.IntegerField()
    
    def __unicode__(self):
        return self.party_name
    
# a constituency
class Constituency(models.Model):
    con_id = models.IntegerField(primary_key=True)
    con_name = models.CharField(max_length=255)
    con_name_bbc = models.CharField(max_length=255)
    con_possible_voters_2010 = models.IntegerField()
    bbc_url_2010 = models.CharField(max_length=255)
    telegraph_url_2010 = models.CharField(max_length=255)
    continuity_2010 = models.IntegerField()
    con_votes_2010 = models.IntegerField()
    con_winning_party_2010 = models.ForeignKey(Party)
    con_majority_2010 = models.IntegerField()
    
    def __unicode__(self):
        return self.con_name
    
# a candidate fighting the 2010 election
class Candidate_2010(models.Model):
    can_id = models.IntegerField(primary_key=True)
    can_name = models.CharField(max_length=255)
    can_party = models.ForeignKey(Party)
    can_votes_2010 = models.IntegerField()
    can_constituency_2010 = models.ForeignKey(Constituency)
    
    def __unicode__(self):
        return self.can_name

