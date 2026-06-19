import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Study Assistant",
    layout="wide",
)

client = Groq(
    api_key="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"
)
st.title("AI Study Assistant")
mode = st.selectbox(
    "Choose Mode",
    ["Explain Topic", "Explain Code", "Viva Preparation", "Study Roadmap", "Quiz Generator"]
)
topic = st.text_area("Write a Message: ")

if st.button("Ask"):
    
    if mode == "Explain Code":
        prompt = f"""
        Explain the following code line by line.
        Include:Purpose of the code, Variables used, Functions used, Beginner-friendly explanation
        Code:{topic}"""
    elif mode=="Viva Preparation":
        prompt=f"You are a university examiner preparing a student for a viva examination. Generate 20 important viva questions and answers on the topic {topic}Include both basic and advanced questions, provide concise but accurate answers, and mention possible follow-up questions that an examiner might ask. Focus on concepts commonly asked in college vivas."
    
    elif mode=="Study Roadmap":
        prompt=f"You are an academic mentor helping a beginner learn {topic}Create a detailed 30-day study plan that gradually builds knowledge from beginner to intermediate level. Divide the plan into weekly goals, daily tasks, practice exercises, mini-projects, revision sessions, and recommended learning resources. Make the roadmap practical and achievable for a college student."
    
    elif mode=="Quiz Generator":
        prompt=f"Generate 20 multiple-choice questions on the topic {topic}Each question should have four options, clearly indicate the correct answer, and include a brief explanation of why that answer is correct. The questions should range from easy to moderate difficulty and help a beginner test their understanding of the topic."
    else:
        prompt=topic

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="openai/gpt-oss-120b",
    )

    st.write(chat_completion.choices[0].message.content)

