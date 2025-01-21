import streamlit as st
from datetime import datetime

def sell_materials_page():
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
        
        .normal-text {
            font-size: 1.1em;
            color: white;
            line-height: 1.6;
        }
        
        .form-container {
            background-color: #CBE4DE;
            padding: 2em;
            border-radius: 10px;
            margin: 1em 0;
        }
        
        .stButton button {
            background-color: #0E8388;
            color: white;
            font-weight: bold;
            padding: 0.5em 2em;
            border-radius: 5px;
            border: none;
            transition: background-color 0.3s;
        }
        
        .stButton button:hover {
            background-color: #2E4F4F;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">List Your Materials</h2>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="normal-text" style="margin-bottom: 2em;">
        Turn your waste into opportunity. List your materials on EcoExchange and connect with potential buyers.
        </div>
    """, unsafe_allow_html=True)
    
    # Material Information Form
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    with st.form("material_listing_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            material_title = st.text_input("Material Title", placeholder="e.g., Clean Plastic Bottles")
            category = st.selectbox("Category", [
                "Organic Waste",
                "Paper & Cardboard",
                "Glass",
                "Plastics",
                "Textiles",
                "Metal Scraps",
                "Wood Waste",
                "Others"
            ])
            quantity = st.number_input("Quantity Available", min_value=1)
            unit = st.selectbox("Unit", ["kg", "piece", "ton", "bundle"])
            
        with col2:
            price_per_unit = st.number_input("Price per Unit (₹)", min_value=0.0, step=0.1)
            location = st.text_input("Location", placeholder="City, State")
            condition = st.selectbox("Material Condition", [
                "New/Unused",
                "Like New",
                "Good",
                "Fair",
                "As Is"
            ])
        
        st.markdown('<h4 class="section-header">Material Description</h4>', unsafe_allow_html=True)
        description = st.text_area(
            "Describe your material in detail",
            placeholder="Include details about quality, source, potential uses, etc.",
            height=150
        )
        
        # Image upload
        st.markdown('<h4 class="section-header">Upload Images</h4>', unsafe_allow_html=True)
        uploaded_files = st.file_uploader(
            "Upload up to 5 images of your material",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True
        )
        
        # Contact Information
        st.markdown('<h4 class="section-header">Contact Information</h4>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            contact_name = st.text_input("Contact Name")
            contact_email = st.text_input("Email")
        with col2:
            contact_phone = st.text_input("Phone Number")
            preferred_contact = st.selectbox("Preferred Contact Method", ["Email", "Phone", "Both"])
        
        # Terms and conditions
        st.markdown("### Terms and Conditions")
        terms_accepted = st.checkbox("I confirm that the information provided is accurate and I have the right to sell these materials")
        
        submit_button = st.form_submit_button("List Material")
        
        if submit_button:
            if terms_accepted:
                st.success("Your material has been listed successfully! Buyers will be able to see your listing now.")
                st.info("You can manage your listings from your dashboard.")
            else:
                st.error("Please accept the terms and conditions to list your material.")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(
        page_title="EcoExchange | Sell Materials",
        page_icon="🌱",
        layout="wide"
    )
    sell_materials_page()