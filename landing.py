import streamlit as st

st.set_page_config(
    page_title="StudyHub - Academic Services",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# CSS - Original design with Discord integration
st.markdown("""
<style>
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    .stDecoration {display: none !important;}
    section[data-testid="stSidebar"] {display: none !important;}
    .stSidebar {display: none !important;}
    [data-testid="collapsedControl"] {display: none !important;}
    .block-container {padding: 0 !important; margin: 0 !important;}
    .main .block-container {max-width: 100% !important; padding: 0 !important;}
    .stApp {margin: 0 !important; padding: 0 !important;}
    section.main > div {padding: 0 !important;}
    div[data-testid="stAppViewContainer"] {padding: 0 !important; margin: 0 !important;}
    
    /* Base styles */
    * {margin: 0; padding: 0; box-sizing: border-box;}
    html, body {margin: 0 !important; padding: 0 !important; overflow-x: hidden; scroll-behavior: smooth;}
    .stApp {background: #0a0a0f; color: #fff; font-family: 'Inter', 'Segoe UI', sans-serif;}
    
    /* Grid background */
    .grid-background {position: fixed; inset: 0; background-image: linear-gradient(rgba(139, 92, 246, 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(139, 92, 246, 0.03) 1px, transparent 1px); background-size: 50px 50px; z-index: 0;}
    
    /* Animated glow effects */
    .glow-orb {position: fixed; width: 800px; height: 800px; border-radius: 50%; filter: blur(120px); opacity: 0.3; z-index: 1; pointer-events: none;}
    .glow-orb.purple {background: radial-gradient(circle, rgba(139, 92, 246, 0.6), transparent); top: -200px; left: 50%; transform: translateX(-50%); animation: float 20s ease-in-out infinite;}
    .glow-orb.pink {background: radial-gradient(circle, rgba(236, 72, 153, 0.4), transparent); bottom: -300px; right: -200px; animation: float 25s ease-in-out infinite reverse;}
    @keyframes float {0%, 100% { transform: translate(-50%, 0) scale(1); } 50% { transform: translate(-50%, -50px) scale(1.1); } }
    @keyframes fadeInUp {from {opacity: 0; transform: translateY(30px);} to {opacity: 1; transform: translateY(0);} }
    .fade-in-up {animation: fadeInUp 0.6s ease-out forwards;}
    
    /* Navigation */
    .nav-container {position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: transparent; backdrop-filter: blur(20px); border-bottom: 1px solid rgba(139, 92, 246, 0.1); transition: all 0.3s ease;}
    nav {position: relative; z-index: 100; display: flex; justify-content: space-between; align-items: center; padding: 1.5rem 4rem; max-width: 1400px; margin: 0 auto;}
    .logo {display: flex; align-items: center; gap: 0.75rem; font-size: 1.5rem; font-weight: 700; color: #8b5cf6; cursor: pointer; letter-spacing: 0.5px;}
    .logo-icon {font-size: 1.8rem; filter: drop-shadow(0 0 10px rgba(139, 92, 246, 0.8)); animation: pulse 2s ease-in-out infinite;}
    @keyframes pulse {0%, 100% { filter: drop-shadow(0 0 10px rgba(139, 92, 246, 0.8)); } 50% { filter: drop-shadow(0 0 20px rgba(139, 92, 246, 1)); } }
    .nav-links {display: flex; gap: 2.5rem; align-items: center;}
    .discord-cta {padding: 0.7rem 1.8rem !important; border-radius: 50px; background: #5865F2; color: #fff; font-weight: 600; cursor: pointer; transition: all 0.3s; border: none; font-size: 0.9rem; box-shadow: 0 4px 20px rgba(88, 101, 242, 0.4); text-decoration: none; display: inline-block;}
    .discord-cta:hover {transform: translateY(-2px); box-shadow: 0 6px 25px rgba(88, 101, 242, 0.6);}
    
    /* Main content */
    .content-wrapper {position: relative; z-index: 10; padding-top: 80px;}
    
    /* Hero section */
    .hero-section {min-height: calc(100vh - 80px); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 4rem 2rem; position: relative;}
    .welcome-badge {display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); padding: 0.6rem 1.5rem; border-radius: 50px; font-size: 0.9rem; color: #fff; font-weight: 500; margin-bottom: 2rem; backdrop-filter: blur(10px); animation: fadeInUp 0.6s ease-out;}
    .hero-title {font-size: 5rem; font-weight: 800; line-height: 1.1; margin-bottom: 1.5rem; background: linear-gradient(135deg, #ffffff 0%, #8b5cf6 50%, #ec4899 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; max-width: 1000px; animation: fadeInUp 0.8s ease-out 0.2s backwards;}
    .hero-subtitle {font-size: 1.25rem; color: rgba(255, 255, 255, 0.6); margin-bottom: 3rem; max-width: 700px; line-height: 1.7; animation: fadeInUp 1s ease-out 0.4s backwards;}
    .hero-cta {padding: 1rem 2.5rem; border-radius: 50px; background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%); color: #fff; font-weight: 600; cursor: pointer; transition: all 0.3s; border: none; font-size: 1.1rem; box-shadow: 0 8px 30px rgba(139, 92, 246, 0.4); animation: fadeInUp 1.2s ease-out 0.6s backwards; text-decoration: none; display: inline-block;}
    .hero-cta:hover {transform: translateY(-3px); box-shadow: 0 12px 40px rgba(139, 92, 246, 0.6);}
    
    /* Stats section */
    .stats-section {display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; max-width: 900px; margin: 4rem auto 0; padding: 0 2rem;}
    .stat-item {text-align: center;}
    .stat-number {font-size: 3rem; font-weight: 800; background: linear-gradient(135deg, #8b5cf6, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem;}
    .stat-label {color: rgba(255, 255, 255, 0.6); font-size: 0.95rem;}
    
    /* Section styling */
    .section {position: relative; z-index: 10; max-width: 1200px; margin: 0 auto; padding: 6rem 2rem; width: 100%; display: flex; flex-direction: column; align-items: center;}
    .section-title {font-size: 3rem; font-weight: 700; text-align: center; margin-bottom: 1rem; color: #fff;}
    .section-subtitle {font-size: 1.15rem; color: rgba(255, 255, 255, 0.5); text-align: center; margin-bottom: 4rem;}
    
    /* Feature cards */
    .features-grid {display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-top: 3rem; width: 100%;}
    .feature-card {background: rgba(139, 92, 246, 0.05); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 24px; padding: 2.5rem; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); backdrop-filter: blur(10px); cursor: pointer; height: 100%; display: flex; flex-direction: column; align-items: center; text-align: center;}
    .feature-card:hover {transform: translateY(-10px); background: rgba(139, 92, 246, 0.1); border-color: rgba(139, 92, 246, 0.5); box-shadow: 0 20px 60px rgba(139, 92, 246, 0.2);}
    .feature-icon {font-size: 3rem; margin-bottom: 1.5rem; display: block; transition: transform 0.3s;}
    .feature-card:hover .feature-icon {transform: scale(1.1);}
    .feature-card h3 {font-size: 1.5rem; margin-bottom: 1rem; color: #fff; font-weight: 600;}
    .feature-card p {color: rgba(255, 255, 255, 0.6); line-height: 1.7; font-size: 0.95rem; flex-grow: 1;}
    
    /* Topics section */
    .topics-grid {display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-top: 3rem; width: 100%;}
    .topic-card {background: rgba(139, 92, 246, 0.05); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 24px; padding: 2rem; transition: all 0.4s; text-align: left;}
    .topic-card:hover {transform: translateY(-8px); background: rgba(139, 92, 246, 0.1); border-color: rgba(139, 92, 246, 0.4); box-shadow: 0 15px 50px rgba(139, 92, 246, 0.2);}
    .topic-icon {font-size: 2.5rem; margin-bottom: 1rem; display: block;}
    .topic-card h3 {font-size: 1.4rem; margin-bottom: 0.75rem; color: #fff; font-weight: 600;}
    .topic-card p {color: rgba(255, 255, 255, 0.6); line-height: 1.6; font-size: 0.9rem; margin-bottom: 1rem;}
    .topic-list {color: rgba(255, 255, 255, 0.5); line-height: 2; font-size: 0.85rem;}
    
    /* Footer */
    .custom-footer {position: relative; z-index: 10; border-top: 1px solid rgba(139, 92, 246, 0.1); margin-top: 5rem; padding: 3rem 2rem; text-align: center; color: rgba(255, 255, 255, 0.4); background: rgba(10, 10, 15, 0.5);}
    .footer-links {display: flex; justify-content: center; gap: 2rem; margin-top: 1rem;}
    .footer-link {color: rgba(255, 255, 255, 0.5); text-decoration: none; font-size: 0.9rem; transition: color 0.3s;}
    .footer-link:hover {color: #8b5cf6;}
    
    /* Responsive */
    @media (max-width: 1024px) {
        .features-grid, .topics-grid {grid-template-columns: repeat(2, 1fr);}
    }
    @media (max-width: 768px) {
        nav {padding: 1rem 1.5rem;}
        .nav-links {display: none;}
        .hero-title {font-size: 2.5rem;}
        .hero-subtitle {font-size: 1.1rem;}
        .features-grid, .topics-grid, .stats-section {grid-template-columns: 1fr;}
        .section-title {font-size: 2rem;}
    }
</style>
""", unsafe_allow_html=True)

# Background elements
st.markdown('<div class="grid-background"></div><div class="glow-orb purple"></div><div class="glow-orb pink"></div>', unsafe_allow_html=True)

# Navigation
st.markdown('''
<div class="nav-container">
    <nav>
        <div class="logo">
            <span class="logo-icon">⚡</span>
            <span>StudyHub</span>
        </div>
        <div class="nav-links">
            <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" class="discord-cta">Join Discord →</a>
        </div>
    </nav>
</div>
''', unsafe_allow_html=True)

# Main Content
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Hero Section
st.markdown('''
<div id="home" class="hero-section">
    <div class="welcome-badge">✨ Get Expert Help with Your Academic Work</div>
    <h1 class="hero-title">Essays, Projects & Code<br/>Done Right</h1>
    <p class="hero-subtitle">Professional help with writing, coding projects, and tutoring. Fast delivery, quality guaranteed. Join our Discord to get started.</p>
    <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" class="hero-cta">Join Discord & Order Now</a>
</div>
''', unsafe_allow_html=True)

# Stats Section
st.markdown('''
<div class="stats-section">
    <div class="stat-item">
        <div class="stat-number">50+</div>
        <div class="stat-label">Happy Students</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">24-48hr</div>
        <div class="stat-label">Average Delivery</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">100%</div>
        <div class="stat-label">Original Work</div>
    </div>
</div>
</div>
''', unsafe_allow_html=True)

# Features Section
st.markdown('''
<div id="features" class="section">
    <h2 class="section-title">Why Choose Us</h2>
    <p class="section-subtitle">Fast, reliable, and quality-focused academic support</p>
    <div class="features-grid">
        <div class="feature-card">
            <span class="feature-icon">⚡</span>
            <h3>Fast Delivery</h3>
            <p>Get your work done quickly. Most orders delivered within 24-48 hours. Rush options available for urgent deadlines.</p>
        </div>
        <div class="feature-card">
            <span class="feature-icon">🎯</span>
            <h3>Quality Guaranteed</h3>
            <p>Every project is carefully reviewed for quality. One free revision included to ensure you're 100% satisfied.</p>
        </div>
        <div class="feature-card">
            <span class="feature-icon">💰</span>
            <h3>Affordable Pricing</h3>
            <p>Student-friendly rates starting at just $20. Pay securely via CashApp, Venmo, or Zelle.</p>
        </div>
        <div class="feature-card">
            <span class="feature-icon">💬</span>
            <h3>Direct Communication</h3>
            <p>Chat with us directly on Discord. Ask questions, share files, and get real-time updates on your order.</p>
        </div>
        <div class="feature-card">
            <span class="feature-icon">🔒</span>
            <h3>100% Original</h3>
            <p>All work is created from scratch. Plagiarism-free guarantee with proper citations and references.</p>
        </div>
        <div class="feature-card">
            <span class="feature-icon">🌟</span>
            <h3>Expert Help</h3>
            <p>Get help from experienced tutors and professionals who understand your subject matter inside and out.</p>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

# CTA Section
st.markdown('''
<div class="section" style="text-align: center;">
    <h2 class="section-title">Ready to Get Started?</h2>
    <p class="section-subtitle">Join our Discord community and place your first order today</p>
    <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" class="hero-cta">Join Discord Now</a>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('''
<div class="custom-footer">
    <p>&copy; 2025 StudyHub. Quality academic services. Fast delivery. Satisfaction guaranteed.</p>
    <p style="margin-top: 0.5rem; opacity: 0.6;">Payment via CashApp, Venmo, or Zelle • All work is 100% original</p>
</div>
''', unsafe_allow_html=True)
