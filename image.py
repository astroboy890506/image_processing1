# import streamlit as st
# import numpy as np
# import cv2

# def main():
#     st.set_page_config(
#         page_title="Image Filtering App",
#         page_icon=":camera:",
#         layout="wide",
#         initial_sidebar_state="expanded"
#     )

#     st.title("Image Filtering")

#     # Upload an image from the user's local PC
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

#     if uploaded_file is not None:
#         img_array = np.fromstring(uploaded_file.read(), np.uint8)
#         uploaded_image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

#         # Display filter options and adjustments in the sidebar
#         st.sidebar.subheader("Filter Options")
#         filter_type = st.sidebar.selectbox("Select a filter", ["Averaging", "Gaussian", "Median", "Non-Local Means Denoising", "Bilateral Filtering"])

#         # Allow users to adjust the window size with odd numbers only
#         window_size = st.sidebar.slider("Window Size (Odd Number)", min_value=1, max_value=50, value=25, step=2)

#         # Allow users to adjust the standard deviation for the Gaussian filter
#         std_dev = None
#         if filter_type == "Gaussian":
#             std_dev = st.sidebar.slider("Standard Deviation", min_value=0.1, max_value=10.0, value=1.0, step=0.1)

#         # Allow users to adjust the displayed image width
#         image_width = st.slider("Adjust Image Width", min_value=100, max_value=300, value=300)

#         if filter_type == "Averaging":
#             # Apply Averaging filtering
#             blurAverage = cv2.blur(uploaded_image, (window_size, window_size))

#             st.subheader("Image Comparison")
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.subheader("Original Image")
#                 st.image(uploaded_image, channels="BGR", width=image_width)

#             with col2:
#                 st.subheader("Averaging Filtered Image")
#                 st.image(blurAverage, channels="BGR", width=image_width)

#         elif filter_type == "Gaussian":
#             # Apply Gaussian filtering
#             blurGauss = cv2.GaussianBlur(uploaded_image, (window_size, window_size), std_dev)

#             st.subheader("Image Comparison")
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.subheader("Original Image")
#                 st.image(uploaded_image, channels="BGR", width=image_width)

#             with col2:
#                 st.subheader("Gaussian Filtered Image")
#                 st.image(blurGauss, channels="BGR", width=image_width)

#         elif filter_type == "Median":
#             # Apply Median filtering
#             blurMedian = cv2.medianBlur(uploaded_image, window_size)

#             st.subheader("Image Comparison")
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.subheader("Original Image")
#                 st.image(uploaded_image, channels="BGR", width=image_width)

#             with col2:
#                 st.subheader("Median Filtered Image")
#                 st.image(blurMedian, channels="BGR", width=image_width)

#         elif filter_type == "Non-Local Means Denoising":
#             # Apply Non-Local Means Denoising
#             smoothed_image = cv2.fastNlMeansDenoisingColored(uploaded_image, None, 10, 10, 7, 21)

#             st.subheader("Image Comparison")
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.subheader("Original Image")
#                 st.image(uploaded_image, channels="BGR", width=image_width)

#             with col2:
#                 st.subheader("Non-Local Means Denoised Image")
#                 st.image(smoothed_image, channels="BGR", width=image_width)

#         elif filter_type == "Bilateral Filtering":
#             # Apply Bilateral Filtering
#             smoothed_image = cv2.bilateralFilter(uploaded_image, 9, 75, 75)

#             st.subheader("Image Comparison")
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.subheader("Original Image")
#                 st.image(uploaded_image, channels="BGR", width=image_width)

#             with col2:
#                 st.subheader("Bilateral Filtered Image")
#                 st.image(smoothed_image, channels="BGR", width=image_width)

# if __name__ == "__main__":
#     main()


#=========================================================================
# import streamlit as st
# import numpy as np
# import cv2

# def main():
#     st.set_page_config(
#         page_title="Image Filtering App",
#         page_icon=":camera:",
#         layout="wide",
#         initial_sidebar_state="expanded"
#     )

#     st.title("Image Filtering")

#     # Upload an image from the user's local PC
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

#     if uploaded_file is not None:
#         img_array = np.fromstring(uploaded_file.read(), np.uint8)
#         uploaded_image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

#         # Display filter options and adjustments in the sidebar
#         st.sidebar.subheader("Filter Options")
#         filter_type = st.sidebar.selectbox("Select a filter", ["Averaging", "Gaussian", "Median"])

#         # Allow users to adjust the window size with odd numbers only
#         window_size = st.sidebar.slider("Window Size (Odd Number)", min_value=1, max_value=50, value=25, step=2)

#         # Allow users to adjust the standard deviation for the Gaussian filter
#         if filter_type == "Gaussian":
#             std_dev = st.sidebar.slider("Standard Deviation", min_value=0.1, max_value=10.0, value=1.0, step=0.1)

#         # Allow users to adjust the displayed image width
#         image_width = st.slider("Adjust Image Width", min_value=100, max_value=300, value=300)

#         if filter_type == "Averaging":
#             # Apply Averaging filtering
#             blurAverage = cv2.blur(uploaded_image, (window_size, window_size))

#             st.subheader("Image Comparison")
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.subheader("Original Image")
#                 st.image(uploaded_image, channels="BGR", width=image_width)

#             with col2:
#                 st.subheader("Averaging Filtered Image")
#                 st.image(blurAverage, channels="BGR", width=image_width)

#         elif filter_type == "Gaussian":
#             # Apply Gaussian filtering
#             blurGauss = cv2.GaussianBlur(uploaded_image, (window_size, window_size), std_dev)

#             st.subheader("Image Comparison")
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.subheader("Original Image")
#                 st.image(uploaded_image, channels="BGR", width=image_width)

#             with col2:
#                 st.subheader("Gaussian Filtered Image")
#                 st.image(blurGauss, channels="BGR", width=image_width)

#         elif filter_type == "Median":
#             # Apply Median filtering
#             blurMedian = cv2.medianBlur(uploaded_image, window_size)

#             st.subheader("Image Comparison")
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.subheader("Original Image")
#                 st.image(uploaded_image, channels="BGR", width=image_width)

#             with col2:
#                 st.subheader("Median Filtered Image")
#                 st.image(blurMedian, channels="BGR", width=image_width)

# if __name__ == "__main__":
#     main()


#============================================================================================

# import streamlit as st
# import numpy as np
# import cv2

# def main():
#     st.set_page_config(
#         page_title="Image Filtering App",
#         page_icon=":camera:",
#         layout="wide",
#         initial_sidebar_state="expanded"
#     )

#     st.title("Image Filtering")

#     # Upload an image from the user's local PC
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

#     if uploaded_file is not None:
#         img_array = np.fromstring(uploaded_file.read(), np.uint8)
#         uploaded_image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

#         # Display filter options and adjustments in the sidebar
#         st.sidebar.subheader("Filter Options")
#         filter_type = st.sidebar.selectbox("Select a filter", ["Averaging", "Gaussian", "Median"])

#         # Allow users to adjust the window size with odd numbers only
#         window_size = st.sidebar.slider("Window Size (Odd Number)", min_value=1, max_value=50, value=25, step=2)

#         # Allow users to adjust the displayed image width
#         image_width = st.slider("Adjust Image Width", min_value=100, max_value=300, value=300)

#         if filter_type == "Averaging":
#             # Apply Averaging filtering
#             blurAverage = cv2.blur(uploaded_image, (window_size, window_size))

#             st.subheader("Image Comparison")
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.subheader("Original Image")
#                 st.image(uploaded_image, channels="BGR", width=image_width)

#             with col2:
#                 st.subheader("Averaging Filtered Image")
#                 st.image(blurAverage, channels="BGR", width=image_width)

#         elif filter_type == "Gaussian":
#             # Apply Gaussian filtering
#             blurGauss = cv2.GaussianBlur(uploaded_image, (window_size, window_size), 0)

#             st.subheader("Image Comparison")
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.subheader("Original Image")
#                 st.image(uploaded_image, channels="BGR", width=image_width)

#             with col2:
#                 st.subheader("Gaussian Filtered Image")
#                 st.image(blurGauss, channels="BGR", width=image_width)

#         elif filter_type == "Median":
#             # Apply Median filtering
#             blurMedian = cv2.medianBlur(uploaded_image, window_size)

#             st.subheader("Image Comparison")
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.subheader("Original Image")
#                 st.image(uploaded_image, channels="BGR", width=image_width)

#             with col2:
#                 st.subheader("Median Filtered Image")
#                 st.image(blurMedian, channels="BGR", width=image_width)

# if __name__ == "__main__":
#     main()

#============================
import streamlit as st
import numpy as np
import cv2
from PIL import Image

def main():
    st.set_page_config(
        page_title="Image Filtering App",
        page_icon=":camera:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("Image Filtering App")

    # Upload an image from the user's local PC
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image file
        image = Image.open(uploaded_file)
        image = np.array(image)

        # Display filter options and adjustments in the sidebar
        st.sidebar.subheader("Filter Options")
        filter_type = st.sidebar.selectbox("Select a filter", [
            "Median", 
            "Gaussian", 
            "Mean", 
            "Bilateral", 
            "Non-Local Means Denoising"
        ])

        # Allow users to adjust the window size with odd numbers only
        window_size = st.sidebar.slider("Window Size (Odd Number)", min_value=1, max_value=50, value=25, step=2)

        # Allow users to adjust the standard deviation for the Gaussian filter
        std_dev = None
        if filter_type == "Gaussian":
            std_dev = st.sidebar.slider("Standard Deviation", min_value=0.1, max_value=10.0, value=1.0, step=0.1)

        # Allow users to adjust the displayed image width
        image_width = st.slider("Adjust Image Width", min_value=100, max_value=800, value=300)

        # Perform filtering based on user selection
        filtered_image = None
        if filter_type == "Mean":
            # Apply Averaging filter (Mean filter)
            filtered_image = cv2.blur(image, (window_size, window_size))
        elif filter_type == "Gaussian":
            # Apply Gaussian filter
            filtered_image = cv2.GaussianBlur(image, (window_size, window_size), std_dev)
        elif filter_type == "Median":
            # Apply Median filter
            filtered_image = cv2.medianBlur(image, window_size)
        elif filter_type == "Bilateral":
            # Apply Bilateral filter
            filtered_image = cv2.bilateralFilter(image, 9, 75, 75)
        elif filter_type == "Non-Local Means Denoising":
            # Apply Non-Local Means Denoising
            filtered_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

        # Display the comparison
        st.subheader("Image Comparison")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(image, channels="BGR", width=image_width)

        with col2:
            st.subheader(f"{filter_type} Filtered Image")
            st.image(filtered_image, channels="BGR", width=image_width)

if __name__ == "__main__":
    main()

