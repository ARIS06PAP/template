# ======================================================
# COFFEELAB PROJECT - MAXIMUM MOBILE OPTIMIZED (ARTISTIC EDITION)
# Features: Viewport Lock, Lead Gate, Rarity Weights, Live 24h Clock, Base64 Logo
# ======================================================

import streamlit as st
import random
import time
from datetime import datetime
import zoneinfo
import requests
import base64

# --- CONFIG ---
st.set_page_config(page_title="Coffee Lab Rewards", page_icon="☕", layout="centered")

# 🚨 PRODUCTION GOOGLE APPS SCRIPT URL LOCKED
SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxo3n9YYtmpVLJ_glXrkeuc0LjgrqLKRQH6Nd5CsetOUqWQew3rUx__kFgyse287Kgc9w/exec"

# --- THE ULTIMATE GLOBAL MOBILE RESET & CENTER (CSS INJECT) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Share+Tech+Mono&display=swap');
    
    /* 1. Global Reset & Streamlit Native Element Override */
    [data-testid="stHeader"], footer {
        display: none !important;
    }
    
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 1.2rem !important;
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
        max-width: 450px !important;
        margin: 0 auto !important;
    }
    
    /* Coffee Lab Official Cyan Background */
    .stApp { 
        background: linear-gradient(180deg, #00b4d8 0%, #0077b6 100%);
    }
    
    /* FORCE ABSOLUTE CENTER ON EVERYTHING WITH FADE-IN ANIMATION */
    .element-container, .stVerticalBlock, [data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
        text-align: center !important;
        animation: fadeIn 0.5s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(5px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Απόλυτο Κεντράρισμα του Custom HTML Logo Container */
    .html-logo-container {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin-top: 5px !important;
        margin-bottom: 10px !important;
        text-align: center !important;
    }
    
    .html-logo-container img {
        width: 130px !important;
        height: auto !important;
        display: block !important;
        filter: drop-shadow(0px 4px 8px rgba(0,0,0,0.15));
    }
    
    /* TYPOGRAPHY & SCALING UPTICK */
    h1, h2, h3, p, span, label {
        font-family: 'Montserrat', sans-serif !important;
        color: #ffffff !important;
        text-align: center !important;
    }
    
    .brand-title {
        font-family: 'Impact', 'Montserrat', sans-serif !important;
        font-weight: 900 !important;
        color: #ffffff !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 5px !important;
        margin-bottom: 4px !important;
        font-size: 26px !important;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
        width: 100% !important;
    }
    
    .brand-subtitle {
        font-family: 'Share Tech Mono', monospace !important;
        color: #f1f1f1 !important;
        font-size: 11px !important;
        letter-spacing: 1.5px;
        margin-bottom: 15px !important;
        text-shadow: 0 1px 4px rgba(0, 0, 0, 0.15);
        width: 100% !important;
    }

    /* PERFECT MOBILE INPUT BOX WITH GLOW */
    div['data-baseweb']="input" {
        background-color: rgba(15, 15, 15, 0.92) !important;
        border: 2px solid #ffffff !important;
        border-radius: 8px !important;
        height: 52px !important;
        width: 100% !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: box-shadow 0.3s ease;
    }
    
    div['data-baseweb']="input"]:focus-within {
        box-shadow: 0 0 15px rgba(255,255,255,0.4) !important;
    }
    
    input {
        color: #00b4d8 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: bold !important;
        font-size: 16px !important;
        text-align: center !important;
    }
    
    .stTextInput {
        width: 100% !important;
    }
    
    .stTextInput label p {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        margin-bottom: 6px !important;
        text-align: center !important;
        width: 100% !important;
    }

    /* THUMB-FRIENDLY ACTION BUTTON WITH HOVER EFFECT */
    .stButton {
        width: 100% !important;
    }
    
    .stButton>button {
        width: 100% !important;
        height: 54px !important;
        background-color: #0f0f0f !important; 
        color: #ffffff !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 900 !important;
        border: 2px solid #ffffff !important;
        border-radius: 8px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 16px !important;
        transition: all 0.2s ease;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
    }
    
    .stButton>button:active {
        background-color: #ffffff !important;
        color: #0077b6 !important;
        transform: scale(0.98);
    }
    
    .stButton>button:disabled {
        background-color: rgba(15, 15, 15, 0.5) !important;
        color: #777777 !important;
        border: 2px solid rgba(255, 255, 255, 0.2) !important;
    }

    /* SUCCESS COUPON SCREEN BLOCK */
    .success-box {
        background: rgba(15, 15, 15, 0.92);
        border: 2px solid #ffffff;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        width: 100% !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    }
    
    .success-title {
        color: #00b4d8 !important;
        font-family: 'Impact', sans-serif !important;
        font-size: 26px;
        letter-spacing: 1px;
    }
    
    .stAlert {
        padding: 10px !important;
        font-size: 13px !important;
        width: 100% !important;
        border-radius: 8px !important;
    }
    
    hr {
        border-color: rgba(255, 255, 255, 0.25) !important;
        width: 100% !important;
        margin-top: 10px !important;
        margin-bottom: 10px !important;
    }

    /* ARTISTIC BRAND FOOTER */
    .brand-footer {
        margin-top: 15px !important;
        padding: 10px !important;
        background: rgba(15, 15, 15, 0.2);
        border-radius: 8px;
        width: 100% !important;
    }
    .brand-footer p {
        margin: 2px 0 !important;
        font-size: 11px !important;
        color: #f1f1f1 !important;
    }
    .brand-footer span {
        font-weight: 700;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BULLETPROOF HTML LOGO INJECTION ---
try:
    with open("logolab.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
        <div class="brand-logo-wrapper" style="display: flex; justify-content: center; width: 100%;">
            <div class="html-logo-container">
                <img src="data:image/png;base64,{encoded_string}" alt="Coffee Lab Logo">
            </div>
        </div>
    """, unsafe_allow_html=True)
except:
    st.markdown("""
        <div style="display:flex; justify-content:center; align-items:center; flex-direction: column; margin-top:5px; margin-bottom:15px;">
            <span style="font-family: 'Impact', sans-serif; font-size: 36px; font-weight: 900; color: #ffffff; line-height: 0.9;">COFFEE</span>
            <span style="font-family: 'Impact', sans-serif; font-size: 36px; font-weight: 900; color: #0f0f0f; letter-spacing: 2px;">LAB</span>
        </div>
    """, unsafe_allow_html=True)

# --- HEADERS ---
st.markdown('<h1 class="brand-title">ΟΛΟΚΛΗΡΩΣΕΣ ΤΗΝ ΑΠΟΣΤΟΛΗ!</h1>', unsafe_allow_html=True)
st.markdown('<p class="brand-subtitle">SCAN & WIN // COFFEE LAB ILIOYPOLI HANDOUT</p>', unsafe_allow_html=True)

rewards = [
    "🎁 1+1 Καφές (Optimization Protocol)",
    "🎁 -20% στην επόμενη παραγγελία",
    "🎁 Δωρεάν Snack / Cookie",
    "🎁 Upgrade σε Large μέγεθος",
    "🎁 Free Extra Shot (Energy Boost)"
]
reward_weights = [5, 15, 15, 32.5, 32.5]

query_params = st.query_params

# 1. CHECK STATUS (Αν ο χρήστης έχει ήδη κλειδωμένο δώρο)
if "gift" in query_params:
    saved_gift = query_params["gift"]
    user_name = query_params.get("user", "Agent")
    start_ts = query_params["t"]

    st.balloons()
    
    st.markdown(f"""
        <div class="success-box">
            <div class="success-title">🎯 ΚΕΡΔΙΣΕΣ!</div>
            <p style='font-size: 15px; margin-top: 4px; color: #aaaaaa; margin-bottom: 0;'>ID: <span style='color:#ffffff; font-weight:bold;'>{user_name}</span></p>
            <div style='background-color: #0077b6; padding: 12px; border-radius: 6px; margin-top: 10px; border: 1px solid #ffffff;'>
                <p style='font-size: 18px; font-weight: 900; color: #ffffff; margin: 0;'>{saved_gift}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='font-size:13px; text-align:center;'>ℹ️ Δείξε την οθόνη στο ταμείο <u><b>ΚΑΙ</b></u> παράδωσε τη φυσική κάρτα.</p>", unsafe_allow_html=True)
    st.write("---")

    # 🕒 LIVE EMBEDDED CLOCK VIA HTML/JS
    live_clock_html = f"""
    <div id="countdown-box" style="
        font-family: 'Share Tech Mono', monospace;
        font-size: 16px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
        background-color: #0f0f0f;
        padding: 12px;
        border-radius: 8px;
        border: 2px solid #ff4b4b;
    ">
        Initializing Real-Time Clock...
    </div>

    <script>
    const startTimestamp = parseInt("{start_ts}");
    
    function updateClock() {{
        const now = new Date();
        const currentTimestamp = Math.floor(Date.now() / 1000);
        
        const timeStr = now.toLocaleTimeString('el-GR', {{ hour12: false }});
        const dateStr = now.toLocaleDateString('el-GR');
        
        const elapsedTime = currentTimestamp - startTimestamp;
        const remainingTime = 86400 - elapsedTime;
        
        const box = document.getElementById("countdown-box");
        
        if (remainingTime <= 0) {{
            box.innerHTML = "❌ ΤΟ ΚΟΥΠΟΝΙ ΕΛΗΞΕ!<br><span style='font-size:11px; color:gray;'>🔒 Το χρονικό όριο των 24 ωρών παρήλθε.</span>";
            box.style.borderColor = "#ff4b4b";
        }} else {{
            const hours = Math.floor(remainingTime / 3600);
            const minutes = Math.floor((remainingTime % 3600) / 60);
            const seconds = remainingTime % 60;
            
            const timerStr = 
                (hours < 10 ? "0" : "") + hours + ":" + 
                (minutes < 10 ? "0" : "") + minutes + ":" + 
                (seconds < 10 ? "0" : "") + seconds;
            
            box.innerHTML = "📅 " + dateStr + " — ⏰ " + timeStr + "<br><span style='color:#00b4d8;'>⏳ ΛΗΞΗ ΣΕ: " + timerStr + "</span>";
        }}
    }}

    setInterval(updateClock, 1000);
    updateClock();
    </script>
    """
    st.components.v1.html(live_clock_html, height=90)
    st.warning("🔒 Η προσπάθεια κλείδωσε. Ισχύει μια εξαργύρωση ανά κάρτα.")

else:
    # 2. INITIAL STATE - DATA CAPTURE (Lead Gate)
  
    input_name = st.text_input("Όνομα ή Instagram ID:", value="", placeholder="@username")
    st.write("---")
    
    if input_name.strip() != "":
        st.markdown("<p style='color:#ffffff; text-align:center; font-weight: bold; font-size:14px; text-shadow: 0 1px 3px rgba(0,0,0,0.3); margin-bottom:4px;'>✓ Η ΣΥΝΔΕΣΗ ΕΝΕΡΓΟΠΟΙΗΘΗΚΕ</p>", unsafe_allow_html=True)
        
        if st.button('ΔΙΕΚΔΙΚΗΣΗ ΔΩΡΟΥ'):
            with st.spinner('Κλήρωση...'):
                
                final_reward = random.choices(rewards, weights=reward_weights, k=1)[0]
                current_ts = str(int(time.time()))
                
                # 📊 BACKGROUND GOOGLE PUSH (HTTP POST)
                tz = zoneinfo.ZoneInfo("Europe/Athens")
                now_gr = datetime.now(tz)
                
                payload = {
                    "Date": now_gr.strftime("%d/%m/%Y"),
                    "Time": now_gr.strftime("%H:%M:%S"),
                    "User": input_name.strip(),
                    "Reward": final_reward
                }
                
                try:
                    requests.post(SCRIPT_URL, json=payload, timeout=5)
                except:
                    pass 

                st.query_params["gift"] = final_reward
                st.query_params["t"] = current_ts
                st.query_params["user"] = input_name.strip()
                
                st.rerun()
    else:
        st.button('ΔΙΕΚΔΙΚΗΣΗ ΔΩΡΟΥ (ΕΙΣΑΓΕΤΕ ΟΝΟΜΑ)', disabled=True)

# --- BRAND FOOTER ---
st.markdown("""
    <div class="brand-footer">
        <p>📍 Θα μας βρείτε στην: <span>Λεωφ. Σοφοκλή Βενιζέλου 106, Ηλιούπολη</span></p>
        <p>🕒 Open: <span>Καθημερινά 07:00 - 23:00</span></p>
    </div>
""", unsafe_allow_html=True)
