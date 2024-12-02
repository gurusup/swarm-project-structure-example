from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing_extensions import List
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import Html2TextTransformer

class InMemoryRag:
  def __init__(self, embedding_model="text-embedding-3-large"):
      self.embeddings = OpenAIEmbeddings(model=embedding_model)
      self.vector_store = InMemoryVectorStore(self.embeddings)
      
  def load_and_index_urls(self, urls: List[str], chunk_size: int = 1000, chunk_overlap: int = 200) -> None:
      all_splits = []

      loader = AsyncChromiumLoader(urls, user_agent="MyAppUserAgent")
      docs = loader.load()

      html2text = Html2TextTransformer()
      docs_transformed = html2text.transform_documents(docs)

      text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap
      )

      splits = text_splitter.split_documents(docs_transformed)
      all_splits.extend(splits)

      self.vector_store.add_documents(documents=all_splits)
  
  def retrieve(self, question: str) -> List[Document]:
      retrieved_docs = self.vector_store.similarity_search(question)
      return retrieved_docs