import streamlit as st

st.title("Coffee Taste poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Vote for Cappuccino")
    st.markdown(
        """
        <img src="https://images.pexels.com/photos/32672392/pexels-photo-32672392.jpeg" 
             width="200" height="150">
        """,
        unsafe_allow_html=True
    )
    vote1 = st.button("Cappuccino")

with col2:
    st.header("vote for Americano")
    st.markdown(
        """
        <img src="https://images.pexels.com/photos/32658788/pexels-photo-32658788.jpeg"
            width="200" height="150">
        """,
        unsafe_allow_html=True
    )
    vote2 = st.button("Americano")

if vote1:
    st.success("Thanks for voting Cappuccino")

elif vote2:
    st.success("Thanks for voting Americano")

name = st.sidebar.text_input("Enter your name.")
coffee = st.sidebar.selectbox("Select your favourite coffee recipe: ", ["Cappuccino", "Latte", "Americano"])
st.sidebar.write(f"Welcome {name} your favourite {coffee} is getting ready.")

with st.expander("Show coffee making instructions"):
    st.write("""
            1. Hot water
            2. Coffee mixing 
            3. Good quality milk
            """)
    
st.markdown("### Welcome to coffee app.")
st.markdown('>Blockquote')