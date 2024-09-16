import chromadb
chroma_client = chromadb.Client()

collection_name = "test_collection"
collection = chroma_client.create_collection(collection_name)

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
