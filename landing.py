import streamlit as st

st.set_page_config(
    page_title="CrypticX - AI Study Tool",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Enhanced CSS
st.markdown("""
<style>
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
    .stApp {background: #0a0a0f; color: #fff; font-family: 'Inter', sans-serif;}
    
    /* Background */
    .grid-background {position: fixed; inset: 0; background-image: linear-gradient(rgba(139, 92, 246, 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(139, 92, 246, 0.03) 1px, transparent 1px); background-size: 50px 50px; z-index: 0;}
    .glow-orb {position: fixed; width: 800px; height: 800px; border-radius: 50%; filter: blur(120px); opacity: 0.3; z-index: 1; pointer-events: none;}
    .glow-orb.purple {background: radial-gradient(circle, rgba(139, 92, 246, 0.6), transparent); top: -200px; left: 50%; transform: translateX(-50%); animation: float 20s ease-in-out infinite;}
    .glow-orb.pink {background: radial-gradient(circle, rgba(236, 72, 153, 0.4), transparent); bottom: -300px; right: -200px; animation: float 25s ease-in-out infinite reverse;}
    @keyframes float {0%, 100% { transform: translate(-50%, 0) scale(1); } 50% { transform: translate(-50%, -50px) scale(1.1); }}
    
    /* Navigation */
    .nav-container {position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: transparent; backdrop-filter: blur(20px); border-bottom: 1px solid rgba(139, 92, 246, 0.1);}
    nav {display: flex; justify-content: space-between; align-items: center; padding: 1.5rem 4rem; max-width: 1400px; margin: 0 auto;}
    .logo {display: flex; align-items: center; gap: 0.75rem; font-size: 1.5rem; font-weight: 700; color: #8b5cf6;}
    .logo-icon {font-size: 1.8rem;}
    
    /* Content */
    .content-wrapper {position: relative; z-index: 10; padding-top: 80px;}
    .hero-section {min-height: calc(100vh - 80px); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 4rem 2rem;}
    .welcome-badge {display: inline-flex; background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); padding: 0.6rem 1.5rem; border-radius: 50px; font-size: 0.9rem; margin-bottom: 2rem;}
    .hero-title {font-size: 5rem; font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem; background: linear-gradient(135deg, #ffffff 0%, #8b5cf6 50%, #ec4899 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; max-width: 1000px;}
    .hero-subtitle {font-size: 1.25rem; color: rgba(255, 255, 255, 0.6); margin-bottom: 3rem; max-width: 700px; line-height: 1.7;}
    
    .stats-section {display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; max-width: 900px; margin: 4rem auto 0;}
    .stat-number {font-size: 3rem; font-weight: 800; background: linear-gradient(135deg, #8b5cf6, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    .stat-label {color: rgba(255, 255, 255, 0.6); font-size: 0.95rem; margin-top: 0.5rem;}
    
    .section {max-width: 1200px; margin: 0 auto; padding: 6rem 2rem;}
    .section-title {font-size: 3rem; font-weight: 700; text-align: center; margin-bottom: 1rem; color: #fff;}
    .section-subtitle {font-size: 1.15rem; color: rgba(255, 255, 255, 0.5); text-align: center; margin-bottom: 4rem;}
    
    .features-grid {display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-top: 3rem;}
    .feature-card {background: rgba(139, 92, 246, 0.05); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 24px; padding: 2.5rem; transition: all 0.4s; text-align: center;}
    .feature-card:hover {transform: translateY(-10px); background: rgba(139, 92, 246, 0.1); box-shadow: 0 20px 60px rgba(139, 92, 246, 0.2);}
    .feature-icon {font-size: 3rem; margin-bottom: 1.5rem;}
    .feature-card h3 {font-size: 1.5rem; margin-bottom: 1rem; color: #fff;}
    .feature-card p {color: rgba(255, 255, 255, 0.6); line-height: 1.7;}
    
    .pricing-grid {display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-top: 3rem;}
    .pricing-card {background: rgba(139, 92, 246, 0.05); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 24px; padding: 3rem 2.5rem; text-align: center; transition: all 0.4s; position: relative;}
    .pricing-card.featured {background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(236, 72, 153, 0.15)); border: 2px solid #8b5cf6; transform: scale(1.05);}
    .pricing-card:hover {transform: translateY(-10px); box-shadow: 0 20px 60px rgba(139, 92, 246, 0.3);}
    .pricing-badge {position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: linear-gradient(135deg, #8b5cf6, #ec4899); color: white; padding: 0.4rem 1.2rem; border-radius: 20px; font-size: 0.8rem;}
    .pricing-card h3 {font-size: 1.5rem; margin-bottom: 1rem; color: #fff;}
    .price {font-size: 3.5rem; font-weight: 800; margin: 1.5rem 0; background: linear-gradient(135deg, #8b5cf6, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    .price-period {font-size: 1rem; color: rgba(255, 255, 255, 0.5);}
    .feature-list {text-align: left; margin: 2rem 0; color: rgba(255, 255, 255, 0.7); line-height: 2.2;}
    
    /* Auth Pages - COMPACT & CENTERED */
    .auth-page {min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 2rem;}
    .auth-box {max-width: 400px; width: 100%; background: rgba(30, 30, 45, 0.9); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 20px; padding: 2rem; backdrop-filter: blur(20px); margin: 0 auto;}
    .auth-icon {width: 50px; height: 50px; background: linear-gradient(135deg, #8b5cf6, #ec4899); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; margin: 0 auto 1rem;}
    .auth-title {font-size: 1.5rem; font-weight: 700; color: #fff; margin-bottom: 0.5rem; text-align: center;}
    .auth-subtitle {color: rgba(255, 255, 255, 0.6); font-size: 0.85rem; text-align: center; margin-bottom: 1.5rem;}
    .auth-link {color: #8b5cf6; cursor: pointer; font-weight: 600;}
    .auth-link:hover {color: #ec4899;}
    .auth-divider {display: flex; align-items: center; margin: 1rem 0; color: rgba(255, 255, 255, 0.4); font-size: 0.85rem;}
    .auth-divider::before, .auth-divider::after {content: ''; flex: 1; height: 1px; background: rgba(139, 92, 246, 0.2);}
    .auth-divider span {padding: 0 0.8rem;}
    .social-buttons {display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem; margin-top: 1rem;}
    .social-btn {padding: 0.7rem; background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 10px; color: #fff; font-size: 0.85rem; text-align: center;}
    
    /* Streamlit overrides */
    .stTextInput > div > div > input {background: rgba(255, 255, 255, 0.05) !important; border: 1px solid rgba(139, 92, 246, 0.3) !important; border-radius: 10px !important; color: #fff !important; padding: 0.8rem !important; font-size: 0.9rem !important;}
    .stTextInput > div > div > input:focus {border-color: #8b5cf6 !important; box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.2) !important;}
    .stButton > button {width: 100%; padding: 0.8rem !important; border-radius: 10px !important; background: linear-gradient(135deg, #8b5cf6, #ec4899) !important; color: #fff !important; font-weight: 600 !important; border: none !important; font-size: 0.9rem !important;}
    .stButton > button:hover {transform: translateY(-2px) !important; box-shadow: 0 8px 25px rgba(139, 92, 246, 0.4) !important;}
    
    .custom-footer {border-top: 1px solid rgba(139, 92, 246, 0.1); margin-top: 5rem; padding: 3rem 2rem; text-align: center; color: rgba(255, 255, 255, 0.4);}
    
    @media (max-width: 1024px) {.features-grid, .pricing-grid {grid-template-columns: repeat(2, 1fr);}}
    @media (max-width: 768px) {.hero-title {font-size: 2.5rem;} .features-grid, .pricing-grid, .stats-section {grid-template-columns: 1fr;} .auth-box {padding: 1.5rem;}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="grid-background"></div><div class="glow-orb purple"></div><div class="glow-orb pink"></div>', unsafe_allow_html=True)

# Navigation with Streamlit buttons
st.markdown('<div class="nav-container"><nav>', unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6, col7 = st.columns([2, 1, 1, 1, 1, 1, 1])
with col1:
    st.markdown('<div class="logo"><span class="logo-icon">⚡</span><span>CrypticX</span></div>', unsafe_allow_html=True)
with col3:
    if st.button("Home", key="home_nav"):
        st.session_state.page = 'home'
        st.rerun()
with col4:
    if st.button("Pricing", key="pricing_nav"):
        st.session_state.page = 'home'
        st.rerun()
with col5:
    if st.button("Dashboard", key="dash_nav"):
        if st.session_state.logged_in:
            st.session_state.page = 'dashboard'
        else:
            st.session_state.page = 'login'
        st.rerun()
with col6:
    if st.button("Login", key="login_nav"):
        st.session_state.page = 'login'
        st.rerun()
with col7:
    if st.button("Sign Up", key="signup_nav", type="primary"):
        st.session_state.page = 'signup'
        st.rerun()
st.markdown('</nav></div>', unsafe_allow_html=True)

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Page routing
if st.session_state.page == 'signup':
    st.markdown("""
    <div class="auth-page">
        <div class="auth-box">
            <div class="auth-icon">😊</div>
            <h2 class="auth-title">Create Account</h2>
            <p class="auth-subtitle">Join thousands of students</p>
    """, unsafe_allow_html=True)
    
    name = st.text_input("", placeholder="Full Name", key="signup_name", label_visibility="collapsed")
    email = st.text_input("", placeholder="Email Address", key="signup_email", label_visibility="collapsed")
    password = st.text_input("", type="password", placeholder="Password", key="signup_password", label_visibility="collapsed")
    
    if st.button("Create Account", key="signup_submit"):
        if name and email and password:
            st.success("✅ Account created!")
            st.session_state.logged_in = True
            st.session_state.page = 'dashboard'
            st.rerun()
        else:
            st.error("Please fill all fields")
    
    st.markdown('<div style="text-align: center; margin-top: 1rem; font-size: 0.85rem; color: rgba(255,255,255,0.6);">Already have an account? <span class="auth-link">Sign In</span></div>', unsafe_allow_html=True)
    
    if st.button("Sign In Instead", key="switch_login", use_container_width=True):
        st.session_state.page = 'login'
        st.rerun()
    
    st.markdown('<div class="auth-divider"><span>Or continue with</span></div><div class="social-buttons"><div class="social-btn">🌐 Google</div><div class="social-btn">📘 Facebook</div></div></div></div>', unsafe_allow_html=True)

elif st.session_state.page == 'login':
    st.markdown("""
    <div class="auth-page">
        <div class="auth-box">
            <div class="auth-icon">👋</div>
            <h2 class="auth-title">Welcome Back</h2>
            <p class="auth-subtitle">Sign in to continue</p>
    """, unsafe_allow_html=True)
    
    email = st.text_input("", placeholder="Email Address", key="login_email", label_visibility="collapsed")
    password = st.text_input("", type="password", placeholder="Password", key="login_password", label_visibility="collapsed")
    
    if st.button("Sign In", key="login_submit"):
        if email and password:
            st.success("✅ Login successful!")
            st.session_state.logged_in = True
            st.session_state.page = 'dashboard'
            st.rerun()
        else:
            st.error("Please fill all fields")
    
    st.markdown('<div style="text-align: center; margin-top: 1rem; font-size: 0.85rem; color: rgba(255,255,255,0.6);">Don\'t have an account? <span class="auth-link">Sign Up</span></div>', unsafe_allow_html=True)
    
    if st.button("Create Account", key="switch_signup", use_container_width=True):
        st.session_state.page = 'signup'
        st.rerun()
    
    st.markdown('<div class="auth-divider"><span>Or continue with</span></div><div class="social-buttons"><div class="social-btn">🌐 Google</div><div class="social-btn">📘 Facebook</div></div></div></div>', unsafe_allow_html=True)

elif st.session_state.page == 'dashboard' and st.session_state.logged_in:
    st.markdown("""
    <div class="dashboard-container" style="padding-top: 100px; max-width: 1200px; margin: 0 auto; padding: 6rem 2rem;">
        <h1 class="dashboard-title" style="font-size: 2.5rem; font-weight: 700; color: #fff; margin-bottom: 0.5rem;">Welcome to Your Dashboard! 🎉</h1>
        <p class="dashboard-subtitle" style="color: rgba(255, 255, 255, 0.6); font-size: 1.1rem; margin-bottom: 3rem;">Your learning journey starts here</p>
        <div class="features-grid">
            <div class="feature-card"><span class="feature-icon">📚</span><h3>My Courses</h3><p>Access all your courses</p></div>
            <div class="feature-card"><span class="feature-icon">📊</span><h3>Progress</h3><p>Track your progress</p></div>
            <div class="feature-card"><span class="feature-icon">🎯</span><h3>Quizzes</h3><p>Test your knowledge</p></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

else:
    # HOME PAGE
    st.markdown("""
    <div id="home" class="hero-section">
        <div class="welcome-badge">✨ Welcome to CrypticX</div>
        <h1 class="hero-title">Master Your Studies with AI-Powered Learning</h1>
        <p class="hero-subtitle">Transform the way you learn with intelligent tools designed to help you understand faster, remember longer, and achieve academic excellence.</p>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Start Learning Free", key="hero_cta", type="primary", use_container_width=True):
            st.session_state.page = 'signup'
            st.rerun()
    
    st.markdown("""
        <div class="stats-section">
            <div style="text-align: center;">
                <div class="stat-number">50K+</div>
                <div class="stat-label">Active Students</div>
            </div>
            <div style="text-align: center;">
                <div class="stat-number">95%</div>
                <div class="stat-label">Satisfaction Rate</div>
            </div>
            <div style="text-align: center;">
                <div class="stat-number">1M+</div>
                <div class="stat-label">Questions Answered</div>
            </div>
        </div>
    </div>
    
    <div id="why-choose" class="section">
        <h2 class="section-title">Why Choose CrypticX</h2>
        <p class="section-subtitle">The smartest way to study in 2025</p>
        <div class="features-grid">
            <div class="feature-card"><span class="feature-icon">⚡</span><h3>Lightning Fast</h3><p>Get instant answers to your questions</p></div>
            <div class="feature-card"><span class="feature-icon">🎯</span><h3>Personalized Learning</h3><p>AI adapts to your learning style</p></div>
            <div class="feature-card"><span class="feature-icon">💰</span><h3>Affordable Excellence</h3><p>Premium quality at a fraction of cost</p></div>
            <div class="feature-card"><span class="feature-icon">📱</span><h3>Study Anywhere</h3><p>Access from any device, anytime</p></div>
            <div class="feature-card"><span class="feature-icon">🔬</span><h3>Proven Methods</h3><p>Built on learning science</p></div>
            <div class="feature-card"><span class="feature-icon">🌟</span><h3>Student Success</h3><p>Join thousands of students</p></div>
        </div>
    </div>
    
    <div id="pricing" class="section">
        <h2 class="section-title">Choose Your Plan</h2>
        <p class="section-subtitle">Start free, upgrade when you're ready</p>
        <div class="pricing-grid">
            <div class="pricing-card">
                <h3>Free</h3>
                <div class="price">$0<span class="price-period">/mo</span></div>
                <div class="feature-list">
                    ✓ 10 AI questions/day<br>
                    ✓ Basic summaries<br>
                    ✓ 5 quizzes/week<br>
                    ✓ Community support
                </div>
    """, unsafe_allow_html=True)
    
    if st.button("Start Free", key="price_free", use_container_width=True):
        st.session_state.page = 'signup'
        st.rerun()
    
    st.markdown("""
            </div>
            <div class="pricing-card featured">
                <div class="pricing-badge">⭐ MOST POPULAR</div>
                <h3>Pro</h3>
                <div class="price">$15<span class="price-period">/mo</span></div>
                <div class="feature-list">
                    ✓ Unlimited AI questions<br>
                    ✓ Advanced summaries<br>
                    ✓ Unlimited quizzes<br>
                    ✓ PDF upload (100MB)<br>
                    ✓ Priority support<br>
                    ✓ Progress analytics
                </div>
    """, unsafe_allow_html=True)
    
    if st.button("Get Pro", key="price_pro", use_container_width=True):
        st.session_state.page = 'signup'
        st.rerun()
    
    st.markdown("""
            </div>
            <div class="pricing-card">
                <h3>Enterprise</h3>
                <div class="price">$35<span class="price-period">/mo</span></div>
                <div class="feature-list">
                    ✓ Everything in Pro<br>
                    ✓ Team accounts<br>
                    ✓ Advanced analytics<br>
                    ✓ Custom integrations<br>
                    ✓ Dedicated support<br>
                    ✓ Unlimited storage
                </div>
    """, unsafe_allow_html=True)
    
    if st.button("Get Enterprise", key="price_enterprise", use_container_width=True):
        st.session_state.page = 'signup'
        st.rerun()
    
    st.markdown('</div></div></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="custom-footer">
    <p>&copy; 2025 CrypticX. All rights reserved.</p>
    <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 1rem;">
        <a href="#" style="color: rgba(255, 255, 255, 0.5); text-decoration: none;">Privacy</a>
        <a href="#" style="color: rgba(255, 255, 255, 0.5); text-decoration: none;">Terms</a>
        <a href="#" style="color: rgba(255, 255, 255, 0.5); text-decoration: none;">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)
