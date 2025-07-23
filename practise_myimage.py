import numpy as np
import streamlit as st 
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO


# set streamlit page config
st.set_page_config(page_title='Rithanya',layout='wide')

# title
st.title('Rithanya Multicolour channel visualizer')

# load image from path
@ st.cache_data
def load_image(Path):
    return Image.open(Path).convert('RGB')

Path=r"D:\Backup\Pictures\161731.jpg"
 
Rithanya=load_image(Path)
st.image(Rithanya,caption="Rithanya original image",use_container_width=False)

# Convert to Numpy array
Rithanya_np=np.array(Rithanya)
R,G,B =Rithanya_np[:,:,0] ,Rithanya_np[:,:,1], Rithanya_np[:,:,2]

# create channel images
red_img=np.zeros_like(Rithanya_np)
green_img=np.zeros_like(Rithanya_np)
blue_img=np.zeros_like(Rithanya_np)

red_img[:,:,0]=R
green_img[:,:,1]=G
blue_img[:,:,2]=B

# Display RGB Channel
st.subheader("RGB channel visualization")
col1 ,col2, col3=st.columns(3)

with col1:
    st.image(red_img,caption='Red channel',use_container_width=False)
    
with col2:
    st.image(green_img,caption='Green channel',use_container_width=False)
    
with col3:
    st.image(blue_img,caption='Blue channel',use_container_width=False)
    
# greyscale + colourmap
st.subheader("Colored map greyscale image")

colormap=st.selectbox("choose a matplotlib colormap",
["turbo","hot","cool","summer","prism","flag"] 
)


Rithanya_grey=Rithanya.convert("L")
Rithanya_grey_np=np.array(Rithanya_grey)

# plot using matplotlib colormap

fig,ax=plt.subplots(figsize=(1,1),dpi=150)
im=ax.imshow(Rithanya_grey_np,cmap=colormap)
plt.axis('off')

st.pyplot(fig)
