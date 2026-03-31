# Context Graph UI

A hybrid retrieval system combining **Graph Databases (Neo4j)** and **Vector Search** to deliver context-aware, relationship-driven insights.

This project demonstrates how to:
- Combine structured relationships (Graph DB) with semantic search (Vector DB)
- Build intelligent retrieval systems beyond traditional RAG
- Visualize entity relationships through an interactive UI

🚀 Ideal for use cases like:
- HR intelligence systems
- Knowledge graphs
- Context-aware search applications

## ⚙️ Setup & Run Instructions

Follow the steps below to run the Context Graph UI project locally.

---

## 🔑 1. Get Required API Keys

### OpenAI API Key

1. Go to: https://platform.openai.com/
2. Login / Sign up
3. Navigate to **API Keys**
4. Click **Create new secret key**
5. Copy the key

---

## 🛠️ 2. Configure Environment Variables

Create a `.env` file in the root folder of the project:

```bash
touch .env

OPENAI_API_KEY=your_openai_api_key_here
NEO4J_URI=your_neo4j_uri_here
NEO4J_USER=your_neo4j_username
NEO4J_PASSWORD=your_neo4j_password

3. Where these values are used
OPENAI_API_KEY → Used in:
embedding generation
LLM response generation
NEO4J_* → Used in:
graph database connection
relationship queries

4. Install Dependencies
Backend (Python)
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

Frontend (UI)
npm install

5. Run the Application
Start Backend
python app.py
Start Frontend
npm start

6. Access the App

Open browser:

http://localhost:3000

Example Query

Try:

Find employees skilled in Python working on AI projects
Important Notes
-------------------------------------------------
Do NOT commit .env file to GitHub
Ensure Neo4j database is running before starting backend
API keys should be kept secure
How It Works
---------------------------------------------------
User enters query
Vector DB finds semantically similar entities
Graph DB expands relationships
Combined context is returned and visualized
