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

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/majid-200/Book-Recommendation-System__Apriori-Algorithm__.git
   
2. **Install dependencies**:
   - Available in the requirements.txt file
    
3. **Run the Streamlit web app**:
   ```bash
   streamlit run Home.py

## SCreenshots from the web app

![Screenshot 2024-07-20 112817](https://github.com/user-attachments/assets/fdbf1623-4dfb-4545-8a1f-e5ca4911d24f)
![Screenshot 2024-07-20 112844](https://github.com/user-attachments/assets/4dfae6ac-b76b-442f-b69b-67a4885c0a17)
![Screenshot 2024-07-20 112904](https://github.com/user-attachments/assets/7417f7c0-ec48-4e59-9210-aac49315ecce)
![Screenshot 2024-07-20 112933](https://github.com/user-attachments/assets/2367ef4b-e9e7-4e29-9e53-d28b04514694)
![Screenshot 2024-07-20 113003](https://github.com/user-attachments/assets/4d6ab364-1e23-4a05-b67c-1b40259c4ceb)
