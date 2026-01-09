import requests, time, threading, random
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- DIS5 MOTORU (2 Dakikalık Pusu Modu) ---
def attack_engine(phone):
    p = "".join(filter(str.isdigit, phone))
    if p.startswith("0"): p = p[1:]
    
    # Buradaki listeye kendi API'lerini ekleyebilirsin liderim
    # Motoru dokunulmaz kıldık, 24 saat boyunca 2 dk arayla vurur.
    while True:
        try:
            # Örnek İstek (Senin API listene göre genişletilir)
            # requests.post("API_URL", json={"phone": p})
            pass
        except:
            pass
        time.sleep(120)

# --- AVCI PANELİ (Lüks Design v12) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DIS5 - EUROPE'S OF PHONE</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            /* Arka plana logonun linkini aşağıya koy liderim */
            background: #000 url('https://i.ibb.co/vzYv3y5/dis5-logo.png') no-repeat center center fixed;
            background-size: contain;
            font-family: 'Orbitron', sans-serif;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        .avci-container {
            background: rgba(0, 0, 0, 0.9);
            border: 2px solid #ff6600;
            box-shadow: 0 0 50px rgba(0, 204, 255, 0.4);
            padding: 50px;
            border-radius: 30px;
            text-align: center;
            width: 400px;
            z-index: 10;
        }

        h1 {
            color: #ff6600;
            font-size: 22px;
            text-transform: uppercase;
            letter-spacing: 3px;
            margin-bottom: 5px;
        }

        .subtitle {
            color: #00ccff;
            font-size: 12px;
            margin-bottom: 30px;
            font-weight: bold;
        }

        input[type="text"] {
            width: 100%;
            padding: 15px;
            margin-bottom: 20px;
            background: #111;
            border: 1px solid #333;
            color: #00ccff;
            border-radius: 8px;
            text-align: center;
            font-size: 16px;
            box-sizing: border-box;
        }

        button {
            width: 100%;
            padding: 15px;
            background: #ff6600;
            color: #fff;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 18px;
            cursor: pointer;
            transition: 0.4s;
        }

        button:hover {
            background: #00ccff;
            box-shadow: 0 0 20px #00ccff;
        }

        #success-screen {
            display: none;
        }

        .op-logo {
            width: 100%;
            max-width: 250px;
            margin-bottom: 20px;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); opacity: 0.8; }
            50% { transform: scale(1.05); opacity: 1; }
            100% { transform: scale(1); opacity: 0.8; }
        }
    </style>
</head>
<body>

    <div class="avci-container" id="panel">
        <div id="input-screen">
            <h1>DIS5 Europe's Of Phone</h1>
            <p class="subtitle">AV DEĞİL, AVCI PANELİ</p>
            <form method="POST" onsubmit="startOp()">
                <input type="text" name="phone" placeholder="HEDEF NUMARA" required>
                <button type="submit">SUCCESS (TETİKLE)</button>
            </form>
        </div>

        <div id="success-screen">
            <img src="https://i.ibb.co/vzYv3y5/dis5-logo.png" class="op-logo">
            <h2 style="color: #ff6600;">OPERASYON BAŞLADI</h2>
            <p style="color: #00ccff;">Render Motoru Devreye Girdi.</p>
        </div>
    </div>

    <script>
        function startOp() {
            document.getElementById('input-screen').style.display = 'none';
            document.getElementById('success-screen').style.display = 'block';
            document.getElementById('panel').style.borderColor = '#00ccff';
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
    app.run(host="0.0.0.0", port=10000)
