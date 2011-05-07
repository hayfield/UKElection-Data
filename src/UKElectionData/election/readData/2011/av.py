# reads in an XML file containing the AV results and saves them in the DB

from UKElectionData.election.models import Constituency_AV
import xml.dom.minidom

# open the file
av_file_name = 'Data/AV_results.xml'
av_file = xml.dom.minidom.parse(av_file_name)
results = av_file.getElementsByTagName('ReferendumResult')[0]
constituencies = results.getElementsByTagName('c')

# parse the constituencies
for c in constituencies:
    constituency = Constituency_AV(id=c.getAttribute('x'),
                                   name=c.getAttribute('p'),
                                   yes=c.getAttribute('y'),
                                   no=c.getAttribute('n'),
                                   outcome=c.getAttribute('v'),
                                   possible_voters=c.getAttribute('e'),
                                   votes=c.getAttribute('t'),
                                   turnout=c.getAttribute('pt'))
    print constituency
    
    # constituency.save()
