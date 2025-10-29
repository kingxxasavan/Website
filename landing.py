import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CrypticX - AI Study Tool",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0; margin: 0;}
    .main .block-container {max-width: 100%; padding: 0;}
    .stApp {margin: 0; padding: 0;}
    .stDeployButton {display:none;}
    .stDecoration {display:none;}
    section.main > div {padding: 0;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

landing_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {margin: 0; padding: 0; box-sizing: border-box;}
        body {font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #000; color: #fff; overflow-x: hidden; min-height: 100vh;}
        .bg-gradient {position: fixed; inset: 0; background: radial-gradient(ellipse at top right, rgba(88, 28, 135, 0.3) 0%, transparent 50%), radial-gradient(ellipse at bottom left, rgba(29, 78, 216, 0.3) 0%, transparent 50%), #000; z-index: 0;}
        .glow-orb {position: fixed; border-radius: 50%; filter: blur(100px); pointer-events: none; z-index: 1;}
        .orb1 {top: -10%; right: -5%; width: 600px; height: 600px; background: radial-gradient(circle, rgba(139, 92, 246, 0.4), transparent); animation: float1 20s ease-in-out infinite;}
        .orb2 {bottom: -10%; left: -5%; width: 700px; height: 700px; background: radial-gradient(circle, rgba(59, 130, 246, 0.4), transparent); animation: float2 25s ease-in-out infinite;}
        @keyframes float1 {0%, 100% {transform: translate(0, 0);} 50% {transform: translate(-100px, 100px);}}
        @keyframes float2 {0%, 100% {transform: translate(0, 0);} 50% {transform: translate(100px, -100px);}}
        
        nav {position: relative; z-index: 100; display: flex; justify-content: space-between; align-items: center; padding: 1.2rem 5rem; max-width: 1600px; margin: 1rem auto; background: rgba(20, 20, 20, 0.6); backdrop-filter: blur(20px); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 20px;}
        .logo {display: flex; align-items: center; gap: 0.5rem; font-size: 1.5rem; font-weight: 700; color: #fff; cursor: pointer;}
        .logo-icon {width: 35px; height: 35px; background: linear-gradient(135deg, #8b5cf6, #6366f1); border-radius: 8px; display: flex; align-items: center; justify-content: center;}
        .nav-links {display: flex; gap: 3rem; list-style: none;}
        .nav-links a {color: #a0a0a0; text-decoration: none; font-size: 1rem; transition: color 0.3s; cursor: pointer;}
        .nav-links a:hover {color: #fff;}
        .nav-buttons {display: flex; gap: 1rem;}
        .nav-btn {padding: 0.7rem 1.8rem; border-radius: 12px; border: 1px solid rgba(139, 92, 246, 0.5); background: transparent; color: #fff; font-weight: 500; cursor: pointer; transition: all 0.3s; font-size: 0.95rem;}
        .nav-btn:hover {background: rgba(139, 92, 246, 0.1); border-color: #8b5cf6;}
        .nav-btn.primary {background: linear-gradient(135deg, #8b5cf6, #6366f1); border: none;}
        .nav-btn.primary:hover {box-shadow: 0 10px 40px rgba(139, 92, 246, 0.5); transform: translateY(-2px);}
        
        .hero {position: relative; z-index: 10; max-width: 1600px; margin: 0 auto; padding: 3rem 5rem 4rem; display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;}
        .hero-content h1 {font-size: 3.5rem; line-height: 1.1; margin-bottom: 1.2rem; font-weight: 300; letter-spacing: -2px; color: #fff;}
        .hero-content p {font-size: 1.1rem; color: #a0a0a0; margin-bottom: 2rem; line-height: 1.7; max-width: 500px;}
        .email-form {display: flex; gap: 1rem; margin-bottom: 1rem;}
        .email-input {flex: 1; padding: 1.2rem 1.5rem; background: rgba(40, 40, 40, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 15px; color: #fff; font-size: 1rem; outline: none; transition: all 0.3s;}
        .email-input:focus {border-color: #8b5cf6; box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1);}
        .cta-btn {padding: 1.2rem 2.5rem; background: linear-gradient(135deg, #8b5cf6, #6366f1); border: none; border-radius: 15px; color: #fff; font-size: 1rem; font-weight: 600; cursor: pointer; transition: all 0.3s; white-space: nowrap;}
        .cta-btn:hover {box-shadow: 0 15px 50px rgba(139, 92, 246, 0.5); transform: translateY(-3px);}
        .hero-note {font-size: 0.9rem; color: #666;}
        
        .section {position: relative; z-index: 10; max-width: 1600px; margin: 4rem auto; padding: 0 5rem;}
        .section-header {text-align: center; margin-bottom: 3rem;}
        .section-title {font-size: 2.8rem; font-weight: 300; margin-bottom: 1rem;}
        .section-subtitle {font-size: 1.1rem; color: #a0a0a0;}
        
        .features-grid {display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;}
        .feature-card {background: rgba(20, 20, 20, 0.6); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 25px; padding: 3rem; transition: all 0.3s; backdrop-filter: blur(20px);}
        .feature-card:hover {border-color: rgba(139, 92, 246, 0.5); box-shadow: 0 20px 60px rgba(139, 92, 246, 0.2); transform: translateY(-10px);}
        .feature-icon {font-size: 3.5rem; margin-bottom: 1.5rem; filter: drop-shadow(0 0 20px rgba(139, 92, 246, 0.5));}
        .feature-card h3 {font-size: 1.6rem; margin-bottom: 1rem; font-weight: 400;}
        .feature-card p {color: #a0a0a0; line-height: 1.7; font-size: 1.05rem;}
        
        .info-grid {display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem; margin-top: 4rem;}
        .info-card {background: rgba(20, 20, 20, 0.6); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 25px; padding: 3rem; transition: all 0.3s; backdrop-filter: blur(20px);}
        .info-card:hover {border-color: rgba(139, 92, 246, 0.5); transform: translateY(-5px); box-shadow: 0 20px 60px rgba(139, 92, 246, 0.2);}
        .info-number {font-size: 4rem; font-weight: 900; background: linear-gradient(135deg, #8b5cf6, #6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 1rem; opacity: 0.3;}
        .info-card h3 {font-size: 1.8rem; margin-bottom: 1rem; font-weight: 400;}
        .info-card p {color: #a0a0a0; line-height: 1.8; font-size: 1.05rem;}
        
        .stats-container {display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; padding: 4rem; background: rgba(139, 92, 246, 0.05); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 30px; backdrop-filter: blur(20px);}
        .stat-card {text-align: center;}
        .stat-number {font-size: 3.5rem; font-weight: 900; background: linear-gradient(135deg, #8b5cf6, #6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem;}
        .stat-label {font-size: 1.1rem; color: #a0a0a0;}
        
        .price-btn {width: 100%; padding: 1rem; border-radius: 15px; border: 1px solid rgba(139, 92, 246, 0.5); background: transparent; color: #fff; font-weight: 600; cursor: pointer; transition: all 0.3s; margin-top: 2rem;}
        .price-btn:hover {box-shadow: 0 10px 30px rgba(139, 92, 246, 0.4); transform: translateY(-3px);}
        
        .page {display: none;}
        .page.active {display: block; animation: fadeIn 0.5s ease-in;}
        @keyframes fadeIn {from {opacity: 0; transform: translateY(20px);} to {opacity: 1; transform: translateY(0);}}
        
        /* Dashboard Specific Styles */
        .dashboard-container {display: flex; min-height: calc(100vh - 120px); position: relative; z-index: 10; max-width: 1800px; margin: 0 auto; padding: 2rem;}
        
        .sidebar {width: 300px; background: rgba(20, 20, 20, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 25px; padding: 2rem; backdrop-filter: blur(20px); margin-right: 2rem; height: fit-content; position: sticky; top: 2rem; animation: slideInLeft 0.6s ease-out;}
        
        @keyframes slideInLeft {from {opacity: 0; transform: translateX(-50px);} to {opacity: 1; transform: translateX(0);}}
        
        .sidebar-header {text-align: center; padding-bottom: 1.5rem; border-bottom: 1px solid rgba(139, 92, 246, 0.2); margin-bottom: 1.5rem;}
        .sidebar-header h3 {font-size: 1.4rem; font-weight: 400; margin-bottom: 0.5rem;}
        .user-status {font-size: 0.9rem; color: #8b5cf6; display: flex; align-items: center; justify-content: center; gap: 0.5rem;}
        .status-dot {width: 8px; height: 8px; background: #8b5cf6; border-radius: 50%; animation: pulse 2s ease-in-out infinite;}
        @keyframes pulse {0%, 100% {opacity: 1;} 50% {opacity: 0.5;}}
        
        .sidebar-menu {list-style: none;}
        .sidebar-menu li {margin-bottom: 0.5rem;}
        .sidebar-menu a {display: flex; align-items: center; gap: 1rem; padding: 1rem 1.2rem; color: #a0a0a0; text-decoration: none; border-radius: 12px; transition: all 0.3s; cursor: pointer;}
        .sidebar-menu a:hover {background: rgba(139, 92, 246, 0.1); color: #fff; transform: translateX(5px);}
        .sidebar-menu a.active {background: rgba(139, 92, 246, 0.2); color: #fff; border-left: 3px solid #8b5cf6;}
        .menu-icon {font-size: 1.3rem;}
        
        .logout-btn {width: 100%; padding: 1rem; margin-top: 2rem; border-radius: 12px; border: 1px solid rgba(220, 38, 38, 0.5); background: transparent; color: #dc2626; font-weight: 600; cursor: pointer; transition: all 0.3s;}
        .logout-btn:hover {background: rgba(220, 38, 38, 0.1); border-color: #dc2626;}
        
        .main-content {flex: 1; animation: fadeInUp 0.6s ease-out;}
        @keyframes fadeInUp {from {opacity: 0; transform: translateY(30px);} to {opacity: 1; transform: translateY(0);}}
        
        .welcome-card {background: rgba(20, 20, 20, 0.6); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 25px; padding: 4rem; text-align: center; backdrop-filter: blur(20px); margin-bottom: 2rem;}
        .welcome-card h1 {font-size: 3rem; font-weight: 300; margin-bottom: 1rem;}
        .welcome-card p {font-size: 1.2rem; color: #a0a0a0; margin-bottom: 2rem;}
        
        .chat-container {background: rgba(20, 20, 20, 0.6); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 25px; padding: 2rem; backdrop-filter: blur(20px); min-height: 500px; display: flex; flex-direction: column;}
        .chat-messages {flex: 1; overflow-y: auto; margin-bottom: 1.5rem; padding: 1rem;}
        .chat-input-container {display: flex; gap: 1rem;}
        .chat-input {flex: 1; padding: 1.2rem 1.5rem; background: rgba(40, 40, 40, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 15px; color: #fff; font-size: 1rem; outline: none; transition: all 0.3s;}
        .chat-input:focus {border-color: #8b5cf6; box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1);}
        .send-btn {padding: 1.2rem 2rem; background: linear-gradient(135deg, #8b5cf6, #6366f1); border: none; border-radius: 15px; color: #fff; font-weight: 600; cursor: pointer; transition: all 0.3s;}
        .send-btn:hover {box-shadow: 0 10px 30px rgba(139, 92, 246, 0.5); transform: translateY(-2px);}
        
        .quick-actions {display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 2rem;}
        .quick-action {background: rgba(20, 20, 20, 0.6); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 20px; padding: 2rem; text-align: center; cursor: pointer; transition: all 0.3s; backdrop-filter: blur(20px);}
        .quick-action:hover {border-color: rgba(139, 92, 246, 0.5); transform: translateY(-5px); box-shadow: 0 15px 40px rgba(139, 92, 246, 0.2);}
        .quick-action-icon {font-size: 2.5rem; margin-bottom: 1rem;}
        .quick-action h4 {font-size: 1.1rem; font-weight: 400;}
        
        footer {position: relative; z-index: 10; border-top: 1px solid rgba(139, 92, 246, 0.2); margin-top: 3rem; padding: 2rem 5rem; text-align: center; color: #666; background: rgba(20, 20, 20, 0.6); backdrop-filter: blur(20px);}
        
        @media (max-width: 1024px) {
            nav {padding: 1rem 2rem;}
            .nav-links {display: none;}
            .hero {grid-template-columns: 1fr; text-align: center; padding: 2rem;}
            .section {padding: 0 2rem;}
            .features-grid {grid-template-columns: 1fr;}
            .info-grid {grid-template-columns: 1fr;}
            .stats-container {grid-template-columns: repeat(2, 1fr);}
            .dashboard-container {flex-direction: column; padding: 1rem;}
            .sidebar {width: 100%; margin-right: 0; margin-bottom: 2rem; position: relative;}
            .quick-actions {grid-template-columns: 1fr;}
        }
    </style>
</head>
<body>
    <div class="bg-gradient"></div>
    <div class="glow-orb orb1"></div>
    <div class="glow-orb orb2"></div>
    
    <nav>
        <div class="logo" onclick="navigateToHome()">
            <div class="logo-icon">⚡</div>
            <span>CrypticX</span>
        </div>
        <ul class="nav-links">
            <li><a onclick="navigateToHome()">Home</a></li>
            <li><a onclick="showPage('features')">Features</a></li>
            <li><a onclick="showPage('pricing')">Pricing</a></li>
            <li><a onclick="showPage('contact')">Contact</a></li>
        </ul>
        <div class="nav-buttons" id="navButtons">
            <button class="nav-btn" onclick="showPage('signup')">Sign Up</button>
            <button class="nav-btn primary" onclick="showPage('login')">Login</button>
        </div>
    </nav>
    
    <!-- HOME PAGE -->
    <div id="home" class="page active">
        <section class="hero">
            <div class="hero-content">
                <h1>Welcome to CrypticX</h1>
                <p>The ultimate tool for school. Master complex concepts, ace your exams, and unlock your full academic potential with cutting-edge AI technology.</p>
                <form class="email-form" onsubmit="event.preventDefault(); showPage('signup');">
                    <input type="email" class="email-input" placeholder="Enter email" required>
                    <button type="submit" class="cta-btn">Get Started</button>
                </form>
                <p class="hero-note">Start your learning journey today</p>
            </div>
            <div style="text-align: center; font-size: 10rem;">🤖</div>
        </section>
        
        <section class="section">
            <div class="section-header">
                <h2 class="section-title">Why Choose CrypticX?</h2>
                <p class="section-subtitle">The ultimate AI study companion for modern students</p>
            </div>
            <div class="info-grid">
                <div class="info-card">
                    <div class="info-number">01</div>
                    <h3>Powered by Advanced AI</h3>
                    <p>Leveraging state-of-the-art artificial intelligence technology to provide accurate, instant, and personalized learning assistance.</p>
                </div>
                <div class="info-card">
                    <div class="info-number">02</div>
                    <h3>Save Time & Study Smarter</h3>
                    <p>Cut your study time in half with intelligent summaries, instant explanations, and automated quiz generation.</p>
                </div>
                <div class="info-card">
                    <div class="info-number">03</div>
                    <h3>Proven Results</h3>
                    <p>Join thousands of students who have improved their grades. Our users report 40% better retention and 35% improvement in test scores.</p>
                </div>
                <div class="info-card">
                    <div class="info-number">04</div>
                    <h3>24/7 Availability</h3>
                    <p>Study anytime, anywhere. CrypticX is always available to help you understand difficult concepts.</p>
                </div>
            </div>
        </section>
        
        <section class="section">
            <div class="stats-container">
                <div class="stat-card">
                    <div class="stat-number">50K+</div>
                    <div class="stat-label">Active Students</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">1M+</div>
                    <div class="stat-label">Questions Answered</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">95%</div>
                    <div class="stat-label">Satisfaction Rate</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">24/7</div>
                    <div class="stat-label">Available Support</div>
                </div>
            </div>
        </section>
    </div>
    
    <!-- DASHBOARD PAGE -->
    <div id="dashboard" class="page">
        <div class="dashboard-container">
            <aside class="sidebar">
                <div class="sidebar-header">
                    <h3 id="dashboardUserName">John Doe</h3>
                    <div class="user-status">
                        <span class="status-dot"></span>
                        <span>Online</span>
                    </div>
                </div>
                
                <ul class="sidebar-menu">
                    <li><a onclick="switchDashboardView('chat')" class="active">
                        <span class="menu-icon">💬</span>
                        <span>AI Chat</span>
                    </a></li>
                    <li><a onclick="switchDashboardView('explainer')">
                        <span class="menu-icon">🧠</span>
                        <span>AI Explainer</span>
                    </a></li>
                    <li><a onclick="switchDashboardView('summarizer')">
                        <span class="menu-icon">📄</span>
                        <span>PDF Summarizer</span>
                    </a></li>
                    <li><a onclick="switchDashboardView('quiz')">
                        <span class="menu-icon">❓</span>
                        <span>Quiz Generator</span>
                    </a></li>
                    <li><a onclick="switchDashboardView('flashcards')">
                        <span class="menu-icon">🎴</span>
                        <span>Flashcard Maker</span>
                    </a></li>
                    <li><a onclick="switchDashboardView('essay')">
                        <span class="menu-icon">✍️</span>
                        <span>Essay Helper</span>
                    </a></li>
                    <li><a onclick="switchDashboardView('planner')">
                        <span class="menu-icon">📅</span>
                        <span>Study Planner</span>
                    </a></li>
                    <li><a onclick="switchDashboardView('progress')">
                        <span class="menu-icon">📊</span>
                        <span>My Progress</span>
                    </a></li>
                </ul>
                
                <button class="logout-btn" onclick="logout()">🚪 Logout</button>
            </aside>
            
            <div class="main-content">
                <div class="welcome-card">
                    <h1 id="welcomeMessage">Welcome back, John! 👋</h1>
                    <p>How can I help you with your studies today?</p>
                </div>
                
                <div class="chat-container">
                    <div class="chat-messages" id="chatMessages">
                        <p style="text-align: center; color: #666; padding: 2rem;">Start a conversation by typing a message below...</p>
                    </div>
                    <div class="chat-input-container">
                        <input type="text" class="chat-input" placeholder="Ask me anything about your studies..." id="chatInput">
                        <button class="send-btn" onclick="sendMessage()">Send</button>
                    </div>
                </div>
                
                <div class="quick-actions">
                    <div class="quick-action" onclick="quickAction('Explain quantum physics')">
                        <div class="quick-action-icon">🔬</div>
                        <h4>Explain a Concept</h4>
                    </div>
                    <div class="quick-action" onclick="quickAction('Summarize my notes')">
                        <div class="quick-action-icon">📝</div>
                        <h4>Summarize Notes</h4>
                    </div>
                    <div class="quick-action" onclick="quickAction('Create a quiz')">
                        <div class="quick-action-icon">🎯</div>
                        <h4>Generate Quiz</h4>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- FEATURES PAGE -->
    <div id="features" class="page">
        <section class="section">
            <div class="section-header">
                <h2 class="section-title">Powerful Features</h2>
                <p class="section-subtitle">Everything you need to excel in your studies</p>
            </div>
            
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🧠</div>
                    <h3>AI Explainer</h3>
                    <p>Break down the most complex topics into simple, digestible explanations tailored to your learning style.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📄</div>
                    <h3>Smart Summarizer</h3>
                    <p>Upload PDFs or paste notes and get concise, accurate summaries in seconds. Save hours of study time.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">❓</div>
                    <h3>Quiz Generator</h3>
                    <p>Create custom quizzes and flashcards to test your knowledge and track your progress over time.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">📊</div>
                    <h3>Progress Tracking</h3>
                    <p>Monitor your learning journey with detailed analytics and insights into your study patterns.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎯</div>
                    <h3>Personalized Learning</h3>
                    <p>AI adapts to your learning pace and style, providing customized content recommendations.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>Lightning Fast</h3>
                    <p>Get instant responses powered by cutting-edge AI technology for seamless learning experience.</p>
                </div>
            </div>
        </section>
    </div>
    
    <!-- PRICING PAGE -->
    <div id="pricing" class="page">
        <section class="section">
            <div class="section-header">
                <h2 class="section-title">Simple Pricing</h2>
                <p class="section-subtitle">Choose the plan that fits your needs</p>
            </div>
            
            <div class="features-grid">
                <div class="feature-card">
                    <h3>Free</h3>
                    <div style="font-size: 3rem; margin: 1rem 0;">$0<span style="font-size: 1rem; color: #a0a0a0;">/month</span></div>
                    <p style="margin-bottom: 1.5rem;">• 10 AI explanations/day<br>• Basic summarization<br>• 5 quizzes/week<br>• Community support</p>
                    <button class="price-btn" onclick="showPage('signup')">Get Started</button>
                </div>
                
                <div class="feature-card" style="border-color: #8b5cf6; background: rgba(139, 92, 246, 0.05);">
                    <div style="color: #8b5cf6; font-weight: 600; margin-bottom: 1rem;">⭐ MOST POPULAR</div>
                    <h3>Pro</h3>
                    <div style="font-size: 3rem; margin: 1rem 0;">$9<span style="font-size: 1rem; color: #a0a0a0;">/month</span></div>
                    <p style="margin-bottom: 1.5rem;">• Unlimited AI explanations<br>• Advanced summarization<br>• Unlimited quizzes<br>• PDF upload (50MB)<br>• Priority support<br>• Progress tracking</p>
                    <button class="price-btn" style="background: linear-gradient(135deg, #8b5cf6, #6366f1);" onclick="showPage('signup')">Start Free Trial</button>
                </div>
                
                <div class="feature-card">
                    <h3>Ultimate</h3>
                    <div style="font-size: 3rem; margin: 1rem 0;">$19<span style="font-size: 1rem; color: #a0a0a0;">/month</span></div>
                    <p style="margin-bottom: 1.5rem;">• Everything in Pro<br>• Study group collaboration<br>• Custom AI training<br>• 1-on-1 tutoring<br>• Exam prep tools<br>• 24/7 VIP support</p>
                    <button class="price-btn" onclick="showPage('contact')">Contact Sales</button>
                </div>
            </div>
        </section>
    </div>
    
    <!-- CONTACT PAGE -->
    <div id="contact" class="page">
        <section class="section">
            <div style="max-width: 900px; margin: 0 auto; background: rgba(20, 20, 20, 0.6); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 30px; padding: 4rem; backdrop-filter: blur(20px);">
                <div class="section-header">
                    <h2 class="section-title">Get In Touch</h2>
                    <p class="section-subtitle">We'd love to hear from you</p>
                </div>
                <form onsubmit="event.preventDefault(); alert('Thank you! We will get back to you soon.');">
                    <input type="email" placeholder="Email" required style="width: 100%; padding: 1.2rem 1.5rem; background: rgba(40, 40, 40, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 15px; color: #fff; font-size: 1rem; margin-bottom: 1.5rem;">
                    <input type="text" placeholder="Subject" required style="width: 100%; padding: 1.2rem 1.5rem; background: rgba(40, 40, 40, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 15px; color: #fff; font-size: 1rem; margin-bottom: 1.5rem;">
                    <textarea placeholder="Message" required style="width: 100%; padding: 1.2rem 1.5rem; background: rgba(40, 40, 40, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 15px; color: #fff; font-size: 1rem; min-height: 150px; margin-bottom: 1.5rem; font-family: inherit;"></textarea>
                    <button type="submit" class="cta-btn" style="width: 100%;">Send Message</button>
                </form>
            </div>
        </section>
    </div>
    
    <!-- LOGIN PAGE -->
    <div id="login" class="page">
        <section class="section">
            <div style="max-width: 500px; margin: 0 auto; background: rgba(20, 20, 20, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 25px; padding: 3rem; backdrop-filter: blur(20px);">
                <div class="section-header">
                    <h2 class="section-title">Welcome Back</h2>
                    <p class="section-subtitle">Login to your CrypticX account</p>
                </div>
                <form onsubmit="handleLogin(event)">
                    <input type="email" id="loginEmail" placeholder="Email" required style="width: 100%; padding: 1.2rem 1.5rem; background: rgba(40, 40, 40, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 15px; color: #fff; font-size: 1rem; margin-bottom: 1.5rem;">
                    <input type="password" id="loginPassword" placeholder="Password" required style="width: 100%; padding: 1.2rem 1.5rem; background: rgba(40, 40, 40, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 15px; color: #fff; font-size: 1rem; margin-bottom: 1.5rem;">
                    <button type="submit" class="cta-btn" style="width: 100%;">Login</button>
                </form>
                <div style="text-align: center; margin-top: 1.5rem; color: #a0a0a0;">
                    Don't have an account? <a href="#" onclick="showPage('signup')" style="color: #8b5cf6; text-decoration: none; font-weight: 600;">Sign up</a>
                </div>
            </div>
        </section>
    </div>
    
    <!-- SIGNUP PAGE -->
    <div id="signup" class="page">
        <section class="section">
            <div style="max-width: 500px; margin: 0 auto; background: rgba(20, 20, 20, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 25px; padding: 3rem; backdrop-filter: blur(20px);">
                <div class="section-header">
                    <h2 class="section-title">Create Account</h2>
                    <p class="section-subtitle">Join CrypticX today</p>
                </div>
                <form onsubmit="handleSignup(event)">
                    <input type="text" id="signupName" placeholder="Full Name" required style="width: 100%; padding: 1.2rem 1.5rem; background: rgba(40, 40, 40, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 15px; color: #fff; font-size: 1rem; margin-bottom: 1.5rem;">
                    <input type="email" id="signupEmail" placeholder="Email" required style="width: 100%; padding: 1.2rem 1.5rem; background: rgba(40, 40, 40, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 15px; color: #fff; font-size: 1rem; margin-bottom: 1.5rem;">
                    <input type="password" id="signupPassword" placeholder="Password" required style="width: 100%; padding: 1.2rem 1.5rem; background: rgba(40, 40, 40, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 15px; color: #fff; font-size: 1rem; margin-bottom: 1.5rem;">
                    <input type="password" id="signupConfirmPassword" placeholder="Confirm Password" required style="width: 100%; padding: 1.2rem 1.5rem; background: rgba(40, 40, 40, 0.8); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 15px; color: #fff; font-size: 1rem; margin-bottom: 1.5rem;">
                    <button type="submit" class="cta-btn" style="width: 100%;">Create Account</button>
                </form>
                <div style="text-align: center; margin-top: 1.5rem; color: #a0a0a0;">
                    Already have an account? <a href="#" onclick="showPage('login')" style="color: #8b5cf6; text-decoration: none; font-weight: 600;">Login</a>
                </div>
            </div>
        </section>
    </div>
    
    <footer>
        <p>© 2025 CrypticX. Empowering students with AI. All rights reserved.</p>
    </footer>
    
    <script>
        // State management
        let isLoggedIn = false;
        let currentUser = null;
        
        // Navigation functions
        function showPage(pageName) {
            // Check if trying to access dashboard without login
            if (pageName === 'dashboard' && !isLoggedIn) {
                showPage('login');
                return;
            }
            
            document.querySelectorAll('.page').forEach(page => {
                page.classList.remove('active');
            });
            document.getElementById(pageName).classList.add('active');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
        
        function navigateToHome() {
            if (isLoggedIn) {
                // If logged in, show dashboard
                showPage('dashboard');
            } else {
                // If not logged in, show home
                showPage('home');
            }
        }
        
        // Authentication functions
        function handleLogin(event) {
            event.preventDefault();
            const email = document.getElementById('loginEmail').value;
            const name = email.split('@')[0]; // Extract name from email
            
            // Simulate login
            isLoggedIn = true;
            currentUser = {
                name: name.charAt(0).toUpperCase() + name.slice(1),
                email: email
            };
            
            updateNavForLoggedInUser();
            updateDashboardUser();
            showPage('dashboard');
        }
        
        function handleSignup(event) {
            event.preventDefault();
            const name = document.getElementById('signupName').value;
            const email = document.getElementById('signupEmail').value;
            const password = document.getElementById('signupPassword').value;
            const confirmPassword = document.getElementById('signupConfirmPassword').value;
            
            if (password !== confirmPassword) {
                alert('Passwords do not match!');
                return;
            }
            
            // Simulate signup
            isLoggedIn = true;
            currentUser = {
                name: name,
                email: email
            };
            
            updateNavForLoggedInUser();
            updateDashboardUser();
            showPage('dashboard');
        }
        
        function logout() {
            isLoggedIn = false;
            currentUser = null;
            updateNavForLoggedOutUser();
            showPage('home');
        }
        
        // Update UI based on login state
        function updateNavForLoggedInUser() {
            const navButtons = document.getElementById('navButtons');
            navButtons.innerHTML = `
                <button class="nav-btn primary" onclick="showPage('dashboard')">Dashboard</button>
                <button class="nav-btn" onclick="logout()">Logout</button>
            `;
        }
        
        function updateNavForLoggedOutUser() {
            const navButtons = document.getElementById('navButtons');
            navButtons.innerHTML = `
                <button class="nav-btn" onclick="showPage('signup')">Sign Up</button>
                <button class="nav-btn primary" onclick="showPage('login')">Login</button>
            `;
        }
        
        function updateDashboardUser() {
            if (currentUser) {
                document.getElementById('dashboardUserName').textContent = currentUser.name;
                document.getElementById('welcomeMessage').textContent = `Welcome back, ${currentUser.name}! 👋`;
            }
        }
        
        // Dashboard functions
        function switchDashboardView(view) {
            // Update active menu item
            document.querySelectorAll('.sidebar-menu a').forEach(link => {
                link.classList.remove('active');
            });
            event.target.closest('a').classList.add('active');
            
            // Show different content based on view
            const chatMessages = document.getElementById('chatMessages');
            chatMessages.innerHTML = `<p style="text-align: center; color: #666; padding: 2rem;">Loading ${view}...</p>`;
            
            setTimeout(() => {
                chatMessages.innerHTML = `<p style="text-align: center; color: #8b5cf6; padding: 2rem;">✨ ${view.toUpperCase()} feature coming soon! Start chatting to get help with your studies.</p>`;
            }, 500);
        }
        
        // Chat functions
        function sendMessage() {
            const input = document.getElementById('chatInput');
            const message = input.value.trim();
            
            if (message) {
                const chatMessages = document.getElementById('chatMessages');
                
                // Clear placeholder if exists
                if (chatMessages.querySelector('p[style*="text-align: center"]')) {
                    chatMessages.innerHTML = '';
                }
                
                // Add user message
                chatMessages.innerHTML += `
                    <div style="background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 15px; padding: 1rem; margin-bottom: 1rem; margin-left: 20%; animation: slideInRight 0.3s ease-out;">
                        <strong style="color: #8b5cf6;">You:</strong> ${message}
                    </div>
                `;
                
                input.value = '';
                
                // Simulate AI response
                setTimeout(() => {
                    chatMessages.innerHTML += `
                        <div style="background: rgba(20, 20, 20, 0.6); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 15px; padding: 1rem; margin-bottom: 1rem; margin-right: 20%; animation: slideInLeft 0.3s ease-out;">
                            <strong style="color: #6366f1;">CrypticX AI:</strong> I'm here to help you with your studies! This is a demo response. The full AI functionality will be available soon. 🚀
                        </div>
                    `;
                    chatMessages.scrollTop = chatMessages.scrollHeight;
                }, 1000);
                
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }
        }
        
        // Quick action function
        function quickAction(action) {
            const input = document.getElementById('chatInput');
            input.value = action;
            sendMessage();
        }
        
        // Allow Enter key to send message
        document.addEventListener('DOMContentLoaded', function() {
            const chatInput = document.getElementById('chatInput');
            if (chatInput) {
                chatInput.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        sendMessage();
                    }
                });
            }
        });
        
        // Add slide animations
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideInRight {
                from {
                    opacity: 0;
                    transform: translateX(50px);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }
            @keyframes slideInLeft {
                from {
                    opacity: 0;
                    transform: translateX(-50px);
                }
                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }
        `;
        document.head.appendChild(style);
    </script>
</body>
</html>
"""

components.html(landing_html, height=900, scrolling=True)
