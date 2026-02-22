import streamlit as st
import time
import re
import pandas as pd
import os
import urllib.parse
from datetime import datetime

# 1. Configuración de Élite e Inicialización
st.set_page_config(page_title="SENTINEL | Strategic Risk Unit", page_icon="🛡️", layout="wide")

if 'lead_saved' not in st.session_state:
    st.session_state['lead_saved'] = False

# 2. Funciones de Lógica y Control de Cupos
def get_daily_slots():
    file_path = 'sentinel_leads.csv'
    limit = 3
    if os.path.isfile(file_path):
        df = pd.read_csv(file_path)
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        today_count = len(df[df['Fecha'].dt.date == datetime.now().date()])
        return max(0, limit - today_count)
    return limit

def sanitize_input(text, pattern, max_len=50):
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
                            columns=['Fecha', 'Dominio', 'Email', 'Nombre'])
    if os.path.isfile(file_path):
        df_existing = pd.read_csv(file_path)
        if ((df_existing['Dominio'] == domain) & (df_existing['Email'] == email)).any():
            return "exists"
        new_data.to_csv(file_path, mode='a', header=False, index=False)
    else:
        new_data.to_csv(file_path, index=False)
    return "saved"

# 3. Interfaz y Estética Corporativa
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp { background-color: #050505; color: #f0f0f0; font-family: 'Inter', sans-serif; }
    .terminal-box { border: 1px solid #1a1a1a; background: #0a0a0a; padding: 30px; border-radius: 8px; border-top: 4px solid #ff4b2b; }
    .btn-payment { display: block; background: #ff4b2b; color: white !important; text-align: center; padding: 18px; font-weight: bold; text-decoration: none; border-radius: 4px; margin-top: 20px; transition: 0.3s; }
    .btn-payment:hover { background: #ffffff; color: #000000 !important; transform: translateY(-2px); }
    .report-preview { background: #111; padding: 15px; border-left: 3px solid #ff4b2b; margin: 15px 0; font-family: monospace; font-size: 0.85rem; color: #888; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p style="color: #444; font-size: 0.75rem; font-weight: bold; letter-spacing: 2px;">SENTINEL | STRATEGIC RISK UNIT</p>', unsafe_allow_html=True)
st.markdown("<h2>PROTOCOLO DE INTERVENCIÓN DIGITAL</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown('<div class="terminal-box">', unsafe_allow_html=True)
    raw_domain = st.text_input("DOMINIO CORPORATIVO:", placeholder="empresa.com").strip().lower()
    target_url = sanitize_input(raw_domain, r'[^a-z0-9.-]')
    
    if target_url and is_valid_domain(target_url):
        st.markdown(f'<div class="report-preview">🔎 <b>RESUMEN PRELIMINAR: {target_url.upper()}</b><br>'
                    f'• Análisis OSINT pasivo: ACTIVADO<br>'
                    f'• Infraestructura pública: RIESGO IDENTIFICADO<br>'
                    f'• Prioridad: EJECUTIVA / URGENTE</div>', unsafe_allow_html=True)
        
        raw_name = st.text_input("NOMBRE Y CARGO EJECUTIVO:")
        user_name = sanitize_input(raw_name, r'[^a-zA-Z0-9 áéíóúÁÉÍÓÚ-]', 60)
        user_email = st.text_input("EMAIL CORPORATIVO DE CONTACTO:").strip().lower()
        
        if user_name and user_email:
            if is_corporate_email(user_email):
                if st.button("REGISTRAR ORDEN Y HABILITAR PAGO"):
                    with st.spinner("Registrando protocolo..."):
                        status = save_lead(target_url, user_email, user_name)
                        st.session_state['lead_saved'] = True
                        if status == "saved": st.success("✔ Orden registrada en el sistema.")
                        else: st.info("✔ Registro previo detectado. Acceso habilitado.")
            else:
                st.error("⚠️ Se requiere un email corporativo (@gmail/@yahoo bloqueados).")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    slots_left = get_daily_slots()
    if st.session_state['lead_saved']:
        st.markdown('<div style="text-align: center; padding: 25px; border: 1px solid #222; background:#0d0d0d; border-radius: 10px;">', unsafe_allow_html=True)
        st.markdown('<h1 style="color: #fff; font-size: 3.2rem; margin: 0;">650€</h1>', unsafe_allow_html=True)
        st.markdown(f'<p style="color: #ff4b2b; font-weight: bold; margin-top: 10px;">⚠️ CUPOS RESTANTES HOY: {slots_left}</p>', unsafe_allow_html=True)
        
        # Encoding seguro para URL
        params = urllib.parse.urlencode({"checkout[email]": user_email, "checkout[name]": user_name, "checkout[custom][domain]": target_url})
        checkout_url = f"https://core-digital-ia.lemonsqueezy.com/checkout?{params}"
        
        st.markdown(f'<a href="{checkout_url}" target="_blank" class="btn-payment">ACTIVAR AUDITORÍA AHORA</a>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 0.75rem; color: #555; margin-top: 15px;">Incluye Informe Ejecutivo + Plan de Mitigación + Entrega < 24h</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info(f"Registre sus datos para habilitar una de las {slots_left} plazas disponibles hoy.")

# Admin Panel
with st.sidebar:
    if st.checkbox("Admin Console"):
        access_key = st.text_input("Access Key", type="password")
        if access_key == st.secrets.get("admin_key", "sentinel2026"):
            if os.path.isfile('sentinel_leads.csv'):
                df = pd.read_csv('sentinel_leads.csv')
                st.write(f"Total Leads: {len(df)}")
                st.dataframe(df)
                st.download_button("Exportar CSV", df.to_csv(index=False), "leads.csv")
