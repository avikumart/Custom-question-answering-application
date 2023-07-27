# Custom-question-answering-application
A question-answering application powered by OpenAI LLM, Pinecone and Streamlit


## Overview:
- An end-to-end question-answering pipeline to chat with your data with OpenAI APIs.
- This app uses OpenAI's `text-davinci` language model to return answers based on users' queries to their data source.
- Currently, the App allows you to query web-based text content and web pdf files.
- It uses open source `sentence transformer` as a text-embedding model
- Application uses `Pinecone` vector database to store vectors of the data sources with functionality to remove existing data source when it is not in use.

### Currently Supported Data:
- Web-based text data
- PDF links

### Application link: [Click Here](https://custom-question-answering.streamlit.app/)
