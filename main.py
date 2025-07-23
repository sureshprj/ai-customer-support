from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
import os

from tools.get_available_products import get_available_products
from tools.get_price import get_price
from tools.offer import offer
from tools.sales_chart import generate_sales_chart

os.environ["OPENAI_API_KEY"] = "your-api-key"  # Replace with your key

llm = ChatOpenAI(temperature=0)

tools = [
    Tool(
        name="get_available_products",
        func=lambda _: ", ".join(get_available_products()),
        description="Lists all available products"
    ),
    Tool(
        name="get_price",
        func=lambda product: f"The price of {product} is ${get_price(product)}",
        description="Gets the price of a specific product"
    ),
    Tool(
        name="offer",
        func=lambda product: f"The current offer for {product} is: {offer(product)}",
        description="Returns offers for a given product"
    ),
    Tool(
        name="generate_sales_chart",
        func=lambda product: f"Chart saved to {generate_sales_chart(product)}",
        description="Generates a sales trend line graph for a given product"
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={
        "system_message": "You are a helpful Sales Agent. You answer all product-related queries such as price, availability, offers, and sales trends. Always be polite and informative."
    }
)

def run():
    print("🤖 Sales Agent Chat Bot\n(Type 'exit' to quit)\n")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        response = agent.run(query)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    run()