import requests
from imp import *
import ast


def msg_luis(inp):
    msg = endpoint + inp
    ldata = requests.get(msg)
    k = ast.literal_eval(ldata.text)
    top_intent = (k['topScoringIntent']['intent'])
    return top_intent


def get_message(inp):
    msg = endpoint + inp
    ldata = requests.get(msg)
    k = ast.literal_eval(ldata.text)
    top_intent = (k['topScoringIntent']['intent'])
    return top_intent
