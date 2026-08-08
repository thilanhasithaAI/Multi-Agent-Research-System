import os
from dotenv import load_dotenv
import requests
from langchain.tools import tool
from tavily import TavilyClient
from rich import print

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """Search the web for a recent information belongs to the topic. return Title,URL and snippetes."""
   
    results = tavily.search(query=query, max_results=5)

    out = []
    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )

    return "\n----\n".join(out)

    

