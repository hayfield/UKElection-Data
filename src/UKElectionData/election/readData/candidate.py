# reads in a CSV file containing the candidate data and saves it in the DB

from UKElectionData.election.models import Candidate_2010
import csv

with open('2010-Data/uk_elections-candidate.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        candidate = Candidate_2010(can_id = row[0],
                            can_name = row[1],
                            can_party = row[2],
                            can_votes_2010 = row[3],
                            can_constituency_2010 = row[4])
        print candidate
        # candidate.save()

