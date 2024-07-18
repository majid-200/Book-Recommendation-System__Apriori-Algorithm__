import streamlit as st
import pandas as pd
import pickle


st.set_page_config(
    page_icon='📊',
    page_title='Data',
    layout='wide'
)

#------------------------------------------------------------------------------------------------------------------------------------
if "Data_loaded" not in st.session_state:
    st.session_state.Data_loaded = False
    st.session_state.View_Data = False
    st.session_state.Results1 = False
    st.session_state.Results2 = False
    st.session_state.Results3 = False

@st.cache_data
def load_model(path):
    loaded_model = pickle.load(open(path, 'rb'))
    return loaded_model

@st.cache_data
def load_data(path):
    data = pd.read_csv(path)
    return data

def disable():
    st.session_state.Data_loaded = True

def Res1():
    st.session_state.Results1 = True

def Res2():
    st.session_state.Results2 = True


def Res3():
    st.session_state.Results3 = True


#------------------------------------------------------------------------------------------------------------------------------------------------

st.title("Loading Data")
st.subheader("The first step would be to load our data")



if st.button("Load Data", type="primary", on_click=disable, disabled=st.session_state.Data_loaded):
    # st.session_state.Data_loaded = True
    st.session_state.books = load_data("data\\Books.csv")
    st.session_state.users = load_data("data\\Users.csv")
    st.session_state.ratings = load_data("data\\Ratings.csv")
    st.session_state.URB = load_data("data\\users_ratings_books.csv")
    st.session_state.URB.drop(columns=st.session_state.URB.columns[0], axis=1,  inplace=True)

    st.session_state.user_rating_book = load_data("data\\users_rating_books.csv")
    st.session_state.user_rating_book.drop(columns=st.session_state.user_rating_book.columns[0], axis=1,  inplace=True)
    st.session_state.fav_books_per_user = load_data("data\\Users_and_their_fav_books.csv")

    st.session_state.Transactions_list = load_model("data\\finalized_Tarnsactions_list.ob")

if st.session_state.Data_loaded:
    code_p1 = ('''
            # The following instruction from the pandas library as pd is used to load a csv file
            Data = pd.read_csv("csvFileName.csv")
            ''')
    st.code(code_p1, language='python')
    st.session_state.View_Data = st.toggle('View Data')

if st.session_state.View_Data:
    st.subheader("Books Data 📚")
    st.write(st.session_state.books)


    left_column, right_column = st.columns(2)

    left_column.subheader("Users Data 👥")
    left_column.dataframe(st.session_state.users, use_container_width=True)

    right_column.subheader("Ratings Data ⭐")
    right_column.dataframe(st.session_state.ratings, use_container_width=True)


    st.subheader("Dataframes Merged 🗄️")
    
    st.dataframe(st.session_state.URB, use_container_width=True)


st.divider() #----------------------------------------------------------------------------------------------------------------------------------

if st.session_state.Data_loaded:
    st.title("Exploratory Data Analysis")
    st.subheader("Next let's explore our data a bit")
    st.markdown(
    """
### Please choose from the :orange[SideBar] which :orange[Statistic] you wanna check 
"""
)
    with st.sidebar:
        op1 = st.checkbox("Ratings Distrubtion")
        op2 = st.checkbox("Books Distrubtion based on the Year Of Publication")
        op3 = st.checkbox("Books Distrubtion based on the Publisher")
        op4 = st.checkbox("Books Distrubtion based on the Author")
        op5 = st.checkbox("Users age Distrubtion")
        op6 = st.checkbox("Books Distrubtion Based on a minimum rating and a minimum occurence")

if st.session_state.Data_loaded:

    if op1:
        st.subheader('Ratings Distrubtion⭐')
        rating = st.slider('Choose a minimum rating', 0, 10, 0)
        st.write("higher or equal to ", rating, ' out of 10')
        st.bar_chart(st.session_state.ratings.drop(st.session_state.ratings.loc[st.session_state.ratings['Book-Rating']<rating].index)['Book-Rating'].value_counts())
    if op2:
        st.subheader('Books Distrubtion based on the Year Of Publication 📚')
        st.bar_chart(st.session_state.books.drop(st.session_state.books.loc[st.session_state.books['Year-Of-Publication']=='0'].index)['Year-Of-Publication'].value_counts())
    if op3:
        st.subheader('Books Distrubtion based on the Publisher 📚')
        pubs_occ = st.slider('Choose a minimum occurence', 0, 7500, 1500)
        st.write("higher or equal to ", pubs_occ, ' occurences')
        st.bar_chart((st.session_state.books[st.session_state.books.groupby('Publisher')['Publisher'].transform('size') > pubs_occ])['Publisher'].value_counts())
    if op4:
        st.subheader('Books Distrubtion based on the Author 📚')
        auth_occ = st.slider('Choose a minimum occurence', 0, 600, 100)
        st.write("higher or equal to ", auth_occ, ' occurences')
        st.bar_chart((st.session_state.books[st.session_state.books.groupby('Book-Author')['Book-Author'].transform('size') > auth_occ])['Book-Author'].value_counts())
    if op5:
        st.subheader('Users age Distrubtion 👥')
        age = st.slider('Choose age', value=[0,250])
        st.write("ages between ", age[0], ' and ', age[1])
        users_age = st.session_state.users.drop(st.session_state.users.loc[st.session_state.users['Age']<age[0]].index)['Age']
        st.bar_chart((users_age.drop(users_age.loc[users_age>age[1]].index)).value_counts())

    #----------------------------------------------------------------------------------------------------------------------------------------
    if op6:
        st.subheader('Books Distrubtion Based on a minimum rating and a minimum occurence 📚')

        rating2 = st.slider('Choose a minimum rating', 0, 10, 5)
        URB_rat = st.session_state.URB.drop(st.session_state.URB.loc[st.session_state.URB['Book-Rating']<rating2].index)
        bk_occ = st.slider('Choose a minimum occurence', 0, 700, 150)
        st.bar_chart((URB_rat[URB_rat.groupby('Book-Title')['Book-Title'].transform('size') > bk_occ])['Book-Title'].value_counts())

    st.divider()

    #---------------------------------------------------------------------------------------------------------------------------------------------

    st.title("Data Pre-Processing")

    st.subheader("Using the pandas library and excuting the following code will merge the necessary dataframes, remove unnecessary features, irrelevant rows and extracting the results for use in the next step ")

    code_p1 = ('''
            #Feature Selection from the books Dataframe
            books.drop(['Image-URL-S', 'Image-URL-M','Image-URL-L','Publisher','Year-Of-Publication','Book-Author'], axis=1, inplace=True)

            #Merging the ratings and books DataFrames
            df = pd.merge(books, ratings, on="ISBN")

            #Order the Dataframe based on user-ID in Ascending order
            df.sort_values(by=['User-ID'],inplace=True)

            #Droping all rows containing raitings lower than 5
            df.drop(df.loc[df['Book-Rating']<5].index, inplace=True)

            #Extracting the results as csv for use in Excel
            df.to_csv("users_ratings_books.csv")

            ''')

    st.code(code_p1, language='python')

    st.button("Excute the code and show results", on_click=Res1, disabled=st.session_state.Results1)

    if st.session_state.Results1:
        
        st.subheader('Generated Dataframe from the previous treatment')
        st.dataframe(st.session_state.user_rating_book, use_container_width=True)

    if st.session_state.Results1:
        st.subheader('Using :orange[Excel] we can generate a :orange[string] with :orange[all the books each user likes]')

        st.button("Excel do your thing", on_click=Res2, disabled=st.session_state.Results2)

        if st.session_state.Results2:
            st.session_state.fav_books_per_user.drop(columns=st.session_state.fav_books_per_user.columns[0], axis=1,  inplace=True)
            st.dataframe(st.session_state.fav_books_per_user, use_container_width=True)

    if st.session_state.Results2:
        st.subheader('Now to generating the :orange[Transactions list] used in the :orange[Apriori Algorithm], which is basically a :orange[list of sublists], where each :orange[item in the list represents a user], and each :orange[item in the sublist is a book] liked by the user')
        code_p2 = ('''
                Import pandas as pd

                #Reading data generted from the excel treatment
                data = pd.read_csv("Users_and_their_fav_books.csv")
                
                #Extracting the books asigned to each user as a list
                users_list =  list(data["HELP3"])

                #Transforming the list in a way acceptable to the applied Apriori Algorithm (aka Transactions)
                    favs = []
                    cln_fav = []

                    for i in range(0,27825):
                        cln_fav = users_list[i].split(" // ")
                        favs.append(list(cln_fav))
                        cln_fav.clear()
                ''')

        st.code(code_p2, language='python')

        st.button("Excute the code and show the List", on_click=Res3, disabled=st.session_state.Results3)

        if st.session_state.Results3:
            with st.expander("A snippet of the Transactions List"):
                st.write(st.session_state.Transactions_list[0:10])

        

    st.divider()





