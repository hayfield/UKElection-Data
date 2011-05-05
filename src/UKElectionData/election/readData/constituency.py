# reads in a CSV file containing the constituency data and saves it in the DB

from UKElectionData.election.models import Constituency
import csv

with open('2010-Data/uk_elections-constituency.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        constituency = Constituency(con_id = row[0],
                            con_name = row[1],
                            con_name_bbc = row[2],
                            con_possible_voters_2010 = row[3],
                            bbc_url_2010 = row[4],
                            telegraph_url_2010 = row[5],
                            continuity_2010 = row[6],
                            con_votes_2010 = row[7],
                            con_winning_party_2010 = row[8],
                            con_majority_2010 = row[9])
        print constituency
        # constituency.save()

