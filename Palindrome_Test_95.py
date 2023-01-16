from flask import Flask
import logging
import json

app = Flask(__name__)

@app.route('/palindrome/<word>', methods = ['GET'])
def palindrome(word):
    logging.info("Word received: [" + str(word) + "]")
    jsonResponse = buildJSON(word)
    logging.info("JSON obtained: {" + jsonResponse + "}")
    return jsonResponse

def times_letter(word):
    times = {}
    for i in word:
        if i in times.keys():
            times[i] += 1
        else:
            times[i] = 1
    return times

def buildJSON(word):
    re_verse =''.join(reversed(word))
    if word == re_verse:
        print("")
        r1 = {'name':f"{word}", 'palindrome': True, 'sorted': times_letter(word)}
        r1.update({'length': len(word)})
        return json.dumps(r1, indent=0)
    else:
        print("")
        r1 = {'name':f"{word}", 'palindrome': False}
        return json.dumps(r1, indent=0)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug = False)
