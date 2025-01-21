import streamlit as st

def login_signup_page():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        
        .section-header {
            background-color: black;
            color: #2C3333;
            font-size: 1.8em;
            font-weight: 600;
            margin-top: 1em;
            text-align: left;
        }
        
        .auth-container {
            background-color: #CBE4DE;
            padding: 2em;
            border-radius: 10px;
            margin: 2em 0;
            max-width: 500px;
        }
        
        .tab-container {
            margin-bottom: 2em;
        }
        
        .stButton button {
            background-color: #0E8388;
            color: white;
            font-weight: bold;
            width: 100%;
            padding: 0.5em;
            border-radius: 5px;
            border: none;
            margin-top: 1em;
        }
        
        .stButton button:hover {
            background-color: #2E4F4F;
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
                st.markdown('<h3 style="color: #2E4F4F;">Welcome Back!</h3>', unsafe_allow_html=True)
                
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                
                remember_me = st.checkbox("Remember me")
                
                if st.form_submit_button("Login"):
                    st.success("Successfully logged in!")
                
                st.markdown("""
                    <div style="text-align: center; margin-top: 1em;">
                        <a href="#" style="color: #0E8388;">Forgot Password?</a>
                    </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with tab2:
            st.markdown('<div class="auth-container">', unsafe_allow_html=True)
            with st.form("signup_form"):
                st.markdown('<h3 style="color: #2E4F4F;">Create Account</h3>', unsafe_allow_html=True)
                
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

