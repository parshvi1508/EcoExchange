import streamlit as st

def login_signup_page():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        
        .section-header {
            background-color: black;
            color: linear-gradient(45deg, var(--eco-green), var(--deep-teal));
            font-size: 1.8em;
            font-weight: 600;
            margin-top: 1em;
            text-align: left;
        }
        
        .auth-container {
            background-color: black;
            padding: 2em;
            border-radius: 10px;
            margin: 2em 0;
            max-width: 500px;
            color: linear-gradient(45deg, var(--eco-green), var(--deep-teal));
        }
        
        .tab-container {
            margin-bottom: 2em;
        }
         div[data-testid="stHorizontalBlock"] > div:first-child {
        background-color: #black;
        border-radius: 8px;
        padding: 0 ;
        border-radius: 8px;
        margin-bottom: 2em;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
    font-family: 'Space Grotesk', sans-serif;
    color: var(--forest-green);
}

.stTextInput > div > div > input,
.stSelectbox > div > div > div {
    
    padding: 10px 20px;
    transition: all 0.3s ease;
}

.stTextInput > div > div > input:focus,
.stSelectbox > div > div > div:focus {
    border-color: var(--eco-green);
    box-shadow: 0 0 0 3px rgba(46, 204, 113, 0.2);
}


    .stTabs [data-baseweb="tab-list"] {
    background: linear-gradient(90deg, var(--eco-green), var(--deep-teal));
    border-radius: 50px;
    padding: 10px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}

.stTabs [data-baseweb="tab"] {
    color: white;
    transition: all 0.3s ease;
    border-radius: 40px;
}

.stTabs [data-baseweb="tab"]:hover {
    background-color: rgba(255,255,255,0.2);
    transform: scale(1.05);
}
        
        .stButton > button {
    background: linear-gradient(45deg, var(--eco-green), var(--deep-teal));
    border: none;
    color: white;
    padding: 12px 25px;
    border-radius: 50px;
    transition: all 0.3s ease;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stButton > button:hover {
    background: linear-gradient(225deg, var(--eco-green), var(--deep-teal));
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}
        
        .normal-text {
            font-size: 1.1em;
            color: white;
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        tab1, tab2 = st.tabs(["Login", "Sign Up"])
        
        with tab1:
            st.markdown('<div class="auth-container">', unsafe_allow_html=True)
            with st.form("login_form"):
                st.markdown('<h3 style="color: linear-gradient(45deg, var(--eco-green), var(--deep-teal));">Welcome Back!</h3>', unsafe_allow_html=True)
                
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                
                remember_me = st.checkbox("Remember me")
                
                if st.form_submit_button("Login"):
                    st.success("Successfully logged in!")
                
                st.markdown("""
                    <div style="text-align: center; margin-top: 1em;">
                        <a href="#" style="color: linear-gradient(45deg, var(--eco-green), var(--deep-teal));">Forgot Password?</a>
                    </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with tab2:
            st.markdown('<div class="auth-container">', unsafe_allow_html=True)
            with st.form("signup_form"):
                st.markdown('<h3 style="color: linear-gradient(45deg, var(--eco-green), var(--deep-teal));">Create Account</h3>', unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    first_name = st.text_input("First Name")
                with col2:
                    last_name = st.text_input("Last Name")
                
                email = st.text_input("Email")
                phone = st.text_input("Phone Number")
                password = st.text_input("Password", type="password")
                confirm_password = st.text_input("Confirm Password", type="password")
                
                user_type = st.selectbox("I want to:", ["Buy Materials", "Sell Materials", "Both"])
                
                terms = st.checkbox("I agree to the Terms and Conditions")
                
                if st.form_submit_button("Create Account"):
                    if terms:
                        st.success("Account created successfully!")
                    else:
                        st.error("Please accept the Terms and Conditions")
                
            st.markdown('</div>', unsafe_allow_html=True)

