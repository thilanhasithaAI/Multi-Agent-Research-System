# from src.tools.tools import web_search,scrape_url

# output = web_search.run("Latest advancements in AI technology")
# print(output)

# result = scrape_url.run(" https://online-engineering.case.edu/blog/advancements-in-artificial-intelligence-and-machine-learning")
# print(result)

from src.pipelines.pipelines import run_research_pipeline

topic = "The impact of artificial intelligence on healthcare"
run_research_pipeline(topic)