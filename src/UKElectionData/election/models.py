from django.db import models
import math

# Create your models here.
# a party
class Party(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    votes_2010 = models.IntegerField()
    votes_fought_2010 = models.IntegerField()
    candidates_2010 = models.IntegerField()
    seats_2010 = models.IntegerField()
    
    # the percentage of votes fought which were won
    def vote_percentage_2010(self):
        if self.votes_fought_2010 == 0:
            percentage = 0
        else:
            percentage = (float(self.votes_2010) / self.votes_fought_2010) * 100
        return percentage
    
    # both of the following are rough guesstimates and may be wildly off 
    # the number of seats under a Proportional Representation system
    def seats_2010_pr(self):
        vote_percentage = self.vote_percentage_2010()
        if self.candidates_2010 < 9:
            seats = 0
        elif self.candidates_2010 < 600:
            if vote_percentage > 1:
                seats = 6
            else:
                seats = math.floor(6.13 * vote_percentage)
            if self.name.find('Union') != -1 or self.name.find('Labour') != -1:
                if seats >= 6:
                    seats = 2
        else:
            seats = math.floor(6.13 * vote_percentage)
        return int(seats)
        
    # the number of seats under a system like in Germany
    def seats_2010_ger(self):
        seats = 0.5 * float(self.seats_2010)
        if self.vote_percentage_2010() > 1:
            seats += 0.5 * self.seats_2010_pr()
        seats *= 1.03
        return int(math.floor(seats))
            
    # a string representation of the class
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
    description_2010 = models.TextField()
    mp_info_2010 = models.TextField()
    times_cid = models.IntegerField(null=True)
    times_mid = models.IntegerField(null=True)
    
    # the number of votes the winning candidate obtained
    def winning_votes_2010(self):
        return self.candidate_2010_set.get(party=self.winning_party_2010).votes_2010
    
    # the percentage of the votes the winning candidate obtained
    def winning_percentage_2010(self):
        return (float(self.winning_votes_2010()) / self.votes_2010) * 100
    
    # the percentage turnout within the constituency
    def turnout_2010(self):
        return (float(self.votes_2010) / self.possible_voters_2010) * 100
    
    # the percentage of votes the winning candidate got above the second candidate
    def majority_percentage_2010(self):
        return (float(self.majority_2010) / self.votes_2010) * 100
    
    def __unicode__(self):
        return self.name
    
# a candidate fighting the 2010 election
class Candidate_2010(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    party = models.ForeignKey(Party)
    votes_2010 = models.IntegerField()
    constituency_2010 = models.ForeignKey(Constituency_2010)
    
    # the percentage of votes within their constituency that the candidate obtained
    def vote_percentage_2010(self):
        return (float(self.votes_2010) / self.constituency_2010.votes_2010) * 100
    
    def __unicode__(self):
        return self.name
    
# a constituency for the 2011 AV referendum
class Constituency_AV(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    yes = models.IntegerField()
    no = models.IntegerField()
    outcome = models.CharField(max_length=7)
    possible_voters = models.IntegerField()
    votes = models.IntegerField()
    turnout = models.DecimalField(max_digits=5, decimal_places=2)
    
    # the percentage of voters who voted yes
    def yes_percentage(self):
        return (float(self.yes) / self.votes) * 100
    
    # the percentage of voters who voted no
    def no_percentage(self):
        return (float(self.no) / self.votes) * 100
    
    def __unicode__(self):
        return self.name
