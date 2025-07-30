# ingest.py
from llama_index import download_loader, GPTSimpleVectorIndex

# 1. Load your website content via sitemap or URL
WebReader = download_loader("WebPageReader")
loader = WebReader()
docs = loader.load_data(urls=["https://test.fhg.global/sitemap.xml"])

# 2. Build and save the vector index
index = GPTSimpleVectorIndex(docs)
index.save_to_disk("index.json")
