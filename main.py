from flask import *

app = Flask(__name__)


@app.route("/postListener", methods=['POST'])
def postListener():
    if request.method == "POST":
        return


if __name__ == '__main__':
    Flask.run(app, host="0.0.0.0", port=10000, debug=True)



