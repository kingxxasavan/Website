import streamlit as st

# Import pages (lazy—only loads on navigation)
from landing import main as landing_page  # Wrapper for your unchanged landing.py
import pages.auth as auth_page
import pages.dashboard as dashboard_page
from utils import USERS, hash_password, get_user_data

# Page config (from your original)
st.set_page_config(
    page_title="CrypticX - AI Study Tool",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Global session state (optimized—minimal keys)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = None
if "user_name" not in st.session_state:
    st.session_state.user_name = None
if "selected_plan" not in st.session_state:
    st.session_state.selected_plan = None
if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = "signup"

# Your exact CSS (consolidated—no changes)
st.markdown("""
<style>
    /* [Your full CSS from the provided code—paste the entire <style> block here] */
</style>
""", unsafe_allow_html=True)

# Background elements (global, loads once)
st.markdown('<div class="grid-background"></div><div class="glow-orb purple"></div><div class="glow-orb pink"></div>', unsafe_allow_html=True)

# Navigation menu (your exact nav HTML, adapted for pages)
def render_nav(is_logged_in: bool):
    if not is_logged_in:
        st.markdown("""
        <div class="nav-container">
            <nav>
                <div class="logo" onclick="window.location.href='?page=home'"><span class="logo-icon">⚡</span><span>CrypticX</span></div>
                <div class="nav-links">
                    <span class="nav-link" onclick="window.location.href='?page=home'">Home</span>
                    <span class="nav-link" onclick="window.location.href='#pricing'">Pricing</span>  <!-- Scroll within home -->
                    <span class="nav-link" onclick="window.location.href='?page=auth'">Login</span>
                    <button class="nav-cta" onclick="window.location.href='?page=auth'">Sign Up</button>
                </div>
            </nav>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="nav-container">
            <nav>
                <div class="logo" onclick="window.location.href='?page=home'"><span class="logo-icon">⚡</span><span>CrypticX</span></div>
                <div class="nav-links">
                    <span class="nav-link" onclick="window.location.href='?page=home'">Home</span>
                    <span class="nav-link" onclick="window.location.href='#pricing'">Pricing</span>
                    <span class="nav-link active" onclick="window.location.href='?page=dashboard'">Dashboard</span>
                    <span class="user-greeting">Hi, {st.session_state.user_name}</span>
                </div>
            </nav>
        </div>
        """, unsafe_allow_html=True)

# Auth check & routing
if not st.session_state.logged_in:
    # Force auth for protected pages
    page = st.query_params.get("page", ["home"])[0]
    if page in ["dashboard"]:
        page = "auth"
    st.query_params["page"] = page
else:
    page = st.query_params.get("page", ["dashboard"])[0]  # Default to dashboard for logged-in

# Render pages via st.navigation (perf: only one runs)
pages = {
    "Home": lambda: (render_nav(False), st.markdown('<div class="content-wrapper">', unsafe_allow_html=True), landing_page(), st.markdown('</div>', unsafe_allow_html=True)),
    "Auth": lambda: (render_nav(False), auth_page.render_auth()),
    "Dashboard": lambda: (render_nav(True), dashboard_page.render_dashboard(), st.columns([1, 4])[0].button("Logout", on_click=lambda: logout_handler()))
}

def logout_handler():
    for key in list(st.session_state.keys()):
        if key not in ["logged_in"]:
            del st.session_state[key]
    st.session_state.logged_in = False
    st.query_params.clear()
    st.rerun()

# Select and run page (efficient—no full rerun)
selected_page = st.navigation(list(pages.keys()))
pages[selected_page]()

# Global footer (your exact)
st.markdown("""
<div class="custom-footer">
    <p>&copy; 2025 CrypticX. All rights reserved.</p>
    <div class="footer-links">
        <a href="#" class="footer-link">Privacy</a><a href="#" class="footer-link">Terms</a><a href="#" class="footer-link">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)
