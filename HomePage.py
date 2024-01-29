import streamlit as st

# Other libraries you might need (e.g., pandas for data handling)
st.set_page_config(
    page_title="Animal Facts",
    page_icon=":tiger:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.sidebar.title('Navigation')
page = st.sidebar.radio("Go to", ('Home', 'Animal Facts', 'Other Page'))
if page == 'Home':
    st.title("Home Page")
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
if page == 'Animal Facts':
    st.title('Animal Facts')

    # User selects or inputs the animal
    animal = st.selectbox('Select an animal', ['Lion', 'Tiger', 'Bear'])
    
    # Display information about the animal
    if animal:
        st.header(f'Facts about {animal}')
        
        # Display how the animal gets food
        st.subheader('How the animal gets food')
        st.write('...')  # Replace with actual information or dynamic content
        
        # Display how the animal protects itself from predators
        st.subheader('How the animal protects itself from predators')
        st.write('...')  # Replace with actual information or dynamic content
        
        # Display the animal's sleeping habits
        st.subheader("Animal's Sleeping Habits")
        st.write('...')  # Replace with actual information or dynamic content
