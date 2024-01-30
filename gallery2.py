import streamlit as st
import os

def load_images(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            images.append(os.path.join(folder_path, filename))
    return images



def animal_gallery():
    st.set_page_config(
        page_title="Animal Gallery",
        page_icon="🐫",
        layout="wide"
    )

    st.title("Welcome to the Animal Gallery!")
    st.image("https://images.unsplash.com/photo-1588190877958-ee2b99f697d1?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", use_column_width=True, caption="Image Source: Example.com")
    
    st.write(
        """
        Explore the beauty of the animal kingdom in our gallery. 
        View captivating pictures of various animals and learn interesting facts about them.
        Feel free to submit your own animal pictures and be part of our community!
        """
    )

    # Load animal images
    animal_images = load_images("images")



    if not animal_images:
        st.warning("No images found in the specified folder.")
        return

    # Display each image with caption and text
    for image_path in animal_images:
        caption = f"Caption for {os.path.basename(image_path)}"
        text = f"Additional information about {os.path.basename(image_path)}."

        st.image(image_path, caption=caption, use_column_width=True, width=300)


        st.write(text)
        st.write("---")  # Add a horizontal line between images

    # Ask visitors to submit their own pictures
    st.header("Submit Your Own Pictures")
    st.write("Do you have your own pictures of these animals? Share them with us!")

    # You can add a form or any input elements for submission here
    # Example:
    user_image = st.file_uploader("Upload Your Picture", type=["jpg", "jpeg", "png"])
    user_caption = st.text_input("Caption for Your Picture")

    if st.button("Submit"):
        # Handle the submission (store the image, caption, etc.)
        st.success("Thank you for submitting your picture!")

if __name__ == "__main__":
    animal_gallery()
