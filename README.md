# Multi-Agent Research System

A lightweight Python research automation project that uses LangChain, Google Gemini, and custom agent tooling to perform web search, content scraping, report writing, and critique.

## Features

- Search agent using Tavily web search
- Reader agent for scraping and extracting web content
- Writer agent for generating structured research reports
- Critic module to review and score the report
- Simple pipeline orchestration in `src/pipelines/pipelines.py`

## Technology Used

- Python 3
- LangChain ecosystem (`langchain`, `langchain-core`, `langchain-google-genai`)
- Google Gemini via `langchain-google-genai`
- Tavily web search API via `tavily-python`
- HTML parsing and extraction with `beautifulsoup4`, `readability-lxml`, `trafilatura`
- HTTP requests with `requests`
- Environment configuration with `python-dotenv`
- Rich console output with `rich`

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd "E:\AI - 2026\Multi-Agent-Research-System"
```

2. Create and activate a Python virtual environment:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1    # PowerShell
# or
.venv\Scripts\activate.bat    # CMD
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables:

Create a `.env` file in the project root and add any required API keys, for example:

```env
TAVILY_API_KEY=your_tavily_api_key
GOOGLE_API_KEY=your_google_api_key
```

## Running the Project

Run the main entry point:

```bash
python main.py
```

The `main.py` script loads the research pipeline and runs a sample topic search and report generation.

## Project Structure

- `main.py` — application entrypoint that starts the research pipeline
- `requirements.txt` — Python dependency manifest
- `src/` — source code package
  - `src/tools/tools.py` — defines `web_search` and `scrape_url` tool functions
  - `src/agents/agents.py` — builds LangChain agents and prompt chains
  - `src/pipelines/pipelines.py` — orchestrates search, scraping, writing, and critique

## Architecture Overview

The codebase follows a simple multi-agent pipeline:

1. `build_search_agent()` creates a LangChain agent that uses the `web_search` tool.
2. `build_reader_agent()` creates a LangChain agent that uses the `scrape_url` tool.
3. `run_research_pipeline()` in `src/pipelines/pipelines.py` executes the workflow:
   - Search for relevant content
   - Scrape the top search result
   - Generate a structured research report
   - Critique the report for strengths and improvements

This keeps responsibilities separated and makes it easy to extend each stage.

## Notes

- The project is designed as an open-source style sample repo.
- Add additional tools or agents by extending `src/tools/tools.py` and updating the pipeline.
- Ensure API keys are present before running the pipeline.
