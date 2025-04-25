from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
import os

def create_agent():
    """
    Create a Langchain agent with tools and LLM.
    
    Returns:
        AgentExecutor: The configured agent executor
    """
    # Set up search tools
    tools = []
    
    # Try to use Tavily search if API key is available
    tavily_api_key = os.environ.get("TAVILY_API_KEY")
    if tavily_api_key:
        search_tool = TavilySearchResults(max_results=2, tavily_api_key=tavily_api_key)
        tools.append(search_tool)
    else:
        # Fall back to DuckDuckGo search if Tavily API key is not available
        print("Warning: TAVILY_API_KEY not found in environment variables. Using DuckDuckGo search instead.")
        search_tool = DuckDuckGoSearchRun()
        tools.append(search_tool)

    # Initialize the chat model
    # Note: Ensure your OpenAI API key is set in environment variables
    model = init_chat_model("gpt-4", model_provider="openai")

    # Create the agent executor (using the React-style interface backed by LangGraph)
    agent_executor = create_react_agent(model, tools)
    
    return agent_executor

def test_agent():
    """Test function for the agent"""
    agent_executor = create_agent()
    response = agent_executor.invoke(
        {"messages": [HumanMessage(content="What's the weather in SF?")]}
    )
    print(response["messages"][-1].content)
    
if __name__ == "__main__":
    test_agent()