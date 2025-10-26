import flask
from flask import Flask
from flask import render_template as rt

app = Flask(__name__)

@app.route("/")
def main():
   return rt('index.html')

if __name__ == "__main__":
   app.run()
