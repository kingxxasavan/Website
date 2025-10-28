import streamlit as st
from datetime import datetime, timedelta
import streamlit.components.v1 as components  # For any embedded HTML if needed

# Custom CSS (mirrors the HTML styling)
def load_custom_css():
    custom_css = """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    /* Header */
    .header {
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        padding: 1rem 2rem !important;
        background: rgba(0, 0, 0, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        z-index: 1000 !important;
    }
    .logo {
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #6366f1, #a855f7) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }
    .header-right {
        display: flex !important;
        align-items: center !important;
        gap: 1rem !important;
    }
    .profile-icon, .settings {
        width: 40px !important;
        height: 40px !important;
        border-radius: 50% !important;
        background: linear-gradient(135deg, #6366f1, #a855f7) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        font-size: 1.2rem !important;
        transition: transform 0.2s ease !important;
        border: none !important;
        color: white !important;
    }
    .profile-icon:hover, .settings:hover {
        transform: scale(1.05) !important;
        background: linear-gradient(135deg, #a855f7, #6366f1) !important;
    }
    /* Main Container */
    .main-container {
        display: flex !important;
        margin-top: 80px !important;
        min-height: 100vh !important;
    }
    .left-panel {
        flex: 1 !important;
        padding: 2rem !important;
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        gap: 2rem !important;
        max-width: 60% !important;
    }
    .card {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 20px !important;
        padding: 2rem !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    .card:hover {
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.3) !important;
    }
    .glow-circle {
        width: 60px !important;
        height: 60px !important;
        border-radius: 50% !important;
        background: linear-gradient(135deg, #6366f1, #a855f7) !important;
        margin: 1rem auto !important;
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.5) !important;
        animation: pulse 2s infinite !important;
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.8; }
    }
    .title {
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        margin-bottom: 1rem !important;
        background: linear-gradient(135deg, #ffffff, #e5e7eb) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }
    .subtitle {
        font-size: 0.9rem !important;
        color: #d1d5db !important;
        line-height: 1.5 !important;
        margin-bottom: 1rem !important;
    }
    .metric {
        display: flex !important;
        align-items: center !important;
        gap: 0.5rem !important;
        font-size: 1.2rem !important;
        font-weight: 500 !important;
        color: #10b981 !important;
        margin: 0.5rem 0 !important;
    }
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1, #a855f7) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        border-radius: 10px !important;
        cursor: pointer !important;
        font-weight: 500 !important;
        transition: transform 0.2s ease !important;
        margin: 0.5rem 0 !important;
        width: 100% !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 15px rgba(99, 102, 241, 0.4) !important;
    }
    .btn-secondary {
        background: transparent !important;
        border: 1px solid #6366f1 !important;
        color: #6366f1 !important;
    }
    .btn-secondary:hover {
        background: #6366f1 !important;
        color: white !important;
    }
    /* Right Panel */
    .right-panel {
        width: 400px !important;
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
        border-left: 1px solid rgba(255, 255, 255, 0.1) !important;
        padding: 2rem !important;
        display: flex !important;
        flex-direction: column !important;
    }
    .new-chat-section {
        margin-bottom: 2rem !important;
    }
    .new-chat-btn {
        background: linear-gradient(135deg, #10b981, #059669) !important;
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        padding: 1rem !important;
        border-radius: 15px !important;
    }
    .new-chat-btn:hover {
        transform: scale(1.02) !important;
        box-shadow: 0 5px 15px rgba(16, 185, 129, 0.4) !important;
    }
    .panel-title {
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        margin-bottom: 1rem !important;
        color: #f3f4f6 !important;
    }
    /* Calendar (customize if using streamlit-calendar) */
    .calendar {
        background: rgba(0, 0, 0, 0.2) !important;
        border-radius: 10px !important;
        padding: 1rem !important;
        margin-bottom: 1.5rem !important;
    }
    .css-1d391kg {  /* Sidebar-like for reminders/dates */
        background: rgba(0, 0, 0, 0.2) !important;
        border-radius: 10px !important;
        padding: 1rem !important;
    }
    .reminder-item, .date-item {
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        padding: 0.5rem 0 !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    .date-item {
        background: rgba(16, 185, 129, 0.2) !important;
        border-radius: 8px !important;
        margin-bottom: 0.5rem !important;
        padding: 0.75rem !important;
    }
    /* Responsive */
    @media (max-width: 1024px) {
        .main-container { flex-direction: column !important; }
        .left-panel { max-width: 100% !important; grid-template-columns: 1fr !important; }
        .right-panel { width: 100% !important; border-left: none !important; border-top: 1px solid rgba(255, 255, 255, 0.1) !important; }
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Load CSS
load_custom_css()

# Session state for reminders/dates (persistent)
if "reminders" not in st.session_state:
    st.session_state.reminders = ["Review Q3 Report", "Team Sync Call", "Update Blockchain Docs"]
if "work_dates" not in st.session_state:
    st.session_state.work_dates = [
        {"event": "Project Deadline", "date": "Nov 5, 2025"},
        {"event": "Client Meeting", "date": "Nov 10, 2025"},
        {"event": "Code Review", "date": "Nov 15, 2025"}
    ]

# Header
with st.container():
    col1, col2 = st.columns([1, 3])  # Spacer for centering
    with col1:
        st.markdown('<div class="logo">∧ BEST AI</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="header-right"><button class="settings">⚙️ Settings</button><div class="profile-icon">👤</div></div>', unsafe_allow_html=True)

# Settings/Profile Modals (using expanders for simplicity)
with st.expander("⚙️ Settings", expanded=False):
    st.write("Account settings: Theme, Notifications, API Keys.")
    if st.button("Save Changes"):
        st.success("Settings updated!")
with st.expander("👤 Profile", expanded=False):
    st.write("Your profile: Edit name, email, subscription.")
    if st.button("Logout"):
        st.warning("Logged out!")

# Main Layout
col_left, col_right = st.columns([3, 1])  # 60/40 split

with col_left:
    st.markdown('<div class="left-panel">', unsafe_allow_html=True)
    
    # Card 1: Go Build Your App
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="glow-circle"></div>', unsafe_allow_html=True)
        st.markdown('<div class="title">Go Build Your App</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Open UI store • Open Code store</div>', unsafe_allow_html=True)
        if st.button("Build Now", key="build_now", help="Launch Builder"):
            st.switch_page("pages/2_Builder.py")  # Link to your builder page
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Card 2: Exponentially Scalable
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="metric">250K TPS</div>', unsafe_allow_html=True)
        st.markdown('<div class="title">Exponentially Scalable</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Modular architecture with capacity for growth</div>', unsafe_allow_html=True)
        st.markdown('<div class="metric">1.98s Latency</div>', unsafe_allow_html=True)
        if st.button("Learn More", key="learn_more"):
            st.info("Scalable with Gemini integration!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Card 3: Be Part of the Hyper Economy
    with col_b:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="title">Be Part of the Hyper Economy</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Enter your email to get started</div>', unsafe_allow_html=True)
        email = st.text_input("your@email.com", key="email_input")
        if st.button("Enter", key="enter_email"):
            st.success(f"Welcome, {email}! Check your inbox.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Card 4: Empty Your Mind
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="glow-circle" style="background: linear-gradient(135deg, #10b981, #059669);"></div>', unsafe_allow_html=True)
        st.markdown('<div class="title">Empty Your Mind</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">Be formless, like water. Use 20% less effort with our tools</div>', unsafe_allow_html=True)
        if st.button("Start Flow", key="start_flow"):
            st.balloons()  # Fun animation; link to quiz/summary
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="right-panel">', unsafe_allow_html=True)
    
    # New Chat Section
    st.markdown('<div class="new-chat-section">', unsafe_allow_html=True)
    if st.button("+ New Chat", key="new_chat", help="Start a new study session"):
        st.session_state.mode = "general"  # Reset to your unified handler
        st.switch_page("pages/3_Chat.py")  # Link to chat page
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Productivity Panel
    st.markdown('<div class="productivity-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Productivity Hub</div>', unsafe_allow_html=True)
    
    # Calendar (Native Streamlit date range for simplicity; upgrade to streamlit-calendar for grid)
    st.markdown('<div class="calendar">', unsafe_allow_html=True)
    today = datetime(2025, 10, 28)  # Current date
    selected_date = st.date_input("Select Date", value=today, key="calendar_date")
    st.write(f"Events on {selected_date}: None scheduled.")  # Integrate with your DB/API
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Reminders
    st.markdown('<div class="css-1d391kg">', unsafe_allow_html=True)  # Reuse sidebar class
    st.markdown('<div class="panel-title">Reminders</div>', unsafe_allow_html=True)
    for i, reminder in enumerate(st.session_state.reminders):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(reminder)
        with col2:
            st.button("•", key=f"pending_{i}")  # Status toggle
        with col3:
            if st.button("✕", key=f"delete_{i}"):
                del st.session_state.reminders[i]
                st.rerun()
    new_reminder = st.text_input("Add Reminder")
    if st.button("Add") and new_reminder:
        st.session_state.reminders.append(new_reminder)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Work Dates
    st.markdown('<div class="css-1d391kg">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Upcoming Work Dates</div>', unsafe_allow_html=True)
    for date_item in st.session_state.work_dates:
        st.markdown(f'<div class="date-item"><span>{date_item["event"]}</span><span>{date_item["date"]}</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer (Optional)
st.markdown("---")
st.markdown("*Powered by BEST AI & Gemini*")
