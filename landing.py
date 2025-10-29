import streamlit as st

st.set_page_config(
    page_title="CrypticX - AI Study Tool",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Complete CSS injection - combines hide_streamlit_style + landing page styles
all_css = """
<style>
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    .stDecoration {display: none !important;}
    
    /* Remove padding */
    .block-container {padding: 0 !important; margin: 0 !important;}
    .main .block-container {max-width: 100% !important; padding: 0 !important;}
    .stApp {margin: 0 !important; padding: 0 !important;}
    section.main > div {padding: 0 !important;}
    div[data-testid="stAppViewContainer"] {padding: 0 !important; margin: 0 !important;}
    
    /* Original landing page styles */
    * {margin: 0; padding: 0; box-sizing: border-box;}
    html, body {margin: 0 !important; padding: 0 !important; overflow-x: hidden;}
    
    .stApp {
        background: #000;
        color: #fff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .bg-gradient {position: fixed; inset: 0; background: radial-gradient(ellipse at top right, rgba(88, 28, 135, 0.3) 0%, transparent 50%), radial-gradient(ellipse at bottom left, rgba(29, 78, 216, 0.3) 0%, transparent 50%), #000; z-index: 0; pointer-events: none;}
    .glow-orb {position: fixed; border-radius: 50%; filter: blur(100px); pointer-events: none; z-index: 1;}
    .orb1 {top: -10%; right: -5%; width: 600px; height: 600px; background: radial-gradient(circle, rgba(139, 92, 246, 0.4), transparent); animation: float1 20s ease-in-out infinite;}
    .orb2 {bottom: -10%; left: -5%; width: 700px; height: 700px; background: radial-gradient(circle, rgba(59, 130, 246, 0.4), transparent); animation: float2 25s ease-in-out infinite;}
    @keyframes float1 {0%, 100% {transform: translate(0, 0);} 50% {transform: translate(-100px, 100px);}}
    @keyframes float2 {0%, 100% {transform: translate(0, 0);} 50% {transform: translate(100px, -100px);}}
    
    nav {position: relative; z-index: 100; display: flex; justify-content: space-between; align-items: center; padding: 1.2rem 5rem; max-width: 1600px; margin: 0 auto 2rem; background: rgba(20, 20, 20, 0.6); backdrop-filter: blur(20px); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 20px;}
    .logo {display: flex; align-items: center; gap: 0.5rem; font-size: 1.5rem; font-weight: 700; color: #fff; cursor: pointer;}
    .logo-icon {width: 35px; height: 35px; background: linear-gradient(135deg, #8b5cf6, #6366f1); border-radius: 8px; display: flex; align-items: center; justify-content: center;}
    
    /* Streamlit button styling */
    .stButton > button {
        all: unset;
        padding: 0.7rem 1.8rem;
        border-radius: 12px;
        border: 1px solid rgba(139, 92, 246, 0.5);
        background: transparent;
        color: #fff !important;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s;
        font-size: 0.95rem;
        text-align: center;
    }
    .stButton > button:hover {
        background: rgba(139, 92, 246, 0.1);
        border-color: #8b5cf6;
    }
    
    /* Primary button style */
    button[kind="primary"] {
        background: linear-gradient(135deg, #8b5cf6, #6366f1) !important;
        border: none !important;
    }
    button[kind="primary"]:hover {
        box-shadow: 0 10px 40px rgba(139, 92, 246, 0.5);
        transform: translateY(-2px);
    }
    
    .hero {position: relative; z-index: 10; max-width: 1600px; margin: 0 auto; padding: 3rem 5rem 4rem; display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;}
    .hero-content h1 {font-size: 3.5rem; line-height: 1.1; margin-bottom: 1.2rem; font-weight: 300; letter-spacing: -2px; color: #fff;}
    .hero-content p {font-size: 1.1rem; color: #a0a0a0; margin-bottom: 2rem; line-height: 1.7; max-width: 500px;}
    .hero-note {font-size: 0.9rem; color: #666;}
    
    .section {position: relative; z-index: 10; max-width: 1600px; margin: 4rem auto; padding: 0 5rem;}
    .section-header {text-align: center; margin-bottom: 3rem;}
    .section-title {font-size: 2.8rem; font-weight: 300; margin-bottom: 1rem;}
    .section-subtitle {font-size: 1.1rem; color: #a0a0a0;}
    
    .features-grid {display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;}
    .feature-card {background: rgba(20, 20, 20, 0.6); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 25px; padding: 3rem; transition: all 0.3s; backdrop-filter: blur(20px);}
    .feature-card:hover {border-color: rgba(139, 92, 246, 0.5); box-shadow: 0 20px 60px rgba(139, 92, 246, 0.2); transform: translateY(-10px);}
    .feature-icon {font-size: 3.5rem; margin-bottom: 1.5rem; filter: drop-shadow(0 0 20px rgba(139, 92, 246, 0.5));}
    .feature-card h3 {font-size: 1.6rem; margin-bottom: 1rem; font-weight: 400;}
    .feature-card p {color: #a0a0a0; line-height: 1.7; font-size: 1.05rem;}
    
    .info-grid {display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem; margin-top: 4rem;}
    .info-card {background: rgba(20, 20, 20, 0.6); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 25px; padding: 3rem; transition: all 0.3s; backdrop-filter: blur(20px);}
    .info-card:hover {border-color: rgba(139, 92, 246, 0.5); transform: translateY(-5px); box-shadow: 0 20px 60px rgba(139, 92, 246, 0.2);}
    .info-number {font-size: 4rem; font-weight: 900; background: linear-gradient(135deg, #8b5cf6, #6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 1rem; opacity: 0.3;}
    .info-card h3 {font-size: 1.8rem; margin-bottom: 1rem; font-weight: 400;}
    .info-card p {color: #a0a0a0; line-height: 1.8; font-size: 1.05rem;}
    
    .stats-container {display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; padding: 4rem; background: rgba(139, 92, 246, 0.05); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 30px; backdrop-filter: blur(20px);}
    .stat-card {text-align: center;}
    .stat-number {font-size: 3.5rem; font-weight: 900; background: linear-gradient(135deg, #8b5cf6, #6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem;}
    .stat-label {font-size: 1.1rem; color: #a0a0a0;}
    
    /* Form styling */
    .stTextInput > div > div > input {
        background: rgba(40, 40, 40, 0.8) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 15px !important;
        color: #fff !important;
        font-size: 1rem !important;
        padding: 1.2rem 1.5rem !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1) !important;
    }
    
    .stTextArea > div > div > textarea {
        background: rgba(40, 40, 40, 0.8) !important;
        border: 1px solid rgba(139, 92, 246, 0.3) !important;
        border-radius: 15px !important;
        color: #fff !important;
        font-size: 1rem !important;
    }
    
    .custom-footer {
        position: relative;
        z-index: 10;
        border-top: 1px solid rgba(139, 92, 246, 0.2);
        margin-top: 3rem;
        padding: 2rem 5rem;
        text-align: center;
        color: #666;
        background: rgba(20, 20, 20, 0.6);
        backdrop-filter: blur(20px);
    }
    
    @media (max-width: 1024px) {
        nav {padding: 1rem 2rem;}
        .hero {grid-template-columns: 1fr; text-align: center; padding: 2rem;}
        .section {padding: 0 2rem;}
        .features-grid {grid-template-columns: 1fr;}
        .info-grid {grid-template-columns: 1fr;}
        .stats-container {grid-template-columns: repeat(2, 1fr);}
    }
</style>
"""

st.markdown(all_css, unsafe_allow_html=True)

# Background elements (always visible)
st.markdown("""
    <div class="bg-gradient"></div>
    <div class="glow-orb orb1"></div>
    <div class="glow-orb orb2"></div>
""", unsafe_allow_html=True)

# Session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

def set_page(page_name):
    st.session_state.current_page = page_name

# Navigation bar
st.markdown("""
    <nav>
        <div class="logo">
            <div class="logo-icon">⚡</div>
            <span>CrypticX</span>
        </div>
    </nav>
""", unsafe_allow_html=True)

# Navigation buttons
nav_cols = st.columns([1, 1, 1, 1, 1, 1, 1])
with nav_cols[0]:
    if st.button("Home", key="nav_home"):
        set_page("home")
with nav_cols[1]:
    if st.button("Dashboard", key="nav_dashboard"):
        set_page("dashboard")
with nav_cols[2]:
    if st.button("Features", key="nav_features"):
        set_page("features")
with nav_cols[3]:
    if st.button("Pricing", key="nav_pricing"):
        set_page("pricing")
with nav_cols[4]:
    if st.button("Contact", key="nav_contact"):
        set_page("contact")
with nav_cols[5]:
    if st.button("Sign Up", key="nav_signup"):
        set_page("signup")
with nav_cols[6]:
    if st.button("Login", key="nav_login", type="primary"):
        set_page("login")

# PAGE FUNCTIONS
def show_home_page():
    st.markdown("""
    <section class="hero">
        <div class="hero-content">
            <h1>Welcome to CrypticX</h1>
            <p>The ultimate tool for school. Master complex concepts, ace your exams, and unlock your full academic potential with cutting-edge AI technology.</p>
        </div>
        <div style="text-align: center; font-size: 10rem;">🤖</div>
    </section>
    """, unsafe_allow_html=True)
    
    # Native Streamlit form
    col1, col2 = st.columns([3, 1])
    with col1:
        email = st.text_input("Enter email", placeholder="Enter your email", label_visibility="collapsed")
    with col2:
        if st.button("Get Started", key="home_cta", type="primary"):
            if email:
                st.success(f"Welcome! Redirecting to dashboard...")
                set_page("dashboard")
                st.rerun()
    
    st.markdown('<p class="hero-note">Start your learning journey today</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <section class="section">
        <div class="section-header">
            <h2 class="section-title">Why Choose CrypticX?</h2>
            <p class="section-subtitle">The ultimate AI study companion for modern students</p>
        </div>
        <div class="info-grid">
            <div class="info-card">
                <div class="info-number">01</div>
                <h3>Powered by Advanced AI</h3>
                <p>Leveraging state-of-the-art artificial intelligence technology to provide accurate, instant, and personalized learning assistance.</p>
            </div>
            <div class="info-card">
                <div class="info-number">02</div>
                <h3>Save Time & Study Smarter</h3>
                <p>Cut your study time in half with intelligent summaries, instant explanations, and automated quiz generation.</p>
            </div>
            <div class="info-card">
                <div class="info-number">03</div>
                <h3>Proven Results</h3>
                <p>Join thousands of students who have improved their grades. Our users report 40% better retention and 35% improvement in test scores.</p>
            </div>
            <div class="info-card">
                <div class="info-number">04</div>
                <h3>24/7 Availability</h3>
                <p>Study anytime, anywhere. CrypticX is always available to help you understand difficult concepts.</p>
            </div>
        </div>
    </section>
    
    <section class="section">
        <div class="stats-container">
            <div class="stat-card">
                <div class="stat-number">50K+</div>
                <div class="stat-label">Active Students</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">1M+</div>
                <div class="stat-label">Questions Answered</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">95%</div>
                <div class="stat-label">Satisfaction Rate</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">24/7</div>
                <div class="stat-label">Available Support</div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

def show_dashboard_page():
    st.markdown("""
    <section class="section">
        <div class="section-header">
            <h2 class="section-title">Your Study Dashboard</h2>
            <p class="section-subtitle">Access all your AI-powered study tools in one place</p>
        </div>
    </section>
    """, unsafe_allow_html=True)
    
    # Feature cards with actual functionality
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <h3>AI Explainer</h3>
            <p>Get instant explanations for any concept or topic. Simply ask and learn.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Launch Tool", key="tool_explainer"):
            st.info("AI Explainer - Coming Soon!")
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📄</div>
            <h3>PDF Summarizer</h3>
            <p>Upload documents and get concise summaries in seconds.</p>
        </div>
        """, unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload PDF", type=["pdf"], key="pdf_upload", label_visibility="collapsed")
        if uploaded_file:
            st.success(f"Processing {uploaded_file.name}...")
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">❓</div>
            <h3>Quiz Generator</h3>
            <p>Create custom quizzes from any material to test your knowledge.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Create Quiz", key="tool_quiz"):
            st.info("Quiz Generator - Coming Soon!")
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎴</div>
            <h3>Flashcard Maker</h3>
            <p>Generate smart flashcards automatically from your study materials.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Make Cards", key="tool_flashcard"):
            st.info("Flashcard Maker - Coming Soon!")
    
    with col5:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">✍️</div>
            <h3>Essay Helper</h3>
            <p>Get help structuring, outlining, and improving your essays.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start Writing", key="tool_essay"):
            st.info("Essay Helper - Coming Soon!")
    
    with col6:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📅</div>
            <h3>Study Planner</h3>
            <p>Create personalized study schedules and track your progress.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Plan Studies", key="tool_planner"):
            st.info("Study Planner - Coming Soon!")
    
    st.markdown("""
    <div class="stats-container" style="margin-top: 4rem;">
        <div class="stat-card">
            <div class="stat-number">127</div>
            <div class="stat-label">Questions Asked</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">23</div>
            <div class="stat-label">PDFs Summarized</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">45</div>
            <div class="stat-label">Quizzes Completed</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">89%</div>
            <div class="stat-label">Average Score</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_features_page():
    st.markdown("""
    <section class="section">
        <div class="section-header">
            <h2 class="section-title">Powerful Features</h2>
            <p class="section-subtitle">Everything you need to excel in your studies</p>
        </div>
        
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">🧠</div>
                <h3>AI Explainer</h3>
                <p>Break down the most complex topics into simple, digestible explanations tailored to your learning style.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📄</div>
                <h3>Smart Summarizer</h3>
                <p>Upload PDFs or paste notes and get concise, accurate summaries in seconds. Save hours of study time.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">❓</div>
                <h3>Quiz Generator</h3>
                <p>Create custom quizzes and flashcards to test your knowledge and track your progress over time.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Progress Tracking</h3>
                <p>Monitor your learning journey with detailed analytics and insights into your study patterns.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3>Personalized Learning</h3>
                <p>AI adapts to your learning pace and style, providing customized content recommendations.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3>Lightning Fast</h3>
                <p>Get instant responses powered by cutting-edge AI technology for seamless learning experience.</p>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

def show_pricing_page():
    st.markdown("""
    <section class="section">
        <div class="section-header">
            <h2 class="section-title">Simple Pricing</h2>
            <p class="section-subtitle">Choose the plan that fits your needs</p>
        </div>
        
        <div class="features-grid">
            <div class="feature-card">
                <h3>Free</h3>
                <div style="font-size: 3rem; margin: 1rem 0;">$0<span style="font-size: 1rem; color: #a0a0a0;">/month</span></div>
                <p style="margin-bottom: 1.5rem;">• 10 AI explanations/day<br>• Basic summarization<br>• 5 quizzes/week<br>• Community support</p>
            </div>
            
            <div class="feature-card" style="border-color: #8b5cf6; background: rgba(139, 92, 246, 0.05);">
                <div style="color: #8b5cf6; font-weight: 600; margin-bottom: 1rem;">⭐ MOST POPULAR</div>
                <h3>Pro</h3>
                <div style="font-size: 3rem; margin: 1rem 0;">$9<span style="font-size: 1rem; color: #a0a0a0;">/month</span></div>
                <p style="margin-bottom: 1.5rem;">• Unlimited AI explanations<br>• Advanced summarization<br>• Unlimited quizzes<br>• PDF upload (50MB)<br>• Priority support<br>• Progress tracking</p>
            </div>
            
            <div class="feature-card">
                <h3>Ultimate</h3>
                <div style="font-size: 3rem; margin: 1rem 0;">$19<span style="font-size: 1rem; color: #a0a0a0;">/month</span></div>
                <p style="margin-bottom: 1.5rem;">• Everything in Pro<br>• Study group collaboration<br>• Custom AI training<br>• 1-on-1 tutoring<br>• Exam prep tools<br>• 24/7 VIP support</p>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Get Started", key="price_free", use_container_width=True):
            set_page("signup")
            st.rerun()
    with col2:
        if st.button("Start Free Trial", key="price_pro", type="primary", use_container_width=True):
            set_page("signup")
            st.rerun()
    with col3:
        if st.button("Contact Sales", key="price_ultimate", use_container_width=True):
            set_page("contact")
            st.rerun()

def show_contact_page():
    st.markdown("""
    <section class="section">
        <div style="max-width: 900px; margin: 0 auto; background: rgba(20, 20, 20, 0.6); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 30px; padding: 4rem; backdrop-filter: blur(20px);">
            <div class="section-header">
                <h2 class="section-title">Get In Touch</h2>
                <p class="section-subtitle">We'd love to hear from you</p>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)
    
    email = st.text_input("Email", placeholder="your@email.com")
    subject = st.text_input("Subject", placeholder="How can we help?")
    message = st.text_area("Message", placeholder="Tell us more...", height=150)
    
    if st.button("Send Message", key="contact_submit", type="primary", use_container_width=True):
        if email and subject and message:
            st.success("Thank you! We will get back to you soon.")
        else:
            st.error("Please fill in all fields")

def show_login_page():
    st.markdown("""
    <section class="section">
        <div style="max-width: 500px; margin: 0 auto; background: rgba(20, 20, 20, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 25px; padding: 3rem; backdrop-filter: blur(20px);">
            <div class="section-header">
                <h2 class="section-title">Welcome Back</h2>
                <p class="section-subtitle">Login to your CrypticX account</p>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)
    
    email = st.text_input("Email", placeholder="your@email.com", key="login_email")
    password = st.text_input("Password", placeholder="••••••••", type="password", key="login_password")
    
    if st.button("Login", key="login_submit", type="primary", use_container_width=True):
        if email and password:
            st.success("Login successful! Redirecting...")
            set_page("dashboard")
            st.rerun()
        else:
            st.error("Please enter email and password")
    
    st.markdown("""
        <div style="text-align: center; margin-top: 1.5rem; color: #a0a0a0;">
            Already have an account? <a href="#" style="color: #8b5cf6; text-decoration: none; font-weight: 600;">Login</a>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Go to Login", key="signup_to_login", use_container_width=True):
        set_page("login")
        st.rerun()

# PAGE ROUTER
page_name = st.session_state.current_page

if page_name == "home":
    show_home_page()
elif page_name == "dashboard":
    show_dashboard_page()
elif page_name == "features":
    show_features_page()
elif page_name == "pricing":
    show_pricing_page()
elif page_name == "contact":
    show_contact_page()
elif page_name == "login":
    show_login_page()
elif page_name == "signup":
    show_signup_page()
else:
    show_home_page()

# Footer
st.markdown("""
    <footer class="custom-footer">
        <p>© 2025 CrypticX. Empowering students with AI. All rights reserved.</p>
    </footer>
""", unsafe_allow_html=True)0a0a0;">
            Don't have an account? <a href="#" style="color: #8b5cf6; text-decoration: none; font-weight: 600;">Sign up</a>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Go to Sign Up", key="login_to_signup", use_container_width=True):
        set_page("signup")
        st.rerun()

def show_signup_page():
    st.markdown("""
    <section class="section">
        <div style="max-width: 500px; margin: 0 auto; background: rgba(20, 20, 20, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 25px; padding: 3rem; backdrop-filter: blur(20px);">
            <div class="section-header">
                <h2 class="section-title">Create Account</h2>
                <p class="section-subtitle">Join CrypticX today</p>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)
    
    name = st.text_input("Full Name", placeholder="John Doe", key="signup_name")
    email = st.text_input("Email", placeholder="your@email.com", key="signup_email")
    password = st.text_input("Password", placeholder="••••••••", type="password", key="signup_password")
    confirm = st.text_input("Confirm Password", placeholder="••••••••", type="password", key="signup_confirm")
    
    if st.button("Create Account", key="signup_submit", type="primary", use_container_width=True):
        if name and email and password and confirm:
            if password == confirm:
                st.success("Account created! Redirecting...")
                set_page("dashboard")
                st.rerun()
            else:
                st.error("Passwords don't match")
        else:
            st.error("Please fill in all fields")
    
    st.markdown("""
        <div style="text-align: center; margin-top: 1.5rem; color: #a
