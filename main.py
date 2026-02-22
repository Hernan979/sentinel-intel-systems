import streamlit as st

# 1. Configuración de Seguridad de Alto Nivel
st.set_page_config(
    page_title="SENTINEL | Executive Audit", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. HACK DE INTERFAZ: Ocultar menús de Streamlit para parecer Software Propietario
st.markdown("""
    <style>
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap');

    /* Fondo de Terminal */
    .stApp {
        background-color: #000000;
        font-family: 'Space Mono', monospace;
        color: #e0e0e0;
    }

    /* Contenedor de Intervención */
    .main-terminal {
        max-width: 800px;
        margin: 50px auto;
        border: 1px solid #1a1a1a;
        padding: 40px;
        background: linear-gradient(180deg, #050505 0%, #000000 100%);
        box-shadow: 0 0 50px rgba(255, 75, 43, 0.1);
    }

    .header-code {
        color: #444;
        font-size: 0.7rem;
        margin-bottom: 20px;
        border-bottom: 1px solid #1a1a1a;
        padding-bottom: 10px;
    }

    .glitch {
        color: #ff4b2b;
        font-weight: bold;
        font-size: 1.8rem;
        letter-spacing: 3px;
        text-transform: uppercase;
    }

    .audit-block {
        margin: 25px 0;
        padding-left: 20px;
        border-left: 2px solid #1a1a1a;
    }

    .audit-block:hover {
        border-left: 2px solid #ff4b2b;
        background: rgba(255, 75, 43, 0.02);
    }

    .price-container {
        margin-top: 40px;
        border: 1px solid #333;
        padding: 30px;
        text-align: center;
    }

    /* El Botón de 650€ - Look de Ejecución */
    .btn-exec {
        display: block;
        background-color: #ffffff;
        color: #000000 !important;
        text-decoration: none;
        padding: 20px;
        font-weight: bold;
        font-size: 1.2rem;
        letter-spacing: 2px;
        transition: 0.2s;
        margin-top: 20px;
    }

    .btn-exec:hover {
        background-color: #ff4b2b;
        color: #ffffff !important;
    }

    </style>
    """, unsafe_allow_html=True)

# 3. Estructura de la Terminal
with st.container():
    st.markdown('<div class="main-terminal">', unsafe_allow_html=True)
    
    st.markdown('<p class="header-code">ID: SENTINEL_V2.0 // STATUS: READY_TO_DEPLOY // ACCESS: RESTRICTED</p>', unsafe_allow_html=True)
    st.markdown('<p class="glitch">SENTINEL INTEL SYSTEMS</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#666; font-size: 0.9rem;">High-Level Risk Mitigation & Executive Intervention</p>', unsafe_allow_html=True)

    # Bloques de Servicio
    st.markdown("""
    <div class="audit-block">
        <p><strong>[GLOBAL_AUDIT_EN]</strong> Infrastructure analysis powered by Alpha assets. Identification of critical financial leaks.</p>
    </div>
    <div class="audit-block">
        <p><strong>[INTERVENTION_FR]</strong> Analyse de haut niveau. Détection des risques et plan d'action immédiat.</p>
    </div>
    <div class="audit-block">
        <p><strong>[MITIGACIÓN_ES]</strong> Informe ejecutivo de activos digitales y escenarios de riesgo. Entrega &lt; 24h.</p>
    </div>
    """, unsafe_allow_html=True)

    # Checkout
    st.markdown("""
    <div class="price-container">
        <p style="color: #444; margin-bottom: 5px;">TOTAL_INVESTMENT</p>
        <p style="font-size: 2.5rem; font-weight: bold; margin: 0;">650,00 €</p>
        <p style="font-size: 0.7rem; color: #ff4b2b; margin-top: 5px;">OFFICIAL INVOICE PROVIDED // MULTILINGUAL SUPPORT</p>
        <a href="https://core-digital-ia.lemonsqueezy.com/checkout" class="btn-exec">AUTHORIZE DEPLOYMENT</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<p style="text-align: center; color: #1a1a1a; font-size: 0.6rem; margin-top: 30px;">SECURE CONNECTION ESTABLISHED // PORT 8080</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
