# pip3 install scholarly
from scholarly import scholarly

search_query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
scholarly.pprint(next(search_query))
