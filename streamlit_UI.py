import streamlit as st

st.title("Materials Defect Analyzer for SEM photos")


st.write("This is a versatile object detection and image segmentation model with YOLOv8 architecture.\
    It is trained to be effective at identifying and differentiating between different types of imperfections\
        in materials. These may include scratches, divots, etc. The dataset I used to train this model on is the NEU\
            Surface Defect Database. This is my first ever independence programming project, thank you for checking it out\
                !")

image = st.file_uploader("Upload image to be examined.", type = ["jpg", "jpeg"])

st.image(image, width = 400)

with st.sidebar:
    
    st.title("About Me")
    
    st.write("Hello, my name is Ethan Huang! I am a Class of 2029 Artificial Intelligence Major at the \
        Jacobs School of Engineering in UC San Diego. I'm interested in AI and ML projects, especially\
            their interdisciplinary applications. At the time of creating this project, I've been researching\
                a lot with TensorFlow, especially their computer vision architectures.")
    
    st.markdown("[![LinkedIn]('https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg')]('www.linkedin.com/in/ethanhuangpy')")
    st.markdown("[![GitHub]('github-mark-white.png')]('www.linkedin.com/in/ethanhuangpy')")
    
    