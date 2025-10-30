import streamlit as st
from utils import USERS, hash_password

def render_auth():
    st.markdown('<div class="content-wrapper"><div class="auth-container"><div class="auth-box">', unsafe_allow_html=True)
    
    # Back button (your exact)
    if st.button("← Back to Home"):
        st.query_params["page"] = "home"
        st.session_state.selected_plan = None
        st.rerun()
    
    # Plan badge (your exact)
    if st.session_state.selected_plan:
        st.markdown(f'<div class="welcome-badge" style="margin-bottom: 1.5rem;">Selected Plan: {st.session_state.selected_plan}</div>', unsafe_allow_html=True)
    
    # Toggle mode (your exact logic)
    if st.session_state.auth_mode == "login":
        st.markdown('<div class="auth-header"><h1 class="auth-title">Welcome Back</h1><p class="auth-subtitle">Sign in to access your dashboard</p></div>', unsafe_allow_html=True)
        email = st.text_input("Email", key="login_email", placeholder="your@email.com")
        password = st.text_input("Password", type="password", key="login_password", placeholder="Enter your password")
        if st.button("Sign In", key="login_submit"):
            if email and password and email in USERS and USERS[email]["password"] == hash_password(password):
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.session_state.user_name = USERS[email]["name"]
                st.query_params["page"] = "dashboard"
                st.success("Welcome back!")
                st.rerun()
            else:
                st.error("⚠ Invalid credentials")
        if st.button("Don't have an account? Create one", key="toggle_signup"):
            st.session_state.auth_mode = "signup"
            st.rerun()
    else:
        st.markdown('<div class="auth-header"><h1 class="auth-title">Create Account</h1><p class="auth-subtitle">Join and start your AI learning journey</p></div>', unsafe_allow_html=True)
        name = st.text_input("Full Name", key="signup_name", placeholder="Enter your name")
        email = st.text_input("Email", key="signup_email", placeholder="your@email.com")
        password = st.text_input("Password", type="password", key="signup_password", placeholder="Create a password")
        if st.button("Create Account", key="signup_submit"):
            if name and email and password:
                # Mock signup—add to USERS in production
                USERS[email] = {"password": hash_password(password), "name": name}
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.session_state.user_name = name
                st.query_params["page"] = "dashboard"
                st.success("Account created!")
                st.rerun()
            else:
                st.error("⚠ Please fill all fields")
        if st.button("Already have an account? Sign In", key="toggle_login"):
            st.session_state.auth_mode = "login"
            st.rerun()
    
    st.markdown('</div></div></div>', unsafe_allow_html=True)
