import streamlit as st

# will display text, dataframe, graph, images
st.write("Hello World!")

# text formating
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")
st.text("This is a plain text")


# markdown

st.markdown("""
            
                # This is title
                ## This is header
                ### This is subheader
                #### This is subheader 2           
            
            """)

# status elements
# success
st.success("this message display text in green color")
# warning   
st.warning("this message display text in yellow color")
# error
st.error("this message display text in red color")
# info
st.info("this message display text in blue color")

# display media
# images and video
st.subheader("Display Images")

st.image("./media/mountains.webp",caption="Mountains",width=300,use_column_width=True)

st.subheader("Display Videos")

video_file = open("./media/star.mp4","rb").read()

st.video(video_file)





