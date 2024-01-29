import streamlit as st

# Set the page title
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