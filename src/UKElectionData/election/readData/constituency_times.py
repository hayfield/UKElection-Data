# reads in a CSV file containing additional constituencyuency data from the Times and saves it in the DB

from UKElectionData.election.models import Constituency_2010
import csv

with open('2010-Data/constituencies-description.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        # try matching the name exactly, replacing brackets with square ones
        constituencies = Constituency_2010.objects.filter(name__iexact=row[2].replace('(','[').replace(')',']'))

        # if a plain fetch doesn't work, try the bbc name
        if constituencies.count() != 1:
            constituencies = Constituency_2010.objects.filter(name_bbc__iexact=row[2])
        
        # then try using the name with underscores
        if constituencies.count() != 1:
            constituencies = Constituency_2010.objects.filter(name__iexact=row[3].replace('_', ' '))
            
        # then try using the name with underscores, plus dashes and 'and's replaced
        if constituencies.count() != 1:
            constituencies = Constituency_2010.objects.filter(
                                name__iexact=row[3].replace('_', ' ').replace('and','&').replace('-',' '))
        
        # then try adding a trailing space because East Antrim seems to have one
        if constituencies.count() != 1:
            constituencies = Constituency_2010.objects.filter(name__iexact=row[3].replace('_', ' ') + ' ')
            
        # and finally do a contains match rather than exact for Na h-Eileanan an Iar
        if constituencies.count() != 1:
            constituencies = Constituency_2010.objects.filter(name__contains=row[2])
            
        if constituencies.count() != 1:
            print row
            
        # update the constituency with the new data
        constituency = constituencies[0]
        constituency.times_cid = int(row[0])
        constituency.times_mid = int(row[1])
        constituency.description_2010 = row[4]
        constituency.mp_info_2010 = row[5]
        
        print constituency
        
        # constituency.save()

