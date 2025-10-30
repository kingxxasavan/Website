import streamlit as st
import hashlib
import pandas as pd
from typing import Dict, Any

@st.cache_data(ttl=3600)  # Cache for 1 hour; refresh if stats change
def get_dashboard_stats() -> Dict[str, Any]:
    """Mock cached stats—replace with real API/DB query."""
    return {
        "questions_answered": 42,
        "quiz_average": "87%",
        "active_courses": 5,
        "study_time": "2h 30m"
    }

@st.cache_resource
def get_user_data(username: str) -> Dict[str, Any]:
    """Cache user-specific resources (e.g., plan, progress)."""
    # Mock—replace with DB fetch
    return {"plan": "Pro", "name": username}  # Use st.session_state if needed

def hash_password(password: str) -> str:
    """Secure hashing for auth."""
    return hashlib.sha256(password.encode()).hexdigest()

# Mock users (production: load from DB)
USERS = {
    "test@example.com": {"password": hash_password("password123"), "name": "Test User"}
    # Add more
}
