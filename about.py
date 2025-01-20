import streamlit as st

def about_page():
    # About page header
    st.markdown('<h1 class="main-header">EcoExchange</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Turning Waste Into Wealth. Driving Sustainability.</p>', unsafe_allow_html=True)
    
    # Mission Statement Section
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
        st.markdown("""
        <div class="card" style="text-align: center;">
            <h3 style="color: #2E4F4F;">Impact Statistics</h3>
            <p class="highlight-text" style="font-size: 2em;">5000+</p>
            <p>Active Users</p>
            <p class="highlight-text" style="font-size: 2em;">10000+</p>
            <p>Successful Trades</p>
            <p class="highlight-text" style="font-size: 2em;">50000+</p>
            <p>Kg of Waste Saved</p>
        </div>
        """, unsafe_allow_html=True)
    
    # About Us Content
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
    
    # Vision Section
    st.markdown('<h3 class="section-header">Our Vision</h3>', unsafe_allow_html=True)
    st.markdown("""
    <div class="normal-text">
        At EcoExchange, our vision is to lead the way in sustainability by building a global community 
        that embraces waste as a valuable resource. We strive to provide a seamless platform where both 
        sellers and buyers can connect and contribute to a greener future.
    </div>
    """, unsafe_allow_html=True)
    
    # Why Choose Us Section
    st.markdown('<h3 class="section-header">Why Choose Us?</h3>', unsafe_allow_html=True)
    st.markdown("""
    <div class="normal-text">
        - **Sustainability Focused:** We prioritize environmentally friendly practices by promoting the reuse of materials.<br>
        - **Circular Economy:** Our platform supports a sustainable and self-sufficient economy where materials have a second life.<br>
        - **Innovative Solutions:** EcoExchange connects buyers and sellers in an innovative way, reducing waste and promoting green solutions.
    </div>
    """, unsafe_allow_html=True)
about_page()