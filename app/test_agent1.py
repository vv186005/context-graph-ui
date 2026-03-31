from agent import agent_answer
from graph_db import GraphDB
from vector_db import VectorDB

graph_db = GraphDB("bolt://localhost:7687", "neo4j", "abcd1234")
vector_db = VectorDB()

while True:
    query = input("\nAsk something (or type 'exit'): ")

    if query.lower() == "exit":
        break

    answer = agent_answer(query, vector_db, graph_db)
    print("\n🤖 Answer:", answer)