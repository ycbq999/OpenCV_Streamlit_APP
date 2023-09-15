import streamlit as st
import os


st.set_page_config(page_title="widgets", page_icon="🧊", layout="wide")
st.title("Streamlit Widgets")

# button
st.header("Button")
button = st.button("Button") # return ture or false
if button:
    st.write("Button clicked!")

# checkbox (Toggle Button)
st.header("Checkbox")
checkbox = st.checkbox("Do you want to agree")
if checkbox:
    st.write("You checked the box!")
else:
    st.write("You unchecked the box!")

# radio button
st.header("Radio Button")

options = ("Inda", "USA", "Canada", "UK")
radio_button = st.radio("what is your favoriate country", options,index = 2) # return an element in a list/tuple
st.write("You selected", radio_button)


# Select Box 
st.header('Select Box')
options = ('Email','Phone','WhatsApp')
select_box = st.selectbox('How would you like to contact',
                          options,index=1)
st.write('Your prefered mode of communication is ',
         select_box)

# Slider
slider_range = st.slider('How Old are you ?',
                         min_value=1,
                         max_value=100,
                         step=1,value=20)
st.write('You age is ',slider_range)

# Text Inputs
name = st.text_input('Enter you Name')
st.write('You name is ',name)

age = st.number_input('Enter you age',min_value=1,
                      max_value=100,step=1,value=25)
st.write('You age is ',age)

# Upload File
st.header('File Upload')
uploaded_file = st.file_uploader('Choose a File')

if uploaded_file is not None:
    st.success('File uploaded sucessfully')
    details = {'filename':uploaded_file.name,
               'filetype':uploaded_file.type,
               'filesize (bytes)':uploaded_file.size}
    
    st.json(details)
    
    # save the file
    path = os.path.join('./upload',uploaded_file.name)
    with open(path,mode='wb') as f:
        f.write(uploaded_file.getbuffer())
        st.success('File Saved successfully')