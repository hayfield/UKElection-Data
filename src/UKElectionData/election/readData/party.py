# reads in a CSV file containing the party data and saves it in the DB

from UKElectionData.election.models import Party
import csv

with open('2010-Data/uk_elections-party.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        party = Party(party_id = row[0],
                  party_name = row[1],
                  party_votes_2010 = row[2],
                  party_votes_fought_2010 = row[3],
                  party_candidates_2010 = row[4],
                  party_seats_2010 = row[5])
        print party
        # party.save()

