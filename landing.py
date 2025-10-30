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

# Global navigation handling via query params
query_params = st.query_params
if 'action' in query_params:
    action = query_params['action'][0] if isinstance(query_params['action'], list) else query_params['action']
    handled = False
    if action == 'home':
        st.session_state.current_page = 'home'
        handled = True
    elif action == 'dashboard':
        st.session_state.current_page = 'dashboard'
        handled = True
    if handled:
        del st.query_params['action']

# Enhanced CSS
st.markdown("""
<style>
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    .stDecoration {display: none !important;}
    
    /* Force hide sidebar completely */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    .stSidebar {
        display: none !important;
    }
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    
    /* Reset padding */
    .block-container {padding: 0 !important; margin: 0 !important;}
    .main .block-container {max-width: 100% !important; padding: 0 !important;}
    .stApp {margin: 0 !important; padding: 0 !important;}
    section.main > div {padding: 0 !important;}
    div[data-testid="stAppViewContainer"] {padding: 0 !important; margin: 0 !important;}
    
    /* Hide all Streamlit buttons completely */
    .stButton {
        display: none !important;
        visibility: hidden !important;
        position: absolute !important;
        width: 0 !important;
        height: 0 !important;
        opacity: 0 !important;
    }
    
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
    
    /* Navigation */
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
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { filter: drop-shadow(0 0 10px rgba(139, 92, 246, 0.8)); }
        50% { filter: drop-shadow(0 0 20px rgba(139, 92, 246, 1)); }
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
        position: relative;
    }
    
    .nav-link:hover {
        color: #fff;
        border-bottom-color: #8b5cf6;
    }
    
    .nav-link.active {
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
    
    /* Main content */
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
        animation: fadeInUp 0.6s ease-out;
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
        animation: fadeInUp 0.8s ease-out 0.2s backwards;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: rgba(255, 255, 255, 0.6);
        margin-bottom: 3rem;
        max-width: 700px;
        line-height: 1.7;
        animation: fadeInUp 1s ease-out 0.4s backwards;
    }
    
    .hero-cta {
        padding: 1rem 2.5rem;
        border-radius: 50px;
        background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);
        color: #fff;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
        border: none;
        font-size: 1.1rem;
        box-shadow: 0 8px 30px rgba(139, 92, 246, 0.4);
        animation: fadeInUp 1.2s ease-out 0.6s backwards;
    }
    
    .hero-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 40px rgba(139, 92, 246, 0.6);
    }
    
    /* Stats section */
    .stats-section {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 2rem;
        max-width: 900px;
        margin: 4rem auto 0;
        padding: 0 2rem;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #8b5cf6, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.95rem;
    }
    
    /* Section styling */
    .section {
        position: relative;
        z-index: 10;
        max-width: 1200px;
        margin: 0 auto;
        padding: 6rem 2rem;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
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
    
    /* Feature cards */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 2rem;
        margin-top: 3rem;
        width: 100%;
    }
    
    .feature-card {
        background: rgba(139, 92, 246, 0.05);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 24px;
        padding: 2.5rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
        cursor: pointer;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
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
        transition: transform 0.3s;
    }
    
    .feature-card:hover .feature-icon {
        transform: scale(1.1);
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
        flex-grow: 1;
    }
    
    /* Pricing cards */
    .pricing-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 2rem;
        margin-top: 3rem;
        width: 100%;
    }
    
    .pricing-card {
        background: rgba(139, 92, 246, 0.05);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 24px;
        padding: 3rem 2.5rem;
        text-align: center;
        transition: all 0.4s;
        position: relative;
    }
    
    .pricing-card.featured {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(236, 72, 153, 0.15));
        border: 2px solid #8b5cf6;
        transform: scale(1.05);
    }
    
    .pricing-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 60px rgba(139, 92, 246, 0.3);
    }
    
    .pricing-card.featured:hover {
        transform: translateY(-10px) scale(1.07);
    }
    
    .pricing-badge {
        position: absolute;
        top: -15px;
        left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(135deg, #8b5cf6, #ec4899);
        color: white;
        padding: 0.4rem 1.2rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    
    .pricing-card h3 {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        color: #fff;
    }
    
    .price {
        font-size: 3.5rem;
        font-weight: 800;
        margin: 1.5rem 0;
        background: linear-gradient(135deg, #8b5cf6, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .price-period {
        font-size: 1rem;
        color: rgba(255, 255, 255, 0.5);
    }
    
    .feature-list {
        text-align: left;
        margin: 2rem 0;
        color: rgba(255, 255, 255, 0.7);
        line-height: 2.2;
        font-size: 0.95rem;
    }
    
    .pricing-button {
        width: 100%;
        padding: 0.9rem;
        border-radius: 12px;
        background: rgba(139, 92, 246, 0.2);
        border: 1px solid rgba(139, 92, 246, 0.3);
        color: #fff;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
        margin-top: 1rem;
    }
    
    .pricing-button:hover {
        background: rgba(139, 92, 246, 0.3);
        border-color: #8b5cf6;
        transform: translateY(-2px);
    }
    
    .pricing-card.featured .pricing-button {
        background: linear-gradient(135deg, #8b5cf6, #ec4899);
        border: none;
    }
    
    /* Dashboard styles */
    .dashboard-section {
        min-height: calc(100vh - 80px);
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        text-align: center;
        padding: 4rem 2rem;
        position: relative;
    }
    
    .dashboard-welcome {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #fff;
    }
    
    .dashboard-subtitle {
        font-size: 1.25rem;
        color: rgba(255, 255, 255, 0.6);
        margin-bottom: 3rem;
        max-width: 700px;
        line-height: 1.7;
    }
    
    .dashboard-stats {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 2rem;
        max-width: 600px;
        margin: 2rem 0;
    }
    
    .dashboard-stat {
        background: rgba(139, 92, 246, 0.05);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
    }
    
    .dashboard-stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #8b5cf6;
    }
    
    .dashboard-stat-label {
        color: rgba(255, 255, 255, 0.6);
        font-size: 1rem;
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
    
    .footer-links {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 1rem;
    }
    
    .footer-link {
        color: rgba(255, 255, 255, 0.5);
        text-decoration: none;
        font-size: 0.9rem;
        transition: color 0.3s;
    }
    
    .footer-link:hover {
        color: #8b5cf6;
    }
    
    /* Responsive */
    @media (max-width: 1024px) {
        .features-grid, .pricing-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        .dashboard-stats {
            grid-template-columns: 1fr;
        }
    }
    
    @media (max-width: 768px) {
        nav {padding: 1rem 1.5rem;}
        .nav-links {display: none;}
        .hero-title {font-size: 2.5rem;}
        .hero-subtitle {font-size: 1.1rem;}
        .features-grid, .pricing-grid, .stats-section {
            grid-template-columns: 1fr;
        }
        .section-title {font-size: 2rem;}
        .pricing-card.featured {transform: scale(1);}
        .dashboard-welcome {font-size: 2rem;}
    }
</style>
""", unsafe_allow_html=True)

# Background elements
st.markdown("""
<div class="grid-background"></div>
<div class="glow-orb purple"></div>
<div class="glow-orb pink"></div>
""", unsafe_allow_html=True)

# Navigation
nav_links = """
<div class="nav-links">
<span class="nav-link active" onclick="window.location.href='#home'">Home</span>
<span class="nav-link" onclick="window.location.href='#pricing'">Pricing</span>
<span class="nav-link" onclick="window.location.href='?action=dashboard'">Dashboard</span>
</div>
"""

nav_full = """
<div class="nav-container">
<nav>
<div class="logo" onclick="window.location.href='#home'">
<span class="logo-icon">⚡</span>
<span>CrypticX</span>
</div>
{} 
</nav>
</div>
""".strip().format(nav_links.strip())
st.markdown(nav_full, unsafe_allow_html=True)

st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

if st.session_state.current_page == 'dashboard':
    # DASHBOARD PAGE
    st.markdown("""
    <div class="dashboard-section">
        <h1 class="dashboard-welcome">Welcome to Your Dashboard!</h1>
        <p class="dashboard-subtitle">Here's a quick overview of your learning progress.</p>
        <div class="dashboard-stats">
            <div class="dashboard-stat">
                <div class="dashboard-stat-number">42</div>
                <div class="dashboard-stat-label">Questions Answered This Week</div>
            </div>
            <div class="dashboard-stat">
                <div class="dashboard-stat-number">87%</div>
                <div class="dashboard-stat-label">Quiz Average</div>
            </div>
            <div class="dashboard-stat">
                <div class="dashboard-stat-number">5</div>
                <div class="dashboard-stat-label">Active Courses</div>
            </div>
            <div class="dashboard-stat">
                <div class="dashboard-stat-number">2h 30m</div>
                <div class="dashboard-stat-label">Study Time Today</div>
            </div>
        </div>
        <button class="hero-cta" onclick="window.location.href='#home'">Explore More</button>
    </div>
    """, unsafe_allow_html=True)
else:
    # HERO / HOME PAGE
    # Hero Section
    st.markdown("""
    <div id="home" class="hero-section">
    <div class="welcome-badge">✨ Welcome to CrypticX - The Ultimate Study Tool</div>
    <h1 class="hero-title">Master Your Studies with AI-Powered Learning</h1>
    <p class="hero-subtitle">Transform the way you learn with intelligent tools designed to help you understand faster, remember longer, and achieve academic excellence.</p>
    <button class="hero-cta" onclick="window.location.href='#home'">Start Learning Free</button>
    <div class="stats-section">
        <div class="stat-item">
            <div class="stat-number">50K+</div>
            <div class="stat-label">Active Students</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">95%</div>
            <div class="stat-label">Satisfaction Rate</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">1M+</div>
            <div class="stat-label">Questions Answered</div>
        </div>
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

    # Pricing Section
    st.markdown('<div id="pricing" class="section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Choose Your Plan</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Start free, upgrade when you are ready</p>', unsafe_allow_html=True)

    st.markdown("""
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
            <button class="pricing-button" onclick="window.location.href='#home'">Start Free</button>
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
            <button class="pricing-button" onclick="window.location.href='#home'">Get Pro</button>
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
            <button class="pricing-button" onclick="window.location.href='#home'">Get Enterprise</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

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
