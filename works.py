import streamlit as st

def how_it_works_page():
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
        
        .process-card {
            background: white;
    border-radius: 15px;
    box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    transition: transform 0.4s ease;
    overflow: hidden;
    position: relative;
        }
        
        .process-card:hover {
           transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        }
        
        .step-number {
            background-color: #0E8388;
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
        }
        .process-card::before {
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
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-header">How EcoExchange Works</h2>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="normal-text">
        EcoExchange makes it easy to buy and sell recyclable materials. Follow these simple steps to get started.
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="section-header">For Sellers</h3>', unsafe_allow_html=True)
    
    seller_steps = [
        {
            "title": "Create Your Account",
            "description": "Sign up for free and verify your email address to start selling materials."
        },
        {
            "title": "List Your Materials",
            "description": "Upload photos, add descriptions, set prices, and specify quantities for your materials."
        },
        {
            "title": "Connect with Buyers",
            "description": "Receive inquiries from interested buyers and negotiate terms directly."
        },
        {
            "title": "Complete the Sale",
            "description": "Arrange delivery or pickup and receive secure payment through our platform."
        }
    ]
    
    for idx, step in enumerate(seller_steps, 1):
        st.markdown(f"""
            <div class="process-card">
                <div class="step-number">{idx}</div>
                <h4 style="color: #2E4F4F;">{step['title']}</h4>
                <p style="color: #2C3333;">{step['description']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="section-header">For Buyers</h3>', unsafe_allow_html=True)
    
    buyer_steps = [
        {
            "title": "Browse Materials",
            "description": "Search our marketplace for available materials filtered by category, location, and price."
        },
        {
            "title": "Contact Sellers",
            "description": "Reach out to sellers directly through our secure messaging system."
        },
        {
            "title": "Verify and Purchase",
            "description": "Inspect materials, agree on terms, and complete secure payment through the platform."
        },
        {
            "title": "Leave Feedback",
            "description": "Rate your experience and help build trust in our community."
        }
    ]
    
    for idx, step in enumerate(buyer_steps, 1):
        st.markdown(f"""
            <div class="process-card">
                <div class="step-number">{idx}</div>
                <h4 style="color: #2E4F4F;">{step['title']}</h4>
                <p style="color: #2C3333;">{step['description']}</p>
            </div>
        """, unsafe_allow_html=True)

