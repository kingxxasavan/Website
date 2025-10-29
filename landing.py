import streamlit as st

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
    
    .beta-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(139, 92, 246, 0.15);
        border: 1px solid rgba(139, 92, 246, 0.3);
        padding: 0.5rem 1.2rem;
        border-radius: 50px;
        font-size: 0.85rem;
        color: #8b5cf6;
        font-weight: 600;
        margin-bottom: 2rem;
    }
    
    .beta-badge::before {
        content: "NEW";
        background: #8b5cf6;
        color: white;
        padding: 0.15rem 0.5rem;
        border-radius: 20px;
        font-size: 0.7rem;
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
    }
    
    .hero-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 40px rgba(139, 92, 246, 0.6);
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
    
    /* Pricing cards */
    .pricing-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 2rem;
        margin-top: 3rem;
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
    }
    
    .pricing-card.featured .pricing-button {
        background: linear-gradient(135deg, #8b5cf6, #ec4899);
        border: none;
    }
    
    /* Contact form */
    .contact-container {
        max-width: 600px;
        margin: 0 auto;
        background: rgba(139, 92, 246, 0.05);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 24px;
        padding: 3rem;
        backdrop-filter: blur(10px);
    }
    
    /* Hide Streamlit buttons in nav */
    .stButton {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .stButton > button {
        all: unset;
        display: inline-block;
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
        .features-grid, .pricing-grid {grid-template-columns: 1fr;}
        .pricing-card.featured {transform: scale(1);}
    }
</style>
""", unsafe_allow_html=True)

# Background elements
st.markdown("""
    <div class="grid-background"></div>
    <div class="glow-orb purple"></div>
    <div class="glow-orb pink"></div>
""", unsafe_allow_html=True)

# Navigation with anchor links
st.markdown("""
    <div class="nav-container">
        <nav>
            <div class="logo">
                <span class="logo-icon">⚡</span>
                <span>CrypticX</span>
            </div>
            <div class="nav-links">
                <a href="#home" class="nav-link">Home</a>
                <a href="#features" class="nav-link">Features</a>
                <a href="#pricing" class="nav-link">Pricing</a>
                <a href="#contact" class="nav-link">Contact</a>
                <button class="nav-cta" onclick="document.getElementById('contact').scrollIntoView({behavior: 'smooth'})">Get Started</button>
            </div>
        </nav>
    </div>
""", unsafe_allow_html=True)

# Content wrapper
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div id="home" class="hero-section">
        <div class="beta-badge">AI Study Tool v4.5 Beta is available</div>
        <h1 class="hero-title">Revolutionizing the Future of Learning</h1>
        <p class="hero-subtitle">Discover what drives results and what doesn't to boost your academic success with AI-powered study tools.</p>
        <button class="hero-cta" onclick="document.getElementById('contact').scrollIntoView({behavior: 'smooth'})">Take Free Trial</button>
    </div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("""
    <div id="features" class="section">
        <h2 class="section-title">Powerful Study Features</h2>
        <p class="section-subtitle">Everything you need to ace your classes</p>
        
        <div class="features-grid">
            <div class="feature-card">
                <span class="feature-icon">🤖</span>
                <h3>AI Tutor</h3>
                <p>24/7 access to an intelligent tutor that explains concepts in your learning style with personalized guidance.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">📄</span>
                <h3>Document Analysis</h3>
                <p>Upload PDFs, Word docs, or slides and get instant summaries and key points extracted automatically.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">🎴</span>
                <h3>Flashcard Generator</h3>
                <p>Automatically create flashcards from your study materials for efficient memorization and retention.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">📊</span>
                <h3>Progress Tracking</h3>
                <p>Monitor your learning with detailed analytics and personalized recommendations based on your performance.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">✍️</span>
                <h3>Essay Helper</h3>
                <p>Get help outlining, structuring, and improving your essays with intelligent AI feedback and suggestions.</p>
            </div>
            <div class="feature-card">
                <span class="feature-icon">🔒</span>
                <h3>Privacy First</h3>
                <p>Your data is encrypted and never shared. Study with complete peace of mind and security.</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Pricing Section
st.markdown("""
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
                <button class="pricing-button">Start Free</button>
            </div>
            
            <div class="pricing-card featured">
                <div class="pricing-badge">⭐ MOST POPULAR</div>
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
                <button class="pricing-button">Try Pro Free</button>
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
                <button class="pricing-button">Contact Sales</button>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
    <div id="contact" class="section">
        <div class="contact-container">
            <h2 style='text-align: center; margin-bottom: 2rem; font-size: 2.5rem;'>Get In Touch</h2>
""", unsafe_allow_html=True)

name = st.text_input("Name", placeholder="Your name", label_visibility="collapsed", key="contact_name")
email = st.text_input("Email", placeholder="your@email.com", label_visibility="collapsed", key="contact_email")
message = st.text_area("Message", placeholder="How can we help?", height=150, label_visibility="collapsed", key="contact_msg")

if st.button("Send Message", key="contact_btn", type="primary", use_container_width=True):
    if name and email and message:
        st.success("✓ Thanks! We'll get back to you within 24 hours.")
    else:
        st.error("Please fill in all fields")

st.markdown('</div></div>', unsafe_allow_html=True)

# Close content wrapper
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <footer class="custom-footer">
        <p>© 2025 CrypticX • Empowering students with AI • Built with ❤️</p>
    </footer>
""", unsafe_allow_html=True)
