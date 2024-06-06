# https://trekhleb.dev/blog/2021/gyro-web/
# https://blog.miguelgrinberg.com/post/add-a-websocket-route-to-your-flask-2-x-application
from flask import Flask
from flask import send_from_directory
from flask_sock import Sock
import json

app = Flask(__name__,
            static_url_path='', 
            static_folder='/static_server_files',
            template_folder='web/templates')
sock = Sock(app)



@app.route('/')
def index():
    return send_from_directory('static_server_files', 'index.html')

@sock.route('/gyrodata')
def echo(sock):
    while True:
        data = sock.receive()
        data = json.loads(data)
        print(data["device"]["name"])
        print("Alpha:")
        print(data["gyroscope_data"]["alpha"])
        print("Beta:")
        print(data["gyroscope_data"]["beta"])
        print("Gamma:")
        print(data["gyroscope_data"]["gamma"])
        # sock.send(data)


if __name__ == "__main__":
    app.run(debug=True)