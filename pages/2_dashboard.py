import streamlit as st
from utils import get_dashboard_stats

def render_dashboard():
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    
    if st.session_state.current_page != "dashboard":  # Fallback
        st.session_state.current_page = "dashboard"
    
    # Cached stats (perf boost)
    stats = get_dashboard_stats()
    plan_badge = f" | Plan: {st.session_state.selected_plan}" if st.session_state.selected_plan else ""
    
    st.markdown(f"""
    <div class="dashboard-section">
        <h1 class="dashboard-welcome">Welcome back, {st.session_state.user_name}!</h1>
        <p class="dashboard-subtitle">Your AI study dashboard{plan_badge}</p>
        <div class="dashboard-stats">
            <div class="dashboard-stat"><div class="dashboard-stat-number">{stats['questions_answered']}</div><div class="dashboard-stat-label">Questions Answered This Week</div></div>
            <div class="dashboard-stat"><div class="dashboard-stat-number">{stats['quiz_average']}</div><div class="dashboard-stat-label">Quiz Average</div></div>
            <div class="dashboard-stat"><div class="dashboard-stat-number">{stats['active_courses']}</div><div class="dashboard-stat-label">Active Courses</div></div>
            <div class="dashboard-stat"><div class="dashboard-stat-number">{stats['study_time']}</div><div class="dashboard-stat-label">Study Time Today</div></div>
        </div>
        <div style="text-align: center; margin-top: 2rem;">
            <h3>Ask your AI study buddy:</h3>
            {st.chat_input("e.g., Explain quantum physics simply")}
        </div>
        <button class="hero-cta" onclick="window.location.reload()">Refresh Progress</button>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
