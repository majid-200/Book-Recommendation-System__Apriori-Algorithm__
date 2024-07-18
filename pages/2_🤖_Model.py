import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_icon='🤖',
    page_title='Model',
    layout='wide'
)

#----------------------------------------------------------------------------------------------------------------------------------------
@st.cache_data
def load_model(path):
    loaded_model = pickle.load(open(path, 'rb'))
    return loaded_model

@st.cache_data
def load_data(path):
    data = pd.read_csv(path)
    return data


Apriori_mod = load_model("data\\finalized_model.ob")
Book_list = load_model('data\\Books_List.ob')

Book_img = load_data("data\\book-img.csv")
#--------------------------------------------------------------------------------------------------------------------------------------

st.title("Books recommendation")

options = st.multiselect('Choose a book 📚:', Book_list)

st.write('The recommended books for you:')

recommendations = []

options.sort()

for search in options:
    for item in Apriori_mod:
        # book = []
        if search in item[0]:

            for rule in item[2]:
                ant = [x for x in rule[0]]
                ant.sort()
                
                if options == ant:
                    seq = [y for y in rule[1]]
                    for bk in seq:
                        if bk not in recommendations:
                            recommendations.append(bk)

                if len(ant) == 1 and ant[0] == search:
                    seq = [y for y in rule[1]]
                    for bk in seq:
                        if bk not in recommendations:
                            recommendations.append(bk)

            # x = [x for x in item[2][0][0]]
            # y = [x for x in item[2][0][1]]

            # if search == x:
            #     book.append(y)
            #     book.append(item[1])
            #     book.append(item[2][0][3])
            #     book.append(item[2][0][2])
            # else:
            #     book.append(x)
            #     book.append(item[1])
            #     book.append(item[2][1][3])
            #     book.append(item[2][1][2])
            

            # pos = True
            # for i in range(len(recommendations)):
            #     if book[2] > recommendations[i][2]:
            #         recommendations.insert(i, list(book))
            #         pos = False
            #         break
            # if pos:
            #     recommendations.append(list(book))

# st.write(recommendations)

#--------------------------------------------------------------------------------------------------------------------------------------------

for b in range(1, len(recommendations)+1):
        
    if b % 5 == 1:
        column1, column2, column3, column4, column5, = st.columns(5)
        # column1.write(Book_img[Book_img['Book-Title'] == recommendations[b-1]].first_valid_index())
        column1.image(Book_img['Image-URL-L'].loc[Book_img[Book_img['Book-Title'] == recommendations[b-1]].first_valid_index()])
    elif b % 5 == 2:
        # column2.write(Book_img[Book_img['Book-Title'] == recommendations[b-1]].first_valid_index())
        column2.image(Book_img['Image-URL-L'].loc[Book_img[Book_img['Book-Title'] == recommendations[b-1]].first_valid_index()])
    elif b % 5 == 3:
        # column3.write(Book_img[Book_img['Book-Title'] == recommendations[b-1]].first_valid_index())
        column3.image(Book_img['Image-URL-L'].loc[Book_img[Book_img['Book-Title'] == recommendations[b-1]].first_valid_index()])
    elif b % 5 == 4:
        # column4.write(Book_img[Book_img['Book-Title'] == recommendations[b-1]].first_valid_index())
        column4.image(Book_img['Image-URL-L'].loc[Book_img[Book_img['Book-Title'] == recommendations[b-1]].first_valid_index()])
    else:
        # column5.write(Book_img[Book_img['Book-Title'] == recommendations[b-1]].first_valid_index())
        column5.image(Book_img['Image-URL-L'].loc[Book_img[Book_img['Book-Title'] == recommendations[b-1]].first_valid_index()])
        st.divider()

#-----------------------------------------------------------------------------------------------------------------------------------------------
st.divider()

st.subheader("Model Code")
code = ('''
         from apyori import apriori
        
        #applying the Apriori Algorithm on the Transaction list created before
         rules= apriori(transactions= favs, min_support=0.0004, min_confidence = 0, min_lift=1.2) 
         results= list(rules)
         ''')

st.code(code,language='python')

st.subheader('A snippet of the rules generated')
with st.expander("Rules"):
    st.write(Apriori_mod[0:5])

st.divider()

