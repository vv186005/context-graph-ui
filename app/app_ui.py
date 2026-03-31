import streamlit as st
from graph_db import GraphDB
from vector_db import VectorDB
from agent import agent_answer
from career_agent import career_copilot

# Initialize DBs
graph_db = GraphDB("bolt://localhost:7687", "neo4j", "abcd1234")
vector_db = VectorDB()

# Page config
st.set_page_config(page_title="AI Career Copilot", layout="wide")

st.title("🚀 AI Career Copilot")

# Sidebar
st.sidebar.header("👤 Profile Insights")

skills = graph_db.get_skills()

st.sidebar.subheader("💡 Your Skills")
st.sidebar.write(skills)

# Tabs
tab1, tab2 = st.tabs(["🤖 General Assistant", "💼 Career Advisor"])

# -------- Tab 1: General AI --------
with tab1:
    st.subheader("Ask Anything")

    user_query = st.text_input("Enter your question")

    if st.button("Get Answer"):
        if user_query:
            answer = agent_answer(user_query, vector_db, graph_db)
            st.success(answer)

# -------- Tab 2: Career --------
with tab2:
    st.subheader("Career Guidance")

    career_query = st.text_input("Ask career question")

    if st.button("Get Career Advice"):
        if career_query:
            advice = career_copilot(skills, career_query)
            st.success(advice)