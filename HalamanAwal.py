import streamlit as st
from  PIL import Image, ImageEnhance
import pickle
import numpy as np
from skimage.io import imread, imsave
import tensorflow as tf
from tensorflow import keras


st.title('Deteksi Masker')


# uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     col1, col2, col3 = st.columns(3)

#     with col2:
#         st.markdown('<p style="text-align: center;">Gambar</p>',unsafe_allow_html=True)
#         st.image(image,width=300)  

uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
if uploaded_file is not None:
        gambar = Image.open(uploaded_file)
        col1, col2, col3 = st.columns(3)
        with col2:
            st.markdown('<p style="text-align: center;">Gambar</p>',unsafe_allow_html=True)
            st.image(gambar,width=300)  
            if st.button('predict'):
                model=tf.keras.models.load_model('model.h5')
                predict=model.predict(uploaded_file)
                print(predict)
                st.success()



 