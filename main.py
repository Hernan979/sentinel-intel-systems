import streamlit as st
import time

# 1. Configuración de Firma Profesional
st.set_page_config(page_title="SENTINEL | Executive Risk Mitigation", page_icon="🛡️", layout="wide")

# 2. CSS Corporativo Minimalista (Foco en el Contenido)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #050505; font-family: 'Inter', sans-serif; color: #f0f0f0; }
    
    .terminal-box {
        border: 1px solid #1a1a1a;
        background: #0a0a0a;
        padding: 35px;
        border-radius: 8px;
        border-top: 4px solid #ff4b2b;
    }
    .stTextInput>div>div>input {
        background-color: #111;
        color: #ffffff;
        border: 1px solid #333;
        font-family: 'Courier New', monospace;
    }
    .btn-payment {
        display: block;
        background: #ff4b2b;
        color: white !important;
        text-align: center;
        padding: 20px;
        font-weight: bold;
        font-size: 1.2rem;
        text-decoration: none;
        margin-top: 20px;
        border-radius: 4px;
        transition: 0.3s;
        text-transform: uppercase;
    }
    .btn-payment:hover {
        background: #ffffff;
        color: #000000 !important;
        box-shadow: 0 10px 30px rgba(255, 75, 43, 0.4);
    }
    .label-executive { color: #555; font-size: 0.75rem; letter-spacing: 2px; font-weight: bold; }
    .status-msg { color: #00ff41; font-size: 0.85rem; font-family: monospace; margin-top: 10px; }
    .legal-disclaimer { color: #333; font-size: 0.65rem; margin-top: 25px; line-height: 1.2; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado
st.markdown('<p class="label-executive">SENTINEL | EXECUTIVE RISK MITIGATION UNIT</p>', unsafe_allow_html=True)
st.markdown("<h2 style='margin-top: -10px;'>ANÁLISIS DE CONTINUIDAD Y PROTECCIÓN DIGITAL</h2>", unsafe_allow_html=True)
st.markdown('<p style="color: #888;">Servicio especializado en mitigación de riesgos operativos para activos digitales críticos.</p>', unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown('<div class="terminal-box">', unsafe_allow_html=True)
    st.markdown("#### >> PROTOCOLO DE EVALUACIÓN MULTI-VECTORIAL")
    
    st.markdown("""
    <div style="line-height: 1.6; margin-top: 15px; color: #bbb;">
        <p>Nuestro protocolo Alpha ejecuta una auditoría estructurada de activos críticos para identificar vectores de riesgo operativo y financiero.</p>
        <p style="font-size: 0.9rem;"><strong>ESTADO ACTUAL:</strong> <span style="color: #ff4b2b;">ESPERANDO ASIGNACIÓN DE OBJETIVO</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    target_url = st.text_input("DOMINIO CORPORATIVO PARA VALIDACIÓN:", placeholder="empresa.com")
    
    if target_url:
        with st.spinner("Validando topología de activos..."):
            time.sleep(1.8) 
            st.markdown('<p class="status-msg">✔ OBJETIVO IDENTIFICADO. CONEXIÓN PASIVA ESTABLECIDA.</p>', unsafe_allow_html=True)
            st.markdown('<p class="status-msg">✔ RIESGO FINANCIERO POTENCIAL: EVALUACIÓN ESTRATÉGICA EN CURSO...</p>', unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

    # Bloque de Entregables (Aumenta conversión al reducir incertidumbre)
    st.markdown("""
    <div style="margin-top:25px; padding:20px; background:#070707; border: 1px solid #111; border-radius: 8px;">
        <h5 style="color:#ff4b2b; margin-bottom:15px;">DOCUMENTACIÓN ENTREGABLE (REPORT_V24):</h5>
        <ul style="color:#999; font-size:0.9rem; line-height:1.6;">
            <li>📄 <strong>Documento Ejecutivo PDF:</strong> Análisis detallado de exposición (10-20 páginas).</li>
            <li>📊 <strong>Clasificación de Riesgos:</strong> Jerarquización por criticidad e impacto.</li>
            <li>🛠️ <strong>Hoja de Ruta Accionable:</strong> Recomendaciones técnicas de implementación inmediata.</li>
            <li>⚡ <strong>Prioridad de Mitigación:</strong> Guía paso a paso para la continuidad de negocio.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    if target_url:
        st.markdown('<div style="text-align: center; padding: 30px; border: 1px solid #222; background:#0d0d0d; border-radius: 10px;">', unsafe_allow_html=True)
        st.markdown('<p class="label-executive">AUDITORÍA PRIORITARIA</p>', unsafe_allow_html=True)
        st.markdown('<h1 style="color: #fff; font-size: 3.5rem; margin: 10px 0;">650€</h1>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align:left; margin: 20px 0; color: #ccc; font-size: 0.9rem; list-style-type: none;">
            <p>✔ Informe de riesgos multi-vectorial</p>
            <p>✔ Revisión estratégica humana incluida</p>
            <p>✔ Confidencialidad profesional garantizada</p>
            <p>✔ Entrega prioritaria < 24 horas</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f'<a href="https://core-digital-ia.lemonsqueezy.com/checkout" class="btn-payment">ACTIVAR INTERVENCIÓN</a>', unsafe_allow_html=True)
        
        st.markdown('<p style="color:#666; font-size:0.75rem; margin-top:15px;">DISPONIBILIDAD LIMITADA POR CONTROL DE CALIDAD</p>', unsafe_allow_html=True)
        st.markdown('<p style="color:#444; font-size:0.7rem;">Facturación oficial emitida tras la confirmación.</p>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Disclaimer Legal
        st.markdown('<p class="legal-disclaimer">La evaluación identifica riesgos potenciales basados en análisis automatizado y revisión estratégica. No constituye una auditoría forense, certificación oficial ni garantía absoluta frente a incidentes terceros.</p>', unsafe_allow_html=True)
    else:
        st.info("⚠️ El sistema requiere un dominio válido para habilitar la orden de intervención.")

st.markdown('<p style="text-align: center; color: #1a1a1a; margin-top: 50px; font-size: 0.6rem;">SENTINEL UNIT // STRATEGIC RISK DIVISION © 2026</p>', unsafe_allow_html=True)


