import numpy as np
import streamlit as st 
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO


# set streamlit page config
st.set_page_config(page_title='Panda',layout='wide')

# title
st.title('Panda Multicolour channel visualizer')

# load image from url
@ st.cache_data
def load_image(url):
    respone=requests.get(url)
    return Image.open(BytesIO(respone.content)).convert ('RGB')

url="https://tinypng.com/images/social/website.jpg"
 
Panda=load_image(url)
st.image(Panda,caption="panda original image",use_column_width=True)

# Convert to Numpy array
Panda_np=np.array(Panda)
R,G,B =Panda_np[:,:,0] ,Panda_np[:,:,1], Panda_np[:,:,2]

# create channel images
red_img=np.zeros_like(Panda_np)
green_img=np.zeros_like(Panda_np)
blue_img=np.zeros_like(Panda_np)

red_img[:,:,0]=R
green_img[:,:,1]=G
blue_img[:,:,2]=B

# Display RGB Channel
st.subheader("RGB channel visualization")
col1 ,col2, col3=st.columns(3)

with col1:
    st.image(red_img,caption='Red channel',use_column_width=True)
    
with col2:
    st.image(green_img,caption='Green channel',use_column_width=True)
    
with col3:
    st.image(blue_img,caption='Blue channel',use_column_width=True)
    
# greyscale + colourmap
st.subheader("Colored map greyscale image")

colormap=st.selectbox("choose a matplotlib colormap",
["turbo","hot","cool","summer","prism","flag"] 
)


Panda_grey=Panda.convert("L")
Panda_grey_np=np.array(Panda_grey)

# plot using matplotlib colormap

fig,ax=plt.subplots(figsize=(7,5))
im=ax.imshow(Panda_grey_np,cmap=colormap)
plt.axis('off')

st.pyplot(fig)

  
     
 
 


 

