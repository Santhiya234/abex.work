from langchain.chat_models import ChatOpenAI
import config

def generate_content(outline):
    llm = ChatOpenAI(api_key=config.OPENAI_API_KEY, model="gpt-4")

    prompt = f"Write a 2000-word blog post based on this outline:\n{outline}"
    response = llm.invoke(prompt)
    
    return response.content

if __name__ == "__main__":
    outline = "1. Introduction\n2. AI's Role in Hiring\n3. Challenges of AI in HR\n4. Future Trends"
    print(generate_content(outline))
