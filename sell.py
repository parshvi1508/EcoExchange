import streamlit as st
import json
import os
from datetime import datetime
import uuid

def load_materials_data():
    """Load existing materials data from JSON file."""
    if not os.path.exists('materials.json'):
        return {"vendors": [], "materials": []}
    
    with open('materials.json', 'r') as file:
        return json.load(file)

def save_materials_data(data):
    """Save updated materials data to JSON file."""
    with open('materials.json', 'w') as file:
        json.dump(data, file, indent=4)

def generate_unique_id(data_list):
    """Generate a unique ID for new materials or vendors."""
    existing_ids = set(item['id'] for item in data_list)
    new_id = 0
    while new_id in existing_ids:
        new_id += 1
    return new_id

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
        
        description = st.text_area(
            "Describe your material in detail",
            placeholder="Include details about quality, source, potential uses, etc.",
            height=150
        )
        
        uploaded_files = st.file_uploader(
            "Upload up to 5 images of your material",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True
        )
        
        col1, col2 = st.columns(2)
        with col1:
            contact_name = st.text_input("Contact Name")
            contact_email = st.text_input("Email")
        with col2:
            contact_phone = st.text_input("Phone Number")
            preferred_contact = st.selectbox("Preferred Contact Method", ["Email", "Phone", "Both"])
        
        terms_accepted = st.checkbox("I confirm that the information provided is accurate and I have the right to sell these materials")
        
        submit_button = st.form_submit_button("List Material")
        
        if submit_button:
            if not all([material_title, category, quantity, price_per_unit, location, contact_name, contact_email, contact_phone]):
                st.error("Please fill in all required fields.")
                return
            
            if not terms_accepted:
                st.error("Please accept the terms and conditions to list your material.")
                return
            
            
            data = load_materials_data()
            
            
            material_id = generate_unique_id(data['materials'])
            vendor_id = generate_unique_id(data['vendors'])
            
            
            new_vendor = {
                "id": vendor_id,
                "name": contact_name,
                "contact_name": contact_name,
                "email": contact_email,
                "phone": contact_phone,
                "location": location,
                "specialization": category
            }
            data['vendors'].append(new_vendor)
            
            
            new_material = {
                "id": material_id,
                "vendor_id": vendor_id,
                "title": material_title,
                "category": category,
                "price_per_unit": price_per_unit,
                "unit": unit,
                "quantity_available": quantity,
                "description": description
            }
            data['materials'].append(new_material)
            
            save_materials_data(data)
            
            st.success("Your material has been listed successfully!")
            st.info(f"Your material ID is {material_id}. You can use this to track your listing.")
    
    st.markdown('</div>', unsafe_allow_html=True)