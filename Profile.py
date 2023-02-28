import streamlit as st

st.title("Hi all, I am Yaswanth")
st.snow()

st.subheader('''
                I am passionate about learning new technologies. Especially, Data Science and Artificial Intelligence.:sunglasses:
                I have a fine grip on Python and SQL. I'm gonna make use of this time and oppurtunity to improve myself.''')

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("Button has been clicked. it's working well")
    st.balloons()