print("SERVER STARTING...")
from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route("/scan_url", methods=["POST"])
def scan_url():
    data = request.json
    url = data.get("url", "")

    score = 0

    if "@" in url:
        score += 3
    if "secure" in url:
        score += 2
    if "-" in url:
        score += 1

    if score >= 5:
        status = "danger"
    elif score >= 2:
        status = "warning"
    else:
        status = "safe"

    return jsonify({
        "status": status,
        "score": score
    })

if _name_ == "_main_":
    app.run(debug=True)
