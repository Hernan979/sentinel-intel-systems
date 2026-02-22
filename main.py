import streamlit as st

# 1. Configuración de Élite
st.set_page_config(page_title="SENTINEL | Executive Risk Mitigation", page_icon="🛡️", layout="wide")

# 2. CSS de Alto Impacto y Limpieza de Interfaz
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #020202; font-family: 'Courier New', Courier, monospace; color: #00ff41; }

    .terminal-box {
        border: 1px solid #111;
        background: #050505;
        padding: 30px;
        border-radius: 5px;
        border-top: 3px solid #ff4b2b;
    }

    .btn-payment {
        display: block;
        background: #ff4b2b;
        color: white !important;
        text-align: center;
        padding: 20px;
        font-weight: bold;
        font-size: 1.4rem;
        text-decoration: none;
        margin-top: 20px;
        border-radius: 5px;
        transition: 0.3s;
        text-transform: uppercase;
    }
    .btn-payment:hover {
        background: #ffffff;
        color: #000000 !important;
        box-shadow: 0 0 30px rgba(255, 75, 43, 0.6);
    }

    .status-text { color: #555; font-size: 0.8rem; text-transform: uppercase; }
    .impact-text { color: #ff4b2b; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado Estratégico
st.markdown("### 🛡️ SENTINEL INTEL SYSTEMS // DIVISIÓN DE INTERVENCIÓN")
st.markdown('<p class="status-text">PROTEGIENDO SU FACTURACIÓN DIGITAL // ACCESO RESTRINGIDO</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1.4, 1])

with col1:
    st.markdown('<div class="terminal-box">', unsafe_allow_html=True)
    st.markdown("#### >> DIAGNÓSTICO DE ACTIVOS CRÍTICOS")
    st.progress(85)
    
    st.markdown(f"""
    <div style="color: #ccc; line-height: 1.8;">
        <p>> <span class="impact-text">RIESGO ESTIMADO DE IMPACTO FINANCIERO:</span> 12.000€ – 85.000€</p>
        <p>> <span class="impact-text">PÉRDIDA POTENCIAL POR INACTIVIDAD:</span> 3-7 DÍAS DE FACTURACIÓN</p>
        <p>> <span class="impact-text">EXPOSICIÓN REPUTACIONAL:</span> CRÍTICA / ALTA</p>
        <hr style="border: 0.1px solid #222;">
        <p><strong>[EN] Global Executive Audit:</strong> Infrastructure analysis & financial leak detection.</p>
        <p><strong>[FR] Audit d'Intervention Prioritaire:</strong> Détection des risques financiers et plan d'action.</p>
        <p><strong>[ES] Auditoría de Mitigación Prioritaria:</strong> Análisis profundo y escenarios de riesgo.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div style="text-align: center; padding: 25px; border: 1px solid #222; background:#070707; border-radius: 10px;">', unsafe_allow_html=True)
    
    st.markdown('<p style="color: #888; font-size: 0.8rem; letter-spacing: 1px;">AUDITORÍA PRIORITARIA DE SEGURIDAD</p>', unsafe_allow_html=True)
    st.markdown('<h1 style="color: #fff; font-size: 3.5rem; margin: 0;">650€</h1>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 0.8rem; color: #aaa; margin-bottom: 20px;">Informe profesional + Recomendaciones + Entrega 24H</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <ul style="text-align:left; color:#ccc; font-size:0.9rem; margin-top:15px; list-style-type: none; padding-left: 10px;">
        <li style="margin-bottom: 8px;">✔ Identificación de riesgos críticos</li>
        <li style="margin-bottom: 8px;">✔ Estimación de impacto financiero</li>
        <li style="margin-bottom: 8px;">✔ Plan de mitigación priorizado</li>
        <li style="margin-bottom: 8px;">✔ Documento oficial para compliance</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown(
        '<a href="https://core-digital-ia.lemonsqueezy.com/checkout" class="btn-payment">ACTIVAR AUDITORÍA PRIORITARIA</a>',
        unsafe_allow_html=True
    )
    
    st.markdown('<p style="color:#ff4b2b; font-size:0.8rem; margin-top:15px; font-weight:bold;">[AVISO] SOLO 3 AUDITORÍAS PRIORITARIAS DISPONIBLES POR DÍA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="status-text">● GARANTÍA DE ENTREGA EN < 24 HORAS</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<p style="text-align: center; color: #111; margin-top: 50px; font-size: 0.6rem;">SENTINEL ELITE CONFIGURATION © 2026 // SECURE_ENVOY_ESTABLISHED</p>', unsafe_allow_html=True)

