import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Rest of your code as it is

def main():
    st.set_page_config(
        page_title="Image Filtering App",
        page_icon=":camera:",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    st.title("Image Filtering")

    # Upload an image from the user's local PC
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img_array = np.fromstring(uploaded_file.read(), np.uint8)
        uploaded_image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # gray_uploaded_image = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)

        # Display the uploaded image
        st.subheader("Uploaded Image")
        st.image(cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2RGB), use_column_width=True)
        #st.image(cv2.cvtColor(gray_uploaded_image, cv2.COLOR_BGR2RGB), use_column_width=True)

        # Display filter options
        filter_type = st.selectbox("Select a filter", ["Averaging", "Gaussian", "Median"])

        if filter_type == "Averaging":
            # Apply Averaging filtering
            blurAverage = cv2.blur(uploaded_image, (5,5))
            st.subheader("Averaging Filtering")
            st.image(blurAverage, use_column_width=True)

        elif filter_type == "Gaussian":
            # Apply Gaussian filtering
            blurGauss = cv2.GaussianBlur(uploaded_image, (5, 5), 0)
            st.subheader("Gaussian Filtering")
            st.image(blurGauss, use_column_width=True)

        elif filter_type == "Median":
            # Apply Median filtering
            blurMedian = cv2.medianBlur(uploaded_image, 5)
            st.subheader("Median Filtering")
            st.image(blurMedian, use_column_width=True)

if __name__ == "__main__":
    main()
