from flask import Flask, render_template, request, send_file, redirect, url_for
import json
from scanner import scan_target
from report_generator import create_pdf

app = Flask(__name__)
HISTORY_FILE = "history.json"


def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_history(data):
    history = load_history()
    history.insert(0, data)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history[:10], f, indent=2)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        results = scan_target(url)
        save_history(results)
        return render_template("result.html", r=results)

    return render_template("index.html")


@app.route("/history")
def history():
    return render_template("history.html", history=load_history())


@app.route("/download")
def download():
    history = load_history()
    if not history:
        return redirect(url_for("index"))

    pdf_path = create_pdf(history[0])
    return send_file(pdf_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)