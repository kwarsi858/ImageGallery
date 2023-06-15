from flask import Flask, request
import requests
from dotenv import load_dotenv
import os


load_dotenv(dotenv_path='backend\.venv\.env.local')
print(os.environ)

UNSPLASH_URL='https://api.unsplash.com/photos/random'
UNSPLASH_KEY='he67RjmIs-GS8LLBDMvPNOGIKHJ8JU4Osh9CXrTkhtc'



app = Flask(__name__)

@app.route('/new-image')
def new_image():
    word = request.args.get("query")
    headers = {
               "Accept-Version": "v1",
               }
    params = {
        "query": word,
        "client_id": UNSPLASH_KEY
    }
    response = requests.get(url=UNSPLASH_URL,headers=headers,params=params)

    data = response.json()
    return data
    


if __name__ == '__main__':

    app.run(debug=True)
