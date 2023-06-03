from flask import Flask, render_template
import requests
import json
import random


app = Flask(__name__)
app.debug = True


@app.route('/')
def get_memes_imgflip():
    url = "https://api.imgflip.com/get_memes"
    response = requests.request("GET",url).text
    response = json.loads(response)
    response = response['data']['memes'][random.randint(0,100)]
    meme_name = response['name']
    meme_url = response['url']
    print(meme_name)
    return render_template('index.html',meme_name = meme_name,meme_url = meme_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)


