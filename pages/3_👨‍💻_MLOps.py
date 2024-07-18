import streamlit as st
import reveal_slides as rs

st.set_page_config(
    page_icon='👨‍💻',
    page_title='MLOps',
    layout='wide'
)

sample_markdown = r'''
# MLOps


---
## What is MLOps?

It stands for Machine Learning Operations.\
As it is a part of Machine Learning engineering,
it focuses on simplifying the production, maintenance and monetization of ML models,
the process MLOps often comprises data scientists, devops engineers and IT.

---
## MLOps vs DevOps

MLOps is a set of engineering practices specific to machine learning projects that borrow from the more widely-adopted DevOps principles in software engineering. 
While DevOps brings a rapid, continuously iterative approach to shipping applications, 
MLOps borrows the same principles to take machine learning models to production.\
In both cases higher quality in a more effecient time.

---

## Where to use MLOps?

The span of MLOps is as the project demands.\
In certain cases, MLOps can encompass everything from the data pipeline to model production, 
while other projects may require MLOps implementation of only parts of the process. 
A majority of MLOps uses are across the following:

--

- Exploratory data analysis (EDA) <!-- .element: class="fragment" data-fragment-index="0" -->
- Data Prep and Feature Engineering <!-- .element: class="fragment" data-fragment-index="1" -->
- Model training and tuning <!-- .element: class="fragment" data-fragment-index="2" -->
- Model review and governance <!-- .element: class="fragment" data-fragment-index="3" -->
- Model inference and serving <!-- .element: class="fragment" data-fragment-index="4" -->
- Model monitoring <!-- .element: class="fragment" data-fragment-index="5" -->
- Automated model retraining <!-- .element: class="fragment" data-fragment-index="6" -->

---
## MLOps platform?

An MLOps platform provides data scientists and software engineers with 
a collaborative environment that facilitates iterative data exploration, 
real-time co-working capabilities for experiment tracking, feature engineering, 
and model management, as well as controlled model transitioning, deployment, and monitoring.

---
# MLFlow

---

## What is MLflow
MLflow is an open-source tool that helps you manage core parts of the machine learning lifecycle.\
It is generally used for experiment tracking, but you can also use it for reproducibility, deployment, and model registry.\
You can manage the machine learning experiments and model metadata by using CLI, Python, R, Java, and REST API.

---

## MLflow Core Components

MLFlow is tailored to assist ML practitioners throughout the various stages of ML development and deployment.\
Despite its expansive offerings, MLflow’s functionalities are rooted in several foundational components:

--

### Tracking

MLflow Tracking provides both an API and UI dedicated to the logging of parameters, 
code versions, metrics, and artifacts during the ML process.\
This centralized repository captures details such as parameters, metrics, artifacts, data, and environment configurations, 
giving teams insight into their models’ evolution over time.\
Whether working in standalone scripts, notebooks, or other environments, Tracking facilitates the logging of results either to local files or a server, 
making it easier to compare multiple runs across different users.

--

### Model Registry

A systematic approach to model management, the Model Registry assists in handling different versions of models, discerning their current state, 
and ensuring smooth productionization.\
It offers a centralized model store, APIs, and UI to collaboratively manage an MLflow Model’s full lifecycle, including model lineage, 
versioning, aliasing, tagging, and annotations.

--

### MLflow Deployments for LLMs

This server, equipped with a set of standardized APIs, streamlines access to both SaaS and OSS LLM models.\
It serves as a unified interface, bolstering security through authenticated access, and offers a common set of APIs for prominent LLMs.

--

### Evaluate

Designed for in-depth model analysis, this set of tools facilitates objective model comparison, be it traditional ML algorithms or cutting-edge LLMs.

--

### Prompt Engineering UI

A dedicated environment for prompt engineering, this UI-centric component provides a space for prompt experimentation, 
refinement, evaluation, testing, and deployment.

--

### Recipes

Serving as a guide for structuring ML projects, Recipes, while offering recommendations, 
are focused on ensuring functional end results optimized for real-world deployment scenarios.

--

### Projects

MLflow Projects standardize the packaging of ML code, workflows, and artifacts, akin to an executable.\
Each project, be it a directory with code or a Git repository, employs a descriptor or convention to define its dependencies and execution method.

---

## Why MLflow?

--

- It is easy to set up a model tracking mechanism in MLflow <!-- .element: class="fragment" data-fragment-index="0" -->
- It offers very intuitive APIs for serving <!-- .element: class="fragment" data-fragment-index="0" -->

--

- It provides data collection, data preparation, model training, and taking the model to production <!-- .element: class="fragment" data-fragment-index="0" -->
- It provides standardized components for each ML lifecycle stage, easing the development of ML applications <!-- .element: class="fragment" data-fragment-index="0" -->

--

- It can easily integrate with the most popular tools that data scientists use <!-- .element: class="fragment" data-fragment-index="0" -->
- You can deploy MLflow models to various existing tools, such as Amazon SageMaker, Microsoft’s Azure ML, and Kubernetes <!-- .element: class="fragment" data-fragment-index="0" -->

--

- It helps us save the model along with the parameters and analysis <!-- .element: class="fragment" data-fragment-index="0" -->
- MLflow models give a standard format for machine learning model packaging <!-- .element: class="fragment" data-fragment-index="0" -->

'''

# with st.sidebar:
#     st.header("Component Parameters")
#     theme = st.selectbox("Theme", ["black", "black-contrast", "blood", "dracula", "moon", "white", "white-contrast", "league", "beige", "sky", "night", "serif", "simple", "solarized"])
#     height = st.number_input("Height", value=500)
#     st.subheader("Slide Configuration")
#     content_height = st.number_input("Content Height", value=900)
#     content_width = st.number_input("Content Width", value=900)
#     scale_range = st.slider("Scale Range", min_value=0.0, max_value=5.0, value=[0.1, 3.0], step=0.1)
#     margin = st.slider("Margin", min_value=0.0, max_value=0.8, value=0.1, step=0.05)
#     plugins = st.multiselect("Plugins", ["highlight", "katex", "mathjax2", "mathjax3", "notes", "search", "zoom"], [])
#     st.subheader("Initial State")
#     hslidePos = st.number_input("Horizontal Slide Position", value=0)
#     vslidePos = st.number_input("Vertical Slide Position", value=0)
#     fragPos = st.number_input("Fragment Position", value=-1)
#     overview = st.checkbox("Show Overview", value=False)
#     paused = st.checkbox("Pause", value=False)


# ![MLflow logo](images\\MLflow_logo.png "MLflow")

currState = rs.slides(sample_markdown, 
                    height=720, 
                    theme='blood', 
                    config={
                            # "width": content_width, 
                            # "height": 720, 
                            # "minScale": scale_range[0], 
                            # "center": True, 
                            # "maxScale": scale_range[1], 
                            # "margin": margin, 
                            # "plugins": plugins
                            }, 
                    initial_state={
                                    "indexh": 0, 
                                    "indexv": 0, 
                                    "indexf": -1, 
                                    "paused": False, 
                                    "overview": False 
                                    }, 
                    markdown_props={"data-separator-vertical":"^--$"}, 
                    key="foo")