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

        window_size = st.sidebar.slider("Window Size", min_value=1, max_value=50, value=25)
        
        # Allow users to adjust the size of the uploaded image
        image_scaling_factor = st.sidebar.slider("Image Scaling Factor", min_value=0.1, max_value=2.0, value=1.0)

        scaled_image = cv2.resize(uploaded_image, None, fx=image_scaling_factor, fy=image_scaling_factor)

        if filter_type == "Averaging":
            # Apply Averaging filtering
            blurAverage = cv2.blur(scaled_image, (window_size, window_size))
            st.subheader("Averaging Filtering")
            st.image(blurAverage, channels="BGR", use_column_width=True)

        elif filter_type == "Gaussian":
            # Apply Gaussian filtering
            blurGauss = cv2.GaussianBlur(scaled_image, (window_size, window_size), 0)
            st.subheader("Gaussian Filtering")
            st.image(blurGauss, channels="BGR", use_column_width=True)

        elif filter_type == "Median":
            # Apply Median filtering
            blurMedian = cv2.medianBlur(scaled_image, window_size)
            st.subheader("Median Filtering")
            st.image(blurMedian, channels="BGR", use_column_width=True)

if __name__ == "__main__":
    main()
