from flask import *
import JsonManager

app = Flask(__name__)

jsonManager = JsonManager.JsonManager()

@app.route("/postListener", methods=['POST'])
def postListener():
    if request.method == "POST":
        current_data = request.get_json()
        print(current_data)
        jsonManager.write_data(current_data)
    return "ok"

@app.route("/getData", methods=['GET'])
def getData():
    if request.method == "GET":
        return jsonManager.read_data()


if __name__ == '__main__':
    Flask.run(app, host="0.0.0.0", port=10000, debug=True)



