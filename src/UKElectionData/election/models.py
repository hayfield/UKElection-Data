from django.db import models

# Create your models here.
# a party
class Party(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    votes_2010 = models.IntegerField()
    votes_fought_2010 = models.IntegerField()
    candidates_2010 = models.IntegerField()
    seats_2010 = models.IntegerField()
    
    def __unicode__(self):
        return self.name
    
# a constituency
class Constituency_2010(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    name_bbc = models.CharField(max_length=255)
    possible_voters_2010 = models.IntegerField()
    bbc_url_2010 = models.CharField(max_length=255)
    telegraph_url_2010 = models.CharField(max_length=255)
    continuity_2010 = models.IntegerField()
    votes_2010 = models.IntegerField()
    winning_party_2010 = models.ForeignKey(Party)
    majority_2010 = models.IntegerField()
    
    def __unicode__(self):
        return self.name
    
# a candidate fighting the 2010 election
class Candidate_2010(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    party = models.ForeignKey(Party)
    votes_2010 = models.IntegerField()
    constituency_2010 = models.ForeignKey(Constituency_2010)
    
    def __unicode__(self):
        return self.name

