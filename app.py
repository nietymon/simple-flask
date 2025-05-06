from flask import Flask, render_template_string, jsonify
import urllib.request, json

app = Flask(__name__)
URL = "https://strugly.com/bt/ea1b01c4-46e3-4ba4-8430-754d228271c8/91a70fc58356e0eab21822ad2acf1a08"

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)

@app.route('/')
def index():
    try:
        dane = fetch_json(URL)
    except Exception as e:
        return f"Błąd pobierania danych", 500

    template = """
    ELO: {{ dane['elo'] }}, LVL: {{ dane['lvl'] }}, Today: {{ dane['telo'] }}, W: {{ dane['tw'] }}, L: {{ dane['tl'] }}, Last matches: {{ dane['lg'] }}
    """
    return render_template_string(template, dane=dane)

if __name__ == "__main__":
    app.run(debug=True)