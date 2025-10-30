This is perfect. You've provided the exact login and signup code you want to use.

Based on our last conversation, the goal is to get these beautiful forms *inside* your `Home.py` page without breaking the layout. The modal approach is still the correct one.

The plan is to **merge** the logic and styling from your `login.py` and `signup.py` files directly into the modal-based `Home.py` I sent earlier.

  * We will take all the **unique CSS** from your `login.py`/`signup.py` (like `.auth-box`, `.auth-title`, `.stTextInput` styles, etc.) and add it to the main `<style>` block in `Home.py`.
  * We will then **fill in** the `show_login_modal()` and `show_signup_modal()` functions with the *exact* HTML structure, Streamlit widgets, and validation logic from your two files.

Here is the new, complete `Home.py` file that integrates everything.

-----

### ⚡ Complete Merged `Home.py`

This is the **only file** you need for the landing page, login, and signup functionality. You can delete the `pages/login.py` and `pages/signup.py` files (or keep them separate if you need to link to them from elsewhere, but your home page won't use `st.switch_page` for them anymore).

```python
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CrypticX - AI Study Tool",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Session State (From Home.py) ---
if 'current_section' not in st.session_state:
    st.session_state.current_section = 'home'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'show_signup' not in st.session_state:
    st.session_state.show_signup = False
if 'show_login' not in st.session_state:
    st.session_state.show_login = False


# --- 1. MERGED CSS ---
# This block now contains ALL CSS from Home.py, login.py, and signup.py
# (with duplicates removed).
st.markdown("""
<style>
    /* --- Base styles from Home.py --- */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    .stDecoration {display: none !important;}
    
    .block-container {padding: 0 !important; margin: 0 !important;}
    .main .block-container {max-width: 100% !important; padding: 0 !important;}
    .stApp {margin: 0 !important; padding: 0 !important;}
    section.main > div {padding: 0 !important;}
    div[data-testid="stAppViewContainer"] {padding: 0 !important; margin: 0 !important;}
    
    * {margin: 0; padding: 0; box-sizing: border-box;}
    html, body {margin: 0 !important; padding: 0 !important; overflow-x: hidden; scroll-behavior: smooth;}
    
    .stApp {
        background: #0a0a0f;
        color: #fff;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    /* --- Backgrounds from Home.py --- */
    .grid-background {
        position: fixed; inset: 0;
        background-image: 
            linear-gradient(rgba(139, 92, 246, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(139, 92, 246, 0.03) 1px, transparent 1px);
        background-size: 50px 50px;
        z-index: 0;
    }
    .glow-orb {
        position: fixed; width: 800px; height: 800px; border-radius: 50%;
        filter: blur(120px); opacity: 0.3; z-index: 1; pointer-events: none;
    }
    .glow-orb.purple {
        background: radial-gradient(circle, rgba(139, 92, 246, 0.6), transparent);
        top: -200px; left: 50%; transform: translateX(-50%);
        animation: float 20s ease-in-out infinite;
    }
    .glow-orb.pink {
        background: radial-gradient(circle, rgba(236, 72, 153, 0.4), transparent);
        bottom: -300px; right: -200px;
        animation: float 25s ease-in-out infinite reverse;
    }
    @keyframes float {
        0%, 100% { transform: translate(-50%, 0) scale(1); }
        50% { transform: translate(-50%, -50px) scale(1.1); }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .fade-in-up { animation: fadeInUp 0.6s ease-out forwards; }
    
    /* --- Nav styles from Home.py --- */
    .nav-container {
        position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
        background: transparent; backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(139, 92, 246, 0.1);
        transition: all 0.3s ease;
    }
    nav {
        position: relative; z-index: 100; display: flex;
        justify-content: space-between; align-items: center;
        padding: 1.5rem 4rem; max-width: 1400px; margin: 0 auto;
    }
    .logo {
        display: flex; align-items: center; gap: 0.75rem;
        font-size: 1.5rem; font-weight: 700; color: #8b5cf6;
        cursor: pointer; letter-spacing: 0.5px;
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
    .nav-links { display: flex; gap: 2.5rem; align-items: center; }
    .nav-link {
        color: rgba(255, 255, 255, 0.7); text-decoration: none;
        font-size: 0.95rem; font-weight: 500; transition: all 0.3s;
        cursor: pointer; padding: 0.5rem 0; border-bottom: 2px solid transparent;
        position: relative;
    }
    .nav-link:hover { color: #fff; border-bottom-color: #8b5cf6; }
    .nav-link.active { color: #fff; border-bottom-color: #8b5cf6; }
    .nav-cta {
        padding: 0.7rem 1.8rem !important; border-radius: 50px;
        background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);
        color: #fff; font-weight: 600; cursor: pointer;
        transition: all 0.3s; border: none; font-size: 0.9rem;
        box-shadow: 0 4px 20px rgba(139, 92, 246, 0.4);
    }
    .nav-cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(139, 92, 246, 0.6);
    }
    
    /* --- Page content styles from Home.py --- */
    .content-wrapper { position: relative; z-index: 10; padding-top: 80px; }
    .hero-section {
        min-height: calc(100vh - 80px); display: flex; flex-direction: column;
        justify-content: center; align-items: center; text-align: center;
        padding: 4rem 2rem; position: relative;
    }
    .welcome-badge {
        display: inline-flex; align-items: center; gap: 0.5rem;
        background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 0.6rem 1.5rem; border-radius: 50px; font-size: 0.9rem;
        color: #fff; font-weight: 500; margin-bottom: 2rem;
        backdrop-filter: blur(10px); animation: fadeInUp 0.6s ease-out;
    }
    .hero-title {
        font-size: 5rem; font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #ffffff 0%, #8b5cf6 50%, #ec4899 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text; max-width: 1000px;
        animation: fadeInUp 0.8s ease-out 0.2s backwards;
    }
    /* ... (All other .hero, .stats, .section, .features, .pricing styles from Home.py) ... */
    
    .hero-subtitle {
        font-size: 1.25rem; color: rgba(255, 255, 255, 0.6); margin-bottom: 3rem;
        max-width: 700px; line-height: 1.7; animation: fadeInUp 1s ease-out 0.4s backwards;
    }
    .hero-cta {
        padding: 1rem 2.5rem; border-radius: 50px;
        background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);
        color: #fff; font-weight: 600; cursor: pointer; transition: all 0.3s;
        border: none; font-size: 1.1rem; box-shadow: 0 8px 30px rgba(139, 92, 246, 0.4);
        animation: fadeInUp 1.2s ease-out 0.6s backwards;
    }
    .hero-cta:hover {
        transform: translateY(-3px); box-shadow: 0 12px 40px rgba(139, 92, 246, 0.6);
    }
    .stats-section {
        display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;
        max-width: 900px; margin: 4rem auto 0; padding: 0 2rem;
    }
    .stat-item { text-align: center; }
    .stat-number {
        font-size: 3rem; font-weight: 800;
        background: linear-gradient(135deg, #8b5cf6, #ec4899);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .stat-label { color: rgba(255, 255, 255, 0.6); font-size: 0.95rem; }
    .section {
        position: relative; z-index: 10; max-width: 1200px; margin: 0 auto;
        padding: 6rem 2rem; width: 100%; display: flex; flex-direction: column;
        align-items: center;
    }
    .section-title {
        font-size: 3rem; font-weight: 700; text-align: center;
        margin-bottom: 1rem; color: #fff;
    }
    .section-subtitle {
        font-size: 1.15rem; color: rgba(255, 255, 255, 0.5);
        text-align: center; margin-bottom: 4rem;
    }
    .features-grid {
        display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;
        margin-top: 3rem;
    }
    .feature-card {
        background: rgba(139, 92, 246, 0.05); border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 24px; padding: 2.5rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px); cursor: pointer; height: 100%;
        display: flex; flex-direction: column; align-items: center; text-align: center;
    }
    .feature-card:hover {
        transform: translateY(-10px); background: rgba(139, 92, 246, 0.1);
        border-color: rgba(139, 92, 246, 0.5); box-shadow: 0 20px 60px rgba(139, 92, 246, 0.2);
    }
    .feature-icon { font-size: 3rem; margin-bottom: 1.5rem; display: block; transition: transform 0.3s; }
    .feature-card:hover .feature-icon { transform: scale(1.1); }
    .feature-card h3 { font-size: 1.5rem; margin-bottom: 1rem; color: #fff; font-weight: 600; }
    .feature-card p { color: rgba(255, 255, 255, 0.6); line-height: 1.7; font-size: 0.95rem; flex-grow: 1; }
    .pricing-grid {
        display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;
        margin-top: 3rem;
    }
    .pricing-card {
        background: rgba(139, 92, 246, 0.05); border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 24px; padding: 3rem 2.5rem; text-align: center;
        transition: all 0.4s; position: relative;
    }
    .pricing-card.featured {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(236, 72, 153, 0.15));
        border: 2px solid #8b5cf6; transform: scale(1.05);
    }
    /* ... (Rest of your landing page styles) ... */
    
    .pricing-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 60px rgba(139, 92, 246, 0.3);
    }
    .pricing-card.featured:hover { transform: translateY(-10px) scale(1.07); }
    .pricing-badge {
        position: absolute; top: -15px; left: 50%; transform: translateX(-50%);
        background: linear-gradient(135deg, #8b5cf6, #ec4899);
        color: white; padding: 0.4rem 1.2rem; border-radius: 20px;
        font-size: 0.8rem; font-weight: 600;
    }
    .pricing-card h3 { font-size: 1.5rem; margin-bottom: 1rem; color: #fff; }
    .price {
        font-size: 3.5rem; font-weight: 800; margin: 1.5rem 0;
        background: linear-gradient(135deg, #8b5cf6, #ec4899);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .price-period { font-size: 1rem; color: rgba(255, 255, 255, 0.5); }
    .feature-list {
        text-align: left; margin: 2rem 0; color: rgba(255, 255, 255, 0.7);
        line-height: 2.2; font-size: 0.95rem;
    }
    .pricing-button {
        width: 100%; padding: 0.9rem; border-radius: 12px;
        background: rgba(139, 92, 246, 0.2); border: 1px solid rgba(139, 92, 246, 0.3);
        color: #fff; font-weight: 600; cursor: pointer; transition: all 0.3s;
        margin-top: 1rem;
    }
    .pricing-button:hover {
        background: rgba(139, 92, 246, 0.3); border-color: #8b5cf6;
        transform: translateY(-2px);
    }
    .pricing-card.featured .pricing-button {
        background: linear-gradient(135deg, #8b5cf6, #ec4899); border: none;
    }
    .custom-footer {
        position: relative; z-index: 10; border-top: 1px solid rgba(139, 92, 246, 0.1);
        margin-top: 5rem; padding: 3rem 2rem; text-align: center;
        color: rgba(255, 255, 255, 0.4); background: rgba(10, 10, 15, 0.5);
    }
    .footer-links { display: flex; justify-content: center; gap: 2rem; margin-top: 1rem; }
    .footer-link {
        color: rgba(255, 255, 255, 0.5); text-decoration: none;
        font-size: 0.9rem; transition: color 0.3s;
    }
    .footer-link:hover { color: #8b5cf6; }
    
    
    /* --- 2. NEW: Styles for Modal, from login.py & signup.py --- */
    
    /* Style the modal background */
    div[data-testid="stModal"] > div:first-child {
        background: none; /* Hide the default modal overlay */
    }
    
    /* Style the modal content box (using .auth-box styles) */
    div[data-testid="stModal"] > div > div {
        max-width: 480px;
        width: 100%;
        background: rgba(139, 92, 246, 0.05);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 24px;
        padding: 3rem;
        backdrop-filter: blur(10px);
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Hide the default modal header/close button */
    div[data-testid="stModal"] > div > div > div > div[data-testid="stModalHeader"] {
        display: none;
    }

    /* Auth header styles (from login.py) */
    .auth-header { text-align: center; margin-bottom: 2.5rem; }
    .auth-title {
        font-size: 2.5rem; font-weight: 700;
        background: linear-gradient(135deg, #ffffff 0%, #8b5cf6 50%, #ec4899 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-clip: text; margin-bottom: 0.5rem;
    }
    .auth-subtitle { color: rgba(255, 255, 255, 0.6); font-size: 1rem; }
    
    /* Form layout styles (from login.py) */
    .form-group { margin-bottom: 1.5rem; }
    .form-label {
        display: block; color: rgba(255, 255, 255, 0.8);
        font-size: 0.9rem; font-weight: 500; margin-bottom: 0.5rem;
    }
    
    /* Input styles (from login.py, adapted for modal) */
    div[data-testid="stModal"] .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 12px !important;
        color: #fff !important;
        padding: 0.9rem 1rem !important;
        font-size: 0.95rem !important;
        width: 100%;
    }
    div[data-testid="stModal"] .stTextInput > div > div > input:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2) !important;
        outline: none !important;
    }
    div[data-testid="stModal"] .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.3) !important;
    }
    
    /* Checkbox styles (from signup.py, adapted for modal) */
    div[data-testid="stModal"] .stCheckbox { margin-top: 1rem !important; }
    div[data-testid="stModal"] .stCheckbox > label {
        color: rgba(255, 255, 255, 0.7) !important;
        font-size: 0.9rem !important;
    }
    div[data-testid="stModal"] .stCheckbox > label a {
        color: #8b5cf6 !important; text-decoration: none !important;
    }
    div[data-testid="stModal"] .stCheckbox > label a:hover {
        color: #ec4899 !important;
    }

    /* Button styles (from login.py, adapted for modal) */
    /* Primary button (Submit) */
    div[data-testid="stModal"] .stButton > button[kind="primary"] {
        width: 100%; padding: 1rem !important; border-radius: 12px !important;
        background: linear-gradient(135deg, #8b5cf6, #ec4899) !important;
        color: #fff !important; font-weight: 600 !important;
        border: none !important; margin-top: 1rem !important;
        transition: all 0.3s !important; font-size: 1rem !important;
        box-shadow: 0 4px 20px rgba(139, 92, 246, 0.4) !important;
    }
    div[data-testid="stModal"] .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(139, 92, 246, 0.6) !important;
    }
    /* Secondary button (Switch modal links) */
    div[data-testid="stModal"] .stButton > button[kind="secondary"] {
        background: none !important; border: none !important;
        color: #8b5cf6 !important; font-weight: 600 !important;
        font-size: 0.95rem !important;
        padding: 0 !important; box-shadow: none !important;
        text-decoration: none !important;
    }
    div[data-testid="stModal"] .stButton > button[kind="secondary"]:hover {
        color: #ec4899 !important;
    }
    
    /* Other auth styles (from login.py) */
    .forgot-password { text-align: right; margin-top: 0.5rem; }
    .forgot-password a {
        color: #8b5cf6; text-decoration: none;
        font-size: 0.9rem; transition: color 0.3s; cursor: pointer;
    }
    .forgot-password a:hover { color: #ec4899; }
    .divider {
        display: flex; align-items: center; margin: 2rem 0;
        color: rgba(255, 255, 255, 0.4); font-size: 0.9rem;
    }
    .divider::before, .divider::after {
        content: ''; flex: 1; height: 1px;
        background: rgba(139, 92, 246, 0.2);
    }
    .divider::before { margin-right: 1rem; }
    .divider::after { margin-left: 1rem; }
    
    .auth-footer {
        text-align: center; margin-top: 2rem;
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.95rem;
    }
    /* Note: .auth-footer-link is handled by .stButton > button[kind="secondary"] */
    
    /* Message styles (from login.py) */
    .success-message {
        background: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 12px; padding: 1rem; color: #4ade80;
        text-align: center; margin-bottom: 1.5rem;
        animation: fadeInUp 0.5s ease-out;
    }
    .error-message {
        background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 12px; padding: 1rem; color: #f87171;
        text-align: center; margin-bottom: 1.5rem;
        animation: fadeInUp 0.5s ease-out;
    }

    /* --- Responsive Styles from Home.py --- */
    @media (max-width: 1024px) {
        .features-grid, .pricing-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 768px) {
        nav {padding: 1rem 1.5rem;}
        .nav-links {display: none;}
        .hero-title {font-size: 2.5rem;}
        .hero-subtitle {font-size: 1.1rem;}
        .features-grid, .pricing-grid, .stats-section { grid-template-columns: 1fr; }
        .section-title {font-size: 2rem;}
        .pricing-card.featured {transform: scale(1);}
        
        /* Responsive for modal */
        div[data-testid="stModal"] > div > div {
            padding: 2rem 1.5rem;
        }
        .auth-title {font-size: 2rem;}
    }

</style>
""", unsafe_allow_html=True)

# Background elements (Original)
st.markdown("""
<div class="grid-background"></div>
<div class="glow-orb purple"></div>
<div class="glow-orb pink"></div>
""", unsafe_allow_html=True)

# JavaScript for smooth scrolling (Original)
st.markdown("""
<script>
    document.addEventListener('DOMContentLoaded', function() {
        const links = document.querySelectorAll('a[href^="#"]');
        links.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

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


# --- 3. MODAL & NAVIGATION LOGIC ---

# Check for navigation parameter to OPEN MODALS or change state
nav_param = st.query_params.get("nav")

if nav_param == "login":
    st.session_state.show_login = True
    st.session_state.show_signup = False
    st.query_params.clear() 
elif nav_param == "signup":
    st.session_state.show_signup = True
    st.session_state.show_login = False
    st.query_params.clear()
elif nav_param == "logout":
    st.session_state.logged_in = False
    st.query_params.clear()
    st.rerun()
elif nav_param == "dashboard":
    if st.session_state.logged_in:
        st.switch_page("pages/dashboard.py")
    else:
        st.session_state.show_login = True
        st.query_params.clear()


# --- 4. NEW: Login Modal Function (from login.py) ---
def show_login_modal():
    with st.modal("", clear_on_submit=False):
        # Header
        st.markdown("""
        <div class="auth-header">
            <h1 class="auth-title">Welcome Back</h1>
            <p class="auth-subtitle">Sign in to continue your learning journey</p>
        </div>
        """, unsafe_allow_html=True)

        # Login Form
        with st.form("login_form", clear_on_submit=False):
            st.markdown('<div class="form-group">', unsafe_allow_html=True)
            st.markdown('<label class="form-label">Email Address</label>', unsafe_allow_html=True)
            email = st.text_input("Email", label_visibility="collapsed", placeholder="you@example.com", key="login_email")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="form-group">', unsafe_allow_html=True)
            st.markdown('<label class="form-label">Password</label>', unsafe_allow_html=True)
            password = st.text_input("Password", type="password", label_visibility="collapsed", placeholder="••••••••", key="login_pass")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="forgot-password"><a>Forgot password?</a></div>', unsafe_allow_html=True)
            
            submitted = st.form_submit_button("Sign In")
            
            if submitted:
                # --- YOUR AUTHENTICATION LOGIC HERE ---
                # Example:
                if email == "admin@test.com" and password == "pass":
                    st.session_state.logged_in = True
                    st.session_state.show_login = False
                    st.markdown('<div class="success-message">✓ Login successful! Redirecting...</div>', unsafe_allow_html=True)
                    st.rerun()
                else:
                    st.markdown('<div class="error-message">⚠ Invalid email or password</div>', unsafe_allow_html=True)

        # Divider and Socials
        st.markdown('<div class="divider">or continue with</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔍 Google", key="google_login", use_container_width=True, type="primary"):
                st.info("Google login coming soon!")
        with col2:
            if st.button("📘 Facebook", key="fb_login", use_container_width=True, type="primary"):
                st.info("Facebook login coming soon!")

        # Footer with link to signup
        st.markdown('<div class="auth-footer">Don\'t have an account?</div>', unsafe_allow_html=True)
        if st.button("Sign up for free", key="goto_signup", type="secondary", use_container_width=True):
            st.session_state.show_login = False
            st.session_state.show_signup = True
            st.rerun()

# --- 5. NEW: Sign Up Modal Function (from signup.py) ---
def show_signup_modal():
    with st.modal("", clear_on_submit=False):
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
            full_name = st.text_input("Name", label_visibility="collapsed", placeholder="John Doe", key="signup_name")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="form-group">', unsafe_allow_html=True)
            st.markdown('<label class="form-label">Email Address</label>', unsafe_allow_html=True)
            email = st.text_input("Email", label_visibility="collapsed", placeholder="you@example.com", key="signup_email")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="form-group">', unsafe_allow_html=True)
            st.markdown('<label class="form-label">Password</label>', unsafe_allow_html=True)
            password = st.text_input("Password", type="password", label_visibility="collapsed", placeholder="•••••••• (at least 8 characters)", key="signup_pass")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="form-group">', unsafe_allow_html=True)
            st.markdown('<label class="form-label">Confirm Password</label>', unsafe_allow_html=True)
            confirm_password = st.text_input("Confirm Password", type="password", label_visibility="collapsed", placeholder="••••••••", key="signup_confirm_pass")
            st.markdown('</div>', unsafe_allow_html=True)
            
            agree_terms = st.checkbox("I agree to the [Terms of Service](https://example.com) and [Privacy Policy](https://example.com)")
            
            submitted = st.form_submit_button("Create Account")
            
            if submitted:
                if not (full_name and email and password and confirm_password):
                    st.markdown('<div class="error-message">⚠ Please fill in all fields</div>', unsafe_allow_html=True)
                elif password != confirm_password:
                    st.markdown('<div class="error-message">⚠ Passwords do not match</div>', unsafe_allow_html=True)
                elif not agree_terms:
                    st.markdown('<div class="error-message">⚠ Please agree to the Terms of Service</div>', unsafe_allow_html=True)
                elif len(password) < 8:
                    st.markdown('<div class="error-message">⚠ Password must be at least 8 characters</div>', unsafe_allow_html=True)
                else:
                    # --- YOUR REGISTRATION LOGIC HERE ---
                    st.markdown('<div class="success-message">✓ Account created successfully! Redirecting to login...</div>', unsafe_allow_html=True)
                    st.session_state.show_signup = False
                    st.session_state.show_login = True
                    st.rerun()

        # Divider and Socials
        st.markdown('<div class="divider">or sign up with</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔍 Google", key="google_signup", use_container_width=True, type="primary"):
                st.info("Google signup coming soon!")
        with col2:
            if st.button("📘 Facebook", key="fb_signup", use_container_width=True, type="primary"):
                st.info("Facebook signup coming soon!")

        # Footer with link to login
        st.markdown('<div class="auth-footer">Already have an account?</div>', unsafe_allow_html=True)
        if st.button("Sign in", key="goto_login", type="secondary", use_container_width=True):
            st.session_state.show_signup = False
            st.session_state.show_login = True
            st.rerun()

# --- Display modals based on session state ---
if st.session_state.show_login:
    show_login_modal()

if st.session_state.show_signup:
    show_signup_modal()


# --- 6. DYNAMIC NAVIGATION BAR (Original) ---
if st.session_state.logged_in:
    # --- NAV BAR FOR LOGGED-IN USERS ---
    st.markdown(f"""
    <div class="nav-container">
    <nav>
        <div class="logo">
        <span class="logo-icon">⚡</span>
        <span>CrypticX</span>
        </div>
        <div class="nav-links">
        <a href="#home" class="nav-link {'active' if st.session_state.current_section == 'home' else ''}">Home</a>
        <a href="#pricing" class="nav-link {'active' if st.session_state.current_section == 'pricing' else ''}">Pricing</a>
        <a href="?nav=dashboard" class="nav-link {'active' if st.session_state.current_section == 'dashboard' else ''}">Dashboard</a>
        <button class="nav-cta" onclick="window.location.href='?nav=logout'">Logout</button>
        </div>
    </nav>
    </div>
    """, unsafe_allow_html=True)
else:
    # --- NAV BAR FOR LOGGED-OUT USERS ---
    st.markdown(f"""
    <div class="nav-container">
    <nav>
        <div class="logo">
        <span class="logo-icon">⚡</span>
        <span>CrypticX</span>
        </div>
        <div class="nav-links">
        <a href="#home" class="nav-link {'active' if st.session_state.current_section == 'home' else ''}">Home</a>
        <a href="#pricing" class="nav-link {'active' if st.session_state.current_section == 'pricing' else ''}">Pricing</a>
        <a href="?nav=dashboard" class="nav-link {'active' if st.session_state.current_section == 'dashboard' else ''}">Dashboard</a>
        <a href="?nav=login" class="nav-link {'active' if st.session_state.current_section == 'login' else ''}">Login</a>
        <button class="nav-cta" onclick="window.location.href='?nav=signup'">Sign Up</button>
        </div>
    </nav>
    </div>
    """, unsafe_allow_html=True)


# --- 7. ORIGINAL HOME PAGE CONTENT (Unchanged) ---
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div id="home" class="hero-section">
<div class="welcome-badge">✨ Welcome to CrypticX - The Ultimate Study Tool</div>
<h1 class="hero-title">Master Your Studies with AI-Powered Learning</h1>
<p class="hero-subtitle">Transform the way you learn with intelligent tools designed to help you understand faster, remember longer, and achieve academic excellence.</p>
<button class="hero-cta" onclick="window.location.href='?nav=signup'">Start Learning Free</button>
<div class="stats-section">
    <div class="stat-item"><div class="stat-number">50K+</div><div class="stat-label">Active Students</div></div>
    <div class="stat-item"><div class="stat-number">95%</div><div class="stat-label">Satisfaction Rate</div></div>
    <div class="stat-item"><div class="stat-number">1M+</div><div class="stat-label">Questions Answered</div></div>
</div>
</div>
""", unsafe_allow_html=True)

# Why Choose Us Section
st.markdown('<div id="why-choose" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Why Choose CrypticX</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">The smartest way to study in 2025</p>', unsafe_allow_html=True)
st.markdown('<div class="features-grid">', unsafe_allow_html=True)
st.markdown("""
<div class="feature-card">
<span class="feature-icon">⚡</span><h3>Lightning Fast</h3>
<p>Get instant answers to your questions. No more waiting hours for tutors or searching through endless resources.</p>
</div>
<div class="feature-card">
<span class="feature-icon">🎯</span><h3>Personalized Learning</h3>
<p>AI adapts to your learning style and pace, providing customized explanations that make sense to you.</p>
</div>
<div class="feature-card">
<span class="feature-icon">💰</span><h3>Affordable Excellence</h3>
<p>Get premium tutoring quality at a fraction of the cost. Start free and upgrade only when you're ready.</p>
</div>
<div class="feature-card">
<span class="feature-icon">📱</span><h3>Study Anywhere</h3>
<p>Access your learning tools from any device, anytime. Study on your schedule, not someone else's.</p>
</div>
<div class="feature-card">
<span class="feature-icon">🔬</span><h3>Proven Methods</h3>
<p>Built on learning science and cognitive psychology principles that are proven to improve retention and understanding.</p>
</div>
<div class="feature-card">
<span class="feature-icon">🌟</span><h3>Student Success</h3>
<p>Join thousands of students who've improved their grades and confidence with CrypticX's intelligent tools.</p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# Pricing Section
st.markdown('<div id="pricing" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Choose Your Plan</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Start free, upgrade when you\'re ready</p>', unsafe_allow_html=True)
st.markdown("""
<div class="pricing-grid">
    <div class="pricing-card">
        <h3>Free</h3><div class="price">$0<span class="price-period">/mo</span></div>
        <div class="feature-list">
            ✓ 10 AI questions/day<br> ✓ Basic summaries<br> ✓ 5 quizzes/week<br> ✓ Community support
        </div>
        <button class="pricing-button" onclick="window.location.href='?nav=signup'">Start Free</button>
    </div>
    <div class="pricing-card featured">
        <div class="pricing-badge">⭐ MOST POPULAR</div>
        <h3>Pro</h3><div class="price">$15<span class="price-period">/mo</span></div>
        <div class="feature-list">
            ✓ Unlimited AI questions<br> ✓ Advanced summaries<br> ✓ Unlimited quizzes<br>
            ✓ PDF upload (100MB)<br> ✓ Priority support<br> ✓ Progress analytics
        </div>
        <button class="pricing-button" onclick="window.location.href='?nav=signup'">Get Pro</button>
    </div>
    <div class="pricing-card">
        <h3>Enterprise</h3><div class="price">$35<span class="price-period">/mo</span></div>
        <div class="feature-list">
            ✓ Everything in Pro<br> ✓ Team accounts<br> ✓ Advanced analytics<br>
            ✓ Custom integrations<br> ✓ Dedicated support<br> ✓ Unlimited storage
        </div>
        <button class="pricing-button" onclick="window.location.href='?nav=signup'">Contact Us</button>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # Close content-wrapper

# Footer
st.markdown("""
<div class="custom-footer">
    <p>&copy; 2025 CrypticX. All rights reserved.</p>
    <div class="footer-links">
        <a href="#" class="footer-link">Privacy</a>
        <a href="#" class="footer-link">Terms</a>
        <a href="#" class="footer-link">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)
```
