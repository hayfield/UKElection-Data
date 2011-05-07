# reads in a CSV file containing the constituency data and saves it in the DB

from UKElectionData.election.models import Constituency_2010, Party
import csv

with open('2010-Data/uk_elections-constituency.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        constituency = Constituency_2010(id = row[0],
                            name = row[1],
                            name_bbc = row[2],
                            possible_voters_2010 = row[3],
                            bbc_url_2010 = row[4],
                            telegraph_url_2010 = row[5],
                            continuity_2010 = row[6],
                            votes_2010 = row[7],
                            winning_party_2010 = Party.objects.get(pk=row[8]),
                            majority_2010 = row[9])
        print constituency
        
        # constituency.save()
