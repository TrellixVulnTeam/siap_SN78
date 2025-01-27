from vino import Vino
import json
import ast

def convertToJson(vina, naziv):
    #jsonData = "["
    jsonData = "["
    for v in vina:
        # jsonData += "{\"country\":\"" + d.__getattribute__('country')
        # jsonData += "\", \"description\":\"" + str(d.__getattribute__('description'))
        # jsonData += "\", \"points\":\"" + d.__getattribute__('points')
        # jsonData += "\", \"price\":\"" + str(d.__getattribute__('price'))
        # jsonData += "\", \"province\":\"" + d.__getattribute__('province')
        # jsonData += "\", \"taster_name\":\"" + str(d.__getattribute__('taster_name'))
        # jsonData += "\", \"title\": \"" + d.__getattribute__('title')
        # jsonData += "\", \"variety\": \"" + d.__getattribute__('variety')
        # jsonData += "\", \"winery\": \"" + d.__getattribute__('winery') + "\"},"
        jsonString = Vino.to_dict(v)
        jsonData += json.dumps(jsonString)
        jsonData += ","

    jsonData = jsonData[:-1]
    jsonData += "]"
    with open(naziv + '.json', 'w') as outfile:
        json.dump(jsonData, outfile)

def convertFromJson(naziv):
    with open(naziv+'_set.json') as f:
        data = json.load(f)
    data = data.split("{")
    retVal = []
    for d in data:
        if(d!="["):
            d = d.replace("null", "\"\"")
            d = "{"+d[:-1]
            aaad = ast.literal_eval(d)
            retVal.append(aaad)
    return retVal

def convertParametri(noveTezine, zaPoredjenje):
    data = {}
    data['noveTezine'] = noveTezine
    data['zaPoredjenje'] = zaPoredjenje
    jsonData = json.dumps(data)
    with open('parametri.json', 'w') as outfile:
        json.dump(jsonData, outfile)
