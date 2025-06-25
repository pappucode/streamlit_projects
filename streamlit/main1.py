import streamlit as st

st.title("Coffee maker app")

if st.button("Make Coffee"):
    st.success("Your Coffee is being brewed")

add_ingredients = st.checkbox("Add Ingredients")
if add_ingredients:
    st.write("Ingredients added!!")

coffee_type = st.radio("Pick your coffee base: ", ["Milk", "Water", "Honey"])

st.write(f"Select coffee base is {coffee_type}")

flavour = st.selectbox("Choose flavour: ", ["Black Coffee", "Nescaffe", "Others coffee"])
st.write(f"Select coffee flavour is {flavour}")

sugar = st.slider("Sugar level (spoon)", 0, 10, 3)
st.write(f"Select Sugar level is {sugar}")

cups = st.number_input("How many cups", 1, 10, 1)
st.write(f"Total cups are {cups}")

name = st.text_input("Enter your name.")
if name:
    st.write(f"Welcome, {name} ! Your Coffee is on the way.")

dob = st.date_input("Select your date of birth!")
st.write(f"Your date of birth is {dob}")