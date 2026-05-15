import streamlit as st
import random
import time
from datetime import datetime
import zoneinfo
import requests
import base64

# ======================================================
# 🟢 MANUAL CONFIGURATION ZONE (ΑΥΤΑ ΑΛΛΑΖΕΙΣ ΓΙΑ ΚΑΘΕ ΝΕΟ ΠΕΛΑΤΗ)
# ======================================================

# 📋 ΚΕΙΜΕΝΑ ΕΠΙΧΕΙΡΗΣΗΣ
BRAND_NAME = "COFFEE LAB ILIOYPOLI"          # Το επίσημο όνομα του μαγαζιού (Φαίνεται και στην καρτέλα του browser)
SUBTITLE_TEXT = "SCAN & WIN // OFFICIAL HANDOUT" # Ο υπότιτλος κάτω από τον κεντρικό τίτλο

# 🎨 DESIGN & ΧΡΩΜΑΤΑ
# Μπορείς να βάλεις single χρώμα (π.χ. "#000000") ή CSS gradient όπως το παρακάτω
BG_GRADIENT = "linear-gradient(180deg, #00b4d8 0%, #0077b6 100%)" # Το φόντο της εφαρμογής
ACCENT_COLOR = "#00b4d8" # Το χρώμα που θα έχουν τα γράμματα μέσα στο Input Box όταν πληκτρολογεί ο πελάτης

# 📐 ΔΙΑΣΤΑΣΕΙΣ & ΕΛΕΓΧΟΣ LOGO
LOGO_FILE = "asset.png"       # Το όνομα του αρχείου της εικόνας. Πρέπει να είναι ΠΑΝΤΑ ίδιο με αυτό που ανεβάζεις στο GitHub
LOGO_WIDTH = "140px"          # Το πλάτος του logo στην οθόνη (Ρυθμίζεις σε pixels: π.χ. 120px, 150px, 180px)
LOGO_TOP_MARGIN = "15px"      # Το κενό (περιθώριο) από την κορυφή της οθόνης του κινητού μέχρι το logo
LOGO_BOTTOM_MARGIN = "5px"    # Το κενό ανάμεσα στο logo και τον κεντρικό τίτλο

# 🎁 ΔΩΡΑ ΚΑΙ ΠΙΘΑΝΟΤΗΤΕΣ (POOL & WEIGHTS MATRIX)
# ΠΡΟΣΟΧΗ: Ο αριθμός των στοιχείων στο REWARDS_POOL πρέπει να είναι ΙΔΙΟΣ με τον αριθμό των στοιχείων στο REWARDS_WEIGHTS
REWARDS_POOL = [
    "🎁 1+1 Καφές (Optimization Protocol)",
    "🎁 -20% στην επόμενη παραγγελία",
    "🎁 Δωρεάν Snack / Cookie",
    "🎁 Upgrade σε Large μέγεθος",
    "🎁 Free Extra Shot (Energy Boost)"
]
REWARDS_WEIGHTS = [5, 15, 15, 32.5, 32.5] # Οι πιθανότητες για κάθε δώρο αντίστοιχα (π.χ. 5%, 15% κτλ.)

# 📊 GOOGLE SHEETS DATABASE WEBHOOK
# Εδώ κάνεις επικόλληση το νέο URL που σου δίνει το Google Apps Script όταν στήνεις το καινούργιο Sheet του πελάτη
SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxDIQ0Iugg5j_7XAw1wx2NVOerhrwoVcCiznF9SyaPTjB1UZGHpalPFsFYLvoQc9K_HGA/exec"

# 📍 ΣΤΟΙΧΕΙΑ ΥΠΟΣΕΛΙΔΟΥ (FOOTER INFO)
LOCATION_TEXT = "Λεωφ. Ελ. Βενιζέλου 142, Ηλιούπολη" # Η διεύθυνση του καταστήματος
HOURS_TEXT = "Καθημερινά 06:00 - 21:00"              # Το ωράριο λειτουργίας


# ======================================================
# 🚨 SYSTEM ENGINE CORE - DO NOT TOUCH | DO NOT TOUCH | DO NOT TOUCH
# ======================================================

# Αρχικό Setup της σελίδας του Streamlit
st.set_page_config(page_title=BRAND_NAME, page_icon="🎯", layout="centered")

# CSS Injection: Κλειδώνει το Mobile Viewport, κάνει Reset τα native elements του Streamlit και κεντράρει τα πάντα
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Share+Tech+Mono&display=swap');
    
    /* Απόκρυψη του default header και footer του Streamlit για white-label εμφάνιση */
    [data-testid="stHeader"], footer {{ display: none !important; }}
    
    /* Κλείδωμα διαστάσεων container για mobile screen */
    .block-container {{
        padding-top: 1.2rem !important;
        padding-bottom: 1.2rem !important;
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
        max-width: 450px !important;
        margin: 0 auto !important;
    }}
    
    /* Εφαρμογή του background gradient του πελάτη */
    .stApp {{ background: {BG_GRADIENT}; }}
    
    /* Απόλυτο ευθυγράμμιση και κεντράρισμα όλων των στοιχείων της σελίδας */
    .element-container, .stVerticalBlock, [data-testid="stVerticalBlock"] {{
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
        text-align: center !important;
    }}
    
    /* Container για το λογότυπο με δυναμικά περιθώρια */
    .html-asset-container {{
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin-top: {LOGO_TOP_MARGIN} !important;       
        margin-bottom: {LOGO_BOTTOM_MARGIN} !important; 
    }}
    
    /* Ρυθμίσεις εικόνας logo με δυναμικό πλάτος και drop shadow */
    .html-asset-container img {{
        width: {LOGO_WIDTH} !important;                
        height: auto !important;
        display: block !important;
        filter: drop-shadow(0px 4px 8px rgba(0,0,0,0.15));
    }}
    
    h1, h2, h3, p, span, label {{
        font-family: 'Montserrat', sans-serif !important;
        color: #ffffff !important;
        text-align: center !important;
    }}
    
    /* CSS για τον κεντρικό τίτλο (Impact στυλ για high convertion) */
    .brand-title {{
        font-family: 'Impact', sans-serif !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 5px !important;
        margin-bottom: 4px !important;
        font-size: 26px !important;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
        width: 100% !important;
    }}
    
    /* CSS για τον υπότιτλο (Share Tech Mono γραμματοσειρά για arcade/gaming look) */
    .brand-subtitle {{
        font-family: 'Share Tech Mono', monospace !important;
        color: #f1f1f1 !important;
        font-size: 11px !important;
        letter-spacing: 1.5px;
        margin-bottom: 15px !important;
        width: 100% !important;
    }}

    /* Στυλιζάρισμα του Text Input Box */
    div['data-baseweb']="input" {{
        background-color: rgba(15, 15, 15, 0.92) !important;
        border: 2px solid #ffffff !important;
        border-radius: 8px !important;
        height: 52px !important;
        width: 100% !important;
    }}
    
    input {{
        color: {ACCENT_COLOR} !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: bold !important;
        font-size: 16px !important;
        text-align: center !important;
    }}
    
    .stTextInput {{ width: 100% !important; }}
    
    .stTextInput label p {{
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        margin-bottom: 6px !important;
    }}

    /* Στυλιζάρισμα του κεντρικού Action Button */
    .stButton {{ width: 100% !important; }}
    
    .stButton>button {{
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
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
    }}
    
    .stButton>button:active {{
        background-color: #ffffff !important;
        color: #0f0f0f !important;
    }}

    /* Το πλαίσιο που εμφανίζεται στην οθόνη επιτυχίας (όταν κερδίζει ο πελάτης) */
    .success-box {{
        background: rgba(15, 15, 15, 0.92);
        border: 2px solid #ffffff;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        width: 100% !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    }}
    
    .success-title {{
        color: {ACCENT_COLOR} !important;
        font-family: 'Impact', sans-serif !important;
        font-size: 26px;
    }}
    
    hr {{ border-color: rgba(255, 255, 255, 0.25) !important; }}

    /* Στυλιζάρισμα του Footer */
    .brand-footer {{
        margin-top: 15px !important;
        padding: 10px !important;
        background: rgba(15, 15, 15, 0.2);
        border-radius: 8px;
        width: 100% !important;
    }}
    .brand-footer p {{ margin: 2px 0 !important; font-size: 11px !important; }}
    .brand-footer span {{ font-weight: 700; }}
    </style>
    """, unsafe_allow_html=True)

# Μηχανισμός Base64: Διαβάζει το τοπικό αρχείο εικόνας και το κάνει embed απευθείας σε HTML
try:
    with open(LOGO_FILE, "rb") as asset_file:
        encoded_string = base64.b64encode(asset_file.read()).decode()
    st.markdown(f'<div class="html-asset-container"><img src="data:image/png;base64,{encoded_string}"></div>', unsafe_allow_html=True)
except:
    # Fail-safe: Αν δεν βρεθεί η εικόνα, τυπώνει απλό κείμενο για να μην κρασάρει η σελίδα
    st.markdown(f'<h1 class="brand-title">{BRAND_NAME}</h1>', unsafe_allow_html=True)

# Εκτύπωση των βασικών Headers της σελίδας
st.markdown('<h1 class="brand-title">ΟΛΟΚΛΗΡΩΣΕΣ ΤΗΝ ΑΠΟΣΤΟΛΗ!</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="brand-subtitle">{SUBTITLE_TEXT}</p>', unsafe_allow_html=True)

# Ανάγνωση των URL Parameters για τον έλεγχο κατάστασης (Anti-Cheat / Lock System)
query_params = st.query_params

# --- ΚΑΤΑΣΤΑΣΗ 1: Ο ΠΕΛΑΤΗΣ ΕΧΕΙ ΗΔΗ ΚΛΕΙΔΩΣΕΙ ΔΩΡΟ (COUPON SCREEN) ---
if "gift" in query_params:
    saved_gift = query_params["gift"]
    user_name = query_params.get("user", "Agent")
    start_ts = query_params["t"]
    st.balloons() # Native εφέ με μπαλόνια στην οθόνη επιτυχίας
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
    
    # Live HTML/JS Clock: Τρέχει ένα real-time countdown 24 ωρών στον browser του χρήστη
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

# --- ΚΑΤΑΣΤΑΣΗ 2: ΑΡΧΙΚΗ ΟΘΟΝΗ - ΦΟΡΜΑ ΕΙΣΑΓΩΓΗΣ ΣΤΟΙΧΕΙΩΝ (LEAD GATE) ---
else:
    st.markdown("<p style='text-align:center; font-size:14px; font-weight: bold; color: #ffffff; margin-bottom:4px;'>ΕΙΣΑΓΕΤΕ ΤΑ ΣΤΟΙΧΕΙΑ ΣΑΣ ΓΙΑ ΝΑ ΠΑΙΞΕΤΕ</p>", unsafe_allow_html=True)
    input_name = st.text_input("Όνομα ή ID:", value="", placeholder="@username")
    
    # Έλεγχος αν ο χρήστης έχει πληκτρολογήσει κάτι (Lead Validation)
    if input_name.strip() != "":
        st.markdown("<p style='color:#ffffff; text-align:center; font-weight: bold; font-size:14px; margin-bottom:4px;'>✓ Η ΣΥΝΔΕΣΗ ΕΝΕΡΓΟΠΟΙΗΘΗΚΕ</p>", unsafe_allow_html=True)
        if st.button('ΔΙΕΚΔΙΚΗΣΗ ΔΩΡΟΥ'):
            with st.spinner('Κλήρωση...'):
                # 1. Τυχαία επιλογή δώρου βάσει των weights που ορίστηκαν στην Config Zone
                final_reward = random.choices(REWARDS_POOL, weights=REWARDS_WEIGHTS, k=1)[0]
                current_ts = str(int(time.time()))
                
                # 2. Καταγραφή ώρας Ελλάδος (Europe/Athens)
                now_gr = datetime.now(zoneinfo.ZoneInfo("Europe/Athens"))
                
                # 3. Δημιουργία Payload για αποστολή στο Google Sheet
                payload = {
                    "Date": now_gr.strftime("%d/%m/%Y"), 
                    "Time": now_gr.strftime("%H:%M:%S"), 
                    "User": input_name.strip(), 
                    "Reward": final_reward
                }
                
                # 4. Ασύγχρονο HTTP POST Request στο Google Apps Script Webhook
                try: requests.post(SCRIPT_URL, json=payload, timeout=5)
                except: pass # Fail-safe: Αν το Sheet έχει καθυστέρηση, η εφαρμογή προχωράει κανονικά για να μην κολλήσει ο πελάτης
                
                # 5. Εγγραφή των στοιχείων στα URL Query Params για να κλειδώσει η οθόνη (Anti-Cheat Mechanism)
                st.query_params["gift"] = final_reward
                st.query_params["t"] = current_ts
                st.query_params["user"] = input_name.strip()
                st.rerun()
    else:
        # Αν το πεδίο είναι άδειο, το κουμπί παραμένει απενεργοποιημένο (Disabled Gate)
        st.button('ΔΙΕΚΔΙΚΗΣΗ ΔΩΡΟΥ (ΕΙΣΑΓΕΤΕ ΟΝΟΜΑ)', disabled=True)

# Εμφάνιση του Footer στο κάτω μέρος της σελίδας
st.markdown(f'<div class="brand-footer"><p>📍 Θα μας βρείτε στην: <span>{LOCATION_TEXT}</span></p><p>🕒 Open: <span>{HOURS_TEXT}</span></p></div>', unsafe_allow_html=True)
