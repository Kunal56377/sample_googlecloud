from flask import Flask

app = Flask(__name__)

@app.route("/hello")

def hello_world():
    
    return "Hello, World!,First Github action CICD"


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
    
	app.run(host="0.0.0.0", port = 8080)