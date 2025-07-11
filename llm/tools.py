from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.document_loaders import UnstructuredURLLoader

search = DuckDuckGoSearchRun()
web_search_tool = Tool(
    name="WebSearch",
    func=search.run,
    description="Useful for searching general information on the internet about a topic."
)


def get_url_content(url: str) -> str:
    """Extracts the main text from a URL."""
    try:
        loader = UnstructuredURLLoader(urls=[url])
        docs = loader.load()
        if docs:
            return "\n".join([doc.page_content for doc in docs])
        return "No content found at the URL."
    except Exception as e:
        return f"Error loading URL: {e}"

read_url_tool = Tool(
    name="ReadURL",
    func=get_url_content,
    description="Useful for reading the content of a specific web page given its URL."
)

tools_list = [web_search_tool, read_url_tool]