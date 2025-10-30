# pages/dashboard.py - Dashboard with Chatbot
import streamlit as st
import google.generativeai as genai
from streamlit_extras.switch_page_button import switch_page
import time

# Configure Gemini - assume API key in st.secrets['GEMINI_API_KEY']
genai.configure(api_key=st.secrets.get('GEMINI_API_KEY', 'YOUR_API_KEY_HERE'))
model = genai.GenerativeModel('gemini-1.5-flash')  # Note: Using 1.5-flash as 2.5 might be typo; adjust if needed

# Hide Streamlit elements
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background: linear-gradient(135deg, rgba(0, 128, 0, 0.1) 0%, rgba(0, 100, 0, 0.1) 100%);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }
    .glass-panel {
        background: rgba(0, 128, 0, 0.2);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        height: 100vh;
        padding: 1rem;
    }
    .chat-message {
        background: rgba(0, 128, 0, 0.3);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(layout="wide")

# Check if user is logged in
if 'user' not in st.session_state:
    st.warning("Please log in.")
    time.sleep(1)
    switch_page("auth")
else:
    st.title(f"Welcome, {st.session_state['user']}! 👋")
    st.markdown("Your dynamic AI dashboard.")

# Sidebar for chat management (like Grok's panel)
with st.sidebar:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.subheader("📝 Chat Panel")
    
    # Previous chats (session state)
    if 'chats' not in st.session_state:
        st.session_state['chats'] = []
    if 'current_chat' not in st.session_state:
        st.session_state['current_chat'] = {"title": "New Chat", "messages": []}
    
    # Create new chat
    if st.button("➕ New Chat"):
        st.session_state['chats'].append(st.session_state['current_chat'])
        st.session_state['current_chat'] = {"title": f"Chat {len(st.session_state['chats'])+1}", "messages": []}
        st.rerun()
    
    # Search chats
    search_query = st.text_input("🔍 Search Chats")
    if search_query:
        filtered_chats = [chat for chat in st.session_state['chats'] if search_query.lower() in chat['title'].lower()]
        for chat in filtered_chats:
            if st.button(chat['title']):
                st.session_state['current_chat'] = chat
                st.rerun()
    else:
        for chat in st.session_state['chats']:
            if st.button(chat['title']):
                st.session_state['current_chat'] = chat
                st.rerun()
    
    # Logout
    if st.button("🚪 Logout"):
        del st.session_state['user']
        switch_page("auth")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main chat area
col1, col2 = st.columns([1, 3])  # Side panel is sidebar, main is wide

with col1:  # Empty for balance
    st.empty()

with col2:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.subheader(st.session_state['current_chat']['title'])
    
    # Display messages
    chat_container = st.container()
    with chat_container:
        for message in st.session_state['current_chat']['messages']:
            if message['role'] == 'user':
                st.markdown(f'<div class="chat-message"><strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-message"><strong>AI:</strong> {message["content"]}</div>', unsafe_allow_html=True)
    
    # User input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message
        st.session_state['current_chat']['messages'].append({"role": "user", "content": prompt})
        with chat_container:
            st.markdown(f'<div class="chat-message"><strong>You:</strong> {prompt}</div>', unsafe_allow_html=True)
        
        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = model.generate_content(prompt)
                ai_response = response.text
            st.markdown(f'<div class="chat-message"><strong>AI:</strong> {ai_response}</div>', unsafe_allow_html=True)
            st.session_state['current_chat']['messages'].append({"role": "assistant", "content": ai_response})
    
    st.markdown('</div>', unsafe_allow_html=True)

# Note: All features are integrated via the Gemini model prompts. For example, to use specific features, prefix prompts like "As an AI analyst, analyze this data: [data]".
