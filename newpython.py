import streamlit as st

# Add gradient background using custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #6a11cb, #2575fc);
        color: white;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Title and Header
st.title('_MY_ :red[_FIRST_] _DEMO-_:blue[_WEBSITE_]')
st.header(":blue[Using Python]")
st.header("We are hiring you for a job")
st.subheader("_Please Fill the Form_")

# Form Layout using columns for better organization
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Enter your name:")
    fname = st.text_input("Enter your father's name:")
    no = st.text_input("Enter your mobile number:")

with col2:
    branch = st.selectbox("Select Your Branch:", ["CSE", 'AIML', 'EC', 'ME', 'CE', 'CSDS', 'IT'])
    about = st.text_area("Enter why should we hire you:")

# Create a submit button
btn = st.button("Submit")

if btn:
    st.markdown(f'''
                <div style="padding: 10px; border: 2px solid white; border-radius: 10px; background-color: rgba(255, 255, 255, 0.1);">
                    <h3>Thank you, {name}, for submitting your application!</h3>
                    <p>Your response has been submitted successfully.</p>
                    <p>We recommend you to stay connected with us for further updates!</p>
                </div>
                ''', unsafe_allow_html=True)
