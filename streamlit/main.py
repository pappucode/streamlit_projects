import streamlit as st

st.title("Hello coffee app")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app.")
st.write("Choose you favourite variety of coffee.")

coffee = st.selectbox("Select your favourite coffee recipe: ", ["Cappuccino", "Latte", "Americano", "Mocha"])

st.write(f"You choose {coffee} ! Excellent choise !!")

st.success("Your Coffee has been brewed.")