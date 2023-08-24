# import streamlit as st
# import numpy as np
# import cv2

# def main():
#     st.set_page_config(
#         page_title="Image Filtering App",
#         page_icon=":camera:",
#         layout="centered",
#         initial_sidebar_state="expanded"
#     )

#     st.title("Image Filtering")

#     # Upload an image from the user's local PC
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

#     if uploaded_file is not None:
#         img_array = np.fromstring(uploaded_file.read(), np.uint8)
#         uploaded_image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

#         # Display the uploaded image
#         st.subheader("Uploaded Image")
#         st.image(uploaded_image, channels="BGR", use_column_width=True)

#         # Display filter options
#         filter_type = st.selectbox("Select a filter", ["Averaging", "Gaussian", "Median"])

#         if filter_type == "Averaging":
#             # Apply Averaging filtering
#             blurAverage = cv2.blur(uploaded_image, (25, 25))
#             st.subheader("Averaging Filtering")
#             st.image(blurAverage, channels="BGR", use_column_width=True)

#         elif filter_type == "Gaussian":
#             # Apply Gaussian filtering
#             blurGauss = cv2.GaussianBlur(uploaded_image, (25, 25), 0)
#             st.subheader("Gaussian Filtering")
#             st.image(blurGauss, channels="BGR", use_column_width=True)

#         elif filter_type == "Median":
#             # Apply Median filtering
#             blurMedian = cv2.medianBlur(uploaded_image, 25)
#             st.subheader("Median Filtering")
#             st.image(blurMedian, channels="BGR", use_column_width=True)

# if __name__ == "__main__":
#     main()


#======================================================================================
#mouse region

import streamlit as st
import numpy as np
import cv2

def apply_filter(image, filter_type):
    if filter_type == "Averaging":
        return cv2.blur(image, (7, 7))
    elif filter_type == "Gaussian":
        return cv2.GaussianBlur(image, (5, 5), 0)
    elif filter_type == "Median":
        return cv2.medianBlur(image, 3)

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

        # Display the uploaded image
        st.subheader("Uploaded Image")
        st.image(uploaded_image, channels="BGR", use_column_width=True)

        # Display filter options
        filter_type = st.selectbox("Select a filter", ["Averaging", "Gaussian", "Median"])

        # Show canvas for user interaction
        canvas_result = st_canvas(
            uploaded_image,
            drawing_mode="rect",
            key="canvas",
            width=uploaded_image.shape[1],
            height=uploaded_image.shape[0],
            drawing_value=(255, 0, 0),
            )

        if canvas_result.image_data is not None:
            selected_region = canvas_result.image_data

            # Apply the filter to the selected region
            filtered_region = apply_filter(selected_region, filter_type)

            # Replace the selected region in the original image
            output_image = uploaded_image.copy()
            output_image[
                canvas_result.top_left[1] : canvas_result.bottom_right[1],
                canvas_result.top_left[0] : canvas_result.bottom_right[0],
            ] = filtered_region

            # Display the filtered image with the selected region
            st.subheader("Filtered Image with Selected Region")
            st.image(output_image, channels="BGR", use_column_width=True)

if __name__ == "__main__":
    main()
