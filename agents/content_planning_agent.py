from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import config

def generate_outline(topic):
    llm = ChatOpenAI(api_key=config.OPENAI_API_KEY, model="gpt-4")

    prompt = PromptTemplate(
        input_variables=["topic"],
        template="Generate a detailed blog outline for the topic: {topic}. Include main headings and subheadings."
    )

    response = llm.invoke(prompt.format(topic=topic))
    return response.content

if __name__ == "__main__":
    print(generate_outline("AI in Hiring"))
