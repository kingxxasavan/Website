import streamlit as st

st.set_page_config(
    page_title="CrypticX - AI Study Tool",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'selected_plan' not in st.session_state:
    st.session_state.selected_plan = None
if 'auth_mode' not in st.session_state:
    st.session_state.auth_mode = 'signup'  # Default to signup
if 'user_name' not in st.session_state:
    st.session_state.user_name = None

# Full CSS (paste your original <style> block here - includes all: hero, pricing, auth, dashboard, etc.)
st.markdown("""
<style>
    /* Paste your entire original CSS here - no changes needed. Includes .hero-section, .pricing-grid, .auth-container, .dashboard-section, responsive, etc. */
    /* For example: */
    * {margin: 0; padding: 0; box-sizing: border-box;}
    .stApp {background: #0a0a0f; color: #fff; font-family: 'Inter', sans-serif;}
    /* ... (full CSS from your first message) ... */
    .auth-container {min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 2rem;}
    .auth-box {max-width: 480px; width: 100%; background: rgba(139, 92, 246, 0.05); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 24px; padding: 3rem; backdrop-filter: blur(20px);}
    .auth-title {font-size: 2.5rem; font-weight: 700; background: linear-gradient(135deg, #ffffff 0%, #8b5cf6 50%, #ec4899 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    /* ... (rest of auth, dashboard, etc.) ... */
</style>
""", unsafe_allow_html=True)

# Background
st.markdown("""
<div class="grid-background"></div>
<div class="glow-orb purple"></div>
<div class="glow-orb pink"></div>
""", unsafe_allow_html=True)

if not st.session_state.logged_in:
    if st.session_state.current_page == 'auth':
        # AUTH PAGE
        st.markdown('<div class="content-wrapper"><div class="auth-container"><div class="auth-box">', unsafe_allow_html=True)
        
        if st.button("← Back to Home"):
            st.session_state.current_page = 'home'
            st.session_state.selected_plan = None
            st.rerun()
        
        if st.session_state.selected_plan:
            st.markdown(f'<div class="welcome-badge">Selected Plan: {st.session_state.selected_plan}</div>', unsafe_allow_html=True)
        
        if st.session_state.auth_mode == 'login':
            st.markdown('<div class="auth-header"><h1 class="auth-title">Welcome Back</h1><p class="auth-subtitle">Sign in to access your dashboard</p></div>', unsafe_allow_html=True)
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Password", type="password", key="login_password")
            if st.button("Sign In"):
                if email and password:
                    st.session_state.logged_in = True
                    st.session_state.current_page = 'dashboard'
                    st.rerun()
                else:
                    st.error("Please fill all fields")
            if st.button("Create Account"):
                st.session_state.auth_mode = 'signup'
                st.rerun()
        else:
            st.markdown('<div class="auth-header"><h1 class="auth-title">Create Account</h1><p class="auth-subtitle">Join and start your AI learning journey</p></div>', unsafe_allow_html=True)
            name = st.text_input("Full Name", key="signup_name")
            email = st.text_input("Email", key="signup_email")
            password = st.text_input("Password", type="password", key="signup_password")
            if st.button("Create Account"):
                if name and email and password:
                    st.session_state.logged_in = True
                    st.session_state.user_name = name
                    st.session_state.current_page = 'dashboard'
                    st.rerun()
                else:
                    st.error("Please fill all fields")
            if st.button("Sign In"):
                st.session_state.auth_mode = 'login'
                st.rerun()
        
        st.markdown('</div></div></div>', unsafe_allow_html=True)
    else:
        # LANDING PAGE
        st.markdown('<div class="nav-container"><nav><div class="logo">⚡ CrypticX</div><div class="nav-links"><span>Home</span><span>Pricing</span><span>Dashboard</span><span>Login</span><button class="nav-cta">Sign Up</button></div></nav></div>', unsafe_allow_html=True)
        st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
        
        # Hero
        st.markdown('<div class="hero-section"><div class="welcome-badge">✨ Welcome to CrypticX</div><h1 class="hero-title">Master Your Studies with AI</h1><p class="hero-subtitle">Transform learning with AI tools.</p>', unsafe_allow_html=True)
        if st.button("Start Learning Free"):
            st.session_state.selected_plan = 'Free'
            st.session_state.current_page = 'auth'
            st.rerun()
        st.markdown('<div class="stats-section"><!-- Stats --></div></div>', unsafe_allow_html=True)
        
        # Features (abbrev - paste full)
        st.markdown('<div class="section"><h2 class="section-title">Why CrypticX</h2><div class="features-grid"><!-- Full features --></div></div>', unsafe_allow_html=True)
        
        # Pricing
        st.markdown('<div class="section"><h2 class="section-title">Choose Plan</h2><div class="pricing-grid">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Start Free"):
                st.session_state.selected_plan = 'Free'
                st.session_state.current_page = 'auth'
                st.rerun()
            st.markdown('<div class="pricing-card"><!-- Free details --></div>', unsafe_allow_html=True)
        with col2:
            if st.button("Get Pro"):
                st.session_state.selected_plan = 'Pro'
                st.session_state.current_page = 'auth'
                st.rerun()
            st.markdown('<div class="pricing-card featured"><!-- Pro details --></div>', unsafe_allow_html=True)
        with col3:
            if st.button("Get Enterprise"):
                st.session_state.selected_plan = 'Enterprise'
                st.session_state.current_page = 'auth'
                st.rerun()
            st.markdown('<div class="pricing-card"><!-- Enterprise details --></div>', unsafe_allow_html=True)
        st.markdown('</div></div></div>', unsafe_allow_html=True)
else:
    # DASHBOARD (main product)
    st.markdown(f'<div class="nav-container"><nav><div class="logo">⚡ CrypticX</div><div class="nav-links"><span>Home</span><span>Pricing</span><span class="nav-link active">Dashboard</span><span class="user-greeting">Hi, {st.session_state.user_name}!</span></div></nav></div>', unsafe_allow_html=True)
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    
    st.markdown(f'<div class="dashboard-section"><h1 class="dashboard-welcome">Welcome, {st.session_state.user_name}!</h1><p class="dashboard-subtitle">Your dashboard {f"(Plan: {st.session_state.selected_plan})" if st.session_state.selected_plan else ""}</p><div class="dashboard-stats"><!-- Stats --></div><div style="text-align: center;"><h3>Ask AI:</h3>{st.chat_input("Your question")}</div></div>', unsafe_allow_html=True)
    
    if st.button("Logout"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="custom-footer"><p>&copy; 2025 CrypticX</p></div>', unsafe_allow_html=True)
