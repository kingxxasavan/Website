import streamlit as st

st.set_page_config(
    page_title="Academic Services - Get Expert Help",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# Navigation
query_params = st.query_params
if 'page' in query_params:
    page = query_params.get('page', ['home'])[0]
    if page in ['home', 'services', 'how-it-works']:
        st.session_state.current_page = page
        query_params.pop('page', None)
        st.rerun()

# CSS - Simplified and compelling
st.markdown("""
<style>
    /* Hide Streamlit elements */
    #MainMenu, footer, header, .stDeployButton, .stDecoration {visibility: hidden !important;}
    section[data-testid="stSidebar"], .stSidebar, [data-testid="collapsedControl"] {display: none !important;}
    .block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
    .stApp {margin: 0 !important; padding: 0 !important;}
    
    /* Base */
    * {margin: 0; padding: 0; box-sizing: border-box;}
    body {font-family: 'Inter', -apple-system, sans-serif; overflow-x: hidden;}
    .stApp {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #fff;}
    
    /* Navigation */
    .nav {position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(0,0,0,0.1); padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center;}
    .logo {font-size: 1.5rem; font-weight: 800; color: #667eea; cursor: pointer;}
    .nav-links {display: flex; gap: 2rem; align-items: center;}
    .nav-link {color: #333; text-decoration: none; font-weight: 600; cursor: pointer; transition: color 0.3s;}
    .nav-link:hover {color: #667eea;}
    .discord-btn {background: #5865F2; color: white; padding: 0.7rem 1.5rem; border-radius: 8px; font-weight: 700; cursor: pointer; transition: transform 0.2s;}
    .discord-btn:hover {transform: translateY(-2px); box-shadow: 0 4px 12px rgba(88, 101, 242, 0.4);}
    
    /* Hero Section */
    .hero {min-height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 6rem 2rem 4rem;}
    .hero-title {font-size: 4rem; font-weight: 900; margin-bottom: 1.5rem; line-height: 1.1; text-shadow: 0 2px 20px rgba(0,0,0,0.1);}
    .hero-subtitle {font-size: 1.4rem; margin-bottom: 2rem; opacity: 0.95; max-width: 700px;}
    .hero-cta {background: white; color: #667eea; padding: 1.2rem 3rem; border-radius: 50px; font-size: 1.2rem; font-weight: 800; cursor: pointer; transition: all 0.3s; box-shadow: 0 8px 30px rgba(0,0,0,0.2); border: none;}
    .hero-cta:hover {transform: translateY(-3px); box-shadow: 0 12px 40px rgba(0,0,0,0.3);}
    .trust-badges {display: flex; gap: 3rem; margin-top: 3rem; flex-wrap: wrap; justify-content: center;}
    .badge {text-align: center;}
    .badge-number {font-size: 2.5rem; font-weight: 800;}
    .badge-label {opacity: 0.9; margin-top: 0.5rem;}
    
    /* Services Grid */
    .section {padding: 5rem 2rem; max-width: 1200px; margin: 0 auto;}
    .section-dark {background: rgba(0,0,0,0.2); backdrop-filter: blur(10px);}
    .section-title {font-size: 3rem; font-weight: 800; text-align: center; margin-bottom: 3rem;}
    .services-grid {display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; margin-top: 2rem;}
    .service-card {background: white; color: #333; border-radius: 20px; padding: 2.5rem; box-shadow: 0 10px 40px rgba(0,0,0,0.1); transition: transform 0.3s; cursor: pointer;}
    .service-card:hover {transform: translateY(-10px); box-shadow: 0 20px 60px rgba(0,0,0,0.2);}
    .service-icon {font-size: 3rem; margin-bottom: 1rem;}
    .service-title {font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem; color: #667eea;}
    .service-price {font-size: 1.8rem; font-weight: 800; color: #333; margin: 1rem 0;}
    .service-desc {color: #666; line-height: 1.6; margin-bottom: 1.5rem;}
    .service-features {text-align: left; color: #666; line-height: 2; margin-bottom: 1.5rem; font-size: 0.95rem;}
    .order-btn {width: 100%; background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 1rem; border-radius: 12px; font-weight: 700; border: none; cursor: pointer; transition: all 0.3s;}
    .order-btn:hover {transform: translateY(-2px); box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);}
    
    /* How It Works */
    .steps {display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-top: 3rem;}
    .step {text-align: center; padding: 2rem;}
    .step-number {width: 60px; height: 60px; background: white; color: #667eea; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; font-weight: 800; margin: 0 auto 1.5rem; box-shadow: 0 4px 20px rgba(0,0,0,0.1);}
    .step-title {font-size: 1.3rem; font-weight: 700; margin-bottom: 0.5rem;}
    .step-desc {opacity: 0.9; line-height: 1.6;}
    
    /* CTA Section */
    .cta-section {text-align: center; padding: 6rem 2rem; background: rgba(0,0,0,0.2);}
    .cta-title {font-size: 3rem; font-weight: 800; margin-bottom: 1.5rem;}
    .cta-subtitle {font-size: 1.3rem; margin-bottom: 2rem; opacity: 0.9;}
    
    /* Footer */
    .footer {text-align: center; padding: 3rem 2rem; background: rgba(0,0,0,0.3); font-size: 0.9rem; opacity: 0.8;}
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-title {font-size: 2.5rem;}
        .hero-subtitle {font-size: 1.1rem;}
        .nav-links {display: none;}
        .section-title {font-size: 2rem;}
        .trust-badges {gap: 2rem;}
    }
</style>
""", unsafe_allow_html=True)

# Navigation Bar
st.markdown(f'''
<div class="nav">
    <div class="logo" onclick="window.location.href='?page=home'">📚 StudyHub</div>
    <div class="nav-links">
        <span class="nav-link" onclick="window.location.href='?page=home'">Home</span>
        <span class="nav-link" onclick="window.location.href='?page=services'">Services</span>
        <span class="nav-link" onclick="window.location.href='?page=how-it-works'">How It Works</span>
        <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" style="text-decoration: none;">
            <button class="discord-btn">Join Discord →</button>
        </a>
    </div>
</div>
''', unsafe_allow_html=True)

# HOME PAGE
if st.session_state.current_page == 'home':
    st.markdown('''
    <div class="hero">
        <h1 class="hero-title">Get Your Projects Done Right</h1>
        <p class="hero-subtitle">Expert help with essays, coding, tutoring, and more. Fast delivery. Quality guaranteed. Join our Discord community.</p>
        <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" style="text-decoration: none;">
            <button class="hero-cta">Join Discord & Order Now</button>
        </a>
        <div class="trust-badges">
            <div class="badge">
                <div class="badge-number">50+</div>
                <div class="badge-label">Happy Customers</div>
            </div>
            <div class="badge">
                <div class="badge-number">24-48hr</div>
                <div class="badge-label">Delivery Time</div>
            </div>
            <div class="badge">
                <div class="badge-number">100%</div>
                <div class="badge-label">Original Work</div>
            </div>
        </div>
    </div>
    
    <div class="section section-dark">
        <h2 class="section-title">Our Services</h2>
        <div class="services-grid">
            <div class="service-card">
                <div class="service-icon">✍️</div>
                <h3 class="service-title">Essay Editing</h3>
                <div class="service-price">$20-40</div>
                <p class="service-desc">Professional proofreading and editing to perfect your essays.</p>
                <div class="service-features">
                    ✓ Grammar & spelling<br>
                    ✓ Structure feedback<br>
                    ✓ Citation formatting<br>
                    ✓ 1 free revision
                </div>
                <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" style="text-decoration: none;">
                    <button class="order-btn">Order on Discord</button>
                </a>
            </div>
            
            <div class="service-card">
                <div class="service-icon">💻</div>
                <h3 class="service-title">Code Help</h3>
                <div class="service-price">$30-60</div>
                <p class="service-desc">Debug, review, or build your coding projects with expert assistance.</p>
                <div class="service-features">
                    ✓ Python, Java, JS<br>
                    ✓ Debugging & review<br>
                    ✓ Explanations included<br>
                    ✓ Fast turnaround
                </div>
                <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" style="text-decoration: none;">
                    <button class="order-btn">Order on Discord</button>
                </a>
            </div>
            
            <div class="service-card">
                <div class="service-icon">📚</div>
                <h3 class="service-title">Tutoring</h3>
                <div class="service-price">$25/hr</div>
                <p class="service-desc">One-on-one help with homework, test prep, and understanding concepts.</p>
                <div class="service-features">
                    ✓ Math, Science, CS<br>
                    ✓ Flexible scheduling<br>
                    ✓ Video or text help<br>
                    ✓ Monthly packages
                </div>
                <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" style="text-decoration: none;">
                    <button class="order-btn">Order on Discord</button>
                </a>
            </div>
            
            <div class="service-card">
                <div class="service-icon">🎨</div>
                <h3 class="service-title">Presentations</h3>
                <div class="service-price">$30-50</div>
                <p class="service-desc">Create compelling PowerPoint or Google Slides presentations.</p>
                <div class="service-features">
                    ✓ Professional design<br>
                    ✓ Custom templates<br>
                    ✓ Unlimited revisions<br>
                    ✓ Quick delivery
                </div>
                <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" style="text-decoration: none;">
                    <button class="order-btn">Order on Discord</button>
                </a>
            </div>
        </div>
    </div>
    
    <div class="cta-section">
        <h2 class="cta-title">Ready to Get Started?</h2>
        <p class="cta-subtitle">Join our Discord community and place your first order today</p>
        <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" style="text-decoration: none;">
            <button class="hero-cta">Join Discord Community</button>
        </a>
    </div>
    ''', unsafe_allow_html=True)

# SERVICES PAGE
elif st.session_state.current_page == 'services':
    st.markdown('''
    <div style="padding-top: 100px;">
        <div class="section">
            <h2 class="section-title">All Services</h2>
            <p style="text-align: center; font-size: 1.2rem; margin-bottom: 3rem; opacity: 0.9;">
                Quality work delivered fast. All orders handled through Discord for direct communication.
            </p>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">✍️</div>
                    <h3 class="service-title">Essay Editing</h3>
                    <div class="service-price">Starting at $20</div>
                    <p class="service-desc">Perfect your essays with professional editing and feedback.</p>
                    <div class="service-features">
                        • 1-5 pages: $20<br>
                        • 6-10 pages: $35<br>
                        • 10+ pages: $40+<br>
                        • Delivery: 3-5 days
                    </div>
                    <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" style="text-decoration: none;">
                        <button class="order-btn">Order Now</button>
                    </a>
                </div>
                
                <div class="service-card">
                    <div class="service-icon">💻</div>
                    <h3 class="service-title">Coding Projects</h3>
                    <div class="service-price">Starting at $30</div>
                    <p class="service-desc">Get help with debugging, code review, or building projects.</p>
                    <div class="service-features">
                        • Simple fix: $30<br>
                        • Full project: $50-100<br>
                        • Monthly help: $120/mo<br>
                        • Delivery: 2-5 days
                    </div>
                    <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" style="text-decoration: none;">
                        <button class="order-btn">Order Now</button>
                    </a>
                </div>
                
                <div class="service-card">
                    <div class="service-icon">📚</div>
                    <h3 class="service-title">Tutoring Sessions</h3>
                    <div class="service-price">$25/session</div>
                    <p class="service-desc">One-on-one tutoring for homework help and test prep.</p>
                    <div class="service-features">
                        • 1 session: $25<br>
                        • 4 sessions: $90/mo<br>
                        • Math, CS, Science<br>
                        • Video or text help
                    </div>
                    <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" style="text-decoration: none;">
                        <button class="order-btn">Order Now</button>
                    </a>
                </div>
                
                <div class="service-card">
                    <div class="service-icon">🎨</div>
                    <h3 class="service-title">Presentations</h3>
                    <div class="service-price">Starting at $30</div>
                    <p class="service-desc">Professional PowerPoint and Google Slides creation.</p>
                    <div class="service-features">
                        • 5-10 slides: $30<br>
                        • 15-20 slides: $45<br>
                        • Custom design<br>
                        • Delivery: 2-4 days
                    </div>
                    <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" style="text-decoration: none;">
                        <button class="order-btn">Order Now</button>
                    </a>
                </div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# HOW IT WORKS PAGE
elif st.session_state.current_page == 'how-it-works':
    st.markdown('''
    <div style="padding-top: 100px;">
        <div class="section">
            <h2 class="section-title">How It Works</h2>
            <p style="text-align: center; font-size: 1.2rem; margin-bottom: 3rem; opacity: 0.9;">
                Simple, fast, and secure. Get your work done in 3 easy steps.
            </p>
            <div class="steps">
                <div class="step">
                    <div class="step-number">1</div>
                    <h3 class="step-title">Join Discord</h3>
                    <p class="step-desc">Click the button to join our Discord server. Browse the service channels to see what we offer.</p>
                </div>
                <div class="step">
                    <div class="step-number">2</div>
                    <h3 class="step-title">Place Your Order</h3>
                    <p class="step-desc">Post in the relevant channel or DM me with your project details. Send payment via CashApp/Venmo.</p>
                </div>
                <div class="step">
                    <div class="step-number">3</div>
                    <h3 class="step-title">Get Your Work</h3>
                    <p class="step-desc">Receive your completed work via Discord DM or email within the agreed timeframe. One free revision included!</p>
                </div>
            </div>
        </div>
        
        <div class="section section-dark">
            <h2 class="section-title">Why Discord?</h2>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">💬</div>
                    <h3 class="service-title">Direct Communication</h3>
                    <p class="service-desc">Chat directly with me in real-time. Ask questions, share files, and get updates instantly.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">🔒</div>
                    <h3 class="service-title">Safe & Secure</h3>
                    <p class="service-desc">All communication is private. Payment through trusted apps like CashApp, Venmo, or Zelle.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">⚡</div>
                    <h3 class="service-title">Fast Response</h3>
                    <p class="service-desc">Usually respond within 1 hour during business hours. No waiting days for email replies.</p>
                </div>
            </div>
        </div>
        
        <div class="cta-section">
            <h2 class="cta-title">Ready to Order?</h2>
            <p class="cta-subtitle">Join Discord now and get your first order started today</p>
            <a href="https://discord.gg/YOUR_INVITE_LINK" target="_blank" style="text-decoration: none;">
                <button class="hero-cta">Join Discord Server</button>
            </a>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# Footer
st.markdown('''
<div class="footer">
    <p>© 2025 StudyHub. Quality academic services. Fast delivery. Satisfaction guaranteed.</p>
    <p style="margin-top: 1rem; opacity: 0.6;">All work is 100% original. Payment via CashApp, Venmo, or Zelle.</p>
</div>
''', unsafe_allow_html=True)
