# -*- coding: utf-8 -*-
import os
import json

VIDEO_URL = "https://<自分のドメイン>/stream.m3u8"

def lambda_handler(event, context):
    print(json.dumps(event))

    if event["request"]["type"] == "LaunchRequest":
      return video_template()

    print("request type unmatch")
    return help()

def help():
    title = "pi camera"
    speech = "This skill show your home camera."
    directives = [
        {
            "type": "Hint",
            "hint": {
                "type": "PlainText",
                "text": "open pi camera"
            }
        }
    ]

    return build_speechlet_response(title, speech, directives, SESSION_BODY_1)

def video_template():

    video_template = {
        "type": "VideoApp.Launch",
        "videoItem":
        {
            "source": VIDEO_URL,
            "metadata": {
                "title": "Pi Camera",
                "subtitle": "movie from raspberry pi"
            }
        }
    }

    body_template = {
        "type": "Display.RenderTemplate",
        "template": {
            "type": "BodyTemplate6",
            "token": "bt6",
            "backButton": "VISIBLE",
            "textContent": {
                "primaryText": {
                    "text": "camera finished.",
                    "type": "PlainText"
                }
            }
        }
    }

    directives = [
        video_template,
        body_template
    ]

    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": None,
            "card": {
                'type': 'Simple',
                'title': "video player",
                'content': "this template play video."
            },
            "directives": directives
        }
    }
    print(json.dumps(response))
    return response

def build_speechlet_response(title, speech, directives, phase):

    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "{}. do you want to see the next template?".format(speech)
            },
            "card": {
                'type': 'Simple',
                'title': title,
                'content': speech
            },
            "directives": directives,
            "shouldEndSession": False
        },
        "sessionAttributes": {
            "template": phase
        }
    }
    print(json.dumps(response))
    return response