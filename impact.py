import streamlit as st
import pandas as pd

def impact_page():
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
        
        .impact-card {
            background-color: #CBE4DE;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
            text-align: center;
        }
        
        .impact-number {
            font-size: 2.5em;
            color: #0E8388;
            font-weight: bold;
            margin: 10px 0;
        }
        
        .testimonial-card {
            background-color: #CBE4DE;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
        }
        
        .normal-text {
            font-size: 1.1em;
            color: white;
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">Our Environmental Impact</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="impact-card">
                <div class="impact-number">50,000+</div>
                <h4 style="color: #2E4F4F;">Tons of Waste Recycled</h4>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="impact-card">
                <div class="impact-number">₹20M+</div>
                <h4 style="color: #2E4F4F;">Value Generated</h4>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class="impact-card">
                <div class="impact-number">5,000+</div>
                <h4 style="color: #2E4F4F;">Active Users</h4>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="section-header">Environmental Benefits</h3>', unsafe_allow_html=True)
    
    benefits = {
        "Carbon Footprint Reduction": "Prevented 75,000 metric tons of CO2 emissions through material recycling",
        "Landfill Diversion": "Diverted 50,000+ tons of waste from landfills",
        "Water Conservation": "Saved 100 million+ liters of water through material reuse",
        "Energy Savings": "Reduced energy consumption by 30% compared to virgin material production"
    }
    
    for title, description in benefits.items():
        st.markdown(f"""
            <div class="testimonial-card">
                <h4 style="color: #2E4F4F;">{title}</h4>
                <p style="color: #2C3333;">{description}</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="section-header">Success Stories</h3>', unsafe_allow_html=True)
    
    testimonials = [
        {
            "name": "Raj Kumar",
            "role": "Material Supplier",
            "text": "EcoExchange helped me transform my waste management business. Now I have a reliable platform to connect with buyers."
        },
        {
            "name": "Priya Singh",
            "role": "Sustainability Manager",
            "text": "We've reduced our raw material costs by 40% while meeting our sustainability goals through EcoExchange."
        }
    ]
    
    for testimonial in testimonials:
        st.markdown(f"""
            <div class="testimonial-card">
                <p style="color: #2C3333; font-style: italic;">"{testimonial['text']}"</p>
                <h4 style="color: #2E4F4F; margin-bottom: 0;">{testimonial['name']}</h4>
                <p style="color: #2C3333; margin-top: 5px;">{testimonial['role']}</p>
            </div>
        """, unsafe_allow_html=True)

