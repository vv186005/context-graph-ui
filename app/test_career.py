from graph_db import GraphDB
from career_agent import skill_gap_analysis

graph_db = GraphDB("bolt://localhost:7687", "neo4j", "abcd1234")

skills = graph_db.get_skills()

result = skill_gap_analysis(skills)

print("\n🚀 Career Advice:\n", result)