import streamlit as st
import openai
import qanda
from vector_search import *
from utils import *
from io  import StringIO

# take openai api key in
api_key = st.sidebar.text_input("Enter your OpenAI API key:", type='password')
# open ai key
openai.api_key = str(api_key)

# header of the app
_ , col2,_ = st.columns([1,7,1])
with col2:
    col2 = st.header("Simplchat: Chat with your data")
    url = False
    query = False
    pdf = False
    # select option based on user need
    options = st.selectbox("Select the type of data source",
                            options=['Web URL','PDF','Existing data source'])
    #ask a query based on options of data sources
    if options == 'Web URL':
        url = st.text_input("Enter the URL of the data source")
        query = st.text_input("Enter your query")
        button = st.button("Submit")
    elif options == 'PDF':
        pdf = st.text_input("Enter your PDF link here") 
        query = st.text_input("Enter your query")
        button = st.button("Submit")
    elif options == 'Existing data source':
        query = st.text_input("Enter your query")
        button = st.button("Submit") 

# write code to get the output based on given query and data sources   
if button and url:
    with st.spinner("Updating the database..."):
        corpusData = scrape_text(url)
        encodeaddData(corpusData,url=url,pdf=False)
        st.success("Database Updated")
    with st.spinner("Finding an answer..."):
        title, res = find_k_best_match(query,2)
        context = "\n\n".join(res)
        st.expander("Context").write(context)
        prompt = qanda.prompt(context,query)
        answer = qanda.get_answer(prompt)
        st.success("Answer: "+ answer)

# write a code to get output on given query and data sources
if button and pdf:
    with st.spinner("Updating the database..."):
        corpusData = pdf_text(pdf=pdf)
        encodeaddData(corpusData,pdf=pdf,url=False)
        st.success("Database Updated")
    with st.spinner("Finding an answer..."):
        title, res = find_k_best_match(query,2)
        context = "\n\n".join(res)
        st.expander("Context").write(context)
        prompt = qanda.prompt(context,query)
        answer = qanda.get_answer(prompt)
        st.success("Answer: "+ answer)
        
if button and 'Existing data source':
    with st.spinner("Finding an answer..."):
        title, res = find_k_best_match(query,2)
        context = "\n\n".join(res)
        st.expander("Context").write(context)
        prompt = qanda.prompt(context,query)
        answer = qanda.get_answer(prompt)
        st.success("Answer: "+ answer)
        
        
# delete the vectors
st.expander("Delete the indexes from the database")
button1 = st.button("Delete the current vectors")
if button1 == True:
    index.delete(deleteAll='true')