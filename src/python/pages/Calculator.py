import streamlit as st
from utils.main import main

 
st.set_page_config(page_title="myPensionBenefit", layout="wide")
st.title("Home Page")


left_col, right_col = st.columns(2)
left_col.title("My Pension Benefit")
left_col.write("---")
right_col.title("Results")
 

# Add a selectbox to the sidebar:


with st.sidebar.form("email_form"):
    st.write("Receive your results")
    email = st.text_input("If you want to receive your results in an email, enter here")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Email", email)

# input 1
age = left_col.number_input(label="Enter your age", 
                      value=30)
 
# input 2
yos = left_col.number_input(label="How long have you been working for the state?", 
                      value=5, 
                      min_value=0, 
                      max_value=70)

# input 3
salary = left_col.number_input(label="What is your current salary?",
                         min_value=10000, 
                         max_value=500000)

# input 4
teacher = left_col.radio(label="Are you a teacher?", 
                   options=["Yes", "No",])

gender = left_col.radio(label="What is your gender?", 
                  options=["Female", "Male"])


def calculate():
    ans = main(yos, age, salary)
    markdown = "### Pension Benefit Details\n"
    for key, value in ans.items():
        markdown += f"- **{key}:** ${value:,.2f}\n"
    right_col.markdown(markdown)


if left_col.button("Calculate result"):
    calculate()
