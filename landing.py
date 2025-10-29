import streamlit as st

st.set_page_config(
    page_title="CrypticX - AI Study Tool",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS matching the reference image (No changes here)
st.markdown("""
<style>
    /* ... (Your existing 500+ lines of CSS) ... */
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden !import;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    
    /* ... (all your other styles) ... */
    
    /* Ensure Streamlit buttons in nav are unstyled */
    .stButton {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .stButton > button {
        all: unset;
        display: inline-block;
    }

    /* ... (rest of your CSS) ... */
</style>
""", unsafe_allow_html=True)

# Background elements
st.markdown("""
    <div class="grid-background"></div>
    <div class="glow-orb purple"></div>
    <div class="glow-orb pink"></div>
""", unsafe_allow_html=True)

# --- [UPDATED] Navigation with new links ---
# Links for Features, Pricing, and Contact now point to Streamlit pages
# "Get Started" button is now an <a> tag styled as a button
st.markdown("""
    <div class="nav-container">
        <nav>
            <div class="logo">
                <span class="logo-icon">⚡</span>
                <span>CrypticX</span>
            </div>
            <div class="nav-links">
                <a href="/" class="nav-link">Home</a>
                <a href="#about" class="nav-link">About</a>
                <a href="#why-choose" class="nav-link">Why Choose Us</a>
                <a href="/Features" class="nav-link">Features</a>
                <a href="/Pricing" class="nav-link">Pricing</a>
                <a href="/Contact" class="nav-link">Contact</a>
                <a href="/Contact" class="nav-cta">Get Started</a>
            </div>
        </nav>
    </div>
""", unsafe_allow_html=True)

# Content wrapper
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Hero Section (No changes)
st.markdown("""
    <div id="home" class="hero-section">
        <div class="welcome-badge">Welcome to CrypticX - The Ultimate Study Tool</div>
        <h1 class="hero-title">Master Your Studies with AI-Powered Learning</h1>
        <p class="hero-subtitle">Transform the way you learn with intelligent tools designed to help you understand faster, remember longer, and achieve academic excellence.</p>
        <a href="/Contact" class="hero-cta">Start Learning Free</a>
    </div>
""", unsafe_allow_html=True)

# About Us Section (No changes - this section already had the max-width fix)
st.markdown('<div id="about" class="section">', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">About Us</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Empowering students to reach their full potential</p>', unsafe_allow_html=True)

# This div is the fix for the text stretching
st.markdown('<div style="max-width: 800px; margin: 0 auto; text-align: center;">', unsafe_allow_html=True)
st.markdown("""
<p style="color: rgba(255, 255, 255, 0.7); font-size: 1.1rem; line-height: 1.9; margin-bottom: 2rem;">
CrypticX was founded by students, for students. We understand the challenges of modern education and created an AI-powered platform that makes studying more efficient, engaging, and effective. Our mission is to democratize access to personalized learning tools that help every student succeed.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<p style="color: rgba(255, 255, 255, 0.7); font-size: 1.1rem; line-height: 1.9;">
With cutting-edge artificial intelligence and a deep understanding of learning science, we've built tools that adapt to your unique learning style, making complex concepts easier to understand and helping you achieve your academic goals faster than ever before.
</p>
""", unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True) # Closes the 800px div and the section

# Why Choose Us Section (No changes)
st.markdown("""
    <div id="why-choose" class="section">
        <h2 class="section-title">Why Choose CrypticX</h2>
        <p class="section-subtitle">The smartest way to study in 2025</p>
        
        <div class="features-grid">
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
        </div>
    </div>
""", unsafe_allow_html=True)

# --- [REMOVED] Contact Section ---
# ... (All the st.markdown, st.text_input, st.button, etc. for the form are deleted) ...

# --- [REMOVED] Features Section ---
# ... (The entire "Powerful Study Features" markdown block is deleted) ...

# --- [REMOVED] Pricing Section ---
# ... (The entire "Choose Your Plan" markdown block is deleted) ...


# Close content wrapper
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <footer class="custom-footer">
        <p>© 2025 CrypticX • Empowering students with AI • Built with ❤️</p>
    </footer>
""", unsafe_allow_html=True)
