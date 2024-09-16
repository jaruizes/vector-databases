import chromadb
import chromadb.utils.embedding_functions as embedding_functions

chroma_client = chromadb.Client()
default_ef = embedding_functions.DefaultEmbeddingFunction()

collection_name = "test_collection"
collection = chroma_client.create_collection(collection_name, embedding_function=default_ef)

documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "How are you?"},
    {"id": "doc3", "text": "Bye, have a nice day!"},
]

for document in documents:
    collection.upsert(ids=[document["id"]], documents=document["text"])

query_texts = "Hello, how are you?"

results = collection.query(query_texts=query_texts, n_results=3)

print(results)
