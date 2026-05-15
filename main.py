# ======================================================
# PLATFORM ENGINE - MULTI-TENANT CORE LOYALTY PROTOCOL
# Generic System Setup // Production Ready // No Syntax Errors
# ======================================================

import streamlit as st
import random
import time
from datetime import datetime
import zoneinfo
import requests
import base64

# --- CONFIG ---
st.set_page_config(page_title="Protocol Portal", page_icon="🎯", layout="centered")

# ======================================================
# 📊 CENTRAL PLATFORM DATABASE (ADD ACCOUNTS HERE)
# ======================================================
CORE_DB = {
    "node01": {
        "title": "COFFEE LAB ILIOYPOLI",
        "endpoint": "https://script.google.com/macros/s/AKfycbw2qkoK1xDY9uZnRWXso3yjAbK-iV5KOW2IcSyaEPrQlEItfWkPZjQr_elQA2Fz3ZDNwg/exec",
        "asset": "asset.png",
        "theme_bg": "linear-gradient(180deg, #00b4d8 0%, #0077b6 100%)",
        "theme_accent": "#00b4d8",
        "pool": [
            "🎁 1+1 Καφές (Optimization Protocol)",
            "🎁 -20% στην επόμενη παραγγελία",
            "🎁 Δωρεάν Snack / Cookie",
            "🎁 Upgrade σε Large μέγεθος",
            "🎁 Free Extra Shot (Energy Boost)"
        ],
        "matrix": [5, 15, 15, 32.5, 32.5],
        "meta_loc": "Λεωφ. Ελ. Βενιζέλου 142, Ηλιούπολη",
        "meta_hrs": "Καθημερινά 06:00 - 21:00"
    }
}

query_params = st.query_params
active_id = query_params.get("id", None)

# --- CASE A: SYSTEM ACTIVE ON VALID NODE ---
if active_id in CORE_DB:
    node = CORE_DB[active_id]
    
    # Global CSS Reset & Theme Injection
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Share+Tech+Mono&display=swap');
        [data-testid="stHeader"], footer {{ display: none !important; }}
        .block-container {{ padding: 1.2rem !important; max-width: 450px !important; margin: 0 auto !important; }}
        .stApp {{ background: {node['theme_bg']}; }}
        .element-container, .stVerticalBlock, [data-testid="stVerticalBlock"] {{
            display: flex !important; flex-direction: column !important; align-items: center !important; justify-content: center !important; width: 100% !important; text-align: center !important;
        }}
        .html-asset-container {{ display: flex !important; justify-content: center !important; align-items: center !important; width: 100% !important; margin-top: 5px !important; margin-bottom: 10px !important; }}
        .html-asset-container img {{ width: 130px !important; height: auto !important; display: block !important; filter: drop-shadow(0px 4px 8px rgba(0,0,0,0.15)); }}
        h1, h2, h3, p, span, label {{ font-family: 'Montserrat', sans-serif !important; color: #ffffff !important; text-align: center !important; }}
        .brand-title {{ font-family: 'Impact', sans-serif !important; font-weight: 900 !important; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 5px !important; font-size: 26px !important; text-shadow: 0 2px 8px rgba(0, 0, 0, 0.25); width: 100% !important; }}
        .brand-subtitle {{ font-family: 'Share Tech Mono', monospace !important; color: #f1f1f1 !important; font-size: 11px !important; letter-spacing: 1.5px; margin-bottom: 15px !important; width: 100% !important; }}
        div['data-baseweb']="input" {{ background-color: rgba(15, 15, 15, 0.92) !important; border: 2px solid #ffffff !important; border-radius: 8px !important; height: 52px !important; width: 100% !important; }}
        input {{ color: {node['theme_accent']} !important; font-family: 'Montserrat', sans-serif !important; font-weight: bold !important; font-size: 16px !important; text-align: center !important; }}
        .stTextInput {{ width: 100% !important; }}
        .stTextInput label p {{ color: #ffffff !important; font-weight: 700 !important; font-size: 14px !important; margin-bottom: 6px !important; }}
        .stButton {{ width: 100% !important; }}
        .stButton>button {{ width: 100% !important; height: 54px !important; background-color: #0f0f0f !important; color: #ffffff !important; font-family: 'Montserrat', sans-serif !important; font-weight: 900 !important; border: 2px solid #ffffff !important; border-radius: 8px !important; text-transform: uppercase; letter-spacing: 1px; font-size: 16px !important; box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2); }}
        .success-box {{ background: rgba(15, 15, 15, 0.92); border: 2px solid #ffffff; border-radius: 8px; padding: 20px; text-align: center; width: 100% !important; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3); }}
        .success-title {{ color: {node['theme_accent']} !important; font-family: 'Impact', sans-serif !important; font-size: 26px; }}
        hr {{ border-color: rgba(255, 255, 255, 0.25) !important; }}
        .brand-footer {{ margin-top: 15px !important; padding: 10px !important; background: rgba(15, 15, 15, 0.2); border-radius: 8px; width: 100% !important; }}
        .brand-footer p {{ margin: 2px 0 !important; font-size: 11px !important; }}
        .brand-footer span {{ font-weight: 700; }}
        </style>
    """, unsafe_allow_html=True)

    # Dynamic Base64 Asset Load
    try:
        with open(node["asset"], "rb") as asset_file:
            encoded_string = base64.b64encode(asset_file.read()).decode()
        st.markdown(f'<div class="html-asset-container"><img src="data:image/png;base64,{encoded_string}"></div>', unsafe_allow_html=True)
    except:
        st.markdown(f'<h1 class="brand-title">{node["title"]}</h1>', unsafe_allow_html=True)

    st.markdown('<h1 class="brand-title">ΟΛΟΚΛΗΡΩΣΕΣ ΤΗΝ ΑΠΟΣΤΟΛΗ!</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="brand-subtitle">SCAN & WIN // {node["title"]}</p>', unsafe_allow_html=True)

    if "gift" in query_params:
        saved_gift = query_params["gift"]
        user_name = query_params.get("user", "Agent")
        start_ts = query_params["t"]
        st.balloons()
        st.markdown(f"""
            <div class="success-box">
                <div class="success-title">🎯 ΚΕΡΔΙΣΕΣ!</div>
                <p style='font-size: 15px; margin-top: 4px; color: #aaaaaa; margin-bottom: 0;'>ID: <span style='color:#ffffff; font-weight:bold;'>{user_name}</span></p>
                <div style='background-color: #111111; padding: 12px; border-radius: 6px; margin-top: 10px; border: 1px solid #ffffff;'>
                    <p style='font-size: 18px; font-weight: 900; color: #ffffff; margin: 0;'>{saved_gift}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<p style='font-size:13px; text-align:center;'>ℹ️ Δείξε την οθόνη στο ταμείο <u><b>ΚΑΙ</b></u> παράδωσε τη φυσική κάρτα.</p>", unsafe_allow_html=True)
        
        # Real-time Clock Engine
        live_clock_html = f"""
        <div id="countdown-box" style="font-family: 'Share Tech Mono', monospace; font-size: 16px; font-weight: bold; color: #ff4b4b; text-align: center; background-color: #0f0f0f; padding: 12px; border-radius: 8px; border: 2px solid #ff4b4b;">Initializing...</div>
        <script>
        const startTimestamp = parseInt("{start_ts}");
        function updateClock() {{
            const currentTimestamp = Math.floor(Date.now() / 1000);
            const remainingTime = 86400 - (currentTimestamp - startTimestamp);
            const box = document.getElementById("countdown-box");
            if (remainingTime <= 0) {{ box.innerHTML = "❌ ΤΟ ΚΟΥΠΟΝΙ ΕΛΗΞΕ!"; }}
            else {{
                const hours = Math.floor(remainingTime / 3600); const minutes = Math.floor((remainingTime % 3600) / 60); const seconds = remainingTime % 60;
                box.innerHTML = "⏳ ΛΗΞΗ ΣΕ: " + (hours < 10 ? "0" : "") + hours + ":" + (minutes < 10 ? "0" : "") + minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
            }}
        }}
        setInterval(updateClock, 1000); updateClock();
        </script>
        """
        st.components.v1.html(live_clock_html, height=45)
        st.warning("🔒 Η προσπάθεια κλείδωσε. Ισχύει μια εξαργύρωση ανά κάρτα.")
    else:
        st.markdown("<p style='text-align:center; font-size:14px; font-weight: bold; color: #ffffff; margin-bottom:4px;'>ΕΙΣΑΓΕΤΕ ΤΑ ΣΤΟΙΧΕΙΑ ΣΑΣ ΓΙΑ ΝΑ ΠΑΙΞΕΤΕ</p>", unsafe_allow_html=True)
        input_name = st.text_input("Όνομα ή ID:", value="", placeholder="@username")
        if input_name.strip() != "":
            if st.button('ΔΙΕΚΔΙΚΗΣΗ ΔΩΡΟΥ'):
                final_reward = random.choices(node["pool"], weights=node["matrix"], k=1)[0]
                current_ts = str(int(time.time()))
                now_gr = datetime.now(zoneinfo.ZoneInfo("Europe/Athens"))
                payload = {"Date": now_gr.strftime("%d/%m/%Y"), "Time": now_gr.strftime("%H:%M:%S"), "User": input_name.strip(), "Reward": final_reward}
                try: requests.post(node["endpoint"], json=payload, timeout=5)
                except: pass
                st.query_params["id"] = active_id
                st.query_params["gift"] = final_reward
                st.query_params["t"] = current_ts
                st.query_params["user"] = input_name.strip()
                st.rerun()
        else:
            st.button('ΔΙΕΚΔΙΚΗΣΗ ΔΩΡΟΥ (ΕΙΣΑΓΕΤΕ ΟΝΟΜΑ)', disabled=True)

    st.markdown(f'<div class="brand-footer"><p>📍 Θα μας βρείτε στην: <span>{node["meta_loc"]}</span></p><p>🕒 Open: <span>{node["meta_hrs"]}</span></p></div>', unsafe_allow_html=True)

# --- CASE B: SYSTEM ROOT (GENERIC TECH PORTAL) ---
else:
    st.markdown("""
        <style>
        [data-testid="stHeader"], footer { display: none !important; }
        .stApp { background-color: #0a0a0c; }
        .block-container { max-width: 500px !important; padding-top: 5rem !important; }
        .main-card { background: #111115; border: 1px solid #22222b; border-radius: 12px; padding: 40px; text-align: center; box-shadow: 0 15px 35px rgba(0,0,0,0.4); }
        h1 { font-family: 'Impact', sans-serif; color: #ffffff; font-size: 32px; letter-spacing: 2px; }
        p { font-family: 'Helvetica Neue', sans-serif; color: #8a8a93; font-size: 14px; line-height: 1.6; }
        .badge { display: inline-block; background: #22222b; color: #00b4d8; font-family: monospace; font-size: 12px; padding: 4px 10px; border-radius: 20px; margin-bottom: 15px; font-weight: bold; }
        </style>
        <div class="main-card">
            <div class="badge">VIBE PROTOCOL v1.0</div>
            <h1>CORE PORTAL</h1>
            <p>Η B2B πλατφόρμα διαχείρισης loyalty & real-time rewards είναι ενεργή.<br>Συνδεθείτε μέσω του επίσημου QR Code της επιχείρησής σας.</p>
        </div>
    """, unsafe_allow_html=True)