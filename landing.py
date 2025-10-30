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
    .grid-background {position: fixed; inset: 0; background-image: linear-gradient(rgba(139, 92, 246, 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(139, 92, 246, 0.03) 1px, transparent 1px); background-size: 50px 50px; z-index: 0;}
    .glow-orb {position: fixed; width: 800px; height: 800px; border-radius: 50%; filter: blur(120px); opacity: 0.3; z-index: 1; pointer-events: none;}
    .glow-orb.purple {background: radial-gradient(circle, rgba(139, 92, 246, 0.6), transparent); top: -200px; left: 50%; transform: translateX(-50%); animation: float 20s ease-in-out infinite;}
    .glow-orb.pink {background: radial-gradient(circle, rgba(236, 72, 153, 0.4), transparent); bottom: -300px; right: -200px; animation: float 25s ease-in-out infinite reverse;}
    @keyframes float {0%, 100% { transform: translate(-50%, 0) scale(1); } 50% { transform: translate(-50%, -50px) scale(1.1); }}
    @keyframes fadeInUp {from {opacity: 0; transform: translateY(30px);} to {opacity: 1; transform: translateY(0);}}
    .nav-container {position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: transparent; backdrop-filter: blur(20px); border-bottom: 1px solid rgba(139, 92, 246, 0.1); transition: all 0.3s ease;}
    nav {display: flex; justify-content: space-between; align-items: center; padding: 1.5rem 4rem; max-width: 1400px; margin: 0 auto;}
    .logo {display: flex; align-items: center; gap: 0.75rem; font-size: 1.5rem; font-weight: 700; color: #8b5cf6; cursor: pointer;}
    .logo-icon {font-size: 1.8rem; filter: drop-shadow(0 0 10px rgba(139, 92, 246, 0.8));}
    .nav-links {display: flex; gap: 2.5rem; align-items: center;}
    .nav-link {color: rgba(255, 255, 255, 0.7); text-decoration: none; font-size: 0.95rem; font-weight: 500; transition: all 0.3s; padding: 0.5rem 0; border-bottom: 2px solid transparent;}
    .nav-link:hover, .nav-link.active {color: #fff; border-bottom-color: #8b5cf6;}
    .nav-cta {padding: 0.7rem 1.8rem; border-radius: 50px; background: linear-gradient(135deg, #8b5cf6, #ec4899); color: #fff; font-weight: 600; cursor: pointer; transition: all 0.3s; border: none; font-size: 0.9rem; box-shadow: 0 4px 20px rgba(139, 92, 246, 0.4);}
    .nav-cta:hover {transform: translateY(-2px); box-shadow: 0 6px 25px rgba(139, 92, 246, 0.6);}
    .content-wrapper {position: relative; z-index: 10; padding-top: 80px;}
    .hero-section {min-height: calc(100vh - 80px); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 4rem 2rem;}
    .welcome-badge {display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); padding: 0.6rem 1.5rem; border-radius: 50px; font-size: 0.9rem; margin-bottom: 2rem; backdrop-filter: blur(10px);}
    .hero-title {font-size: 5rem; font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem; background: linear-gradient(135deg, #ffffff 0%, #8b5cf6 50%, #ec4899 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; max-width: 1000px;}
    .hero-subtitle {font-size: 1.25rem; color: rgba(255, 255, 255, 0.6); margin-bottom: 3rem; max-width: 700px; line-height: 1.7;}
    .hero-cta {padding: 1rem 2.5rem; border-radius: 50px; background: linear-gradient(135deg, #8b5cf6, #ec4899); color: #fff; font-weight: 600; cursor: pointer; transition: all 0.3s; border: none; font-size: 1.1rem; box-shadow: 0 8px 30px rgba(139, 92, 246, 0.4);}
    .hero-cta:hover {transform: translateY(-3px); box-shadow: 0 12px 40px rgba(139, 92, 246, 0.6);}
    .stats-section {display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; max-width: 900px; margin: 4rem auto 0; padding: 0 2rem;}
    .stat-number {font-size: 3rem; font-weight: 800; background: linear-gradient(135deg, #8b5cf6, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem;}
    .stat-label {color: rgba(255, 255, 255, 0.6); font-size: 0.95rem;}
    .section {max-width: 1200px; margin: 0 auto; padding: 6rem 2rem; width: 100%;}
    .section-title {font-size: 3rem; font-weight: 700; text-align: center; margin-bottom: 1rem; color: #fff;}
    .section-subtitle {font-size: 1.15rem; color: rgba(255, 255, 255, 0.5); text-align: center; margin-bottom: 4rem;}
    .features-grid {display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-top: 3rem;}
    .feature-card {background: rgba(139, 92, 246, 0.05); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 24px; padding: 2.5rem; transition: all 0.4s; backdrop-filter: blur(10px); text-align: center;}
    .feature-card:hover {transform: translateY(-10px); background: rgba(139, 92, 246, 0.1); border-color: rgba(139, 92, 246, 0.5); box-shadow: 0 20px 60px rgba(139, 92, 246, 0.2);}
    .feature-icon {font-size: 3rem; margin-bottom: 1.5rem;}
    .feature-card h3 {font-size: 1.5rem; margin-bottom: 1rem; color: #fff; font-weight: 600;}
    .feature-card p {color: rgba(255, 255, 255, 0.6); line-height: 1.7; font-size: 0.95rem;}
    .pricing-grid {display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-top: 3rem;}
    .pricing-card {background: rgba(139, 92, 246, 0.05); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 24px; padding: 3rem 2.5rem; text-align: center; transition: all 0.4s; position: relative;}
    .pricing-card.featured {background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(236, 72, 153, 0.15)); border: 2px solid #8b5cf6; transform: scale(1.05);}
    .pricing-card:hover {transform: translateY(-10px) scale(1.02); box-shadow: 0 20px 60px rgba(139, 92, 246, 0.3);}
    .pricing-badge {position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: linear-gradient(135deg, #8b5cf6, #ec4899); color: white; padding: 0.4rem 1.2rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600;}
    .pricing-card h3 {font-size: 1.5rem; margin-bottom: 1rem; color: #fff;}
    .price {font-size: 3.5rem; font-weight: 800; margin: 1.5rem 0; background: linear-gradient(135deg, #8b5cf6, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    .price-period {font-size: 1rem; color: rgba(255, 255, 255, 0.5);}
    .feature-list {text-align: left; margin: 2rem 0; color: rgba(255, 255, 255, 0.7); line-height: 2.2; font-size: 0.95rem;}
    .pricing-button {width: 100%; padding: 0.9rem; border-radius: 12px; background: rgba(139, 92, 246, 0.2); border: 1px solid rgba(139, 92, 246, 0.3); color: #fff; font-weight: 600; cursor: pointer; transition: all 0.3s; margin-top: 1rem;}
    .pricing-button:hover {background: rgba(139, 92, 246, 0.3); border-color: #8b5cf6; transform: translateY(-2px);}
    .pricing-card.featured .pricing-button {background: linear-gradient(135deg, #8b5cf6, #ec4899); border: none;}
    .auth-page {min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 2rem; position: relative; z-index: 10;}
    .auth-container {display: flex; max-width: 1100px; width: 100%; gap: 4rem; align-items: center;}
    .auth-left {flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center;}
    .buddy-mascot {width: 400px; height: 400px; background: rgba(139, 92, 246, 0.1); border: 2px solid rgba(139, 92, 246, 0.3); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 120px; margin-bottom: 2rem; animation: float 3s ease-in-out infinite;}
    .buddy-speech {background: rgba(139, 92, 246, 0.2); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 20px; padding: 1.5rem 2rem; color: #fff; font-size: 1.1rem; text-align: center; max-width: 350px; position: relative; margin-top: -40px; backdrop-filter: blur(10px);}
    .auth-right {flex: 1; max-width: 450px;}
    .auth-box {background: rgba(30, 30, 45, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 24px; padding: 2.5rem; backdrop-filter: blur(20px);}
    .auth-header {text-align: center; margin-bottom: 2rem;}
    .auth-icon {width: 70px; height: 70px; background: linear-gradient(135deg, #8b5cf6, #ec4899); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 35px; margin: 0 auto 1.5rem;}
    .auth-title {font-size: 1.8rem; font-weight: 700; color: #fff; margin-bottom: 0.5rem;}
    .auth-subtitle {color: rgba(255, 255, 255, 0.5); font-size: 0.95rem;}
    .auth-subtitle .link {color: #8b5cf6; cursor: pointer; text-decoration: none; font-weight: 600;}
    .checkbox-group {display: flex; align-items: flex-start; gap: 0.8rem; margin: 1.5rem 0;}
    .checkbox-label {color: rgba(255, 255, 255, 0.6); font-size: 0.85rem; line-height: 1.5;}
    .checkbox-label a {color: #8b5cf6; text-decoration: none; font-weight: 600;}
    .auth-divider {display: flex; align-items: center; margin: 1.5rem 0; color: rgba(255, 255, 255, 0.4); font-size: 0.9rem;}
    .auth-divider::before, .auth-divider::after {content: ''; flex: 1; height: 1px; background: rgba(139, 92, 246, 0.2);}
    .auth-divider span {padding: 0 1rem;}
    .social-buttons {display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1.5rem;}
    .social-btn {display: flex; align-items: center; justify-content: center; gap: 0.7rem; padding: 0.8rem; background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 12px; color: #fff; font-weight: 600; font-size: 0.9rem; cursor: pointer; transition: all 0.3s;}
    .social-btn:hover {background: rgba(139, 92, 246, 0.2); border-color: #8b5cf6; transform: translateY(-2px);}
    .auth-footer {margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid rgba(139, 92, 246, 0.2); display: flex; justify-content: center; gap: 2rem; font-size: 0.85rem;}
    .footer-link {color: rgba(255, 255, 255, 0.5); text-decoration: none;}
    .dashboard-container {max-width: 1200px; margin: 0 auto; padding: 2rem;}
    .dashboard-title {font-size: 2.5rem; font-weight: 700; color: #fff; margin-bottom: 0.5rem;}
    .dashboard-subtitle {color: rgba(255, 255, 255, 0.6); font-size: 1.1rem;}
    .stTextInput > div > div > input {background: rgba(255, 255, 255, 0.05) !important; border: 1px solid rgba(139, 92, 246, 0.3) !important; border-radius: 12px !important; color: #fff !important; padding: 0.9rem !important;}
    .stTextInput > div > div > input:focus {border-color: #8b5cf6 !important; box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.2) !important;}
    .stButton > button {width: 100%; padding: 0.9rem !important; border-radius: 12px !important; background: linear-gradient(135deg, #8b5cf6, #ec4899) !important; color: #fff !important; font-weight: 600 !important; border: none !important; margin-top: 1rem !important;}
    .stButton > button:hover {transform: translateY(-2px) !important; box-shadow: 0 8px 25px rgba(139, 92, 246, 0.4) !important;}
    .custom-footer {border-top: 1px solid rgba(139, 92, 246, 0.1); margin-top: 5rem; padding: 3rem 2rem; text-align: center; color: rgba(255, 255, 255, 0.4);}
    @media (max-width: 1024px) {.features-grid, .pricing-grid {grid-template-columns: repeat(2, 1fr);} .auth-left {display: none;}}
    @media (max-width: 768px) {nav {padding: 1rem 1.5rem;} .nav-links {display: none;} .hero-title {font-size: 2.5rem;} .features-grid, .pricing-grid, .stats-section {grid-template-columns: 1fr;} .social-buttons {grid-template-columns: 1fr;}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="grid-background"></div><div class="glow-orb purple"></div><div class="glow-orb pink"></div>', unsafe_allow_html=True)

# Navigation
st.markdown(f"""
<div class="nav-container"><nav>
<div class="logo" onclick="window.location.href='?page=home'"><span class="logo-icon">⚡</span><span>CrypticX</span></div>
<div class="nav-links">
<a href="?page=home" class="nav-link {'active' if st.session_state.page == 'home' else ''}">Home</a>
<a href="?page=home#pricing" class="nav-link">Pricing</a>
<a href="?page=dashboard" class="nav-link {'active' if st.session_state.page == 'dashboard' else ''}">Dashboard</a>
<a href="?page=login" class="nav-link {'active' if st.session_state.page == 'login' else ''}">Login</a>
<button class="nav-cta" onclick="window.location.href='?page=signup'">Sign Up</button>
</div></nav></div>
""", unsafe_allow_html=True)

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

query_params = st.query_params
if 'page' in query_params:
    st.session_state.page = query_params['page']

if st.session_state.page == 'signup':
    st.markdown("""
    <div class="auth-page"><div class="auth-container">
    <div class="auth-left">
        <div class="buddy-mascot">🤖</div>
        <div class="buddy-speech"><strong>Hello, Can you help me?</strong><br><span style="color: #8b5cf6; font-weight: 600;">Buddy!</span><br>Sure, Buddy is ready to help you</div>
    </div>
    <div class="auth-right"><div class="auth-box">
        <div class="auth-header">
            <div class="auth-icon">😊</div>
            <h2 class="auth-title">Welcome to Sign Up</h2>
            <p class="auth-subtitle" style="color: #8b5cf6; font-weight: 600;">Buddy!</p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("signup_form"):
        name = st.text_input("", placeholder="Enter your name", key="signup_name", label_visibility="collapsed")
        email = st.text_input("", placeholder="Enter your email", key="signup_email", label_visibility="collapsed")
        password = st.text_input("", type="password", placeholder="Enter your password", key="signup_password", label_visibility="collapsed")
        st.markdown('<div class="checkbox-group"><input type="checkbox" id="terms"/><label class="checkbox-label">I agree to <a href="#">Terms of Conditions</a> and <a href="#">Privacy of Policy</a></label></div>', unsafe_allow_html=True)
        submit = st.form_submit_button("Sign Up", use_container_width=True)
        if submit and name and email and password:
            st.success("✅ Account created! Redirecting...")
            st.session_state.logged_in = True
            st.session_state.page = 'dashboard'
            st.rerun()
    
    st.markdown("""
        <p class="auth-subtitle" style="margin-top: 1.5rem;">Already have an account? <a href="?page=login" class="link">Sign In</a></p>
        <div class="auth-divider"><span>Or continue with</span></div>
        <div class="social-buttons">
            <button class="social-btn">🌐 Google</button>
            <button class="social-btn">📘 Facebook</button>
        </div>
        <div class="auth-footer"><a href="#" class="footer-link">Terms of Service</a><a href="#" class="footer-link">Privacy Policy</a></div>
    </div></div></div></div>
    """, unsafe_allow_html=True)

elif st.session_state.page == 'login':
    st.markdown("""
    <div class="auth-page"><div class="auth-container">
    <div class="auth-left">
        <div class="buddy-mascot">🤖</div>
        <div class="buddy-speech"><strong>Hello, Can you help me?</strong><br><span style="color: #8b5cf6; font-weight: 600;">Buddy!</span><br>Sure, Buddy is ready to help you</div>
    </div>
    <div class="auth-right"><div class="auth-box">
        <div class="auth-header">
            <div class="auth-icon">😊</div>
            <h2 class="auth-title">Welcome to Sign In</h2>
            <p class="auth-subtitle" style="color: #8b5cf6; font-weight: 600;">Buddy!</p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("login_form"):
        email = st.text_input("", placeholder="Enter your email", key="login_email", label_visibility="collapsed")
        password = st.text_input("", type="password", placeholder="Enter your password", key="login_password", label_visibility="collapsed")
        st.markdown('<div class="checkbox-group"><input type="checkbox" id="terms_login"/><label class="checkbox-label">I agree to <a href="#">Terms of Conditions</a> and <a href="#">Privacy of Policy</a></label></div>', unsafe_allow_html=True)
        submit = st.form_submit_button("Sign In", use_container_width=True)
        if submit and email and password:
            st.success("✅ Login successful! Redirecting...")
            st.session_state.logged_in = True
            st.session_state.page = 'dashboard'
            st.rerun()
    
    st.markdown("""
        <p class="auth-subtitle" style="margin-top: 1.5rem;">Don't have an account? <a href="?page=signup" class="link">Sign Up</a></p>
        <div class="auth-divider"><span>Or continue with</span></div>
        <div class="social-buttons">
            <button class="social-btn">🌐 Google</button>
            <button class="social-btn">📘 Facebook</button>
        </div>
        <div class="auth-footer"><a href="#" class="footer-link">Terms of Service</a><a href="#" class="footer-link">Privacy Policy</a></div>
    </div></div></div></div>
    """, unsafe_allow_html=True)

elif st.session_state.page == 'dashboard' and st.session_state.logged_in:
    st.markdown("""
    <div class="dashboard-container" style="padding-top: 100px;">
        <div class="dashboard-header"><h1 class="dashboard-title">Welcome to Your Dashboard! 🎉</h1><p class="dashboard-subtitle">Your learning journey starts here</p></div>
        <div class="features-grid">
            <div class="feature-card"><span class="feature-icon">📚</span><h3>My Courses</h3><p>Access all your enrolled courses</p></div>
            <div class="feature-card"><span class="feature-icon">📊</span><h3>Progress</h3><p>Track your learning progress</p></div>
            <div class="feature-card"><span class="feature-icon">🎯</span><h3>Quizzes</h3><p>Test your knowledge</p></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div id="home" class="hero-section">
    <div class="welcome-badge">✨ Welcome to CrypticX</div>
    <h1 class="hero-title">Master Your Studies with AI-Powered Learning</h1>
    <p class="hero-subtitle">Transform the way you learn with intelligent tools designed to help you understand faster, remember longer, and achieve academic excellence.</p>
    <button class="hero-cta" onclick="window.location.href='?page=signup'">Start Learning Free</button>
    <div class="stats-section">
        <div class="stat-item"><div class="stat-number">50K+</div><div class="stat-label">Active Students</div></div>
        <div class="stat-item"><div class="stat-number">95%</div><div class="stat-label">Satisfaction Rate</div></div>
        <div class="stat-item"><div class="stat-number">1M+</div><div class="stat-label">Questions Answered</div></div>
    </div></div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div id="why-choose" class="section"><h2 class="section-title">Why Choose CrypticX</h2><p class="section-subtitle">The smartest way to study in 2025</p><div class="features-grid">', unsafe_allow_html=True)
    st.markdown("""
    <div class="feature-card"><span class="feature-icon">⚡</span><h3>Lightning Fast</h3><p>Get instant answers to your questions</p></div>
    <div class="feature-card"><span class="feature-icon">🎯</span><h3>Personalized Learning</h3><p>AI adapts to your learning style</p></div>
    <div class="feature-card"><span class="feature-icon">💰</span><h3>Affordable Excellence</h3><p>Premium quality at a fraction of the cost</p></div>
    <div class="feature-card"><span class="feature-icon">📱</span><h3>Study Anywhere</h3><p>Access from any device, anytime</p></div>
    <div class="feature-card"><span class="feature-icon">🔬</span><h3>Proven Methods</h3><p>Built on learning science principles</p></div>
    <div class="feature-card"><span class="feature-icon">🌟</span><h3>Student Success</h3><p>Join thousands of successful students</p></div>
    </div></div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div id="pricing" class="section"><h2 class="section-title">Choose Your Plan</h2><p class="section-subtitle">Start free, upgrade when you\'re ready</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="pricing-grid">
        <div class="pricing-card">
            <h3>Free</h3><div class="price">$0<span class="price-period">/mo</span></div>
            <div class="feature-list">✓ 10 AI questions/day<br>✓ Basic summaries<br>✓ 5 quizzes/week<br>✓ Community support</div>
            <button class="pricing-button" onclick="window.location.href='?page=signup'">Start Free</button>
        </div>
        <div class="pricing-card featured">
            <div class="pricing-badge">⭐ MOST POPULAR</div>
            <h3>Pro</h3><div class="price">$15<span class="price-period">/mo</span></div>
            <div class="feature-list">✓ Unlimited AI questions<br>✓ Advanced summaries<br>✓ Unlimited quizzes<br>✓ PDF upload (100MB)<br>✓ Priority support<br>✓ Progress analytics</div>
            <button class="pricing-button" onclick="window.location.href='?page=signup'">Get Pro</button>
        </div>
        <div class="pricing-card">
            <h3>Enterprise</h3><div class="price">$35<span class="price-period">/mo</span></div>
            <div class="feature-list">✓ Everything in Pro<br>✓ Team accounts<br>✓ Advanced analytics<br>✓ Custom integrations<br>✓ Dedicated support<br>✓ Unlimited storage</div>
            <button class="pricing-button" onclick="window.location.href='?page=signup'">Contact Us</button>
        </div>
    </div></div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="custom-footer">
    <p>&copy; 2025 CrypticX. All rights reserved.</p>
    <div class="footer-links" style="display: flex; justify-content: center; gap: 2rem; margin-top: 1rem;">
        <a href="#" style="color: rgba(255, 255, 255, 0.5); text-decoration: none;">Privacy</a>
        <a href="#" style="color: rgba(255, 255, 255, 0.5); text-decoration: none;">Terms</a>
        <a href="#" style="color: rgba(255, 255, 255, 0.5); text-decoration: none;">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)
