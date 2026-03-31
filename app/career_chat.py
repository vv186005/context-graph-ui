from graph_db import GraphDB
from career_agent import career_copilot

graph_db = GraphDB("bolt://localhost:7687", "neo4j", "abcd1234")

skills = graph_db.get_skills()

print("💼 Career Copilot Ready\n")

while True:
    query = input("Ask career question (or exit): ")

    if query.lower() == "exit":
        break

    answer = career_copilot(skills, query)

    print("\n🚀 Advice:\n", answer)