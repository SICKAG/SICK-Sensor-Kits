from flask import Flask, render_template, Response
import client
import os

app = Flask(__name__)

@app.route("/")
def start_page():
    return render_template('start.html')

@app.route("/play")
def start_play():
    return render_template('play.html') 

@app.route("/getCurrentSign", methods=['GET'])
def getCurrentSign():
    connection = client.run_client()
    if connection == "TimeoutError":
        eingabe = "Keine Verbindung"
    else:
        eingabe = client.get_request()
    return Response('{"sign": "' + eingabe + '"}',status=200)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)