import streamlit as st
import time
import re
import pandas as pd
import os
import urllib.parse
import socket
import ssl
import requests
from datetime import datetime

# 1. GLOBAL EXECUTIVE CONFIGURATION
st.set_page_config(page_title="SENTINEL | Strategic Risk Advisory", page_icon="🛡️", layout="wide")

if 'lead_saved' not in st.session_state:
    st.session_state['lead_saved'] = False

# 2. LOGIC & SECURITY ENGINES
def get_daily_slots():
    file_path = 'sentinel_leads.csv'
    limit = 3
    if os.path.isfile(file_path):
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        today_count = len(df[df['Date'].dt.date == datetime.now().date()])
        return max(0, limit - today_count)
    return limit

def sanitize_input(text, pattern, max_len=60):
    sanitized = re.sub(pattern, '', text)
    return sanitized[:max_len]

def is_valid_domain(domain):
    return re.match(r'^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$', domain.lower())

def is_corporate_email(email):
    forbidden = ['gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com', 'icloud.com']
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email): return False
    return email.split('@')[-1].lower() not in forbidden

def save_lead(domain, email, name):
    file_path = 'sentinel_leads.csv'
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = pd.DataFrame([[timestamp, domain, email, name]], 
                            columns=['Date', 'Domain', 'Email', 'Name'])
    if os.path.isfile(file_path):
        df_existing = pd.read_csv(file_path)
        if ((df_existing['Domain'] == domain) & (df_existing['Email'] == email)).any():
            return "exists"
        new_data.to_csv(file_path, mode='a', header=False, index=False)
    else:
        new_data.to_csv(file_path, index=False)
    return "saved"

# 3. HIGH-END VISUAL IDENTITY (CSS)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp { background-color: #ffffff; color: #1a1a1a; font-family: 'Inter', sans-serif; }
    .main-card { border: 1px solid #e1e4e8; background: #f8f9fa; padding: 40px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .btn-payment { display: block; background: #1a1a1a; color: #ffffff !important; text-align: center; padding: 20px; font-weight: 600; text-decoration: none; border-radius: 6px; margin-top: 25px; font-size: 1.1rem; transition: 0.2s; }
    .btn-payment:hover { background: #333333; transform: translateY(-1px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
    .preview-box { background: #eef2f7; padding: 20px; border-left: 4px solid #1a1a1a; margin: 20px 0; font-size: 0.9rem; color: #444; }
    .section-title { color: #888; font-size: 0.8rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; }
    .how-it-works { background-color: #f1f3f5; padding: 25px; border-radius: 10px; margin-bottom: 30px; border: 1px solid #dee2e6; }
    .legal-footer { text-align: center; color: #999; font-size: 0.7rem; line-height: 1.5; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 4. HEADER & DESCRIPTION
st.markdown('<p class="section-title">Sentinel | Strategic Risk Advisory</p>', unsafe_allow_html=True)
st.markdown("<h1>Digital Continuity & Asset Protection</h1>", unsafe_allow_html=True)

st.markdown("""
    <div class="how-it-works">
        <h3 style="color: #1a1a1a; margin-top: 0;">Our Methodology: Passive Risk Intelligence</h3>
        <p style="color: #444; font-size: 0.95rem;">
            Sentinel performs a <b>Passive OSINT (Open Source Intelligence)</b> assessment. We analyze your digital footprint from the outside, identifying what an external threat actor sees before they strike.
        </p>
        <div style="display: flex; gap: 20px; margin-top: 15px;">
            <div style="flex: 1;"><b style="color: #000;">1. Asset Mapping</b><br><span style="font-size: 0.85rem; color: #666;">We map every public server and cloud entry point.</span></div>
            <div style="flex: 1;"><b style="color: #000;">2. Vulnerability Scan</b><br><span style="font-size: 0.85rem; color: #666;">Detection of expired SSLs, open ports, and misconfigurations.</span></div>
            <div style="flex: 1;"><b style="color: #000;">3. Mitigation Roadmap</b><br><span style="font-size: 0.85rem; color: #666;">20-page executive guide to close gaps in 48h.</span></div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.divider()

# 5. MAIN INTERFACE
col1, col2 = st.columns([1.4, 1])

with col1:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("### 🛡️ Initiate Alpha Protocol")
    
    raw_domain = st.text_input("ENTER TARGET DOMAIN:", placeholder="company.com").strip().lower()
    target_url = sanitize_input(raw_domain, r'[^a-z0-9.-]')
    
    if target_url and is_valid_domain(target_url):
        st.markdown(f'<div class="preview-box"><b>PRELIMINARY SCAN: {target_url.upper()}</b><br>'
                    f'• Public asset exposure: IDENTIFIED<br>'
                    f'• OSINT reconnaissance: ACTIVE<br>'
                    f'• Criticality Level: HIGH PRIORITY</div>', unsafe_allow_html=True)
        
        raw_name = st.text_input("FULL NAME & EXECUTIVE TITLE:")
        user_name = sanitize_input(raw_name, r'[^a-zA-Z0-9 áéíóúÁÉÍÓÚ-]', 60)
        user_email = st.text_input("CORPORATE EMAIL:").strip().lower()
        
        if user_name and user_email:
            if is_corporate_email(user_email):
                if st.button("REGISTER ASSESSMENT ORDER"):
                    with st.spinner("Processing protocol..."):
                        status = save_lead(target_url, user_email, user_name)
                        st.session_state['lead_saved'] = True
                        if status == "saved": st.success("✔ Order registered. Priority slot locked.")
                        else: st.info("✔ Lead already in system. Access granted.")
            else:
                st.error("⚠️ Corporate email required. Public providers (Gmail/Yahoo) are restricted.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    slots_left = get_daily_slots()
    if st.session_state['lead_saved']:
        st.markdown('<div style="text-align: center; padding: 40px; border: 2px solid #1a1a1a; background:#ffffff; border-radius: 12px;">', unsafe_allow_html=True)
        st.markdown('<p class="section-title">TOTAL INVESTMENT</p>', unsafe_allow_html=True)
        st.markdown('<h1 style="font-size: 4rem; margin: 0;">$650</h1>', unsafe_allow_html=True)
        st.markdown(f'<p style="color: #d73a49; font-weight: bold; margin-top: 15px;">⚠️ {slots_left} SLOTS REMAINING TODAY</p>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("<p style='font-size: 0.9rem; text-align: left;'><b>Legal Authorization</b></p>", unsafe_allow_html=True)
        legal_check = st.checkbox("I certify that I have the legal authority to request this audit. I authorize a non-intrusive, passive OSINT assessment.")

        if legal_check:
            params = urllib.parse.urlencode({"checkout[email]": user_email, "checkout[name]": user_name, "checkout[custom][domain]": target_url})
            checkout_url = f"https://core-digital-ia.lemonsqueezy.com/checkout?{params}"
            st.markdown(f'<a href="{checkout_url}" target="_blank" class="btn-payment">ACTIVATE AUDIT NOW</a>', unsafe_allow_html=True)
        else:
            st.warning("Authorization required to proceed.")
            
        st.markdown('<p style="font-size: 0.85rem; color: #888; margin-top: 20px;">Includes 20-page Strategic Report + <24h Priority Delivery</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info(f"Submit target domain and contact details to unlock one of today's {slots_left} slots.")

# 6. LEGAL FOOTER
st.markdown("""
    <div class="legal-footer">
        <hr>
        <b>LEGAL NOTICE:</b> Sentinel operates strictly within ethical OSINT methodologies. 
        We do not perform penetration testing or unauthorized access to private systems. 
        This report is a strategic evaluation of public digital footprints. 
        By using this service, you agree that Sentinel is not liable for existing security breaches.
        Sentinel Unit © 2026.
    </div>
""", unsafe_allow_html=True)

# 7. ADMIN CONSOLE
with st.sidebar:
    if st.checkbox("Admin Console"):
        admin_pass = st.secrets.get("admin_key", "sentinel2026")
        access_key = st.text_input("Key", type="password")
        if access_key == admin_pass:
            if os.path.isfile('sentinel_leads.csv'):
                df = pd.read_csv('sentinel_leads.csv')
                st.write(f"Total Leads: {len(df)}")
                st.dataframe(df)
                st.download_button("Export CSV", df.to_csv(index=False), "leads.csv")
