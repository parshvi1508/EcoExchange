import streamlit as st
import pandas as pd
import plotly.express as px

def about_page():
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

.highlight-text {
    color:linear-gradient(45deg, var(--eco-green), var(--deep-teal));
    }
.stButton > button:hover {
    background: linear-gradient(225deg, var(--eco-green), var(--deep-teal));
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}
    </style>
""", unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Our Mission</h2>', unsafe_allow_html=True)
    mission_col1, mission_col2 = st.columns([2, 1])
    with mission_col1:
        st.markdown("""
        <div class="normal-text">
            At EcoExchange, we're on a mission to revolutionize waste management through circular economy principles. 
            We believe that one person's waste is another's treasure, and we're here to make those connections happen.
            <br><br>
            Our platform serves as a bridge between those who have reusable materials and those who can transform them 
            into valuable products, promoting sustainability while creating economic opportunities.
        </div>
        """, unsafe_allow_html=True)
    
    with mission_col2:
        sustainability_data = pd.DataFrame({
        'Material': ['Paper', 'Plastic', 'Metal', 'Glass', 'Organic Waste'],
        'Recycling_Rate': [68, 9, 34, 26, 4.1],
        'Carbon_Saved_Tons': [1.2, 0.5, 1.8, 0.7, 0.3],
        'Economic_Value_Rupees': [5000, 2500, 7500, 3500, 1500]
    })
        fig_economic = px.pie(
            sustainability_data, 
            values='Economic_Value_Rupees', 
            names='Material', 
            title='Economic Value by Material'
        )
        st.plotly_chart(fig_economic)

    fig_recycling = px.bar(
            sustainability_data, 
            x='Material', 
            y='Recycling_Rate', 
            title='Recycling Rates by Material',
            labels={'Recycling_Rate': 'Recycling Rate (%)'}
        )
    st.plotly_chart(fig_recycling)
    st.markdown('<h2 class="section-header">About Us</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="normal-text">
        EcoExchange is a marketplace that connects sellers and buyers of reusable materials, 
        such as coconut shells, glass bottles, and used cardboard. Our platform is designed to 
        encourage sustainability by promoting the reuse and recycling of materials, turning waste 
        into valuable resources. Whether you are looking to sell waste materials or purchase affordable 
        raw materials for your projects, EcoExchange is here to facilitate a circular economy.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="section-header">Our Vision</h3>', unsafe_allow_html=True)
    st.markdown("""
    <div class="normal-text">
        At EcoExchange, our vision is to lead the way in sustainability by building a global community 
        that embraces waste as a valuable resource. We strive to provide a seamless platform where both 
        sellers and buyers can connect and contribute to a greener future.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="section-header">Why Choose Us?</h3>', unsafe_allow_html=True)
    st.markdown("""
    <div class="normal-text">
        - Sustainability Focused: We prioritize environmentally friendly practices by promoting the reuse of materials.<br>
        - Circular Economy: Our platform supports a sustainable and self-sufficient economy where materials have a second life.<br>
        - Innovative Solutions: EcoExchange connects buyers and sellers in an innovative way, reducing waste and promoting green solutions.
    </div>
    """, unsafe_allow_html=True)
about_page()