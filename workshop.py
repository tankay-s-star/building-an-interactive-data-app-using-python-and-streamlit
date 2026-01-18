import streamlit as st


st.title("My First Streamlit App")
st.header("Hello World 👏")
st.write("This is an example of a simple Streamlit app.")
import pandas as pd
import streamlit as st


st.title("My First Streamlit App")
st.header("Hello World 👏")
st.write("This is an example of a simple Streamlit app.")

df = pd.read_csv("datasets/1642645053.csv", encoding="tis-620")
st.write(df)

number = st.slider("Select a number", 0, 100, 50)
st.write("The current number is ", number)

rating = st.radio(
    "How would you rate this class?",
    ("1", "2", "3", "4", "5")
)
st.write(f"You selected {rating}")
# Button
if st.button("Submit"):
    st.success(f"Thank you! Rating: {rating}, Course: {course}")

    # Dropdown (Selectbox)
course = st.selectbox(
    "Which course are you interested in?",
    ["Python", "Data Science", "Machine Learning", "Web Development"]
) 