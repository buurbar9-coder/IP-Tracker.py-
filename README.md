🕵️‍♂️ IP-TRACKER V1.0 
Tool casri ah oo loogu talagalay in lagu helo xogta IP-yada iyo macluumaadka aaladaha soo booqda link-gaaga, adigoo adeegsanaya Cloudflare Tunnel.
📝 SHARRAXAAD KOOBAN
Tool-kani wuxuu isticmaalaa Flask Framework Marka qofku riixo link-gaaga wuxuu si otomaatig ah u ururinayaa xogta soo socota:
 * 📡 IP Address: Cinwaanka internet-ka ee qofka
 * 🌍 Location: Wadanka iyo Magaalada uu qofku joogo
 * 📱 Device Info: Nooca mobile-ka ama computer-ka uu isticmaalayo
 * ⏰ Timestamp: Saacadda saxda ah ee uu link-ga furay
🚀 TILLAABOOYINKA RAKIBAADDA Sida loo soo dejiyo
Dooro nidaamka (OS) aad isticmaalayso:
📱 Android (Termux)
pkg update && pkg upgrade -y
pkg install python git cloudflared -y
git clone https://github.com/buurbar9-coder/IP-Tracker.py.git
cd IP-Tracker.py
pip install -r requirements.txt
python IP-Tracker.py

💻 Windows
 * Soo deji Python (python.org) iyo Git.
 * Furi CMD ama PowerShell:
<!-- end list -->
git clone https://github.com/buurbar9-coder/IP-Tracker.py.git
cd IP-Tracker.py
pip install -r requirements.txt
python IP-Tracker.py

🍎 macOS
brew install python git cloudflared
git clone https://github.com/buurbar9-coder/IP-Tracker.py.git
cd IP-Tracker.py
pip install -r requirements.txt
python3 IP-Tracker.py

⚙️ SETUP-KA BOT-KA
Ka hor inta aadan tool-ka shidin, fur faylka IP-Tracker.py oo ku qor macluumaadkan:
 * BOT_TOKEN: Ka soo qaado @BotFather.
 * CHAT_ID: Ka soo qaado @userinfobot.
🌐 SIDA LOO PUBLIC GAREEYO (Cloudflared)
isticmaal Cloudflared si aad u hesho link caalami ah:
 * run garee tool-ka (Terminal-ka koowaad): python IP-Tracker.py
 * Fur Terminal kale (Terminal-ka labaad) oo qor:
   cloudflared tunnel --url http://127.0.0.1:4500

 * Copy garee link-ga ku dhamaanaya .trycloudflare.com oo u dir qofka aad rabto
📋 XOGTA AAD HELAYSO
Marka qofku riixo link-gaaga waxaad Telegram-kaaga ku helaysaa xog dhamaystiran oo nidaamsan
👨‍💻 DEVELOPER INFO
 * Author: Hackerwd1 🎃
 * GitHub: buurbar9-coder
 * Status: Active ✅
