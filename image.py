import streamlit as st
import numpy as np
import cv2

def main():
    st.set_page_config(
        page_title="Image Filtering App",
        page_icon=":camera:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("Image Filtering")

    # Upload an image from the user's local PC
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        img_array = np.fromstring(uploaded_file.read(), np.uint8)
        uploaded_image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # Display filter options and adjustments in the sidebar
        st.sidebar.subheader("Filter Options")
        filter_type = st.sidebar.selectbox("Select a filter", ["Averaging", "Gaussian", "Median"])

        # Allow users to adjust the window size with odd numbers only
        window_size = st.sidebar.slider("Window Size (Odd Number)", min_value=1, max_value=50, value=25, step=2)

        # Allow users to adjust the displayed image width
        image_width = st.slider("Adjust Image Width", min_value=100, max_value=300, value=300)

        if filter_type == "Averaging":
            # Apply Averaging filtering
            blurAverage = cv2.blur(uploaded_image, (window_size, window_size))

            st.subheader("Image Comparison")
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(uploaded_image, channels="BGR", width=image_width)

            with col2:
                st.subheader("Averaging Filtered Image")
                st.image(blurAverage, channels="BGR", width=image_width)

        elif filter_type == "Gaussian":
            # Apply Gaussian filtering
            blurGauss = cv2.GaussianBlur(uploaded_image, (window_size, window_size), 0)

            st.subheader("Image Comparison")
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(uploaded_image, channels="BGR", width=image_width)

            with col2:
                st.subheader("Gaussian Filtered Image")
                st.image(blurGauss, channels="BGR", width=image_width)

        elif filter_type == "Median":
            # Apply Median filtering
            blurMedian = cv2.medianBlur(uploaded_image, window_size)

            st.subheader("Image Comparison")
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Original Image")
                st.image(uploaded_image, channels="BGR", width=image_width)

            with col2:
                st.subheader("Median Filtered Image")
                st.image(blurMedian, channels="BGR", width=image_width)

if __name__ == "__main__":
    main()
