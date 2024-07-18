import streamlit as st

st.set_page_config(
    page_icon='👋',
    page_title='Home',
    layout='wide'

)


st.title(":blue[Welcome] to the Home page! 👋")
st.subheader('This is an interactive experince of :blue[Preparing Data] to train an :blue[Apriori Model] to create a :blue[Book Recommendation System]')
st.markdown(
    """
    ### The source of the used Data
    - Check out [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset?resource=download&select=Books.csv)
"""
)
st.markdown(
    """
### Please choose the :orange[Data Page] in the sidebar to start
"""
)