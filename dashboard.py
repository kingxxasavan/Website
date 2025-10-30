# dashboard.py
# Run with: streamlit run dashboard.py
# Requires Google Generative AI: pip install google-generativeai
# Set your API key in st.secrets or env var.

import streamlit as st
import google.generativeai as genai
from datetime import datetime

# Configure Gemini - replace with your API key
genai.configure(api_key=st.secrets.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE"))
model = genai.GenerativeModel('gemini-1.5-flash')  # Using 1.5 Flash; update if 2.5 available

# Custom CSS for transparent glass green dashboard
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
        color: white;
    }
    .sidebar {
        background: rgba(0, 255, 127, 0.1);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(0, 255, 127, 0.2);
    }
    .chat-container {
        background: rgba(0, 255, 127, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        height: 70vh;
        overflow-y: auto;
    }
    .chat-message {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
    .user-message {
        background: rgba(0, 255, 127, 0.2);
        text-align: right;
    }
    .ai-message {
        background: rgba(255, 255, 255, 0.05);
    }
    .input-area {
        position: fixed;
        bottom: 20px;
        left: 20px;
        right: 20px;
        background: rgba(0, 255, 127, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 25px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Check authentication
if 'authenticated' not in st.session_state:
    st.switch_page('home.py')

# Sidebar for chat management
with st.sidebar:
    st.markdown("<h2 style='color: #00ff7f;'>Chat Hub</h2>", unsafe_allow_html=True)
    
    # Create new chat
    if st.button("New Chat", key="new_chat"):
        if 'current_chat' not in st.session_state:
            st.session_state.current_chat = "New Chat"
        else:
            st.session_state.current_chat = f"Chat {len(st.session_state.get('chats', [])) + 1}"
        st.session_state.messages = []
    
    # Search chats
    search_query = st.text_input("Search Chats")
    
    # Previous chats - store in session state as list of dicts
    if 'chats' not in st.session_state:
        st.session_state.chats = []
    if 'current_chat' not in st.session_state:
        st.session_state.current_chat = "Welcome Chat"
        st.session_state.messages = [{"role": "ai", "content": "Hello! I'm your AI assistant powered by Gemini. How can I help?"}]
        st.session_state.chats.append({"id": len(st.session_state.chats), "title": st.session_state.current_chat, "timestamp": datetime.now().isoformat()})
    
    # Display and select previous chats
    filtered_chats = [chat for chat in st.session_state.chats if search_query.lower() in chat['title'].lower()] if search_query else st.session_state.chats
    for chat in filtered_chats:
        if st.button(chat['title'], key=f"chat_{chat['id']}"):
            st.session_state.current_chat = chat['title']
            # Load messages - in full impl, store per chat; here simplified to current
            st.session_state.messages = []  # Placeholder; expand to load history
    
    # Save current chat on change
    if st.button("Save Chat"):
        if st.session_state.current_chat not in [c['title'] for c in st.session_state.chats]:
            st.session_state.chats.append({"id": len(st.session_state.chats), "title": st.session_state.current_chat, "timestamp": datetime.now().isoformat()})

# Main chat area
st.title(f"Chat: {st.session_state.current_chat}")
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.generate_content(prompt, stream=True)
            full_response = ""
            for chunk in response:
                full_response += chunk.text
                st.write(chunk.text, end='')
            st.session_state.messages.append({"role": "assistant", "content": full_response})

# Note: For fixed input, use the CSS positioned input-area, but st.chat_input works well.
# Expand chats storage for full multi-chat support by using a dict of lists for messages per chat.
# Streaming is used for dynamic feel.
