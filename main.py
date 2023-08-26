import streamlit as st
import pandas as pd
import time as ts
from datetime import time

table = pd.DataFrame({"Column1":[1,2,3,4,5,6,7], "column2":[11,12,13,14,15,16,17]})    

st.markdown("""
<style>

.css-6q9sum.ef3psqc3
{
    visibility:hidden;
}

.css-cio0dv.ea3mdgi1
{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

st.title("Hi I am Streamlit web app !!")
st.subheader("Hi I am your Sub-header")
st.header("I am Header")
st.text("Hi I am text function and programmers uses me inplace of paragraph tag.")
st.markdown("**Hello** *World*")
st.markdown("# Hello world")
st.markdown("### Hello world")
st.markdown("`Hello world`")
st.markdown("[Google](https://www.google.com)")
st.markdown("---")
st.caption("Hi I am Caption")

st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

json = {"a":"1,2,3", "b":"4,5,6"}
st.json(json)

code = """
print("Hello World")
def funct():
    return 0;
"""

st.code(code, language="Python")

st.write("## H2")

st.metric(label="Wind Speed", value="120ms⁻¹", delta="1.4ms⁻¹")


st.table(table)

st.dataframe(table)

st.image("taal.png", caption="This is my Image", width=635)

st.audio("Krishno Preme.mp3")
st.video("Timer.mp4")

def change():
    #print("Changed")
    print(st.session_state.checker)

state = st.checkbox("CheckBox", value=True, on_change=change, key="checker")
# if state:
#     st.write("Hi, the default of the checkBox Is false, But change the state.")
# else:
#     pass

radio_btn = st.radio("In which Country Do you want to live?", options=("US", "UK", "Canada"))
#print(radio_btn)

def btn_click():
    print("Button Clicked")
btn = st.button("Click Me!", on_click = btn_click)
select = st.selectbox("What is your favourite car?", options = ("Audi", "BMW", "Ferreri"))
#print(select)

multi_select = st.multiselect("What is your favourite Tech Brand?", options=("MicroSoft","Apple", "Amazon", "Oracle"))
st.write(multi_select)

st.write("## Uploading Files")
st.markdown("---")
images = st.file_uploader("Please Upload an Image", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)

# video = st.file_uploader("Please Upload a video", type=["mp4", "mpeg"])
# if video is not None:
#     st.video(image, format="video/mp4")


val = st.slider("This is Slider", min_value=50, max_value=150, value=70)
#print(val)

val = st.text_input("Enter Your Course Title", max_chars=60)
#print(val)

val = st.text_area("Course Description")
#print(val)

val = st.date_input("Enter your Registrstion Date")
#print(val)

st.markdown("---")
st.write("### Progress Bar")

def converter(value):
    m,s,mm = value.split(":")
    t_s = int(m)*60+int(s)+int(mm)/1000
    return t_s

val = st.time_input("Set Timer", value=time(0,0,0))
if str(val) == "00:00:00":
    st.write("Please sent timer")
else:
    sec = converter(str(val))
    print(sec)
    bar =st.progress(0)
    per = sec/100
    progress_status = st.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i+1)+" %")
        ts.sleep(per)


























