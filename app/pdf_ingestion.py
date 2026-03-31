#from langchain.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import Docx2txtLoader
#from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from vector_db import VectorDB
from graph_db import GraphDB
from ingestion import ingest  # your LLM triple extractor

# Initialize DBs
graph_db = GraphDB("bolt://localhost:7687", "neo4j", "abcd1234")
vector_db = VectorDB()

# 1. Load document
loader = Docx2txtLoader("C:/Users/LENOVO/context-graph-ai/Vineeta_Vijaykumar.docx")
documents = loader.load()

# 2. Split
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

print(f"Total chunks: {len(chunks)}")

# 3. Process each chunk
for chunk in chunks:
    text = chunk.page_content

    # Store in vector DB
    vector_db.add(text)

    # Extract and store graph knowledge
    ingest(text, graph_db, vector_db)

print("✅ PDF ingestion complete")