import streamlit as st
import time

st.set_page_config(
    page_title="AI Loan Risk System",
    page_icon="🏦",
    layout="wide"
)

# CSS + ANIMATIONS
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0F172A, #1E293B);
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #0F172A);
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #E2E8F0 !important;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    margin-bottom: 20px;
    animation: fadeIn 1s ease-in-out;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #3B82F6, #2563EB);
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
}

/* Animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.title("🏦 Loan AI")

    st.markdown("""
    ### Navigation

    • Home  
    • Predict Loan Risk  

    ---
    **Model Info**

    ✔ Random Forest  
    ✔ Accuracy ~78%  
    ✔ Top Feature: Credit History  
    """)

# TITLE
st.title("🏦 AI Loan Risk Dashboard")

# ANIMATED LOADING
with st.spinner("Loading AI Model..."):
    time.sleep(1)

col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
    <div class="card">
    <h3>📌 About</h3>
    <p>This system predicts loan approval risk using Machine Learning.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>⚙️ Features</h3>
    <ul>
    <li>Risk Score Prediction</li>
    <li>Explainable AI (SHAP)</li>
    <li>Smart Decision System</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>📊 Summary</h3>
    <p><b>Model:</b> Random Forest</p>
    <p><b>Accuracy:</b> ~78%</p>
    </div>
    """, unsafe_allow_html=True)

st.success("🚀 Navigate using sidebar to start prediction")