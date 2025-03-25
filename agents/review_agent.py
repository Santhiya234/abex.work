from langchain.chat_models import ChatOpenAI
import config

def review_content(content):
    llm = ChatOpenAI(api_key=config.OPENAI_API_KEY, model="gpt-4")

    prompt = f"Review and improve the following blog post for grammar, readability, and flow:\n{content}"
    response = llm.invoke(prompt)
    
    return response.content

if __name__ == "__main__":
    print(review_content("AI in hiring is the future. It helps in recruitment."))
