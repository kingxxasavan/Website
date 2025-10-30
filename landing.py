import streamlit as st
import streamlit.components.v1 as components
import re  # For email validation

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
    st.session_state.auth_mode = 'signup'
if 'user_name' not in st.session_state:
    st.session_state.user_name = None
if 'questions_answered' not in st.session_state:
    st.session_state.questions_answered = 42  # Mock dynamic stat

# Enhanced CSS (fixed dashboard flex-direction)
st.markdown("""
<style>
    /* [Your full CSS here - I'm truncating for brevity, but include the original with this fix] */
    /* ... (copy all your CSS from the original code) ... */
    
    /* Fixed: Dashboard flex-direction */
    .dashboard-section {
        min-height: calc(100vh - 80px);
        display: flex;
        flex-direction: column;  /* Fixed: Was '0' */
        justify-content: flex-start;
        align-items: center;
        text-align: center;
        padding: 4rem 2rem;
        position: relative;
    }
    
    /* New: Nav button styles for functionality */
    .nav-button {
        background: none;
        border: none;
        color: inherit;
        cursor: pointer;
        padding: 0.5rem;
        margin: 0 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Background elements (unchanged)
st.markdown("""
<div class="grid-background"></div>
<div class="glow-orb purple"></div>
<div class="glow-orb pink"></div>
""", unsafe_allow_html=True)

# Helper: Email validation
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Main logic (mostly unchanged, with fixes)
if not st.session_state.logged_in:
    if st.session_state.current_page == 'auth':
        # [Your auth code here, with added validation]
        # Example fix in signup/login:
        # In signup block:
        if st.button("Create Account", key="signup_btn", use_container_width=True):
            if name and email and password and is_valid_email(email):
                # ... (success logic)
            else:
                error_msg = "⚠ Please fill in all fields and use a valid email."
                if email and not is_valid_email(email):
                    error_msg += " Invalid email format."
                st.markdown(f'<div class="message-box message-error">{error_msg}</div>', unsafe_allow_html=True)
        # Similar for login...
        
    else:
        # Landing page nav (now with functional buttons)
        col_nav1, col_nav2 = st.columns([3, 1])
        with col_nav1:
            st.markdown('<div class="logo">⚡ CrypticX</div>', unsafe_allow_html=True)
        with col_nav2:
            if st.button("Pricing", key="nav_pricing"):
                st.session_state.current_page = 'pricing'  # Add 'pricing' page logic if needed
                st.rerun()
            if st.button("Sign Up", key="nav_signup"):
                st.session_state.current_page = 'auth'
                st.rerun()
        
        # [Rest of landing/pricing unchanged]
        
else:
    # Dashboard (fixed nav)
    col_logo, col_nav = st.columns([1, 4])
    with col_logo:
        st.markdown('<div class="logo">⚡ CrypticX</div>', unsafe_allow_html=True)
    with col_nav:
        col_links, col_user = st.columns([3, 1])
        with col_links:
            if st.button("Home", key="nav_home_logged"):
                st.session_state.current_page = 'home'
                st.rerun()
            if st.button("Pricing", key="nav_pricing_logged"):
                st.session_state.current_page = 'pricing'
                st.rerun()
            st.button("Dashboard", disabled=True)  # Active state
        with col_user:
            st.markdown(f'<span class="user-greeting">Hi, {st.session_state.user_name}!</span>', unsafe_allow_html=True)
            if st.button("Logout", key="nav_logout"):
                # Reset session
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
    
    # Dashboard content (with functional Explore More)
    # [Your dashboard markdown...]
    if st.button("Explore More", key="explore_more"):
        st.success("Redirecting to study tools...")  # Mock; add real redirect
    
    # Chat input handling
    user_input = st.chat_input("e.g., Explain calculus simply")
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        # Mock AI response (replace with real API call)
        ai_response = f"Based on your plan ({st.session_state.selected_plan}), here's a simple explanation: {user_input} involves rates of change. Imagine speed as the derivative of distance!"
        with st.chat_message("assistant"):
            st.write(ai_response)
        st.session_state.questions_answered += 1  # Update stat

# Footer (unchanged)

# For Enterprise Contact: Add a simple expander form
if st.session_state.selected_plan == 'Enterprise':
    with st.expander("Contact Us for Enterprise"):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.button("Send Inquiry"):
            st.success("Thanks! We'll reach out soon.")
