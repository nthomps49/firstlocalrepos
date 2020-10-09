from flask import Flask
from flask import render_template
import os
import sys

def create_app():
        app = Flask(__name__)
        @app.route('/')
        def home():
                return render_template("index.html")

#Initialize our ngrok settings into flask
        app.config.from_mapping(
                BASE_URL="http://192.168.0.29:8888",
                USE_NGROK=os.environ.get("USE_NGROK", "False") == "True" and os.environ.get("WERKZEUG_RUN_MAIN") != "true"
    )
        if app.config.get("ENV") == "development" and app.config["USE_NGROK"]:
# pyngrok will only be installed, and should only ever be initialized, in a dev environment
                from pyngrok import ngrok
# Get the dev server port (defaults to 5000 for Flask, can be overridden with `--port`
# when starting the server
                port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 5000
# Open a ngrok tunnel to the dev server
                public_url = ngrok.connect(port)
                print(" * ngrok tunnel \"{}\" -> \"http://192.168.0.29:{}/\"".format(public_url, port))



        if __name__ == '__main__':
                app.run(host='192.168.0.29',port=8888,debug=False) #debug=True allows changes without manual recycle


