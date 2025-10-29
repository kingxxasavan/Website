import streamlit as st

st.set_page_config(
    page_title="CrypticX - AI Study Tool",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS with better colors and spacing
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
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #fff;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    /* Animated background */
    .bg-gradient {
        position: fixed;
        inset: 0;
        background: 
            radial-gradient(circle at 20% 50%, rgba(120, 119, 198, 0.3), transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(138, 43, 226, 0.3), transparent 50%),
            radial-gradient(circle at 40% 20%, rgba(72, 85, 218, 0.2), transparent 50%);
        z-index: 0;
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    /* Navigation */
    nav {
        position: relative;
        z-index: 100;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.5rem 3rem;
        max-width: 1400px;
        margin: 0 auto;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .logo {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        font-size: 1.8rem;
        font-weight: 700;
        color: #fff;
        cursor: pointer;
    }
    
    .logo-icon {
        font-size: 2rem;
        filter: drop-shadow(0 0 10px rgba(138, 43, 226, 0.8));
    }
    
    /* Button styling */
    .stButton > button {
        all: unset;
        padding: 0.6rem 1.5rem;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.1);
        color: #fff !important;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s;
        font-size: 0.95rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .stButton > button:hover {
        background: rgba(255, 255, 255, 0.15);
        transform: translateY(-2px);
    }
    
    button[kind="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    button[kind="primary"]:hover {
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        transform: translateY(-3px);
    }
    
    /* Hero section */
    .hero {
        position: relative;
        z-index: 10;
        max-width: 1200px;
        margin: 0 auto;
        padding: 5rem 2rem;
        text-align: center;
    }
    
    .hero h1 {
        font-size: 4rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero p {
        font-size: 1.3rem;
        color: rgba(255, 255, 255, 0.8);
        margin-bottom: 3rem;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.6;
    }
    
    .cta-buttons {
        display: flex;
        gap: 1rem;
        justify-content: center;
        margin-top: 2rem;
    }
    
    /* Sections */
    .section {
        position: relative;
        z-index: 10;
        max-width: 1200px;
        margin: 4rem auto;
        padding: 0 2rem;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
        color: #fff;
    }
    
    .section-subtitle {
        font-size: 1.1rem;
        color: rgba(255, 255, 255, 0.7);
        text-align: center;
        margin-bottom: 3rem;
    }
    
    /* Feature cards */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2.5rem;
        transition: all 0.3s;
        backdrop-filter: blur(10px);
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1.5rem;
        display: block;
    }
    
    .feature-card h3 {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        color: #fff;
    }
    
    .feature-card p {
        color: rgba(255, 255, 255, 0.7);
        line-height: 1.6;
    }
    
    /* Pricing cards */
    .pricing-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .pricing-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2.5rem;
        text-align: center;
        transition: all 0.3s;
    }
    
    .pricing-card.featured {
        background: rgba(102, 126, 234, 0.1);
        border: 2px solid #667eea;
        transform: scale(1.05);
    }
    
    .pricing-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
    }
    
    .price {
        font-size: 3rem;
        font-weight: 800;
        margin: 1rem 0;
        color: #667eea;
    }
    
    .price-period {
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.6);
    }
    
    .feature-list {
        text-align: left;
        margin: 2rem 0;
        color: rgba(255, 255, 255, 0.8);
        line-height: 2;
    }
    
    /* Form styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px !important;
        color: #fff !important;
        font-size: 1rem !important;
        padding: 1rem !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2) !important;
    }
    
    /* Auth container */
    .auth-container {
        max-width: 450px;
        margin: 3rem auto;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 25px;
        padding: 3rem;
        backdrop-filter: blur(10px);
    }
    
    /* Footer */
    .custom-footer {
        position: relative;
        z-index: 10;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        margin-top: 5rem;
        padding: 2rem;
        text-align: center;
        color: rgba(255, 255, 255, 0.6);
        background: rgba(255, 255, 255, 0.02);
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        nav {padding: 1rem;}
        .hero h1 {font-size: 2.5rem;}
        .hero p {font-size: 1.1rem;}
        .features-grid, .pricing-grid {grid-template-columns: 1fr;}
        .pricing-card.featured {transform: scale(1);}
    }
</style>
""", unsafe_allow_html=True)

# Background
st.markdown('<div class="bg-gradient"></div>', unsafe_allow_html=True)

# Session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'show_auth_modal' not in st.session_state:
    st.session_state.show_auth_modal = False
if 'auth_mode' not in st.session_state:
    st.session_state.auth_mode = 'login'

def set_page(page_name):
    st.session_state.current_page = page_name
    st.session_state.show_auth_modal = False

def show_auth(mode='login'):
    st.session_state.show_auth_modal = True
    st.session_state.auth_mode = mode

# Navigation
st.markdown("""
    <nav>
        <div class="logo">
            <span class="logo-icon">⚡</span>
            <span>CrypticX</span>
        </div>
    </nav>
""", unsafe_allow_html=True)

nav_cols = st.columns([1, 1, 1, 1, 6, 1, 1])
with nav_cols[0]:
    if st.button("Home", key="nav_home"):
        set_page("home")
with nav_cols[1]:
    if st.button("Features", key="nav_features"):
        set_page("features")
with nav_cols[2]:
    if st.button("Pricing", key="nav_pricing"):
        set_page("pricing")
with nav_cols[3]:
    if st.button("Contact", key="nav_contact"):
        set_page("contact")
with nav_cols[5]:
    if st.button("Login", key="nav_login"):
        show_auth('login')
with nav_cols[6]:
    if st.button("Sign Up", key="nav_signup", type="primary"):
        show_auth('signup')

# Auth Modal
if st.session_state.show_auth_modal:
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    
    if st.session_state.auth_mode == 'login':
        st.markdown("<h2 style='text-align: center; margin-bottom: 1rem;'>Welcome Back</h2>", unsafe_allow_html=True)
        email = st.text_input("Email", placeholder="your@email.com", key="login_email")
        password = st.text_input("Password", placeholder="••••••••", type="password", key="login_password")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Login", key="login_btn", type="primary", use_container_width=True):
                if email and password:
                    st.success("Login successful!")
                    set_page("dashboard")
                    st.rerun()
                else:
                    st.error("Please fill all fields")
        with col2:
            if st.button("Sign Up Instead", key="switch_signup", use_container_width=True):
                st.session_state.auth_mode = 'signup'
                st.rerun()
    else:
        st.markdown("<h2 style='text-align: center; margin-bottom: 1rem;'>Create Account</h2>", unsafe_allow_html=True)
        name = st.text_input("Full Name", placeholder="John Doe", key="signup_name")
        email = st.text_input("Email", placeholder="your@email.com", key="signup_email")
        password = st.text_input("Password", placeholder="••••••••", type="password", key="signup_password")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Sign Up", key="signup_btn", type="primary", use_container_width=True):
                if name and email and password:
                    st.success("Account created!")
                    set_page("dashboard")
                    st.rerun()
                else:
                    st.error("Please fill all fields")
        with col2:
            if st.button("Login Instead", key="switch_login", use_container_width=True):
                st.session_state.auth_mode = 'login'
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# PAGE CONTENT
if st.session_state.current_page == 'home' and not st.session_state.show_auth_modal:
    st.markdown("""
    <div class="hero">
        <h1>Study Smarter with AI</h1>
        <p>Master any subject with personalized AI tutoring, instant explanations, and smart study tools designed for modern students.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Get Started Free", key="hero_cta", type="primary", use_container_width=True):
            show_auth('signup')
            st.rerun()
    
    st.markdown("""
    <div class="section">
        <h2 class="section-title">Why Students Choose CrypticX</h2>
        <p class="section-subtitle">Powerful AI tools designed to help you excel</p>
        
        <div class="features-grid">
            <div class="feature-card">
                <span class="feature-icon">🎯</span>
                <h3>Instant Answers</h3>
                <p>Get explanations for any topic in seconds. Never get stuck on homework again.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">📚</span>
                <h3>Smart Summaries</h3>
                <p>Upload textbooks or notes and get concise summaries that save hours of reading.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">✨</span>
                <h3>Practice Quizzes</h3>
                <p>Auto-generate quizzes from any material to test your knowledge and track progress.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.current_page == 'features':
    st.markdown("""
    <div class="section">
        <h2 class="section-title">Powerful Study Features</h2>
        <p class="section-subtitle">Everything you need to ace your classes</p>
        
        <div class="features-grid">
            <div class="feature-card">
                <span class="feature-icon">🤖</span>
                <h3>AI Tutor</h3>
                <p>24/7 access to an intelligent tutor that explains concepts in your learning style.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">📄</span>
                <h3>Document Analysis</h3>
                <p>Upload PDFs, Word docs, or slides and get instant summaries and key points.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">🎴</span>
                <h3>Flashcard Generator</h3>
                <p>Automatically create flashcards from your study materials for efficient memorization.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">📊</span>
                <h3>Progress Tracking</h3>
                <p>Monitor your learning with detailed analytics and personalized recommendations.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">✍️</span>
                <h3>Essay Helper</h3>
                <p>Get help outlining, structuring, and improving your essays with AI feedback.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">🔒</span>
                <h3>Privacy First</h3>
                <p>Your data is encrypted and never shared. Study with complete peace of mind.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.current_page == 'pricing':
    st.markdown("""
    <div class="section">
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
            </div>
            
            <div class="pricing-card featured">
                <div style="color: #667eea; font-weight: 700; margin-bottom: 1rem;">⭐ MOST POPULAR</div>
                <h3>Pro</h3>
                <div class="price">$12<span class="price-period">/mo</span></div>
                <div class="feature-list">
                    ✓ Unlimited AI questions<br>
                    ✓ Advanced summaries<br>
                    ✓ Unlimited quizzes<br>
                    ✓ PDF upload (100MB)<br>
                    ✓ Priority support<br>
                    ✓ Progress analytics
                </div>
            </div>
            
            <div class="pricing-card">
                <h3>Ultimate</h3>
                <div class="price">$25<span class="price-period">/mo</span></div>
                <div class="feature-list">
                    ✓ Everything in Pro<br>
                    ✓ Group collaboration<br>
                    ✓ Custom AI training<br>
                    ✓ 1-on-1 tutoring sessions<br>
                    ✓ Exam prep tools<br>
                    ✓ 24/7 VIP support
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Start Free", key="price_free", use_container_width=True):
            show_auth('signup')
            st.rerun()
    with col2:
        if st.button("Try Pro Free", key="price_pro", type="primary", use_container_width=True):
            show_auth('signup')
            st.rerun()
    with col3:
        if st.button("Contact Sales", key="price_ult", use_container_width=True):
            set_page("contact")
            st.rerun()

elif st.session_state.current_page == 'contact':
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>Get In Touch</h2>", unsafe_allow_html=True)
    
    name = st.text_input("Name", placeholder="Your name")
    email = st.text_input("Email", placeholder="your@email.com")
    message = st.text_area("Message", placeholder="How can we help?", height=150)
    
    if st.button("Send Message", key="contact_btn", type="primary", use_container_width=True):
        if name and email and message:
            st.success("Thanks! We'll get back to you within 24 hours.")
        else:
            st.error("Please fill in all fields")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'dashboard':
    st.markdown("""
    <div class="section">
        <h2 class="section-title">Your Dashboard</h2>
        <p class="section-subtitle">Access all your study tools</p>
        
        <div class="features-grid">
            <div class="feature-card">
                <span class="feature-icon">🧠</span>
                <h3>AI Explainer</h3>
                <p>Ask any question and get instant, detailed explanations.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">📄</span>
                <h3>PDF Summarizer</h3>
                <p>Upload documents for quick summaries and key insights.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">❓</span>
                <h3>Quiz Generator</h3>
                <p>Create practice tests from any study material.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <footer class="custom-footer">
        <p>© 2025 CrypticX • Empowering students with AI</p>
    </footer>
""", unsafe_allow_html=True)
