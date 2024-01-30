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
page = st.sidebar.radio("Go to", ('Home', 'Animal Facts', 'Other Page'))

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
