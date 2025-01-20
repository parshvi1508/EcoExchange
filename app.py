import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
from about import about_page
st.set_page_config(
        page_title="EcoExchange | Home",
        page_icon="🌱",
        layout="wide"
    )
def main():
    
    initialize_session_state()

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    
    .main-header {
        font-family: 'Poppins', sans-serif;
        color: #2E4F4F;
        font-size: 3.5em;
        font-weight: 600;
        margin-bottom: 0;
        text-align: center;
    }
    
    .tagline {
        color: #0E8388;
        font-size: 1.5em;
        font-style: italic;
        text-align: center;
        margin-bottom: 2em;
    }
    
    .section-header {
        background-color: black;
        color: #2C3333;
        font-size: 1.8em;
        font-weight: 600;
        margin-top: 1em;
        text-align: left;
        
    }
    
    .card {
        background-color: #CBE4DE;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: left;
    }
    
    .normal-text {
        font-size: 1.1em;
        color: white;
        line-height: 1.6;
    }

    
    .stSelectbox > div > div {
        background-color: #2E4F4F;
        padding: 1em 0;
    }
    
    
    div[data-testid="stHorizontalBlock"] > div:first-child {
        background-color: #2E4F4F;
        border-radius: 8px;
        padding: 0 ;
        border-radius: 8px;
        margin-bottom: 2em;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .nav-link {
        color: #CBE4DE;
        text-decoration: none;
        padding: 0.8em 1.2em;
        margin: 0 0.5em;
        border-radius: 4px;
        transition: all 0.3s ease;
        font-family: 'Poppins', sans-serif;
        font-size: 1.1em;
    }
    
    .nav-link:hover {
        background-color: #0E8388 ;
        color: white ;
    }
    
    .nav-link.active {
        background-color: #0E8388 ;
        color: white ;
    }
    
    </style>
""", unsafe_allow_html=True)

def initialize_session_state():
    if 'login_status' not in st.session_state:
        st.session_state.login_status = False
    if 'username' not in st.session_state:
        st.session_state.username = None

st.image("./logo.jpg", width=100)
st.markdown('<h1 class="main-header">EcoExchange</h1>', unsafe_allow_html=True)
st.markdown('<p class="tagline">Turning Waste Into Wealth. Driving Sustainability.</p>', unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Home", "About Us", "Browse Materials", "Sell Materials", "How It Works", "Impact", "Login/Signup"],
    icons=["house", "info-circle", "search", "shop", "gear", "graph-up", "person"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0", "background-color": "#2E4F4F"},
        "icon": {"color": "#CBE4DE", "font-size": "1em"}, 
        "nav-link": {
            "font-family": "Poppins, sans-serif",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#0E8388",
            "color": "#CBE4DE",
        },
        "nav-link-selected": {"background-color": "#0E8388"},
    }
)

if selected == "Home":
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown('<h2 class="section-header">Transform Waste into Opportunity</h2>', unsafe_allow_html=True)
        st.markdown("""
        <div class="normal-text">
        Join our revolutionary marketplace where sustainability meets profitability. 
        EcoExchange connects conscious sellers and innovative buyers in a circular economy platform.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<h3 class="section-header">Featured Materials</h3>', unsafe_allow_html=True)
        
        materials = {
            "Coconut Shells": "Perfect for crafts, activated carbon production, and decorative items",
            "Coconut Husk/Fiber": "Ideal for rope-making, mats, brushes, and gardening products",
            "Used Cardboard": "Ready for recycling into packaging or upcycled crafts",
            "Glass Bottles & Jars": "Reusable for storage, crafts, or recycling"
        }
        
        for material, description in materials.items():
            st.markdown(f"""
            <div class="card">
                <h4 style="color: #2E4F4F;">{material}</h4>
                <p style="color: #2C3333;">{description}</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown('<h3 class="section-header">Platform Benefits</h3>', unsafe_allow_html=True)
        
        benefits = {
            "For Sellers": [
                "Monetize your waste materials",
                "Connect with genuine buyers",
                "Contribute to sustainability"
            ],
            "For Buyers": [
                "Access affordable raw materials",
                "Support sustainable practices",
                "Find unique resources for projects"
            ]
        }
        
        for group, points in benefits.items():
            st.markdown(f"""
            <div class="card">
                <h4 style="color: #2E4F4F;">{group}</h4>
                <ul style="color: #2C3333;">
                {''.join(f'<li>{point}</li>' for point in points)}
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align: center; margin-top: 2em;">
            <h3 class="section-header">Join the Circular Economy</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.button("Start Selling", use_container_width=True)
        with col2:
            st.button("Start Buying", use_container_width=True)
elif selected == "About Us":
    about_page()
st.markdown("""
<div style="text-align: center; margin-top: 3em; padding: 2em; background-color: #CBE4DE;">
    <p style="color: #2C3333;">© 2025 EcoExchange. Making sustainability profitable.</p>
</div>
""", unsafe_allow_html=True)
if __name__ == "__main__":
    main()