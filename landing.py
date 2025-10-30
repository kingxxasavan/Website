import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CrypticX - AI Study Tool",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 1. UPDATE: Enhanced Session State ---
# Initialize session state
if 'current_section' not in st.session_state:
    st.session_state.current_section = 'home'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'show_signup' not in st.session_state:
    st.session_state.show_signup = False
if 'show_login' not in st.session_state:  # Added for login modal
    st.session_state.show_login = False

# --- 2. NEW: Add CSS for Modals ---
# Enhanced CSS with smooth scrolling and animations
st.markdown("""
<style>
    /* --- ALL YOUR ORIGINAL CSS... --- */
    
    /* ... (your existing 500+ lines of CSS) ... */
    
    /* --- ADD THIS CSS AT THE END OF THE <style> TAG --- */
    
    /* Modal styling */
    div[data-testid="stModal"] > div {
        background: rgba(30, 30, 45, 0.9);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 16px;
        backdrop-filter: blur(15px);
    }
    div[data-testid="stModal"] h1 {
        color: #fff;
        font-size: 1.5rem;
        text-align: center;
    }
    /* Style modal primary button */
    div[data-testid="stModal"] .stButton > button[kind="primary"] {
        width: 100%;
        padding: 0.7rem 1.8rem;
        border-radius: 50px;
        background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);
        color: #fff;
        font-weight: 600;
        border: none;
        transition: all 0.3s;
        box-shadow: 0 4px 20px rgba(139, 92, 246, 0.4);
    }
    div[data-testid="stModal"] .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(139, 92, 246, 0.6);
    }
    /* Style modal secondary/default button */
    div[data-testid="stModal"] .stButton > button[kind="secondary"] {
        width: 100%;
        background: transparent;
        color: #8b5cf6;
        box-shadow: none;
        border: none;
    }
    div[data-testid="stModal"] .stButton > button[kind="secondary"]:hover {
        background: rgba(139, 92, 246, 0.1);
        color: #fff;
    }
    /* Style modal inputs */
    div[data-testid="stModal"] div[data-testid="stTextInput"] > div > div > input {
        background-color: rgba(255, 255, 255, 0.1);
        color: #fff;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 8px;
    }
    div[data-testid="stModal"] div[data-testid="stTextInput"] label {
        color: rgba(255, 255, 255, 0.7) !important;
    }
</style>
""", unsafe_allow_html=True)

# Background elements (Original)
st.markdown("""
<div class="grid-background"></div>
<div class="glow-orb purple"></div>
<div class="glow-orb pink"></div>
""", unsafe_allow_html=True)

# JavaScript for smooth scrolling (Original)
st.markdown("""
<script>
    /* ... (your original script) ... */
</script>
""", unsafe_allow_html=True)


# --- 3. DELETE: Remove Old Navigation Handler ---
# DELETE the entire `components.html` block and the old `st.query_params` check
# We replace it with the new handler below.


# --- 4. NEW: Updated Query Parameter & Modal Logic ---

# Check for navigation parameter to OPEN MODALS or change state
nav_param = st.query_params.get("nav")

if nav_param == "login":
    st.session_state.show_login = True
    st.session_state.show_signup = False
    st.query_params.clear() 
elif nav_param == "signup":
    st.session_state.show_signup = True
    st.session_state.show_login = False
    st.query_params.clear()
elif nav_param == "logout":
    st.session_state.logged_in = False
    # Add any other logout logic (e.g., clear user data)
    st.query_params.clear()
    st.rerun()
elif nav_param == "dashboard":
    if st.session_state.logged_in:
        # If logged in, switch to the dashboard page
        st.switch_page("pages/dashboard.py")
    else:
        # If not logged in, just open login modal
        st.session_state.show_login = True
        st.query_params.clear()


# --- Define Modal Functions ---

def show_login_modal():
    with st.modal("Login", clear_on_submit=False):
        st.text_input("Username", key="login_user")
        st.text_input("Password", type="password", key="login_pass")
        
        if st.button("Login", type="primary", key="login_submit"):
            # --- ADD YOUR REAL LOGIN LOGIC HERE ---
            # Example: check_password(st.session_state.login_user, st.session_state.login_pass)
            if st.session_state.login_user == "admin" and st.session_state.login_pass == "pass":
                st.success("Logged in successfully!")
                st.session_state.logged_in = True
                st.session_state.show_login = False # Close modal
                st.rerun() # Rerun to update nav bar
            else:
                st.error("Invalid username or password")
        
        if st.button("Don't have an account? Sign Up", key="login_to_signup"):
            st.session_state.show_login = False
            st.session_state.show_signup = True
            st.rerun()

def show_signup_modal():
    with st.modal("Sign Up", clear_on_submit=False):
        st.text_input("Username", key="signup_user")
        st.text_input("Email", key="signup_email")
        st.text_input("Password", type="password", key="signup_pass")
        
        if st.button("Create Account", type="primary", key="signup_submit"):
            # --- ADD YOUR REAL SIGNUP LOGIC HERE ---
            # Example: create_user(st.session_state.signup_user, ...)
            st.success("Account created! Please log in.")
            st.session_state.show_signup = False # Close modal
            st.session_state.show_login = True   # Open login modal
            st.rerun()
        
        if st.button("Already have an account? Login", key="signup_to_login"):
            st.session_state.show_signup = False
            st.session_state.show_login = True
            st.rerun()

# --- Display modals based on session state ---
if st.session_state.show_login:
    show_login_modal()

if st.session_state.show_signup:
    show_signup_modal()


# --- 5. UPDATE: Dynamic Navigation Bar ---
# This block now uses Python's `if/else` to show a different
# nav bar if the user is logged in.

if st.session_state.logged_in:
    # --- NAV BAR FOR LOGGED-IN USERS ---
    st.markdown(f"""
    <div class="nav-container">
    <nav>
        <div class="logo">
        <span class="logo-icon">⚡</span>
        <span>CrypticX</span>
        </div>
        <div class="nav-links">
        <a href="#home" class="nav-link {'active' if st.session_state.current_section == 'home' else ''}">Home</a>
        <a href="#pricing" class="nav-link {'active' if st.session_state.current_section == 'pricing' else ''}">Pricing</a>
        <a href="?nav=dashboard" class="nav-link {'active' if st.session_state.current_section == 'dashboard' else ''}">Dashboard</a>
        <button class="nav-cta" onclick="window.location.href='?nav=logout'">Logout</button>
        </div>
    </nav>
    </div>
    """, unsafe_allow_html=True)
else:
    # --- NAV BAR FOR LOGGED-OUT USERS (Your Original) ---
    st.markdown(f"""
    <div class="nav-container">
    <nav>
        <div class="logo">
        <span class="logo-icon">⚡</span>
        <span>CrypticX</span>
        </div>
        <div class="nav-links">
        <a href="#home" class="nav-link {'active' if st.session_state.current_section == 'home' else ''}">Home</a>
        <a href="#pricing" class="nav-link {'active' if st.session_state.current_section == 'pricing' else ''}">Pricing</a>
        <a href="#dashboard" class="nav-link {'active' if st.session_state.current_section == 'dashboard' else ''}">Dashboard</a>
        <a href="?nav=login" class="nav-link {'active' if st.session_state.current_section == 'login' else ''}">Login</a>
        <button class="nav-cta" onclick="window.location.href='?nav=signup'">Sign Up</button>
        </div>
    </nav>
    </div>
    """, unsafe_allow_html=True)


# --- ALL YOUR ORIGINAL CONTENT HTML (Unchanged) ---

# Content wrapper
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div id="home" class="hero-section">
<div class="welcome-badge">✨ Welcome to CrypticX - The Ultimate Study Tool</div>
<h1 class="hero-title">Master Your Studies with AI-Powered Learning</h1>
<p class="hero-subtitle">Transform the way you learn with intelligent tools designed to help you understand faster, remember longer, and achieve academic excellence.</p>
<button class="hero-cta" onclick="window.location.href='?nav=signup'">Start Learning Free</button>
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
st.markdown('<p class="section-subtitle">Start free, upgrade when you\'re ready</p>', unsafe_allow_html=True)
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
        <button class="pricing-button" onclick="window.location.href='?nav=signup'">Start Free</button>
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
        <button class="pricing-button" onclick="window.location.href='?nav=signup'">Get Pro</button>
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
        <button class="pricing-button" onclick="window.location.href='?nav=signup'">Contact Us</button>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Close content wrapper
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
