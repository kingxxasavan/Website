# home.py
# This is the main homepage file. Run with: streamlit run home.py
# For multi-page navigation, place auth.py and dashboard.py in a 'pages' folder.
# However, since separate files are requested, we'll use session state for simple navigation simulation.
# For full multi-page, restructure as per Streamlit docs.

import streamlit as st
import streamlit.components.v1 as components

# Custom CSS to match the futuristic blue/purple gradient theme
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
        color: white;
    }
    .header {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 20px;
        margin: 10px;
    }
    .logo {
        font-size: 2em;
        color: #00d4ff;
    }
    .nav-link {
        color: white;
        text-decoration: none;
        margin: 0 10px;
        transition: color 0.3s;
    }
    .nav-link:hover {
        color: #00d4ff;
    }
    .hero-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 50px;
        text-align: center;
    }
    .hero-title {
        font-size: 3em;
        background: linear-gradient(45deg, #00d4ff, #ff00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }
    .hero-subtitle {
        font-size: 1.5em;
        color: #ccc;
        margin-bottom: 30px;
    }
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin: 50px 0;
    }
    .feature-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        transition: transform 0.3s;
    }
    .feature-card:hover {
        transform: translateY(-5px);
    }
    .prices-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin: 50px 0;
    }
    .price-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }
    .btn-primary {
        background: linear-gradient(45deg, #00d4ff, #ff00ff);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 25px;
        cursor: pointer;
        transition: opacity 0.3s;
    }
    .btn-primary:hover {
        opacity: 0.8;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
    <div class="header">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div class="logo">🤖 AI ChatBot</div>
            <div>
                <a href="#" class="nav-link">Home</a>
                <a href="#" class="nav-link">Services</a>
                <a href="#" class="nav-link">Contact</a>
                <a href="#" class="nav-link">About</a>
            </div>
            <div>
                <button class="btn-primary" onclick="window.location.href='auth.py'">Login</button>
                <button class="btn-primary" onclick="window.location.href='auth.py?mode=signup'">Sign Up</button>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Introducing AI ChatBot</h1>
        <p class="hero-subtitle">AI Generated Chat Bot for Effect Conversation</p>
        <p>Lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum has been the industry's standard dummy text ever since the 1500s.</p>
        <button class="btn-primary" style="font-size: 1.2em; padding: 15px 30px; margin-top: 20px;" onclick="window.location.href='auth.py'">Get Started</button>
    </div>
""", unsafe_allow_html=True)

# Placeholder for robot image - replace with actual image URL or upload
st.image("https://via.placeholder.com/400x600/1a1a2e/00d4ff?text=AI+Robot", use_column_width=True)

# Features Section
st.markdown("<h2 style='text-align: center; color: #00d4ff;'>Features</h2>", unsafe_allow_html=True)
features = [
    {"title": "Natural Conversations", "desc": "Engage in seamless, human-like chats."},
    {"title": "Multi-Language Support", "desc": "Communicate in over 100 languages."},
    {"title": "Real-Time Responses", "desc": "Instant replies powered by advanced AI."},
    {"title": "Secure & Private", "desc": "Your data stays confidential."}
]
cols = st.columns(len(features))
for i, feature in enumerate(features):
    with cols[i]:
        st.markdown(f"""
            <div class="feature-card">
                <h3>{feature['title']}</h3>
                <p>{feature['desc']}</p>
            </div>
        """, unsafe_allow_html=True)

# Prices Section
st.markdown("<h2 style='text-align: center; color: #00d4ff;'>Pricing Plans</h2>", unsafe_allow_html=True)
prices = [
    {"name": "Free", "price": "$0/mo", "features": ["Basic Chat", "Limited Queries"]},
    {"name": "Pro", "price": "$9.99/mo", "features": ["Unlimited Chat", "Advanced Features", "Priority Support"]},
    {"name": "Enterprise", "price": "$29.99/mo", "features": ["All Pro", "Custom Integrations", "Dedicated Support"]}
]
cols = st.columns(len(prices))
for i, plan in enumerate(prices):
    with cols[i]:
        st.markdown(f"""
            <div class="price-card">
                <h3>{plan['name']}</h3>
                <h2>{plan['price']}</h2>
                <ul>
                    {''.join([f'<li>{f}</li>' for f in plan['features']])}
                </ul>
                <button class="btn-primary" onclick="window.location.href='auth.py'">Get Started</button>
            </div>
        """, unsafe_allow_html=True)

# Note: For actual navigation in Streamlit, use st.switch_page('pages/auth.py') in multi-page setup.
# Here, using HTML onclick for simulation; adjust for production.
