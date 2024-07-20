# Book Recommendation System (Apriori Algorithm)

![Screenshot 2024-07-20 001513](https://github.com/user-attachments/assets/89ddbbb7-619d-45ad-a949-6f90f68785ce)

## Overview

This book recommendation system is an interactive web app that utilizes Machine Learning to allow its users to get recommendations based on their preferences and ratings. It offers a wide range of books from the 1980s to the 2000s. Let’s dive into the details:

- **DataSet**: The dataset used to allow the model to generate the relevant rules is the **Book Recommendation Dataset** (https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset?resource=download&select=Books.csv). The dataset offers over 240,000 books from over 100,000 authors and ratings from over 55,000 users.

- **Apriori Algorithm**: After preprocessing the dataset and formatting it in a way usable by the Apriori Algorithm, the latter analyzed the data and generated a set of rules used to base the recommendations on.
  
- **Book Recommendations**:
  - The user can choose one or multiple items from a list of available books.
  - Based on the chosen books, the system will offer multiple recommendations, prioritizing some over others based on the input.

- **Streamlit Interface**:
  - Streamlit offers a simple and interactive UI to not only showcase the system but also provide more options like showcasing code to give more insight into the project.
  - The project is split into multiple pages, the main two being to showcase the thought process of processing the data and to test the system.
