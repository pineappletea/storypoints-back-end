from flask import Flask, request, jsonify
import json
from getdata import testdata
from tokencheck import tokenOK
from createstory import createstory
from get_stories_in_range import get_stories_in_range
app = Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False


# Halutut kutsut: /koordinaatit, jolloin tulee vaikka 3km alueella kaikkien: sijainti, tagit, nimi, ID
# tietyn storin tiedoston hakeminen /stories/storyID
# uuden stoorin lähettäminen /stories/post
# /stories1
# try with location 60.20157127986968, 24.934423183549658
 
testdata = testdata()

@app.route('/', methods=['GET'])
def stories():
    return "Server is up"

@app.route('/stories/<storyID>', methods=['GET'])
def getStoryByID(storyID):
    return 'Here you will find recording for story %s' % storyID

@app.route('/around/<lat>/<long>/', methods=['GET'])
def getStoriesAroundPoint(lat, long):
    return jsonify(get_stories_in_range(lat, long, testdata))

@app.route('/stories/post/<token>', methods=['POST'])
def createStoryPost(token):
    if tokenOK(token):
        req_data = request.get_json()

        StoryTitle = req_data['StoryTitle']
        Coordinates = req_data['Coordinates']
        LocationDescription = req_data['LocationDescription']
        #IdentifierHash = req_data['IdentifierHash']

        createstory(StoryTitle, Coordinates, LocationDescription)
        return 'POST OK'
    else: 
        return deny()

def deny():
    return "Access denied"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)