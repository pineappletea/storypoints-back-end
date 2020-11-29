from geopy.distance import geodesic
from public_story import public_story
range = 3

def get_stories_in_range(lat, long, storylist):
    print("called for stories in range of ", lat, long)
    storiesInRange = []

    for story in storylist:
        if is_in_range(lat, long, story):
            storiesInRange.append(public_story(story))

    return storiesInRange

def is_in_range(lat, long, story): 
    userSpot = (lat, long)
    storySpot = (story['Coordinates']['lat'], story['Coordinates']['long'])
    distance = geodesic(userSpot, storySpot).km
    
    if distance <= range:
        return True
    else:
        return False
    