import json

# Input is dict
# Output is json object with the properties we want public

# Exampledata only has attributes that can be shared without authorization

def public_story(story):
    public_json = json.dumps(story)
    return public_json