import streamlit as st
from gallery import animal_gallery  # Import the animal_gallery method from the first file


st.set_page_config(
    page_title="Animal Facts",
    page_icon=":camel:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS to change background color
custom_css = """
    <style>
        /* Main page background */
        .stApp {
            background-color: #f4f1de;  /* Soft Sand color */
        }
        /* Sidebar background */
        .css-1d391kg {
            background-color: #e8e4d9;  /* A shade darker than main background for subtle contrast */
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)



def animal_homepage():
   

    st.title("Welcome to the Animal Fun Zone!")
    st.image("https://example.com/kid_friendly_cover_image.jpg", use_column_width=True, caption="Image Source: Example.com")
    
    st.write(
        """
        Explore the magical world of animals in our fun gallery. 
        View adorable pictures of various animals and discover interesting facts about them.
        Join us and let's have a blast learning about our furry friends!
        """
    )

    st.button("Let's Explore!", on_click=animal_gallery)

    # New section with data about movies, books, documentaries, articles, and misrepresentations
    st.header("Popular Culture References")

    st.subheader("Movies:")
    st.write("""
        - **Lawrence of Arabia (1962):** This epic film features camels prominently, as it depicts T.E. Lawrence's World War I experiences in the Arabian Peninsula.
        - **Aladdin (1992):** The character of Abu, Aladdin's monkey companion, occasionally transforms into a camel in this animated Disney classic.
        - **The Mummy (1999):** Camels are seen in various scenes of this action-adventure film set in ancient Egypt.
    """)

    st.subheader("Books:")
    st.write("""
        - **The Little Prince by Antoine de Saint-Exupéry:** The Little Prince encounters a fox on Earth who speaks about taming and relationships. The fox mentions a desert and the importance of taming a camel.
        - **Just So Stories by Rudyard Kipling:** "How the Camel Got His Hump" is one of the stories in this collection, explaining how camels acquired their distinctive humps.
    """)

    st.subheader("Documentaries:")
    st.write("""
        - **BBC Earth's 'Planet Earth' series:** Several episodes feature camels in their natural habitats, showcasing their adaptations to survive in challenging environments.
        - **National Geographic's 'Wild Arabia' (2013):** This documentary explores the wildlife and landscapes of the Arabian Peninsula, including camels.
    """)

    st.subheader("Articles:")
    st.write("""
        - **National Geographic's 'Camels: Ship of the Desert':** National Geographic has published articles discussing the unique adaptations of camels, their importance in various cultures, and their role as pack animals in deserts.
        - **Smithsonian Magazine's 'The Complicated Role of the Camel in Ancient Israel':** This article delves into the historical and cultural significance of camels in ancient Israel.
    """)

    st.subheader("Misrepresentations:")
    st.write("""
        - **Comedic Stereotypes:** In some cartoons and comedic contexts, camels may be portrayed as grumpy or ill-tempered, often emphasizing their supposed stubbornness.
        - **Commercial Use:** Camels are sometimes used in advertising to create humorous or memorable images, but these representations may oversimplify or exaggerate certain characteristics.
    """)

if __name__ == "__main__":
    animal_homepage()
