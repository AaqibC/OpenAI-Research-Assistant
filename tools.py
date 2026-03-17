from datetime import datetime
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


@tool
def save_text_to_file(data: str, filename: str = "research_output.txt") -> str:
    """Save the research output to a text file with a timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


search_tool = DuckDuckGoSearchRun()

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

tools = [save_text_to_file, search_tool, wiki_tool]