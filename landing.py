import streamlit as st
from streamlit.switch_page_button import switch_page  # Note: Use st.switch_page in Streamlit 1.28+

st.set_page_config(
    page_title="CrypticX - AI Study Tool",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS matching the reference image
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
    
    /* Hero section */
    .hero-section {
        min-height: calc(100vh - 80px);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 4rem 2rem;
        position: relative;
    }
    
    .welcome-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 0.6rem 1.5rem;
        border-radius: 50px;
        font-size: 0.9rem;
        color: #fff;
        font-weight: 500;
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
    }
    
    .hero-title {
        font-size: 5rem;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #ffffff 0%, #8b5cf6 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        max-width: 1000px;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: rgba(255, 255, 255, 0.6);
        margin-bottom: 3rem;
        max-width: 700px;
        line-height: 1.7;
    }
    
    /* Style for Streamlit buttons to match hero-cta */
    .stButton > button {
        padding: 1rem 2.5rem !important;
        border-radius: 50px !important;
        background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%) !important;
        color: #fff !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: all 0.3s !important;
        border: none !important;
        font-size: 1.1rem !important;
        box-shadow: 0 8px 30px rgba(139, 92, 246, 0.4) !important;
        margin: 0 auto !important;
        display: block !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 40px rgba(139, 92, 246, 0.6) !important;
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
    
    /* About content */
    .about-content {
        max-width: 800px;
        margin: 0 auto;
        text-align: center;
    }
    
    .about-text {
        color: rgba(255, 255, 255, 0.7);
        font-size: 1.1rem;
        line-height: 1.9;
        margin-bottom: 2rem;
    }
    
    /* Feature cards */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .feature-card {
        background: rgba(139, 92, 246, 0.05);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 24px;
        padding: 2.5rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
    }
    
    .feature-card:hover {
        transform: translateY(-10px);
        background: rgba(139, 92, 246, 0.1);
        border-color: rgba(139, 92, 246, 0.5);
        box-shadow: 0 20px 60px rgba(139, 92, 246, 0.2);
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
        font-weight: 600;
    }
    
    .feature-card p {
        color: rgba(255, 255, 255, 0.6);
        line-height: 1.7;
        font-size: 0.95rem;
    }
    
    /* CTA Section */
    .cta-section {
        text-align: center;
        padding: 4rem 2rem;
        background: rgba(139, 92, 246, 0.05);
        border-radius: 24px;
        margin: 4rem 2rem;
        backdrop-filter: blur(10px);
    }
    
    .cta-title {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        color: #fff;
    }
    
    .cta-subtitle {
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.6);
        margin-bottom: 2rem;
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
        .hero-title {font-size: 2.5rem;}
        .hero-subtitle {font-size: 1.1rem;}
        .features-grid {grid-template-columns: 1fr;}
    }
</style>
""", unsafe_allow_html=True)

# Background elements
st.markdown("""
    <div class="grid-background"></div>
    <div class="glow-orb purple"></div>
    <div class="glow-orb pink"></div>
""", unsafe_allow_html=True)

# Navigation (updated links for multi-page)
st.markdown("""
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

# Hero Section
st.markdown("""
    <div class="hero-section">
        <div class="welcome-badge">Welcome to CrypticX - The Ultimate Study Tool</div>
        <h1 class="hero-title">Master Your Studies with AI-Powered Learning</h1>
        <p class="hero-subtitle">Transform the way you learn with intelligent tools designed to help you understand faster, remember longer, and achieve academic excellence.</p>
""", unsafe_allow_html=True)

# Functional Hero Button - Routes to Login (handles sign-up too)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Start Learning Free"):
        switch_page("pages/login.py")

st.markdown("</div>", unsafe_allow_html=True)

# About Us Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">About Us</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Empowering students to reach their full potential</p>', unsafe_allow_html=True)
st.markdown('<div class="about-content">', unsafe_allow_html=True)
st.markdown("""
    <p class="about-text">
        CrypticX was founded by students, for students. We understand the challenges of modern education and created an AI-powered platform that makes studying more efficient, engaging, and effective. Our mission is to democratize access to personalized learning tools that help every student succeed.
    </p>
    <p class="about-text">
        With cutting-edge artificial intelligence and a deep understanding of learning science, we've built tools that adapt to your unique learning style, making complex concepts easier to understand and helping you achieve your academic goals faster than ever before.
    </p>
""", unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# Why Choose Us Section
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Why Choose CrypticX</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">The smartest way to study in 2025</p>', unsafe_allow_html=True)
st.markdown('<div class="features-grid">', unsafe_allow_html=True)

st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">⚡</span>
        <h3>Lightning Fast</h3>
        <p>Get instant answers to your questions. No more waiting hours for tutors or searching through endless resources.</p>
    </div>
    <div class="feature-card">
        <span class="feature-icon">🎯</span>
        <h3>Personalized Learning</h3>
        <p>AI adapts to your learning style and pace, providing customized explanations that make sense to you.</p>
    </div>
    <div class="feature-card">
        <span class="feature-icon">💰</span>
        <h3>Affordable Excellence</h3>
        <p>Get premium tutoring quality at a fraction of the cost. Start free and upgrade only when you're ready.</p>
    </div>
    <div class="feature-card">
        <span class="feature-icon">📱</span>
        <h3>Study Anywhere</h3>
        <p>Access your learning tools from any device, anytime. Study on your schedule, not someone else's.</p>
    </div>
    <div class="feature-card">
        <span class="feature-icon">🔬</span>
        <h3>Proven Methods</h3>
        <p>Built on learning science and cognitive psychology principles that are proven to improve retention and understanding.</p>
    </div>
    <div class="feature-card">
        <span class="feature-icon">🌟</span>
        <h3>Student Success</h3>
        <p>Join thousands of students who've improved their grades and confidence with CrypticX's intelligent tools.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# Final CTA Section
st.markdown("""
    <div class="cta-section">
        <h2 class="cta-title">Ready to Unlock Your Potential?</h2>
        <p class="cta-subtitle">Join thousands of students transforming their learning today.</p>
""", unsafe_allow_html=True)

# Functional CTA Button - Routes to Pricing (for plan selection before login)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Get Started Free"):
        switch_page("pages/pricing.py")

st.markdown("</div>", unsafe_allow_html=True)

# Close content wrapper
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <footer class="custom-footer">
        <p>© 2025 CrypticX • Empowering students with AI • Built with ❤️</p>
    </footer>
""", unsafe_allow_html=True)
