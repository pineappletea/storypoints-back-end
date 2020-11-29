import uuid

def createstory(StoryTitle, Coordinates, LocationDescription):

    print("called createstory with", StoryTitle, Coordinates, LocationDescription)
    print("id will be", uuid.uuid1())

    # Save into database