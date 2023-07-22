import pinecone
from sentence_transformers import SentenceTransformer

# initiate the model object
model = SentenceTransformer('all-MiniLM-L6-v2')

# initilize the pinecone
pinecone.init(api_key="1983f7f1-4a49-469b-aa7f-e2f2e7bf9874", environment='us-west1-gcp-free')
index = pinecone.Index("langchain-qa-index")

# load the corpus and encode each chunks
def encodeaddData(corpusData, url, pdf):
    id = index.describe_index_stats()["total_vector_count"]
    if url:
        for i in range(len(corpusData)):
            chunk = corpusData[i]
            chunkInfo=(str(id+i),
                    model.encode(chunk).tolist(),
                    {'title':url,'context':chunk})
            index.upsert([chunkInfo])
    if pdf:
        for i in range(len(corpusData)):
            chunk = corpusData[i]
            chunkInfo=(str(id+i),
                    model.encode(chunk).tolist(),
                    {'title':pdf,'context':chunk})
            index.upsert([chunkInfo])
    
# find the best match from index    
def find_k_best_match(query,k):
    query_em = model.encode(str(query)).tolist()
    result = index.query(query_em, top_k=k, includeMetadata=True)
    
    return [result['matches'][i]['metadata']['title'] for i in range(k)],[result['matches'][i]['metadata']['context'] for i in range(k)]
        