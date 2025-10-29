import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CrypticX - AI Study Tool",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

landing_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #000000;
            color: #ffffff;
            overflow-x: hidden;
        }
        
        /* Animated gradient background */
        .bg-gradient {
            position: fixed;
            inset: 0;
            background: radial-gradient(ellipse at top right, rgba(88, 28, 135, 0.3) 0%, transparent 50%),
                        radial-gradient(ellipse at bottom left, rgba(29, 78, 216, 0.3) 0%, transparent 50%),
                        #000000;
            z-index: 0;
        }
        
        /* Glowing orbs */
        .glow-orb {
            position: fixed;
            border-radius: 50%;
            filter: blur(100px);
            pointer-events: none;
            z-index: 1;
        }
        
        .orb1 {
            top: -10%;
            right: -5%;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(139, 92, 246, 0.4), transparent);
            animation: float1 20s ease-in-out infinite;
        }
        
        .orb2 {
            bottom: -10%;
            left: -5%;
            width: 700px;
            height: 700px;
            background: radial-gradient(circle, rgba(59, 130, 246, 0.4), transparent);
            animation: float2 25s ease-in-out infinite;
        }
        
        @keyframes float1 {
            0%, 100% { transform: translate(0, 0); }
            50% { transform: translate(-100px, 100px); }
        }
        
        @keyframes float2 {
            0%, 100% { transform: translate(0, 0); }
            50% { transform: translate(100px, -100px); }
        }
        
        /* Navigation */
        nav {
            position: relative;
            z-index: 100;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 5rem;
            max-width: 1600px;
            margin: 0 auto;
            background: rgba(20, 20, 20, 0.6);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 20px;
            margin-top: 2rem;
        }
        
        .logo {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 1.5rem;
            font-weight: 700;
            color: #ffffff;
        }
        
        .logo-icon {
            width: 35px;
            height: 35px;
            background: linear-gradient(135deg, #8b5cf6, #6366f1);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .nav-links {
            display: flex;
            gap: 3rem;
            list-style: none;
        }
        
        .nav-links a {
            color: #a0a0a0;
            text-decoration: none;
            font-size: 1rem;
            transition: color 0.3s;
        }
        
        .nav-links a:hover {
            color: #ffffff;
        }
        
        .nav-buttons {
            display: flex;
            gap: 1rem;
        }
        
        .nav-btn {
            padding: 0.7rem 1.8rem;
            border-radius: 12px;
            border: 1px solid rgba(139, 92, 246, 0.5);
            background: transparent;
            color: #ffffff;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 0.95rem;
        }
        
        .nav-btn:hover {
            background: rgba(139, 92, 246, 0.1);
            border-color: #8b5cf6;
        }
        
        .nav-btn.primary {
            background: linear-gradient(135deg, #8b5cf6, #6366f1);
            border: none;
        }
        
        .nav-btn.primary:hover {
            box-shadow: 0 10px 40px rgba(139, 92, 246, 0.5);
            transform: translateY(-2px);
        }
        
        /* Hero Section */
        .hero {
            position: relative;
            z-index: 10;
            max-width: 1600px;
            margin: 0 auto;
            padding: 8rem 5rem 6rem;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 6rem;
            align-items: center;
            min-height: 85vh;
        }
        
        .hero-content h1 {
            font-size: 4.5rem;
            line-height: 1.1;
            margin-bottom: 1.5rem;
            font-weight: 300;
            letter-spacing: -2px;
        }
        
        .hero-content p {
            font-size: 1.2rem;
            color: #a0a0a0;
            margin-bottom: 2.5rem;
            line-height: 1.7;
            max-width: 500px;
        }
        
        .email-form {
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
        }
        
        .email-input {
            flex: 1;
            padding: 1.2rem 1.5rem;
            background: rgba(40, 40, 40, 0.8);
            border: 1px solid rgba(139, 92, 246, 0.3);
            border-radius: 15px;
            color: #ffffff;
            font-size: 1rem;
            outline: none;
            transition: all 0.3s;
        }
        
        .email-input:focus {
            border-color: #8b5cf6;
            box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1);
        }
        
        .email-input::placeholder {
            color: #666;
        }
        
        .cta-btn {
            padding: 1.2rem 2.5rem;
            background: linear-gradient(135deg, #8b5cf6, #6366f1);
            border: none;
            border-radius: 15px;
            color: #ffffff;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            white-space: nowrap;
        }
        
        .cta-btn:hover {
            box-shadow: 0 15px 50px rgba(139, 92, 246, 0.5);
            transform: translateY(-3px);
        }
        
        .hero-note {
            font-size: 0.9rem;
            color: #666;
        }
        
        /* Hero Image - AI Robot */
        .hero-visual {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            perspective: 1000px;
        }
        
        .robot-container {
            position: relative;
            width: 500px;
            height: 600px;
            animation: floatRobot 6s ease-in-out infinite;
        }
        
        @keyframes floatRobot {
            0%, 100% { transform: translateY(0) rotateY(-5deg); }
            50% { transform: translateY(-30px) rotateY(5deg); }
        }
        
        /* Robot parts */
        .robot-head {
            position: absolute;
            top: 50px;
            left: 50%;
            transform: translateX(-50%);
            width: 200px;
            height: 200px;
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
            border-radius: 40% 40% 45% 45%;
            box-shadow: 0 20px 60px rgba(99, 102, 241, 0.6),
                        inset 0 -20px 40px rgba(0, 0, 0, 0.3);
            border: 3px solid rgba(139, 92, 246, 0.5);
        }
        
        .robot-eye {
            position: absolute;
            width: 70px;
            height: 70px;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: radial-gradient(circle, #8b5cf6 0%, #6366f1 50%, #1e3a8a 100%);
            border-radius: 50%;
            box-shadow: 0 0 40px #8b5cf6, 0 0 80px #6366f1, inset 0 0 20px rgba(255,255,255,0.3);
            animation: eyeGlow 2s ease-in-out infinite;
        }
        
        .eye-inner {
            position: absolute;
            width: 30px;
            height: 30px;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: radial-gradient(circle, #ffffff 0%, #a78bfa 100%);
            border-radius: 50%;
            box-shadow: 0 0 20px #ffffff;
        }
        
        @keyframes eyeGlow {
            0%, 100% { box-shadow: 0 0 40px #8b5cf6, 0 0 80px #6366f1, inset 0 0 20px rgba(255,255,255,0.3); }
            50% { box-shadow: 0 0 60px #8b5cf6, 0 0 120px #6366f1, inset 0 0 30px rgba(255,255,255,0.5); }
        }
        
        .robot-body {
            position: absolute;
            top: 230px;
            left: 50%;
            transform: translateX(-50%);
            width: 180px;
            height: 200px;
            background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
            border-radius: 30px;
            box-shadow: 0 20px 60px rgba(37, 99, 235, 0.5),
                        inset 0 -20px 40px rgba(0, 0, 0, 0.3);
            border: 3px solid rgba(139, 92, 246, 0.5);
        }
        
        .body-light {
            position: absolute;
            width: 40px;
            height: 40px;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: radial-gradient(circle, #6366f1, transparent);
            border-radius: 50%;
            animation: pulse 2s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 0.5; transform: translate(-50%, -50%) scale(1); }
            50% { opacity: 1; transform: translate(-50%, -50%) scale(1.2); }
        }
        
        .robot-arm {
            position: absolute;
            width: 80px;
            height: 25px;
            background: linear-gradient(90deg, #2563eb, #3b82f6);
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(37, 99, 235, 0.4);
            border: 2px solid rgba(139, 92, 246, 0.5);
        }
        
        .arm-left {
            top: 280px;
            left: 30px;
            transform: rotate(-20deg);
            animation: armMove 3s ease-in-out infinite;
        }
        
        .arm-right {
            top: 280px;
            right: 30px;
            transform: rotate(20deg);
            animation: armMove 3s ease-in-out infinite reverse;
        }
        
        @keyframes armMove {
            0%, 100% { transform: rotate(-20deg); }
            50% { transform: rotate(-10deg); }
        }
        
        .robot-leg {
            position: absolute;
            width: 40px;
            height: 120px;
            background: linear-gradient(180deg, #1e3a8a, #2563eb);
            border-radius: 20px;
            box-shadow: 0 15px 40px rgba(37, 99, 235, 0.4);
            border: 2px solid rgba(139, 92, 246, 0.5);
        }
        
        .leg-left {
            bottom: 50px;
            left: 170px;
        }
        
        .leg-right {
            bottom: 50px;
            right: 170px;
        }
        
        .robot-foot {
            position: absolute;
            bottom: -15px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 30px;
            background: linear-gradient(135deg, #2563eb, #3b82f6);
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(59, 130, 246, 0.6);
        }
        
        /* Floating particles */
        .particle {
            position: absolute;
            width: 4px;
            height: 4px;
            background: #8b5cf6;
            border-radius: 50%;
            box-shadow: 0 0 10px #8b5cf6;
            animation: particleFloat 8s ease-in-out infinite;
        }
        
        .particle:nth-child(1) { top: 100px; left: 50px; animation-delay: 0s; }
        .particle:nth-child(2) { top: 200px; right: 80px; animation-delay: 1s; }
        .particle:nth-child(3) { bottom: 150px; left: 100px; animation-delay: 2s; }
        .particle:nth-child(4) { top: 300px; right: 150px; animation-delay: 3s; }
        
        @keyframes particleFloat {
            0%, 100% { transform: translateY(0) scale(1); opacity: 0.3; }
            50% { transform: translateY(-50px) scale(1.5); opacity: 1; }
        }
        
        /* Features Section */
        .section {
            position: relative;
            z-index: 10;
            max-width: 1600px;
            margin: 8rem auto;
            padding: 0 5rem;
        }
        
        .section-header {
            text-align: center;
            margin-bottom: 5rem;
        }
        
        .section-title {
            font-size: 3.5rem;
            font-weight: 300;
            margin-bottom: 1rem;
        }
        
        .section-subtitle {
            font-size: 1.2rem;
            color: #a0a0a0;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
        }
        
        .feature-card {
            background: rgba(20, 20, 20, 0.6);
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 25px;
            padding: 3rem;
            transition: all 0.3s;
            backdrop-filter: blur(20px);
        }
        
        .feature-card:hover {
            border-color: rgba(139, 92, 246, 0.5);
            box-shadow: 0 20px 60px rgba(139, 92, 246, 0.2);
            transform: translateY(-10px);
        }
        
        .feature-icon {
            font-size: 3.5rem;
            margin-bottom: 1.5rem;
            filter: drop-shadow(0 0 20px rgba(139, 92, 246, 0.5));
        }
        
        .feature-card h3 {
            font-size: 1.6rem;
            margin-bottom: 1rem;
            font-weight: 400;
        }
        
        .feature-card p {
            color: #a0a0a0;
            line-height: 1.7;
            font-size: 1.05rem;
        }
        
        /* Pricing Section */
        .pricing-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            margin-top: 4rem;
        }
        
        .pricing-card {
            background: rgba(20, 20, 20, 0.6);
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 25px;
            padding: 3rem;
            text-align: center;
            transition: all 0.3s;
            backdrop-filter: blur(20px);
        }
        
        .pricing-card.featured {
            border-color: #8b5cf6;
            transform: scale(1.05);
            background: rgba(139, 92, 246, 0.05);
        }
        
        .pricing-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 60px rgba(139, 92, 246, 0.3);
        }
        
        .pricing-tag {
            display: inline-block;
            padding: 0.5rem 1.2rem;
            background: rgba(139, 92, 246, 0.2);
            border: 1px solid rgba(139, 92, 246, 0.5);
            border-radius: 20px;
            color: #8b5cf6;
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
        }
        
        .pricing-card h3 {
            font-size: 2rem;
            margin-bottom: 1rem;
            font-weight: 400;
        }
        
        .price {
            font-size: 3.5rem;
            font-weight: 300;
            margin-bottom: 2rem;
        }
        
        .price-period {
            font-size: 1rem;
            color: #a0a0a0;
        }
        
        .features-list {
            list-style: none;
            margin: 2rem 0;
            text-align: left;
        }
        
        .features-list li {
            padding: 0.8rem 0;
            color: #a0a0a0;
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }
        
        .features-list li::before {
            content: '✓';
            color: #8b5cf6;
            font-weight: bold;
            font-size: 1.2rem;
        }
        
        .price-btn {
            width: 100%;
            padding: 1rem;
            border-radius: 15px;
            border: 1px solid rgba(139, 92, 246, 0.5);
            background: transparent;
            color: #ffffff;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 2rem;
        }
        
        .featured .price-btn {
            background: linear-gradient(135deg, #8b5cf6, #6366f1);
            border: none;
        }
        
        .price-btn:hover {
            box-shadow: 0 10px 30px rgba(139, 92, 246, 0.4);
            transform: translateY(-3px);
        }
        
        /* Contact Section */
        .contact-container {
            max-width: 900px;
            margin: 8rem auto;
            padding: 4rem;
            background: rgba(20, 20, 20, 0.6);
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 30px;
            backdrop-filter: blur(20px);
        }
        
        .contact-form {
            display: grid;
            gap: 1.5rem;
        }
        
        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
        }
        
        .form-group {
            display: flex;
            flex-direction: column;
            gap: 0.7rem;
        }
        
        .form-group label {
            color: #a0a0a0;
            font-weight: 500;
            font-size: 0.95rem;
        }
        
        .form-group input,
        .form-group textarea {
            padding: 1.2rem 1.5rem;
            border-radius: 15px;
            border: 1px solid rgba(139, 92, 246, 0.3);
            background: rgba(40, 40, 40, 0.8);
            color: #ffffff;
            font-size: 1rem;
            transition: all 0.3s;
            font-family: inherit;
        }
        
        .form-group input:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #8b5cf6;
            box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1);
        }
        
        .form-group textarea {
            min-height: 150px;
            resize: vertical;
        }
        
        .submit-btn {
            padding: 1.3rem;
            border-radius: 15px;
            border: none;
            background: linear-gradient(135deg, #8b5cf6, #6366f1);
            color: #ffffff;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .submit-btn:hover {
            box-shadow: 0 15px 50px rgba(139, 92, 246, 0.5);
            transform: translateY(-3px);
        }
        
        /* Auth Forms (Login/Signup) */
        .auth-container {
            max-width: 500px;
            margin: 6rem auto;
            padding: 3rem;
            background: rgba(20, 20, 20, 0.8);
            border: 1px solid rgba(139, 92, 246, 0.3);
            border-radius: 25px;
            backdrop-filter: blur(20px);
        }
        
        .auth-header {
            text-align: center;
            margin-bottom: 2.5rem;
        }
        
        .auth-header h2 {
            font-size: 2.5rem;
            font-weight: 400;
            margin-bottom: 0.5rem;
        }
        
        .auth-header p {
            color: #a0a0a0;
        }
        
        .social-login {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin-bottom: 2rem;
        }
        
        .social-btn {
            padding: 1rem;
            border: 1px solid rgba(139, 92, 246, 0.3);
            background: rgba(40, 40, 40, 0.6);
            border-radius: 12px;
            color: #ffffff;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        }
        
        .social-btn:hover {
            background: rgba(139, 92, 246, 0.1);
            border-color: #8b5cf6;
        }
        
        .divider {
            text-align: center;
            margin: 2rem 0;
            color: #666;
            position: relative;
        }
        
        .divider::before,
        .divider::after {
            content: '';
            position: absolute;
            top: 50%;
            width: 40%;
            height: 1px;
            background: rgba(139, 92, 246, 0.2);
        }
        
        .divider::before { left: 0; }
        .divider::after { right: 0; }
        
        .auth-link {
            text-align: center;
            margin-top: 1.5rem;
            color: #a0a0a0;
        }
        
        .auth-link a {
            color: #8b5cf6;
            text-decoration: none;
            font-weight: 600;
        }
        
        .auth-link a:hover {
            text-decoration: underline;
        }
        
        /* Footer */
        footer {
            position: relative;
            z-index: 10;
            border-top: 1px solid rgba(139, 92, 246, 0.2);
            margin-top: 8rem;
            padding: 3rem 5rem;
            text-align: center;
            color: #666;
            background: rgba(20, 20, 20, 0.6);
            backdrop-filter: blur(20px);
        }
        
        /* Page Transitions */
        .page {
            display: none;
        }
        
        .page.active {
            display: block;
            animation: fadeIn 0.5s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @media (max-width: 1024px) {
            .hero {
                grid-template-columns: 1fr;
                text-align: center;
            }
            .hero-content p {
                max-width: 100%;
            }
            .robot-container {
                transform: scale(0.8);
            }
            .features-grid,
            .pricing-grid {
                grid-template-columns: 1fr;
            }
            nav {
                padding: 1rem 2rem;
            }
            .nav-links {
                display: none;
            }
            .form-row {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="bg-gradient"></div>
    <div class="glow-orb orb1"></div>
    <div class="glow-orb orb2"></div>
    
    <nav>
        <div class="logo">
            <div class="logo-icon">⚡</div>
            <span>CrypticX</span>
        </div>
        <ul class="nav-links">
            <li><a href="#" onclick="showPage('home')">Home</a></li>
            <li><a href="#" onclick="showPage('features')">Features</a></li>
            <li><a href="#" onclick="showPage('pricing')">Pricing</a></li>
            <li><a href="#" onclick="showPage('contact')">Contact</a></li>
        </ul>
        <div class="nav-buttons">
            <button class="nav-btn" onclick="showPage('login')">Sign Up</button>
            <button class="nav-btn primary" onclick="showPage('login')">Login</button>
        </div>
    </nav>
    
    <!-- HOME PAGE -->
    <div id="home" class="page active">
        <section class="hero">
            <div class="hero-content">
                <h1>Get ready for the new era of AI</h1>
                <p>Your all-in-one AI-powered study tool designed exclusively for students. Master complex concepts, ace your exams, and unlock your full academic potential with cutting-edge technology.</p>
                <form class="email-form" onsubmit="event.preventDefault(); alert('Thank you for your interest!');">
                    <input type="email" class="email-input" placeholder="Enter email" required>
                    <button type="submit" class="cta-btn">Get Started</button>
                </form>
                <p class="hero-note">Start your learning journey today</p>
            </div>
            
            <div class="hero-visual">
                <div class="robot-container">
                    <div class="robot-head">
                        <div class="robot-eye">
                            <div class="eye-inner"></div>
                        </div>
                    </div>
                    <div class="robot-body">
                        <div class="body-light"></div>
                    </div>
                    <div class="robot-arm arm-left"></div>
                    <div class="robot-arm arm-right"></div>
                    <div class="robot-leg leg-left">
                        <div class="robot-foot"></div>
                    </div>
                    <div class="robot-leg leg-right">
                        <div class="robot-foot"></div>
                    </div>
                    <div class="particle"></div>
                    <div class="particle"></div>
                    <div class="particle"></div>
                    <div class="particle"></div>
                </div>
            </div>
        </section>
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
            
            <div class="pricing-grid">
                <div class="pricing-card">
                    <div class="pricing-tag">BASIC</div>
                    <h3>Free</h3>
                    <div class="price">$0<span class="price-period">/month</span></div>
                    <ul class="features-list">
                        <li>10 AI explanations per day</li>
                        <li>Basic summarization</li>
                        <li>5 quizzes per week</li>
                        <li>Community support</li>
                        <li>Access to core features</li>
                    </ul>
                    <button class="price-btn">Get Started</button>
                </div>
                
                <div class="pricing-card featured">
                    <div class="pricing-tag">⭐ MOST POPULAR</div>
                    <h3>Pro</h3>
                    <div class="price">$9<span class="price-period">/month</span></div>
                    <ul class="features-list">
                        <li>Unlimited AI explanations</li>
                        <li>Advanced summarization</li>
                        <li>Unlimited quizzes</li>
                        <li>PDF upload (up to 50MB)</li>
                        <li>Priority support</li>
                        <li>Progress tracking</li>
                        <li>No ads</li>
                    </ul>
                    <button class="price-btn">Start Free Trial</button>
                </div>
                
                <div class="pricing-card">
                    <div class="pricing-tag">PREMIUM</div>
                    <h3>Ultimate</h3>
                    <div class="price">$19<span class="price-period">/month</span></div>
                    <ul class="features-list">
                        <li>Everything in Pro</li>
                        <li>Study group collaboration</li>
                        <li>Custom AI training</li>
                        <li>1-on-1 tutoring sessions</li>
                        <li>Exam preparation tools</li>
                        <li>24/7 VIP support</li>
                        <li>Unlimited storage</li>
                    </ul>
                    <button class="price-btn">Contact Sales</button>
                </div>
            </div>
        </section>
    </div>
    
    <!-- CONTACT PAGE -->
    <div id="contact" class="page">
        <div class="contact-container">
            <div class="section-header">
                <h2 class="section-title">Get In Touch</h2>
                <p class="section-subtitle">We'd love to hear from you</p>
            </div>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Thank you! We will get back to you soon.');">
                <div class="form-row">
                    <div class="form-group">
                        <label>First Name</label>
                        <input type="text" placeholder="John" required>
                    </div>
                    <div class="form-group">
                        <label>Last Name</label>
                        <input type="text" placeholder="Doe" required>
                    </div>
                </div>
                <div class="form-group">
                    <label>Email Address</label>
                    <input type="email" placeholder="john@example.com" required>
                </div>
                <div class="form-group">
                    <label>Subject</label>
                    <input type="text" placeholder="How can we help?" required>
                </div>
                <div class="form-group">
                    <label>Message</label>
                    <textarea placeholder="Tell us more about your inquiry..." required></textarea>
                </div>
                <button type="submit" class="submit-btn">Send Message</button>
            </form>
        </div>
    </div>
    
    <!-- LOGIN PAGE -->
    <div id="login" class="page">
        <div class="auth-container">
            <div class="auth-header">
                <h2>Welcome Back</h2>
                <p>Login to your CrypticX account</p>
            </div>
            
            <div class="social-login">
                <button class="social-btn">
                    <span>🔵</span> Google
                </button>
                <button class="social-btn">
                    <span>⚫</span> GitHub
                </button>
            </div>
            
            <div class="divider">or</div>
            
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Login functionality coming soon!');">
                <div class="form-group">
                    <label>Email Address</label>
                    <input type="email" placeholder="your@email.com" required>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" placeholder="••••••••" required>
                </div>
                <button type="submit" class="submit-btn">Login</button>
            </form>
            
            <div class="auth-link">
                Don't have an account? <a href="#" onclick="showPage('signup')">Sign up</a>
            </div>
        </div>
    </div>
    
    <!-- SIGNUP PAGE -->
    <div id="signup" class="page">
        <div class="auth-container">
            <div class="auth-header">
                <h2>Create Account</h2>
                <p>Join CrypticX today</p>
            </div>
            
            <div class="social-login">
                <button class="social-btn">
                    <span>🔵</span> Google
                </button>
                <button class="social-btn">
                    <span>⚫</span> GitHub
                </button>
            </div>
            
            <div class="divider">or</div>
            
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Signup functionality coming soon!');">
                <div class="form-group">
                    <label>Full Name</label>
                    <input type="text" placeholder="John Doe" required>
                </div>
                <div class="form-group">
                    <label>Email Address</label>
                    <input type="email" placeholder="your@email.com" required>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" placeholder="••••••••" required>
                </div>
                <div class="form-group">
                    <label>Confirm Password</label>
                    <input type="password" placeholder="••••••••" required>
                </div>
                <button type="submit" class="submit-btn">Create Account</button>
            </form>
            
            <div class="auth-link">
                Already have an account? <a href="#" onclick="showPage('login')">Login</a>
            </div>
        </div>
    </div>
    
    <footer>
        <p>© 2025 CrypticX. Empowering students with AI. All rights reserved.</p>
    </footer>
    
    <script>
        function showPage(pageName) {
            // Hide all pages
            document.querySelectorAll('.page').forEach(page => {
                page.classList.remove('active');
            });
            
            // Show selected page
            document.getElementById(pageName).classList.add('active');
            
            // Scroll to top
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    </script>
</body>
</html>
"""

components.html(landing_html, height=4500, scrolling=True)
