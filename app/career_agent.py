from openai import OpenAI

client = OpenAI(api_key="key")

def career_copilot(skills, query):
    prompt = f"""
You are a senior career coach for data professionals.

User profile:
- Current skills: {skills}
- Background: Data Engineer transitioning to leadership

User question:
{query}

Instructions:
- Give practical, specific advice
- Avoid generic suggestions
- If skill gap → explain WHY it matters
- If roadmap → give structured plan
- Keep it actionable

Answer clearly.
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content