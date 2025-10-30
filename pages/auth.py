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
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'selected_plan' not in st.session_state:
    st.session_state.selected_plan = None
if 'auth_mode' not in st.session_state:
    st.session_state.auth_mode = 'signup'  # Default to signup for easier onboarding
if 'user_name' not in st.session_state:
    st.session_state.user_name = None

# Your full CSS (unchanged)
st.markdown("""
<style>
    /* [All your original CSS here - paste the entire <style> block from before, including auth styles, hero, pricing, dashboard, etc. No changes needed] */
    /* For brevity, assuming you paste it; it includes .auth-container, .auth-box, forms, etc. */
</style>
""", unsafe_allow_html=True)

# Background elements (unchanged)
st.markdown("""
<div class="grid-background"></div>
<div class="glow-orb purple"></div>
<div class="glow-orb pink"></div>
""", unsafe_allow_html=True)

# Main page logic
if not st.session_state.logged_in:
    # Not logged in: Show landing or auth based on current_page
    if st.session_state.current_page == 'auth':
        # AUTH PAGE (your original custom form, but auto-signup mode)
        st.markdown("""
        <div class="nav-container">
        <nav>
        <div class="logo" onclick="history.back()">  <!-- Simple back -->
        <span class="logo-icon">⚡</span>
        <span>CrypticX</span>
        </div>
        </nav>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="content-wrapper"><div class="auth-container"><div class="auth-box">', unsafe_allow_html=True)
        
        # Back link
        if st.button("← Back to Home", key="back_home"):
            st.session_state.current_page = 'home'
            st.session_state.selected_plan = None
            st.rerun()
        
        # Show selected plan badge
        if st.session_state.selected_plan:
            st.markdown(f'<div class="welcome-badge" style="margin-bottom: 1.5rem;">Selected Plan: {st.session_state.selected_plan}</div>', unsafe_allow_html=True)
        
        if st.session_state.auth_mode == 'login':
            st.markdown("""
            <div class="auth-header">
                <h1 class="auth-title">Welcome Back</h1>
                <p class="auth-subtitle">Sign in to access your dashboard</p>
            </div>
            """, unsafe_allow_html=True)
            
            email = st.text_input("Email", key="login_email", placeholder="your@email.com")
            password = st.text_input("Password", type="password", key="login_password", placeholder="Enter your password")
            
            if st.button("Sign In", key="login_submit"):
                if email and password:  # Dummy validation - add real check here
                    st.session_state.logged_in = True
                    st.session_state.current_page = 'dashboard'  # Go straight to dashboard
                    st.session_state.auth_mode = 'signup'  # Reset
                    st.rerun()
                else:
                    st.error("⚠ Please fill all fields")
            
            if st.button("Don't have an account? Create one", key="toggle_signup"):
                st.session_state.auth_mode = 'signup'
                st.rerun()
                
        else:  # signup mode (default)
            st.markdown("""
            <div class="auth-header">
                <h1 class="auth-title">Create Account</h1>
                <p class="auth-subtitle">Join and start your AI learning journey</p>
            </div>
            """, unsafe_allow_html=True)
            
            name = st.text_input("Full Name", key="signup_name", placeholder="Enter your name")
            email = st.text_input("Email", key="signup_email", placeholder="your@email.com")
            password = st.text_input("Password", type="password", key="signup_password", placeholder="Create a password")
            
            if st.button("Create Account", key="signup_submit"):
                if name and email and password:  # Dummy validation
                    st.session_state.logged_in = True
                    st.session_state.user_name = name
                    st.session_state.current_page = 'dashboard'  # Go to dashboard
                    st.session_state.auth_mode = 'signup'  # Reset
                    st.rerun()
                else:
                    st.error("⚠ Please fill all fields")
            
            if st.button("Already have an account? Sign In", key="toggle_login"):
                st.session_state.auth_mode = 'login'
                st.rerun()
        
        st.markdown('</div></div></div>', unsafe_allow_html=True)
    
    else:
        # LANDING PAGE (home/hero/pricing)
        # Nav (unchanged, but buttons now use st.button callbacks below)
        st.markdown("""
        <div class="nav-container">
        <nav>
        <div class="logo">⚡ CrypticX</div>
        <div class="nav-links">
        <span class="nav-link">Home</span>
        <span class="nav-link">Pricing</span>
        <span class="nav-link">Dashboard</span>
        <span class="nav-link">Login</span>
        <button class="nav-cta">Sign Up</button>
        </div>
        </nav>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
        
        # Hero (button callback: sets plan + auth)
        st.markdown("""
        <div class="hero-section">
        <div class="welcome-badge">✨ Welcome to CrypticX - The Ultimate Study Tool</div>
        <h1 class="hero-title">Master Your Studies with AI-Powered Learning</h1>
        <p class="hero-subtitle">Transform the way you learn with intelligent tools designed to help you understand faster, remember longer, and achieve academic excellence.</p>
        """, unsafe_allow_html=True)
        
        if st.button("Start Learning Free", key="hero_start"):
            st.session_state.selected_plan = 'Free'
            st.session_state.current_page = 'auth'
            st.rerun()  # Triggers auth signup
        
        st.markdown("""
        <div class="stats-section">
            <div class="stat-item"><div class="stat-number">50K+</div><div class="stat-label">Active Students</div></div>
            <div class="stat-item"><div class="stat-number">95%</div><div class="stat-label">Satisfaction Rate</div></div>
            <div class="stat-item"><div class="stat-number">1M+</div><div class="stat-label">Questions Answered</div></div>
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Features section (unchanged)
        st.markdown('<div class="section"><h2 class="section-title">Why Choose CrypticX</h2><p class="section-subtitle">The smartest way to study in 2025</p><div class="features-grid">', unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card"><span class="feature-icon">⚡</span><h3>Lightning Fast</h3><p>Get instant answers...</p></div>
        <!-- Paste all 6 feature cards here - unchanged -->
        """, unsafe_allow_html=True)  # Abbrev for space; use your full
        st.markdown('</div></div>', unsafe_allow_html=True)
        
        # Pricing (buttons with callbacks)
        st.markdown('<div class="section"><h2 class="section-title">Choose Your Plan</h2><p class="section-subtitle">Start free, upgrade when ready</p><div class="pricing-grid">', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Start Free", key="plan_free"):
                st.session_state.selected_plan = 'Free'
                st.session_state.current_page = 'auth'
                st.rerun()
            st.markdown('<div class="pricing-card"><h3>Free</h3><div class="price">$0/mo</div><div class="feature-list">✓ 10 questions/day...</div></div>', unsafe_allow_html=True)
        
        with col2:
            if st.button("Get Pro", key="plan_pro"):
                st.session_state.selected_plan = 'Pro'
                st.session_state.current_page = 'auth'
                st.rerun()
            st.markdown('<div class="pricing-card featured"><div class="pricing-badge">⭐ MOST POPULAR</div><h3>Pro</h3><div class="price">$15/mo</div><div class="feature-list">✓ Unlimited...</div></div>', unsafe_allow_html=True)
        
        with col3:
            if st.button("Get Enterprise", key="plan_enterprise"):
                st.session_state.selected_plan = 'Enterprise'
                st.session_state.current_page = 'auth'
                st.rerun()
            st.markdown('<div class="pricing-card"><h3>Enterprise</h3><div class="price">$35/mo</div><div class="feature-list">✓ Everything in Pro...</div></div>', unsafe_allow_html=True)
        
        st.markdown('</div></div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close content-wrapper

else:
    # LOGGED IN: Show dashboard as main product page
    st.markdown("""
    <div class="nav-container">
    <nav>
    <div class="logo" onclick="history.back()">⚡ CrypticX</div>
    <div class="nav-links">
    <span class="nav-link">Home</span>
    <span class="nav-link">Pricing</span>
    <span class="nav-link active">Dashboard</span>
    <span class="user-greeting">Hi, {}</span>
    """.format(st.session_state.user_name), unsafe_allow_html=True)
    
    if st.button("Logout", key="logout"):
        st.session_state.logged_in = False
        st.session_state.user_name = None
        st.session_state.selected_plan = None
        st.session_state.current_page = 'home'
        st.rerun()
    
    st.markdown('</div></nav></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    
    # DASHBOARD (main product - expand here with AI tools, e.g., st.chat_input for questions)
    plan_badge = f"Plan: {st.session_state.selected_plan}" if st.session_state.selected_plan else ""
    st.markdown(f"""
    <div class="dashboard-section">
        <h1 class="dashboard-welcome">Welcome back, {st.session_state.user_name}!</h1>
        <p class="dashboard-subtitle">Your AI study dashboard {plan_badge}</p>
        <div class="dashboard-stats">
            <div class="dashboard-stat"><div class="dashboard-stat-number">42</div><div class="dashboard-stat-label">Questions Answered</div></div>
            <div class="dashboard-stat"><div class="dashboard-stat-number">87%</div><div class="dashboard-stat-label">Quiz Average</div></div>
            <div class="dashboard-stat"><div class="dashboard-stat-number">5</div><div class="dashboard-stat-label">Active Courses</div></div>
            <div class="dashboard-stat"><div class="dashboard-stat-number">2h 30m</div><div class="dashboard-stat-label">Study Time Today</div></div>
        </div>
        <!-- Main product: Add your AI features here, e.g.: -->
        <div style="text-align: center; margin-top: 2rem;">
            <h3>Ask your AI study buddy:</h3>
            {st.chat_input("e.g., Explain quantum physics simply")}
        </div>
        <button class="hero-cta" onclick="window.location.reload()">Refresh Progress</button>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer (unchanged)
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
