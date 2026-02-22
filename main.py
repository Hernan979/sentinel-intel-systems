import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Sentinel Intelligence Systems | Elite Security",
    page_icon="🛡️",
    layout="centered"
)

# --- ESTILOS PERSONALIZADOS (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%);
        color: white;
        border: none;
        padding: 15px;
        font-weight: bold;
        border-radius: 5px;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 5px 15px rgba(255, 75, 43, 0.4); }
    .card {
        background-color: #1a1c24;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4b2b;
        margin-bottom: 20px;
    }
    .price-tag { font-size: 2rem; font-weight: bold; color: #ff4b2b; }
    </style>
    """, unsafe_allow_html=True)

# --- VARIABLES DE CONTROL ---
CHECKOUT_URL = "https://core-digital-ia.lemonsqueezy.com/checkout/buy/62103e18-fa4d-4ad1-890b-6cd3ff1e2e35"

# --- CABECERA (BRANDING) ---
st.image("https://raw.githubusercontent.com/tu-repositorio/logo.png", width=200) # Opcional: añade tu logo
st.title("🛡️ SENTINEL INTELLIGENCE SYSTEMS")
st.subheader("Intervención Ejecutiva: Mitigación de Riesgos Críticos")

# --- CUERPO DE VENTAS ---
st.markdown(f"""
<div class="card">
    <h3>[EN] Global Executive Audit</h3>
    <p>Professional infrastructure analysis powered by 138 Alpha assets. 
    Identification of financial leaks and critical vulnerabilities.</p>
</div>

<div class="card">
    <h3>[FR] Audit d'Intervention Prioritaire</h3>
    <p>Analyse de sécurité de haut niveau. Détection des risques financiers 
    et plan d'action immédiat pour votre entreprise.</p>
</div>

<div class="card">
    <h3>[ES] Auditoría de Mitigación Prioritaria</h3>
    <p>Análisis profundo de activos digitales. Entrega de informe ejecutivo 
    con escenarios de riesgo financiero en menos de 24 horas.</p>
</div>
""", unsafe_allow_html=True)

# --- SECCIÓN DE PRECIO Y PAGO ---
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### INVERSIÓN")
    st.markdown('<p class="price-tag">650,00 €</p>', unsafe_allow_html=True)
    st.write("✅ Entrega en < 24 horas")
    st.write("✅ Soporte Multilingüe (EN/FR/ES)")
    st.write("✅ Factura Oficial para Deducción")

with col2:
    st.write("")
    st.write("")
    st.markdown(f'''
    <a href="{CHECKOUT_URL}" target="_blank" style="text-decoration: none;">
        <button style="
            width: 100%;
            background: linear-gradient(90deg, #ff4b2b 0%, #ff416c 100%);
            color: white;
            padding: 20px;
            font-size: 1.2rem;
            font-weight: bold;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(255, 75, 43, 0.4);">
            PROTEGER MI FACTURACIÓN
        </button>
    </a>
    ''', unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
st.markdown("---")
st.caption("Sentinel Intelligence Systems | Secure Global Infrastructure | Trusted by Digital Creators")