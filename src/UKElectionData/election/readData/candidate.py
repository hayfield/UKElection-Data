# reads in a CSV file containing the candidate data and saves it in the DB

from UKElectionData.election.models import Candidate_2010, Party, Constituency_2010
import csv

with open('2010-Data/uk_elections-candidate.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        candidate = Candidate_2010(id = row[0],
                            name = row[1],
                            party = Party.objects.get(pk=row[2]),
                            votes_2010 = row[3],
                            constituency_2010 = Constituency_2010.objects.get(pk=row[4]))
        print candidate
        
        # candidate.save()
