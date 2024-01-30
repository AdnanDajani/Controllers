import streamlit as st

# Set the page config as the first command
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

# Sidebar navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio("Go to", ('Home', 'Animal Facts', 'Other Page','Popular Culture'))

if page == 'Home':
    st.title("Welcome to the Camel World!")

    # Introduction to camels
    st.markdown("""
    ### Discover the Majestic World of Camels
    Camels are remarkable creatures known for their ability to adapt to extreme environments. From the hot, arid deserts to the cold, barren steppes, camels have been invaluable companions to humans for thousands of years.
    """)

    # Display multiple images of camels with captions
    camel_images = ["camel_image_1.png", "camel_image_2.png", "camel_image_3.png"]  # Replace with your actual image paths or URLs


    
     # Create columns for each image
    cols = st.columns(len(camel_images))
    for idx, img in enumerate(camel_images):
        # Display each image in a column, setting the width to make them smaller
        cols[idx].image(img, use_column_width=True, caption="Majestic Camel")

    # More detailed introduction about camels
    st.markdown("""
    #### Fascinating Camel Facts
    - **Adaptation**: Camels have adapted incredibly well to life in the desert. Their humps store fat, which can be converted to water and energy when sustenance is not available.
    - **Resilience**: These hardy animals can survive in temperatures ranging from below freezing to over 50°C (122°F).
    - **Importance**: Camels have been domesticated for their milk, meat, wool, and as transportation. Their ability to carry heavy loads for long distances makes them indispensable for desert travel.
    """)
elif page == 'Animal Facts':
    # This sets the title of the Animal Facts page
    st.title('Animal Facts')

    # Creates a dropdown menu for users to select an animal
    # You can add more animals to the list
    animal = st.selectbox('Select an animal', ['Camel'])
    
    # Once an animal is selected, display information about that animal
    if animal:

        st.title("The Majestic Camel")

        # Download or use a local image path for the camel picture
        camel_image = "bm_camel_free.webp"  # Replace with your image URL

        # Add the image with centered alignment
        st.image(camel_image, use_column_width=True)

        # Write the description below the image
        st.markdown("""
        The camel is a fascinating creature adapted to harsh desert environments. With its hump storing fat for energy, strong legs for traversing sand, and wide nostrils for filtering dust, the camel thrives where few animals can.

        They have played a crucial role in human history as transportation, a source of milk and wool, and even symbols of resilience and strength.
        """)
        st.title("The Majestic Camel")

    # ... (image and description code)

        st.subheader("Interesting Facts about Camels")
        st.write("**1. Water-Wise Wonders:** Contrary to popular belief, camels don't store water in their humps. Instead, those humps are packed with fatty tissue that can be broken down for energy and water when needed, allowing them to survive for weeks in the desert without drinking.")
        st.write("**2. Sandstorm Survivors:** Camels have special adaptations to protect them from harsh desert conditions. Their nostrils can close to keep out sand, and their thick eyelashes and three eyelids shield their eyes from blowing dust.")
        st.write("**3. Super-Sippers:** When a camel does find water, it can drink up to 40 gallons in a single session! That's about 150 liters, or as much as a bathtub full of water.")



elif page == 'Other Page':
    # Sets the title of the Other Page
    st.title('Other Page Title')

    # You can add content here just like you did in the Animal Facts section.
    # For example, you might want to display text, images, tables, or charts.
    st.write('Content for the other page goes here.')

    # For example, displaying some text
    st.subheader('Section 1: Introduction')
    st.write('This is the introduction section of the other page.')

    # Displaying an image (you need to have an image in the same directory as your script)
    st.subheader('Section 2: Image')
    st.image('path_to_your_image.jpg', caption='Image caption.')

    # Displaying a table
    st.subheader('Section 3: Data Table')
    # Assuming you have a pandas DataFrame named 'df'
    # df = ...
    st.table(df)

    # You can also add interactive elements like buttons, sliders, etc.
    st.subheader('Section 4: Interactive Elements')
    if st.button('Say hello'):
        st.write('Hello, Streamlit!')


elif page == 'Popular Culture':
    # Sets the title of the Other Page
    st.title("Welcome to the Animal Fun Zone!")
    st.image("https://example.com/kid_friendly_cover_image.jpg", use_column_width=True, caption="Image Source: Example.com")
    
    st.write(
        """
        Explore the magical world of animals in our fun gallery. 
        View adorable pictures of various animals and discover interesting facts about them.
        Join us and let's have a blast learning about our furry friends!
        """
    )

    #st.button("Let's Explore!", on_click=animal_gallery)

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
