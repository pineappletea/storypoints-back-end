from flask import Flask, request
import json
from getdata import testdata
from tokencheck import tokenOK
from createstory import createstory
app = Flask(__name__)
app.config["DEBUG"] = True

#hardcoded token as placeholder

# Kutsuihin tunnistautumistokenin lisääminen jos jää aikaa
# Halutut kutsut: /koordinaatit, jolloin tulee vaikka 3km alueella kaikkien: sijainti, tagit, nimi, ID
# tietyn storin tiedoston hakeminen /stories/storyID
# uuden stoorin lähettäminen /stories/post
# /stories1

@app.route('/', methods=['GET'])
def stories():
    return "nothing here"

@app.route('/stories/<storyID>/<token>', methods=['GET'])
def endpoint2(storyID, token):
    return 'Here you will find story %s' % storyID

@app.route('/around/<lat>/<long>/<token>', methods=['GET'])
def getStoriesAroundPoint(lat, long, token):
    if tokenOK(token):
        return 'Here is a list of stories 3km from %s, %s' % (lat, long)
    else:
        return deny()

@app.route('/stories/post/<token>', methods=['POST'])
def createStoryPost(token):
    if tokenOK(token):
        req_data = request.get_json()

        StoryTitle = req_data['StoryTitle']
        Coordinates = req_data['Coordinates']
        LocationDescription = req_data['LocationDescription']

        createstory(StoryTitle, Coordinates, LocationDescription)
        return 'POST OK'
    else: 
        return deny()

def deny():
    return "Access denied"
app.run()