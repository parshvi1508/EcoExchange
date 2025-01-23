import streamlit as st
import json
import pandas as pd
from datetime import datetime

def load_materials_data():
    """Load materials and vendor data from JSON file."""
    try:
        with open('materials.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        st.error("Materials database not found!")
        return {"materials": [], "vendors": []}

def browse_materials_page():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        
        .material-card {
            background-color: #CBE4DE;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            transition: transform 0.3s ease;
        }
        
        .material-card:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .sidebar-style {
            background-color: #2E4F4F;
            color: white;
        }
        
        .stButton>button {
            background-color: #0E8388;
            color: white;
            border: none;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        
        .stButton>button:hover {
            background-color: #2C3333;
        }
        </style>
    """, unsafe_allow_html=True)

    
    st.title("🌍 EcoExchange: Material Marketplace")
    
    
    data = load_materials_data()
    materials = data.get('materials', [])
    vendors = data.get('vendors', [])
    
    
    st.sidebar.header("🔍 Material Filters")
    
    
    categories = ["All", 
        "Organic Waste",
        "Paper & Cardboard",
        "Glass",
        "Plastics",
        "Textiles",
        "Metal Scraps",
        "Wood Waste",
        "Others"
    ]
    selected_category = st.sidebar.selectbox("Select Category", categories)
    
    max_price = max([mat['price_per_unit'] for mat in materials], default=0.0)
    min_price = st.sidebar.slider(
        "Minimum Price per Unit", 
        min_value=0.0, 
        max_value=max_price,
        value=0.0,
        step=0.1
    )
    
    search_term = st.sidebar.text_input("Search Materials")
    
    sort_options = [
        "Newest Listings", 
        "Price: Low to High", 
        "Price: High to Low", 
        "Quantity: Most Available"
    ]
    sort_by = st.sidebar.selectbox("Sort By", sort_options)
    
    filtered_materials = [
        mat for mat in materials 
        if (selected_category == "All" or mat['category'] == selected_category) and
           mat['price_per_unit'] >= min_price and
           (search_term.lower() in mat['title'].lower() or 
            search_term.lower() in mat['description'].lower())
    ]
    
    if sort_by == "Newest Listings":
        filtered_materials.sort(key=lambda x: x.get('listing_date', ''), reverse=True)
    elif sort_by == "Price: Low to High":
        filtered_materials.sort(key=lambda x: x['price_per_unit'])
    elif sort_by == "Price: High to Low":
        filtered_materials.sort(key=lambda x: x['price_per_unit'], reverse=True)
    elif sort_by == "Quantity: Most Available":
        filtered_materials.sort(key=lambda x: x['quantity_available'], reverse=True)
    
    st.write(f"**{len(filtered_materials)} Materials Found**")
    
    if not filtered_materials:
        st.warning("No materials found matching your filters.")
    
    for material in filtered_materials:
        vendor = next((v for v in vendors if v['id'] == material['vendor_id']), None)
        
        st.markdown(f"""
        <div class="material-card">
            <div class="row">
                <div class="col-9">
                    <h3 style="color: #2E4F4F;">{material['title']}</h3>
                    <p><strong>Category:</strong> {material['category']}</p>
                    <p><strong>Price:</strong> ₹{material['price_per_unit']} per {material['unit']}</p>
                    <p><strong>Available Quantity:</strong> {material['quantity_available']} {material['unit']}</p>
                    <p><strong>Description:</strong> {material['description']}</p>
                </div>
                <div class="col-3">
                    {"" if not vendor else f"<p><strong>Vendor:</strong> {vendor['name']}<br><strong>Location:</strong> {vendor['location']}</p>"}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if vendor and st.button(f"Contact {vendor['name']}", key=f"contact_{material['id']}"):
                st.write(f"**Email:** {vendor['email']}")
                st.write(f"**Phone:** {vendor['phone']}")
        
        st.markdown("---")

if __name__ == "__main__":
    browse_materials_page()