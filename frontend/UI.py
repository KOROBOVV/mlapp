import requests
import streamlit as st
import plots

url = "http://127.0.0.1:8000/classify_iris"
col1, col2 = st.columns(2)

if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def set_page():
    st.session_state.page = st.session_state.nav

def home():
    st.session_state.page = 'Home'

if st.session_state.page == 'Home':
    st.sidebar.selectbox(
        "Navigation",
        ['Home', 'Classifier', 'Visualization'], 
        key='nav',
        on_change=set_page
    )
else:
    st.sidebar.button('Back to Home', on_click=home)

match st.session_state.page:
    case 'Home':
        st.title(""" Iris Classification App """)
    case 'Classifier':
        st.title('Classifier')
        
        sep_l = st.sidebar.number_input("Sepal Length")
        sep_w = st.sidebar.number_input("Sepal Width")
        pet_l = st.sidebar.number_input("Petal Length")
        pet_w = st.sidebar.number_input("Petal Width")

        if st.sidebar.button("Predict"):
    
            payload = {"sepal_length": float(sep_l), 
                "sepal_width": float(sep_w), 
                "petal_length": float(pet_l),
                "petal_width": float(pet_w)}
            try:
                r = requests.post(url=url, json=payload).json()
                st.write(f"""Your Iris is: **{r.get('class')}**\n
                            With prediction probability: {round(r.get('probability') * 100)}%
                         """)
            except:
                st.write("Something going wrong with server!\n Please reconnect")
            
    case 'Visualization':
        nav = st.sidebar.selectbox(
        "Navigation",
        ['Info','Scatter', 'Distribution', "Correlation matrix"],
    )
        if nav == "Info":
            st.title('Visualization')
        
        if nav == "Distribution":
            st.title("Distribution")
            param = st.sidebar.radio("Your parameter:", ['Sepal length', 'Sepal width', 'Petal length', 'Petal width'])
            plots.dist(param)
            
        if nav == "Scatter":
            st.title("Scatter plot")
            x = st.sidebar.selectbox("Select X", options={'Sepal length', 'Petal width', 'Petal length', 'Petal width'})
            y = st.sidebar.selectbox("Select Y", options={'Sepal length', 'Sepal width', 'Petal length', 'Petal width'})
            plots.scatter(x, y)
            
        if nav == "Correlation matrix":
            st.title("Correlation matrix")
            plots.corrmatrix()
            
                
        

    




