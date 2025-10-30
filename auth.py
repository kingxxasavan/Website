# auth.py
# Run with: streamlit run auth.py
# This handles both login and signup based on query param or session state.

import streamlit as st
import streamlit.components.v1 as components
from urllib.parse import urlparse, parse_qs

# Custom CSS for centered, small, glass-like auth form matching homepage theme
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        color: white;
    }
    .auth-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 40px;
        width: 400px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
    }
    .auth-title {
        font-size: 2em;
        background: linear-gradient(45deg, #00d4ff, #ff00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }
    .auth-form input {
        width: 100%;
        padding: 12px;
        margin: 10px 0;
        border: none;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.2);
        color: white;
        font-size: 1em;
    }
    .auth-form input::placeholder {
        color: #ccc;
    }
    .btn-primary {
        background: linear-gradient(45deg, #00d4ff, #ff00ff);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 25px;
        cursor: pointer;
        width: 100%;
        margin: 10px 0;
        font-size: 1em;
        transition: opacity 0.3s;
    }
    .btn-primary:hover {
        opacity: 0.8;
    }
    .switch-link {
        color: #00d4ff;
        text-decoration: none;
        margin-top: 20px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# Get mode from query params or default to login
query_params = st.experimental_get_query_params()
mode = query_params.get('mode', ['login'])[0]

if mode == 'signup':
    title = "Sign Up"
    button_text = "Sign Up"
    alt_mode = 'login'
    alt_text = "Already have an account? Login"
else:
    title = "Login"
    button_text = "Login"
    alt_mode = 'signup'
    alt_text = "Don't have an account? Sign Up"

# Auth form
st.markdown(f"""
    <div class="auth-container">
        <h1 class="auth-title">{title}</h1>
        <form class="auth-form">
            <input type="email" placeholder="Email" required>
            <input type="password" placeholder="Password" required>
            <button class="btn-primary">{button_text}</button>
        </form>
        <a href="?mode={alt_mode}" class="switch-link">{alt_text}</a>
    </div>
""", unsafe_allow_html=True)

# Dummy auth logic - in production, integrate with database/auth service
if st.button(button_text):
    st.session_state['authenticated'] = True
    st.switch_page('dashboard.py')  # Assumes multi-page; adjust if single file

# For single-file simulation, use session state to show dashboard inline, but keeping separate.
