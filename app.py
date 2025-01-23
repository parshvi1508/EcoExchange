import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
from about import about_page
from browse import browse_materials_page
from sell import sell_materials_page
from works import how_it_works_page
from impact import impact_page
from login import login_signup_page

st.set_page_config(
        page_title="EcoExchange | Home",
        page_icon="♻️",
        layout="wide"
    )
def main():
    
    initialize_session_state()
    

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600&family=Inter:wght@300;400;500;600&display=swap');

:root {
    --eco-green: #2ecc71;
    --forest-green: #27ae60;
    --ocean-blue: #3498db;
    --deep-teal: #16a085;
    --soft-gray: #ecf0f1;
} 
    body {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1) 0%, rgba(39, 174, 96, 0.1) 100%);
    font-family: 'Inter', sans-serif;
}


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
        background: white;
    border-radius: 15px;
    box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    transition: all 0.4s ease;
    overflow: hidden;
    position: relative;
    }
    .card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
}

    .card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 5px;
    background: linear-gradient(90deg, var(--eco-green), var(--ocean-blue));
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
    </style>
""", unsafe_allow_html=True)

def initialize_session_state():
    if 'login_status' not in st.session_state:
        st.session_state.login_status = False
    if 'username' not in st.session_state:
        st.session_state.username = None

st.image("./logo.jpg", width=100)
st.markdown("""
    <div style="background: linear-gradient(135deg, var(--eco-green), var(--deep-teal)); 
                color: white; 
                padding: 50px; 
                border-radius: 20px; 
                text-align: center; 
                margin-bottom: 30px;">
        <h1 style="font-size: 3.5em; margin-bottom: 20px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            EcoExchange
        </h1>
        <p style="font-size: 1.2em; opacity: 0.9; max-width: 700px; margin: 0 auto;">Turning Waste Into Wealth. Driving Sustainability.
        </p>
    </div>
    """, unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Home", "About Us", "Browse Materials", "Sell Materials", "How It Works", "Impact", "Login/Signup"],
    icons=["house", "info-circle", "search", "shop", "gear", "graph-up", "person"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#eee","Color":"black"},
            "nav-link-selected": {"background-color": "#02ab21"},
            "options":{"color":"black"}
    }
)


def create_card(title, description, icon="♻️", impact_metric=None):
    st.markdown(f"""<div class="card">
    <div class="material-card" style="padding: 20px; margin-bottom: 20px;">
        <div style="display: flex; align-items: center; margin-bottom: 15px;">
            <div style="font-size: 2.5em; margin-right: 15px; color: var(--forest-green);">{icon}</div>
            <h3 style="margin: 0; color: var(--deep-teal);">{title}</h3>
        </div>
        <p style="color: #666; margin-bottom: 15px;">{description}</p>
        {f'<div style="background-color: var(--soft-gray);color:black; padding: 10px; border-radius: 10px;"><strong>Impact:</strong> {impact_metric}</div>' if impact_metric else ''}
    </div>
    </div>
    """, unsafe_allow_html=True)


if selected == "Home":
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown('<h2 class="section-header">Transform Waste into Treasure</h2>', unsafe_allow_html=True)
        st.markdown("""
        <div class="normal-text">
        Join our revolutionary marketplace where sustainability meets profitability. 
        EcoExchange connects conscious sellers and innovative buyers in a circular economy platform.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<h3 class="section-header">Featured Materials</h3>', unsafe_allow_html=True)
        
        
        create_card(
            "Coconut Shells", 
            "Transform agricultural waste into valuable resources.<br> Perfect for crafts, activated carbon production, and decorative items",
            "♻️",
            "Reduces landfill waste by 95%"
        )
        create_card(
            "Used Cardboard", 
            "Upcycle packaging into new sustainable products. <br> Ready for recycling into packaging or upcycled crafts",
            "📦",
            "Saves 17 trees per ton recycled"
        )
        create_card(
            "Glass Bottles & Jars", 
            "Close the loop on glass packaging. <br> Reusable for storage, crafts, or recycling.",
            "🍾",
            "90% energy savings in recycling"
        )
        create_card(
            "Coconut Husk/Fiber", 
            "Convert waste into new treasures. <br> Ideal for rope-making, mats, brushes, and gardening products.",
            "🍂",
            "Reduces coconut waste by 60%"
        )

    with col2:
        st.markdown('<h3 class="section-header">Platform Benefits</h3>', unsafe_allow_html=True)
        
        benefits = {
            "For Sellers": [
                "💰Monetize your waste materials",
                "🌍Connect with genuine buyers",
                "📈Contribute to sustainability"
            ],
            "For Buyers": [
                "🔧Access affordable raw materials",
                "♻️Support sustainable practices",
                "💡Find unique resources for projects"
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
            if st.button(" Login", use_container_width=True):
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
        
elif selected == "About Us":
    about_page()
elif selected == "Browse Materials":
    browse_materials_page()
elif selected == "Sell Materials":
    sell_materials_page()
elif selected == "How It Works":
    how_it_works_page()
elif selected == "Impact":
    impact_page()
elif selected == "Login/Signup":
    login_signup_page()
    
st.markdown("""
            <div style="background: linear-gradient(135deg, var(--eco-green), var(--deep-teal)); 
                color: white; 
                padding: 50px; 
                border-radius: 20px; 
                text-align: center; 
                margin-bottom: 30px;">
        <h3 style="font-size: 1.5em; margin-bottom: 20px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            © 2025 EcoExchange.
        </h3>
        <p style="font-size: 0.9em; opacity: 0.9; max-width: 700px; margin: 0 auto;">Making sustainability profitable.</p>
    </div>
""", unsafe_allow_html=True)
if __name__ == "__main__":
    main()