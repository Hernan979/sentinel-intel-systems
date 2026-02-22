import streamlit as st
import time

# 1. Configuración de Élite
st.set_page_config(page_title="SENTINEL | Intelligence Unit", page_icon="🛡️", layout="wide")

# 2. CSS de Grado Militar (Hackeo de Interfaz)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #000000; font-family: 'Courier New', Courier, monospace; color: #00ff00; }
    
    .terminal-header {
        border-bottom: 2px solid #ff4b2b;
        padding-bottom: 10px;
        margin-bottom: 30px;
    }
    .status-online { color: #00ff00; font-size: 0.8rem; animation: blinker 1s linear infinite; }
    @keyframes blinker { 50% { opacity: 0; } }
    
    .scan-line { font-size: 0.9rem; color: #888; margin: 5px 0; }
    
    .price-card {
        background: #0a0a0a;
        border: 1px solid #333;
        padding: 40px;
        text-align: center;
        border-top: 5px solid #ff4b2b;
    }
    
    .btn-buy {
        display: block;
        background: #ff4b2b;
        color: white !important;
        text-decoration: none;
        padding: 25px;
        font-weight: bold;
        font-size: 1.5rem;
        margin-top: 30px;
        border-radius: 5px;
    }
    .btn-buy:hover { background: #ffffff; color: #000000 !important; box-shadow: 0 0 40px #ff4b2b; }
    </style>
    """, unsafe_allow_html=True)

# 3. Interfaz de Usuario (Terminal Activa)
st.markdown('<div class="terminal-header">', unsafe_allow_html=True)
st.markdown('<h1>🛡️ SENTINEL INTEL SYSTEMS</h1>', unsafe_allow_html=True)
st.markdown('<p class="status-online">● SYSTEM_ONLINE // SECURE_ENCRYPTION_ACTIVE</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🖥️ DIAGNÓSTICO DE ACTIVOS")
    st.markdown('<p class="scan-line">> Scanning global infrastructure...</p>', unsafe_allow_html=True)
    st.progress(85)
    st.markdown('<p class="scan-line">> 138 Alpha assets detected.</p>', unsafe_allow_html=True)
    st.markdown('<p class="scan-line">> Vulnerability check: PENDING_PAYMENT</p>', unsafe_allow_html=True)
    
    st.info("""
    **SERVICIO DE INTERVENCIÓN EJECUTIVA**
    - [EN] Global Executive Audit: Infrastructure analysis & financial leak detection.
    - [FR] Audit d'Intervention Prioritaire: Détection des risques financiers.
    - [ES] Auditoría de Mitigación Prioritaria: Informe de riesgo en < 24h.
    """)

with col2:
    st.markdown('<div class="price-card">', unsafe_allow_html=True)
    st.markdown('<p style="color: #888;">INVERSIÓN TOTAL</p>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-size: 3rem; color: #fff;">650,00 €</h2>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 0.8rem;">ENTREGA GARANTIZADA < 24H</p>', unsafe_allow_html=True)
    st.markdown(f'<a href="https://core-digital-ia.lemonsqueezy.com/checkout" class="btn-buy">INICIAR AUDITORÍA</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<p style="color: #222; text-align: center; margin-top: 100px;">ACCESS_POINT: 192.168.1.104 // ENCRYPTED_BY_SENTINEL_ELITE</p>', unsafe_allow_html=True)

