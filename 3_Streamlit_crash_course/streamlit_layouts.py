import streamlit as st

st.set_page_config(page_title="Layouts", page_icon="🧊", layout="wide")
st.title("Streamlit Layouts")

# sidebar

sidebar = st.sidebar    
sidebar.write("## Sidebar")
sidebar.header("Sidebar Header")

# columns
col1,col2,col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.image("./media/cat.jpg", width=300)

with col2:
    st.header("Column 2")
    st.image("./media/dog.jpg", width=300)

with col3:
    st.header("Column 3")
    st.image("./media/owl.jpg", width=300)

# tabs

st.header("Display in Tabs")

tab1,tab2,tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])


with tab1:
    st.header("Tab 1")
    st.image("./media/cat.jpg", width=300)

with tab2:
    st.header("Tab 2")
    st.image("./media/dog.jpg", width=300)

with tab3:
    st.header("Tab 3")
    st.image("./media/owl.jpg", width=300)



