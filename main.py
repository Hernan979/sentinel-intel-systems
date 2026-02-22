import streamlit as st
import time

# 1. Configuración de Terminal de Inteligencia
st.set_page_config(page_title="SENTINEL | Intelligence Unit", page_icon="🛡️", layout="wide")

# 2. Hack de Interfaz: Estilo de Consola Militar
st.markdown("""
    <style>
    /* Desaparecer rastros de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #020202; font-family: 'Courier New', Courier, monospace; color: #00ff41; }

    /* Efecto de Terminal */
    .terminal-box {
        border: 1px solid #111;
        background: #050505;
        padding: 30px;
        border-radius: 5px;
        border-top: 3px solid #ff0000;
        box-shadow: 0 0 20px rgba(255, 0, 0, 0.1);
    }

    .blinking-cursor {
        font-weight: bold;
        animation: blink 1s step-end infinite;
    }
    @keyframes blink { 50% { opacity: 0; } }

    /* Botón de Pago Brutalista */
    .btn-payment {
        display: block;
        background: #ff0000;
        color: white !important;
        text-align: center;
        padding: 20px;
        font-weight: bold;
        font-size: 1.3rem;
        text-decoration: none;
        margin-top: 20px;
        letter-spacing: 2px;
        transition: 0.3s;
    }
    .btn-payment:hover {
        background: #ffffff;
        color: #000000 !important;
        box-shadow: 0 0 30px #ff0000;
    }

    .status-text { color: #555; font-size: 0.8rem; }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado de la Terminal
st.markdown("### 🛡️ SENTINEL_CORE_V2.0.4")
st.markdown('<p class="status-text">CONNECTION: SECURE // ENCRYPTION: AES-256 // OPERATOR: HERNAN979</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown('<div class="terminal-box">', unsafe_allow_html=True)
    st.write(">> INICIANDO ESCANEO DE ACTIVOS ALPHA...")
    st.progress(65)
    
    st.write(">> [EN] Infrastructure Audit: 138 Vulnerabilities potential.")
    st.write(">> [FR] Audit Prioritaire: Risques financiers identifiés.")
    st.write(">> [ES] Mitigación Crítica: Escenarios de riesgo listos.")
    
    st.markdown('<p style="color: #ff0000; margin-top:20px;">[ALERTA] ACCESO RESTRINGIDO: SE REQUIERE AUTORIZACIÓN FINANCIERA</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div style="text-align: center; padding: 20px; border: 1px solid #222;">', unsafe_allow_html=True)
    st.markdown('<p style="color: #888; font-size: 0.8rem;">SERVICE_FEE</p>', unsafe_allow_html=True)
    st.markdown('<h1 style="color: #fff; font-size: 3.5rem; margin: 0;">650€</h1>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 0.7rem; color: #444;">INCLUDES OFFICIAL INVOICE & 24H DELIVERY</p>', unsafe_allow_html=True)
    
    st.markdown(f'<a href="https://core-digital-ia.lemonsqueezy.com/checkout" class="btn-payment">AUTHORIZE_DEPLOYMENT</a>', unsafe_allow_html=True)
    
    st.markdown('<p class="status-text" style="margin-top:15px;">● SYSTEM WAITING FOR CONFIRMATION...</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<p style="text-align: center; color: #111; margin-top: 50px;">SENTINEL ELITE SYSTEMS - ZERO EMOTIONS CONFIGURATION</p>', unsafe_allow_html=True)
