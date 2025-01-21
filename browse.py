import streamlit as st
import pandas as pd

def browse_materials_page():
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
        
        .material-card {
            background-color: #CBE4DE;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            transition: transform 0.2s;
        }
        
        .material-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        .normal-text {
            font-size: 1.1em;
            color: white;
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">Browse Available Materials</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        search_term = st.text_input("Search Materials", placeholder="Enter keywords...")
    with col2:
        category = st.selectbox("Category", [
            "All Categories",
            "Organic Waste",
            "Paper & Cardboard",
            "Glass",
            "Plastics",
            "Textiles",
            "Metal Scraps",
            "Wood Waste",
            "Others"
        ])
    with col3:
        sort_by = st.selectbox("Sort By", ["Newest", "Price: Low to High", "Price: High to Low"])
    
    materials_data = {
        "title": ["Coconut Shells", "Used Cardboard Boxes", "Glass Bottles (Clear)", "Cotton Textile Waste"],
        "category": ["Organic Waste", "Paper & Cardboard", "Glass", "Textiles"],
        "price_per_unit": [2.50, 0.75, 0.30, 1.20],
        "unit": ["kg", "kg", "piece", "kg"],
        "quantity_available": [500, 1000, 750, 300],
        "location": ["Mumbai", "Delhi", "Bangalore", "Chennai"],
        "seller_rating": [4.5, 4.2, 4.8, 4.0]
    }
    df = pd.DataFrame(materials_data)
    
    cols = st.columns(3)
    for idx, row in df.iterrows():
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="material-card">
                    <h3 style="color: #2E4F4F;">{row['title']}</h3>
                    <p style="color: #2C3333;">Category: {row['category']}</p>
                    <p style="color: #2C3333;">Price: ₹{row['price_per_unit']} per {row['unit']}</p>
                    <p style="color: #2C3333;">Available: {row['quantity_available']} {row['unit']}</p>
                    <p style="color: #2C3333;">Location: {row['location']}</p>
                    <p style="color: #2C3333;">Seller Rating: {'⭐' * int(row['seller_rating'])}</p>
                </div>
            """, unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.button(f"Contact Seller {idx}", key=f"contact_{idx}")
            with col2:
                st.button(f"View Details {idx}", key=f"details_{idx}")

