from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    # Forcing Docker image 1.2m without merging before actions
    return "Hello all ACG Students!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
