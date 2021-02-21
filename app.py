import streamlit as st
import cv2 as cv2
from PIL import Image
from tempfile import NamedTemporaryFile
st.title("Basics OpenCV operation")
#uploading Image file
img_file=st.file_uploader("Choose Image to upload ",type=["jpeg","jpg"])
temp_file = NamedTemporaryFile(delete=False)

threshold_value =st.slider("Select Threshold value", 20, 210)
if img_file is not None:
    image_loc = st.empty()
    text_loc=st.empty()
    temp_file.write(img_file.getvalue())
    img=Image.open(temp_file.name)
    img_1=cv2.imread(temp_file.name,0)
    ret, thr_img = cv2.threshold(img_1, threshold_value, 255, cv2.THRESH_BINARY)
    threshold_type=st.sidebar.selectbox("Select threshold types",("THRESH_BINARY","THRESH_BINARY_INV","THRESH_TRUNC","THRESH_TO_ZERO",))
    if threshold_type=="THRESH_BINARY_INV":
        ret, thr_img = cv2.threshold(img_1, threshold_value, 255, cv2.THRESH_BINARY_INV)
        image_loc.image(thr_img)
        text_loc.write("The Threshold type is {} and its value is {}".format(threshold_type,threshold_value))
    if threshold_type=="THRESH_TRUNC":
        ret, thr_img = cv2.threshold(img_1, threshold_value, 255, cv2.THRESH_TRUNC)
        image_loc.image(thr_img)
        text_loc.write("The Threshold type is {} and its value is {}".format(threshold_type, threshold_value))
    if threshold_type=="THRESH_BINARY":
        ret, thr_img = cv2.threshold(img_1, threshold_value, 255, cv2.THRESH_BINARY)
        image_loc.image(thr_img)
        text_loc.write("The Threshold type is {} and its value is {}".format(threshold_type, threshold_value))
    if threshold_type=="THRESH_TO_ZERO":
        ret, thr_img = cv2.threshold(img_1, threshold_value, 255, cv2.THRESH_TOZERO)
        image_loc.image(thr_img)
        text_loc.write("The Threshold type is {} and its value is {}".format(threshold_type, threshold_value))


