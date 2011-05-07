# reads in a CSV file containing the party data and saves it in the DB

from UKElectionData.election.models import Party
import csv

with open('Data/uk_elections-party.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        party = Party(id = row[0],
                  name = row[1],
                  votes_2010 = row[2],
                  votes_fought_2010 = row[3],
                  candidates_2010 = row[4],
                  seats_2010 = row[5])
        print party
        
        # party.save()
