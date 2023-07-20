import pinecone
from sentence_transformers import SentenceTransformer

# initiate the model object
model = SentenceTransformer('all-MiniLM-L6-v2')

pinecone.init(api_key="api_key", environment='env')
index = pinecone.Index("Index_name")

# load the corpus and encode each chunks
def encodeaddData(corpusData, url, pdf):
    id = index.describe_index_stats(["total_vector_count"])
    if url == True:
        for i in range(len(corpusData)):
            chunk = corpusData[i]
            chunkInfo=(str(id+i),
                    model.encode(chunk).tolist(),
                    {'title':url,'context':chunk})
            index.upsert(vectors=[chunkInfo])
    if pdf == True:
        for i in range(len(corpusData)):
            chunk = corpusData[i]
            chunkInfo=(str(id+i),
                    model.encode(chunk).tolist(),
                    {'title':pdf,'context':chunk})
            index.upsert(vectors=[chunkInfo])
    
# find the best match from index    
def find_k_best_match(query,k):
    query_em = model.encode(query).tolist()
    result = index.query(query_em, top_k=k, includeMetadata=True)
    
    return [result['matches'][i]['metadata']['title'] for i in range(k)],[result['matches'][i]['metadata']['context'] for i in range(k)]
        