from openai import OpenAI
import json
import re

client = OpenAI(api_key="key")

def normalize(text):
    return text.strip().title()

def extract_triples(text):
    prompt = f"""
You are an expert resume parser.

Extract structured knowledge triples from the resume text.

Focus ONLY on:
- Skills
- Tools
- Companies
- Roles
- Education

Rules:
- Output ONLY JSON list
- Format: ["subject", "relation", "object"]
- Use relations:
    HAS_SKILL
    USED_TOOL
    WORKED_AT
    WORKED_AS
    STUDIED_AT
- Subject must be "Vineeta"
- No explanation, no markdown

Text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content.strip()

    # 🔥 REMOVE markdown if present
    content = re.sub(r"```json", "", content)
    content = re.sub(r"```", "", content)

    try:
        triples = json.loads(content)
    except Exception as e:
        print("⚠️ JSON parsing failed:", content)
        triples = []

    return triples


def ingest(text, graph_db, vector_db):
    triples = extract_triples(text)

    print("\n📄 TEXT:", text[:100])
    print("🔗 TRIPLES:", triples)

    for triple in triples:
        if len(triple) == 3:
            s, r, o = triple

            s = normalize(s)
            r = normalize(r)
            o = normalize(o)

            print(f"➡️ Adding: {s} - {r} -> {o}")

            graph_db.add_relation(s, r, o)

    vector_db.add(text)