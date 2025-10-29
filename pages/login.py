import streamlit as st

st.set_page_config(
    page_title="CrypticX Login",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Full CSS from home page + login-specific styles
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
    html, body {margin: 0 !important; padding: 0 !important; overflow-x: hidden; scroll-behavior: smooth;}
    
    .stApp {
        background: #0a0a0f;
        color: #fff;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    /* Grid background like in image */
    .grid-background {
        position: fixed;
        inset: 0;
        background-image: 
            linear-gradient(rgba(139, 92, 246, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(139, 92, 246, 0.03) 1px, transparent 1px);
        background-size: 50px 50px;
        z-index: 0;
    }
    
    /* Animated glow effect */
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
    
    /* Navigation */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: rgba(10, 10, 15, 0.8);
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
    }
    
    .nav-links {
        display: flex;
        gap: 2.5rem;
        align-items: center;
    }
    
    .nav-link {
        color: rgba(255, 255, 255, 0.7);
        text-decoration: none;
        font-size: 0.95rem;
        font-weight: 500;
        transition: all 0.3s;
        cursor: pointer;
        padding: 0.5rem 0;
        border-bottom: 2px solid transparent;
    }
    
    .nav-link:hover {
        color: #fff;
        border-bottom-color: #8b5cf6;
    }
    
    .nav-cta {
        padding: 0.7rem 1.8rem !important;
        border-radius: 50px;
        background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);
        color: #fff;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
        border: none;
        font-size: 0.9rem;
        box-shadow: 0 4px 20px rgba(139, 92, 246, 0.4);
    }
    
    .nav-cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(139, 92, 246, 0.6);
    }
    
    /* Main content wrapper */
    .content-wrapper {
        position: relative;
        z-index: 10;
        padding-top: 80px;
    }
    
    /* Section styling */
    .section {
        position: relative;
        z-index: 10;
        max-width: 1200px;
        margin: 0 auto;
        padding: 6rem 2rem;
    }
    
    .section-title {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
        color: #fff;
    }
    
    .section-subtitle {
        font-size: 1.15rem;
        color: rgba(255, 255, 255, 0.5);
        text-align: center;
        margin-bottom: 4rem;
    }
    
    /* Login-specific: Centered form */
    .login-section {
        min-height: calc(100vh - 80px);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 2rem;
    }
    
    .auth-form {
        max-width: 450px;
        width: 100%;
        background: rgba(139, 92, 246, 0.05);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 24px;
        padding: 3rem;
        backdrop-filter: blur(10px);
    }
    
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 12px !important;
        color: #fff !important;
        padding: 1rem !important;
        margin-bottom: 1rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.2) !important;
    }
    
    .stButton > button {
        width: 100%;
        padding: 1rem !important;
        border-radius: 12px !important;
        background: linear-gradient(135deg, #8b5cf6, #ec4899) !important;
        color: #fff !important;
        font-weight: 600 !important;
        border: none !important;
        font-size: 1rem !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px rgba(139, 92, 246, 0.6) !important;
    }
    
    /* Footer */
    .custom-footer {
        position: relative;
        z-index: 10;
        border-top: 1px solid rgba(139, 92, 246, 0.1);
        margin-top: 5rem;
        padding: 3rem 2rem;
        text-align: center;
        color: rgba(255, 255, 255, 0.4);
        background: rgba(10, 10, 15, 0.5);
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        nav {padding: 1rem 1.5rem;}
        .nav-links {display: none;}
    }
</style>
""", unsafe_allow_html=True)

# Background and Nav
st.markdown("""
    <div class="grid-background"></div>
    <div class="glow-orb purple"></div>
    <div class="glow-orb pink"></div>
    <div class="nav-container">
        <nav>
            <div class="logo">
                <span class="logo-icon">⚡</span>
                <span>CrypticX</span>
            </div>
            <div class="nav-links">
                <a href="/" class="nav-link">Home</a>
                <a href="/pricing" class="nav-link">Pricing</a>
                <a href="/dashboard" class="nav-link">Dashboard</a>
                <a href="/login" class="nav-link">Login</a>
                <button class="nav-cta">Sign Up</button>
            </div>
        </nav>
    </div>
""", unsafe_allow_html=True)

# Content wrapper
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Login Section
st.markdown("""
    <div class="login-section">
        <h2 class="section-title">Welcome Back</h2>
        <p class="section-subtitle">Sign in to continue your learning journey</p>
        <div class="auth-form">
""", unsafe_allow_html=True)

email = st.text_input("Email", placeholder="your@email.com")
password = st.text_input("Password", placeholder="••••••••", type="password")

if st.button("Sign In"):
    if email and password:
        st.success("✓ Welcome back! Redirecting to dashboard...")
        st.switch_page("pages/dashboard.py")  # Redirect to dashboard on success
    else:
        st.error("Please fill in all fields.")

# Optional: Add a "Don't have an account? Sign up" link
if st.button("Create Account"):
    st.switch_page("pages/pricing.py")  # Or a dedicated signup page

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <footer class="custom-footer">
        <p>© 2025 CrypticX • Empowering students with AI • Built with ❤️</p>
    </footer>
""", unsafe_allow_html=True)
