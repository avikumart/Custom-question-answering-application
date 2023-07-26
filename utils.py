import requests
from bs4 import BeautifulSoup
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


# html functions to load data from any web url
def get_html_content(url):
    response = requests.get(url)
    return response.content 

# get the text from html content
def get_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

# recursive text splitter
def split_docs(text, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_text(text)
    return texts

# get text chunks from web url func
def scrape_text(url, max_chars=1000):
    html_content = get_html_content(str(url))
    text = get_text_from_html(html_content)
    chunks = split_docs(text, chunk_size=max_chars)
    return chunks

# pdf loader using langchain pypdf loader
def pdf_loader(pdf):
    loader = PyPDFLoader(pdf)
    pages = loader.load_and_split() # load and split to get chunks
    return pages  

# split pdf docs
def split_documents(text, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(text)
    return texts

# get text from pdf url
def pdf_text(pdf, max_chars=1000):
    pages = pdf_loader(pdf)
    chunks = split_documents(pages,chunk_size=max_chars)
    return [list(p)[0][1] for p in chunks]        