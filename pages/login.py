import streamlit as st

st.set_page_config(
    page_title="CrypticX - Sign In",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'show_signup' not in st.session_state:
    st.session_state.show_signup = False
if 'auth_error' not in st.session_state:
    st.session_state.auth_error = ""
if 'auth_success' not in st.session_state:
    st.session_state.auth_success = ""

# Enhanced CSS matching landing page style
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
    
    .fade-in-up {
        animation: fadeInUp 0.6s ease-out forwards;
    }
    
    /* Navigation (simplified for auth page) */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: transparent;
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(139, 92, 246, 0.1);
        transition: all 0.3s ease;
    }
    
    nav {
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
        text-decoration: none;
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
    
    .nav-back {
        color: rgba(255, 255, 255, 0.7);
        text-decoration: none;
        font-size: 0.95rem;
        font-weight: 500;
        transition: all 0.3s;
        cursor: pointer;
    }
    
    .nav-back:hover {
        color: #fff;
    }
    
    /* Main content */
    .content-wrapper {
        position: relative;
        z-index: 10;
        padding-top: 80px;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* Auth section */
    .auth-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: 4rem 2rem;
        max-width: 500px;
        width: 100%;
    }
    
    .auth-title {
        font-size: 3rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #ffffff 0%, #8b5cf6 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: fadeInUp 0.8s ease-out backwards;
    }
    
    .auth-subtitle {
        font-size: 1.15rem;
        color: rgba(255, 255, 255, 0.6);
        margin-bottom: 3rem;
        line-height: 1.7;
        animation: fadeInUp 1s ease-out 0.2s backwards;
    }
    
    /* Auth form */
    .auth-form {
        width: 100%;
        background: rgba(139, 92, 246, 0.05);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 24px;
        padding: 3rem;
        backdrop-filter: blur(10px);
        animation: fadeInUp 1.2s ease-out 0.4s backwards;
    }
    
    .auth-tabs {
        display: flex;
        gap: 1rem;
        margin-bottom: 2rem;
    }
    
    .auth-tab {
        flex: 1;
        padding: 1rem;
        border-radius: 12px;
        background: transparent;
        border: 1px solid rgba(139, 92, 246, 0.3);
        color: rgba(255, 255, 255, 0.6);
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
        text-align: center;
    }
    
    .auth-tab.active {
        background: rgba(139, 92, 246, 0.2);
        border-color: #8b5cf6;
        color: #fff;
    }
    
    .stTextInput > div > div > input {
        width: 100%;
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 12px !important;
        color: #fff !important;
        padding: 1rem !important;
        font-size: 1rem !important;
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
        margin-top: 1rem !important;
        transition: all 0.3s !important;
        font-size: 1rem !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(139, 92, 246, 0.4) !important;
    }
    
    .switch-link {
        color: rgba(255, 255, 255, 0.7);
        text-decoration: none;
        font-size: 0.95rem;
        cursor: pointer;
        transition: color 0.3s;
        display: inline-block;
        margin-top: 1.5rem;
    }
    
    .switch-link:hover {
        color: #8b5cf6;
    }
    
    .switch-link strong {
        color: #8b5cf6;
    }
    
    /* Success and Error Messages */
    .success-message {
        background: rgba(34, 197, 94, 0.1);
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 12px;
        padding: 1rem;
        color: #4ade80;
        text-align: center;
        margin-top: 1rem;
        animation: fadeInUp 0.5s ease-out;
    }
    
    .error-message {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 12px;
        padding: 1rem;
        color: #f87171;
        text-align: center;
        margin-top: 1rem;
        animation: fadeInUp 0.5s ease-out;
    }
    
    /* Dashboard Teaser (on success) */
    .dashboard-teaser {
        text-align: center;
        padding: 2rem;
        background: rgba(139, 92, 246, 0.05);
        border-radius: 24px;
        margin-top: 2rem;
    }
    
    .dashboard-title {
        font-size: 2rem;
        color: #8b5cf6;
        margin-bottom: 1rem;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        nav {padding: 1rem 1.5rem;}
        .auth-title {font-size: 2rem;}
        .auth-subtitle {font-size: 1rem;}
        .auth-form {padding: 2rem;}
    }
</style>

""", unsafe_allow_html=True)

# Background elements
st.markdown("""
<div class="grid-background"></div>
<div class="glow-orb purple"></div>
<div class="glow-orb pink"></div>
""", unsafe_allow_html=True)

# JavaScript for nav hide on scroll (kept for consistency)
st.markdown("""
<script>
    document.addEventListener('DOMContentLoaded', function() {
        let lastScrollTop = 0;
        window.addEventListener("scroll", function(){
            let st = window.pageYOffset || document.documentElement.scrollTop;
            const nav = document.querySelector('.nav-container');
            if (st > lastScrollTop && st > 100) {
                nav.style.transform = 'translateY(-100%)';
            } else {
                nav.style.transform = 'translateY(0)';
            }
            lastScrollTop = st <= 0 ? 0 : st;
        }, false);
    });
</script>
""", unsafe_allow_html=True)

# Navigation (simple back to home)
st.markdown("""
<div class="nav-container">
<nav>
<a href="http://localhost:8501" class="logo">  <!-- Adjust URL for your landing page -->
<span class="logo-icon">⚡</span>
<span>CrypticX</span>
</a>
<a href="#" class="nav-back">← Back to Home</a>  <!-- Or use st.switch_page if multi-page -->
</nav>
</div>
""", unsafe_allow_html=True)

# Content wrapper
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Main Auth Section
st.markdown('<div class="auth-section">', unsafe_allow_html=True)

if st.session_state.logged_in:
    # Success: Show dashboard teaser
    st.markdown('<div class="dashboard-teaser">', unsafe_allow_html=True)
    st.markdown('<h2 class="dashboard-title">Welcome Back!</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color: rgba(255, 255, 255, 0.7);">You\'re now logged in. Redirecting to your dashboard...</p>', unsafe_allow_html=True)
    if st.button("Go to Dashboard"):
        st.session_state.current_section = 'dashboard'  # Or switch_page('dashboard.py')
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
else:
    # Auth Form
    st.markdown('<h1 class="auth-title">Welcome Back</h1>', unsafe_allow_html=True)
    st.markdown('<p class="auth-subtitle">Sign in to your account to continue your learning journey</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="auth-form">', unsafe_allow_html=True)
    
    # Tabs for Login/Signup (using buttons for simplicity)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login", key="login_tab", help="Switch to Login"):
            st.session_state.show_signup = False
            st.rerun()
    with col2:
        if st.button("Sign Up", key="signup_tab", help="Switch to Sign Up"):
            st.session_state.show_signup = True
            st.rerun()
    
    # Clear errors on rerun
    if st.session_state.auth_error:
        st.markdown(f'<div class="error-message">{st.session_state.auth_error}</div>', unsafe_allow_html=True)
        st.session_state.auth_error = ""
    if st.session_state.auth_success:
        st.markdown(f'<div class="success-message">{st.session_state.auth_success}</div>', unsafe_allow_html=True)
        st.session_state.auth_success = ""
    
    if not st.session_state.show_signup:
        # Login Form
        with st.form("login_form"):
            email = st.text_input("Email", placeholder="Enter your email", key="login_email")
            password = st.text_input("Password", type="password", placeholder="Enter your password", key="login_password")
            submitted = st.form_submit_button("Sign In")
            if submitted:
                if email == "demo@crypticx.com" and password == "demo":  # Mock auth
                    st.session_state.logged_in = True
                    st.session_state.auth_success = "Login successful! 🎉"
                    st.rerun()
                else:
                    st.session_state.auth_error = "Invalid email or password. Try demo@crypticx.com / demo."
                    st.rerun()
        
        st.markdown('<a href="#" class="switch-link" onclick="document.querySelector(\'[data-testid=\\\'signup_tab\\\']").click(); return false;">Don\'t have an account? <strong>Sign up</strong></a>', unsafe_allow_html=True)
    
    else:
        # Signup Form
        with st.form("signup_form"):
            email = st.text_input("Email", placeholder="Enter your email", key="signup_email")
            password = st.text_input("Password", type="password", placeholder="Create a password", key="signup_password")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password", key="signup_confirm")
            submitted = st.form_submit_button("Create Account")
            if submitted:
                if not email or not password or not confirm_password:
                    st.session_state.auth_error = "Please fill in all fields."
                elif password != confirm_password:
                    st.session_state.auth_error = "Passwords do not match."
                else:
                    # Mock signup
                    st.session_state.logged_in = True
                    st.session_state.auth_success = "Account created successfully! Welcome aboard! 🚀"
                    st.rerun()
                st.rerun()
        
        st.markdown('<a href="#" class="switch-link" onclick="document.querySelector(\'[data-testid=\\\'login_tab\\\']").click(); return false;">Already have an account? <strong>Sign in</strong></a>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close auth-form

st.markdown('</div></div>', unsafe_allow_html=True)  # Close auth-section and content-wrapper
