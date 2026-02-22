import streamlit as st
import socket
import ssl
import requests
import re
import pandas as pd
import os
import urllib.parse
from datetime import datetime

# =========================================================
# 1. CONFIGURACIÓN SOBERANA (TELEGRAM)
# =========================================================
TELEGRAM_TOKEN = "TU_TOKEN_AQUÍ"
TELEGRAM_CHAT_ID = "TU_CHAT_ID_AQUÍ"

# =========================================================
# 2. MOTOR DE ANÁLISIS INTERNO (OSINT PASIVO)
# =========================================================
def run_internal_scan(domain):
    results = {"hits": [], "level": "LOW", "top_finding": "No critical exposure"}
    
    # A. Subdominios Olvidados (Gatillo de curiosidad)
    subdomains = ['dev', 'test', 'staging', 'api', 'vpn', 'admin']
    for sub in subdomains:
        try:
            target = f"{sub}.{domain}"
            socket.gethostbyname(target)
            results['hits'].append(f"EXPOSURE: Unprotected subdomain detected: {target}")
            if results['level'] != "CRITICAL": results['level'] = "HIGH"
        except: continue

    # B. Puertos de Bases de Datos (Gatillo de miedo)
    db_ports = {3306: "MySQL", 27017: "MongoDB", 5432: "PostgreSQL", 9200: "Elasticsearch", 6379: "Redis"}
    for port, name in db_ports.items():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2.0)
            if s.connect_ex((domain, port)) == 0:
                results['hits'].append(f"CRITICAL: Exposed {name} database port (unauthorized access risk).")
                results['level'] = "CRITICAL"

    # C. Archivos Críticos y SSL
    try:
        # Check de archivo .env
        env_res = requests.get(f"https://{domain}/.env", timeout=2, verify=False)
        if env_res.status_code == 200:
            results['hits'].append("CRITICAL: Environment configuration file (.env) is public.")
            results['level'] = "CRITICAL"
        
        # SSL Status
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=2) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                ssock.getpeercert()
    except:
        results['hits'].append("HIGH: SSL/TLS vulnerabilities or misconfiguration.")
        if results['level'] == "LOW": results['level'] = "HIGH"

    if results['hits']: results['top_finding'] = results['hits'][0]
    return results

def send_telegram_alert(domain, hits, email, name, top_finding):
    findings = "\n".join([f"• {h}" for h in hits])
    msg = (f"🛡️ *SENTINEL: NEW LEAD DETECTED*\n\n"
           f"🔥 *Top Critical:* {top_finding}\n"
           f"👤 *Client:* {name}\n"
           f"📧 *Email:* {email}\n"
           f"🌐 *Domain:* {domain}\n\n"
           f"📋 *Full Scan Results:*\n{findings}")
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try: requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    except: pass

# =========================================================
# 3. INTERFAZ DE VENTA (ESTÉTICA HIGH-END)
# =========================================================
st.set_page_config(page_title="SENTINEL | Strategic Risk Advisory", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1a1a1a; font-family: 'Inter', sans-serif; }
    .main-card { border: 1px solid #e1e4e8; background: #f8f9fa; padding: 40px; border-radius: 12px; }
    .btn-payment { display: block; background: #1a1a1a; color: #ffffff !important; text-align: center; padding: 18px; font-weight: 800; text-decoration: none; border-radius: 6px; margin-top: 15px; font-size: 1.1rem; }
    .btn-tripwire { background: #444444; }
    .critical-alert { background: #fff5f5; border-left: 5px solid #e53e3e; padding: 15px; margin: 10px 0; color: #c53030; font-weight: bold; font-size: 0.9rem; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p style="color:#888; font-weight:700; letter-spacing:1.5px;">SENTINEL | STRATEGIC RISK ADVISORY</p>', unsafe_allow_html=True)
st.markdown("<h1>Digital Continuity & Asset Protection</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader("🛡️ Alpha Protocol Initiation")
    domain_input = st.text_input("ENTER TARGET DOMAIN:").strip().lower()
    
    if domain_input:
        with st.spinner("Analyzing risk surface..."):
            scan = run_internal_scan(domain_input)
            if scan['hits']:
                st.markdown(f"### ⚠️ {scan['level']} RISK VECTORS DETECTED")
                for hit in scan['hits']:
                    st.markdown(f'<div class="critical-alert">{hit}</div>', unsafe_allow_html=True)
            else: st.success("Initial scan clear. Advanced vectors may still be present in the deep-audit.")

        client_name = st.text_input("FULL NAME:")
        client_email = st.text_input("CORPORATE EMAIL:")

        if client_name and client_email:
            if st.button("REGISTER ASSESSMENT ORDER"):
                pd.DataFrame([[datetime.now(), domain_input, client_email, client_name]]).to_csv('sentinel_leads.csv', mode='a', header=not os.path.exists('sentinel_leads.csv'), index=False)
                send_telegram_alert(domain_input, scan['hits'], client_email, client_name, scan['top_finding'])
                st.session_state['lead_saved'] = True
                st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if st.session_state.get('lead_saved'):
        st.markdown('<div style="text-align: center; padding: 30px; border: 2px solid #1a1a1a; border-radius: 12px; background: white;">', unsafe_allow_html=True)
        
        # OPCIÓN 1: EL GANCHO (TRIPWIRE)
        st.markdown('<p style="color:#666; font-weight:bold; margin-bottom:0;">BASIC FLASH REPORT</p>', unsafe_allow_html=True)
        st.markdown('<h2 style="margin:0;">$99</h2>', unsafe_allow_html=True)
        st.write("Instant 3-page technical gap analysis.")
        
        params_99 = urllib.parse.urlencode({"checkout[email]": client_email, "checkout[name]": client_name, "checkout[custom][domain]": domain_input})
        url_99 = f"https://TU-TIENDA.lemonsqueezy.com/checkout/buy/ID-GANCHO?{params_99}"
        st.markdown(f'<a href="{url_99}" target="_blank" class="btn-payment btn-tripwire">GET FLASH REPORT</a>', unsafe_allow_html=True)
        
        st.markdown("<br><p style='font-size:0.8rem; color:#bbb;'>— RECOMMENDED —</p>", unsafe_allow_html=True)
        
        # OPCIÓN 2: EL ELITE (CORE OFFER)
        st.markdown('<p style="color:#1a1a1a; font-weight:bold; margin-bottom:0;">FULL STRATEGIC AUDIT</p>', unsafe_allow_html=True)
        st.markdown('<h2 style="margin:0;">$650</h2>', unsafe_allow_html=True)
        st.write("20-page roadmap + Priority intervention.")
        
        params_650 = urllib.parse.urlencode({"checkout[email]": client_email, "checkout[name]": client_name, "checkout[custom][domain]": domain_input})
        url_650 = f"https://core-digital-ia.lemonsqueezy.com/checkout?{params_650}"
        st.markdown(f'<a href="{url_650}" target="_blank" class="btn-payment">ACTIVATE FULL AUDIT</a>', unsafe_allow_html=True)
        
        st.markdown("---")
        legal_auth = st.checkbox("I certify I am the authorized representative.")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("Complete the initiation protocol to unlock strategic options.")

# Footer
st.markdown('<p style="text-align:center; color:#999; font-size:0.7rem; margin-top:100px;">Sentinel Unit © 2026. Non-intrusive OSINT Methodology.</p>', unsafe_allow_html=True)
