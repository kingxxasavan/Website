import streamlit as st

st.set_page_config(
    page_title="Sign Up - CrypticX",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'signed_up' not in st.session_state:
    st.session_state.signed_up = False

# CSS matching landing.py style
st.markdown("""
<style>
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    .stDecoration {display: none !important;}
    
    /* Reset padding */
    .block-container {padding: 0 !important; margin: 0 !important;}
    .main .block-container {max-width: 100% !important; padding: 0 !important;}
    .stApp {margin: 0 !important; padding: 0 !important;}
    section.main > div {padding: 0 !important;}
    div[data-testid="stAppViewContainer"] {padding: 0 !important; margin: 0 !important;}
    
    /* Base styles */
    * {margin: 0; padding: 0; box-sizing: border-box;}
    html, body {margin: 0 !important; padding: 0 !important; overflow-x: hidden;}
    
    .stApp {
        background: #0a0a0f;
        color: #fff;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    /* Grid background */
    .grid-background {
        position: fixed;
        inset: 0;
        background-image: 
            linear-gradient(rgba(139, 92, 246, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(139, 92, 246, 0.03) 1px, transparent 1px);
        background-size: 50px 50px;
        z-index: 0;
    }
    
    /* Animated glow effects */
    .glow-orb {
        position: fixed;
        width: 800px;
        height: 800px;
        border-radius: 50%;
        filter: blur(120px);
        opacity: 0.3;
        z-index: 1;
        pointer-events: none;
    }
    
    .glow-orb.purple {
        background: radial-gradient(circle, rgba(139, 92, 246, 0.6), transparent);
        top: -200px;
        left: 50%;
        transform: translateX(-50%);
        animation: float 20s ease-in-out infinite;
    }
    
    .glow-orb.pink {
        background: radial-gradient(circle, rgba(236, 72, 153, 0.4), transparent);
        bottom: -300px;
        right: -200px;
        animation: float 25s ease-in-out infinite reverse;
    }
    
    @keyframes float {
        0%, 100% { transform: translate(-50%, 0) scale(1); }
        50% { transform: translate(-50%, -50px) scale(1.1); }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Navigation */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: transparent;
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(139, 92, 246, 0.1);
    }
    
    nav {
        position: relative;
        z-index: 100;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.5rem 4rem;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .logo {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        font-size: 1.5rem;
        font-weight: 700;
        color: #8b5cf6;
        cursor: pointer;
        letter-spacing: 0.5px;
    }
    
    .logo-icon {
        font-size: 1.8rem;
        filter: drop-shadow(0 0 10px rgba(139, 92, 246, 0.8));
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { filter: drop-shadow(0 0 10px rgba(139, 92, 246, 0.8)); }
        50% { filter: drop-shadow(0 0 20px rgba(139, 92, 246, 1)); }
    }
    
    /* Auth container */
    .auth-container {
        position: relative;
        z-index: 10;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 6rem 2rem 2rem;
    }
    
    .auth-box {
        max-width: 480px;
        width: 100%;
        background: rgba(139, 92, 246, 0.05);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 24px;
        padding: 3rem;
        backdrop-filter: blur(10px);
        animation: fadeInUp 0.6s ease-out;
    }
    
    .auth-header {
        text-align: center;
        margin-bottom: 2.5rem;
    }
    
    .auth-title {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #ffffff 0%, #8b5cf6 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    .auth-subtitle {
        color: rgba(255, 255, 255, 0.6);
        font-size: 1rem;
    }
    
    .form-group {
        margin-bottom: 1.5rem;
    }
    
    .form-label {
        display: block;
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.9rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 12px !important;
        color: #fff !important;
        padding: 0.9rem 1rem !important;
        font-size: 0.95rem !important;
        width: 100%;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2) !important;
        outline: none !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.3) !important;
    }
    
    .stCheckbox {
        margin-top: 1rem !important;
    }
    
    .stCheckbox > label {
        color: rgba(255, 255, 255, 0.7) !important;
        font-size: 0.9rem !important;
    }
    
    .stCheckbox > label a {
        color: #8b5cf6 !important;
        text-decoration: none !important;
    }
    
    .stCheckbox > label a:hover {
        color: #ec4899 !important;
    }
    
    .stButton > button {
        width: 100%;
        padding: 1rem !important;
        border-radius: 12px !important;
        background: linear-gradient(135deg, #8b5cf6, #ec4899) !important;
        color: #fff !important;
        font-weight: 600 !important;
        border: none !important;
        margin-top: 1rem !important;
        transition: all 0.3s !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 20px rgba(139, 92, 246, 0.4) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(139, 92, 246, 0.6) !important;
    }
    
    .divider {
        display: flex;
        align-items: center;
        margin: 2rem 0;
        color: rgba(255, 255, 255, 0.4);
        font-size: 0.9rem;
    }
    
    .divider::before,
    .divider::after {
        content: '';
        flex: 1;
        height: 1px;
        background: rgba(139, 92, 246, 0.2);
    }
    
    .divider::before {
        margin-right: 1rem;
    }
    
    .divider::after {
        margin-left: 1rem;
    }
    
    .auth-footer {
        text-align: center;
        margin-top: 2rem;
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.95rem;
    }
    
    .success-message {
        background: rgba(34, 197, 94, 0.1);
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 12px;
        padding: 1rem;
        color: #4ade80;
        text-align: center;
        margin-bottom: 1.5rem;
        animation: fadeInUp 0.5s ease-out;
    }
    
    .error-message {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 12px;
        padding: 1rem;
        color: #f87171;
        text-align: center;
        margin-bottom: 1.5rem;
        animation: fadeInUp 0.5s ease-out;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        nav {padding: 1rem 1.5rem;}
        .auth-box {padding: 2rem 1.5rem;}
        .auth-title {font-size: 2rem;}
    }
</style>
""", unsafe_allow_html=True)

# Background elements
st.markdown("""
<div class="grid-background"></div>
<div class="glow-orb purple"></div>
<div class="glow-orb pink"></div>
""", unsafe_allow_html=True)

# Navigation with back button
st.markdown('<div class="nav-container">', unsafe_allow_html=True)
st.markdown('<nav>', unsafe_allow_html=True)

col_nav1, col_nav2 = st.columns([3, 1])
with col_nav1:
    st.markdown("""
    <div class="logo">
        <span class="logo-icon">⚡</span>
        <span>CrypticX</span>
    </div>
    """, unsafe_allow_html=True)
with col_nav2:
    if st.button("← Back to Home", key="back_home"):
        st.switch_page("landing.py")

st.markdown('</nav>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Auth Container
st.markdown('<div class="auth-container">', unsafe_allow_html=True)
st.markdown('<div class="auth-box">', unsafe_allow_html=True)

# Header
st.markdown("""
<div class="auth-header">
    <h1 class="auth-title">Join CrypticX</h1>
    <p class="auth-subtitle">Start your journey to academic excellence</p>
</div>
""", unsafe_allow_html=True)

# Signup Form
with st.form("signup_form", clear_on_submit=False):
    st.markdown('<div class="form-group">', unsafe_allow_html=True)
    st.markdown('<label class="form-label">Full Name</label>', unsafe_allow_html=True)
    full_name = st.text_input("Name", label_visibility="collapsed", placeholder="John Doe")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="form-group">', unsafe_allow_html=True)
    st.markdown('<label class="form-label">Email Address</label>', unsafe_allow_html=True)
    email = st.text_input("Email", label_visibility="collapsed", placeholder="you@example.com")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="form-group">', unsafe_allow_html=True)
    st.markdown('<label class="form-label">Password</label>', unsafe_allow_html=True)
    password = st.text_input("Password", type="password", label_visibility="collapsed", placeholder="••••••••")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="form-group">', unsafe_allow_html=True)
    st.markdown('<label class="form-label">Confirm Password</label>', unsafe_allow_html=True)
    confirm_password = st.text_input("Confirm Password", type="password", label_visibility="collapsed", placeholder="••••••••")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Terms and conditions
    agree_terms = st.checkbox("I agree to the Terms of Service and Privacy Policy")
    
    submitted = st.form_submit_button("Create Account")
    
    if submitted:
        if full_name and email and password and confirm_password:
            if password != confirm_password:
                st.markdown('<div class="error-message">⚠ Passwords do not match</div>', unsafe_allow_html=True)
            elif not agree_terms:
                st.markdown('<div class="error-message">⚠ Please agree to the Terms of Service</div>', unsafe_allow_html=True)
            elif len(password) < 8:
                st.markdown('<div class="error-message">⚠ Password must be at least 8 characters</div>', unsafe_allow_html=True)
            else:
                # Here you would add your registration logic
                # For demo purposes, we'll just show a success message
                st.session_state.signed_up = True
                st.markdown('<div class="success-message">✓ Account created successfully! Redirecting to login...</div>', unsafe_allow_html=True)
                # You would redirect to login page here
        else:
            st.markdown('<div class="error-message">⚠ Please fill in all fields</div>', unsafe_allow_html=True)

# Divider
st.markdown('<div class="divider">or sign up with</div>', unsafe_allow_html=True)

# Social Signup
col1, col2 = st.columns(2)
with col1:
    if st.button("🔍 Google", key="google_signup", use_container_width=True):
        st.info("Google signup coming soon!")
with col2:
    if st.button("📘 Facebook", key="fb_signup", use_container_width=True):
        st.info("Facebook signup coming soon!")

# Footer with link to login
st.markdown('<div class="auth-footer">', unsafe_allow_html=True)
st.markdown('Already have an account? ', unsafe_allow_html=True)
if st.button("Sign in", key="goto_login", type="secondary"):
    st.switch_page("pages/login.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
