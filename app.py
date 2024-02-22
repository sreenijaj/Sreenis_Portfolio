
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.markdown("""
    <style>
    .reportview-container .markdown-text-container {
        padding-top: 2rem; /* Adjust the top padding of the text container */
    }
    .reportview-container .row-widget.stRadio > div {
        padding-top: 1rem; /* Adjust the top padding of the radio buttons */
    }
    /* You can add more styles here to target specific containers or widgets */
    </style>
    """, unsafe_allow_html=True)

# Load Lottie animations
def load_lottiefile(filepath):
    with open(filepath, "r") as file:
        return json.load(file)

animation1_path = "/Users/sreenija.jallipeta/Desktop/Webpage/Animation - 1708066665115.json"  # Update this path
animation2_path = "/Users/sreenija.jallipeta/Desktop/Webpage/Animation - 1708378569899.json"  # Update this path

animation1 = load_lottiefile(animation1_path)
animation2 = load_lottiefile(animation2_path)

    
    

# Header Section
with st.container():
    st.subheader("Hi :wave: I am Sreenija ")
    st.title("Software Developer / Data analyst")
    st.write("---")

st.header("**About Me**")
# About Me Section
with st.container():
    custom_bullet_points = """
        <ul style="list-style: none;">
            <li>* I am currently pursuing my final semester of Master's in Information Technology and Management at University of Texas at Dallas</li>
            <li>* I am very passionate about learning new ways to code efficiently using different technologies</li>
            <li>* I always try to look into improving myself by working more on developing my skills and knowledge</li>
        </ul>
    """
# Use the markdown function to render the HTML
st.markdown(custom_bullet_points, unsafe_allow_html=True)
st.write("---")

st.header(f"**Professional Experience**")
# What I Did - Section 1
with st.container():
    col1, col2 = st.columns([2, 2])
    with col1:
        st.subheader("Spectral MD, Dallas - System Engineering Intern")
        st.write("""
            - **Healthcare App Development**: Spearheaded the foundational development of a cutting-edge healthcare application, significantly enhancing user interaction and experience.
            - **Prototype Design**: Crafted an intuitive account management prototype, streamlining the end-user experience.
        """)
    with col2:
        st_lottie(animation1, height=250, key="animation1")

# What I Did - Section 2
with st.container():
    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader("Tata Consultancy Services, Hyderabad - Software Developer")
        st.write("""
            - **Automation and Efficiency**: Revolutionized testing and deployment processes through automation, accelerating software development velocity.
            - **Data and Project Management**: Implemented sophisticated systems for deep data analysis and seamless project management, ensuring smooth operations.
            - **Technology Mastery**: Utilized a versatile toolkit including Python, SQL, and advanced cloud computing tools, driving innovation and efficiency.
        """)
    with col2:
        st_lottie(animation2, height=300, key="animation2")
st.write("---")

#Projects Section 
st.header(f"**Projects**")

        


#Contact Section
with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")
    
    contact_form="""
                <form action="https://formsubmit.co/sreenija.j1998@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Your name" required><br>
                    <input type="email" name="email" placeholder="Your email" required><br>
                    <textarea name="message" placeholder="Your message here" required></textarea> <br>
                    <button type="submit">Send</button>
                </form>
                """
    st.markdown(contact_form , unsafe_allow_html =True)
    st.markdown("""
                <style>
/* Style inputs with type="text", select elements and textareas */
input[type=text],input[type=email], select, textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */
  border: 1px solid black; /* lack border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 12px; /* Add a top margin, increase if you want more space */
  margin-bottom: 12px; /* Bottom margin, increase if you want more space */
  resize: vertical; /* Allow the user to vertically resize the textarea (not horizontally) */
  background-color: white; /* Change the background color inside the box */
}

/* Style the submit button with a specific background color etc */
input[type=submit] {
  background-color: black;
  color: black;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 12px; /* Add a top margin, same as input for consistent spacing */
}

/* When moving the mouse over the submit button, add a darker green color */
input[type=submit]:hover {
  background-color: #45a049;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""",unsafe_allow_html=True)
    
        
