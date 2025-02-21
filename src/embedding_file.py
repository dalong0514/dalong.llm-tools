from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings

def text_splitter(filepath, chunk_size):
    loader = TextLoader(filepath)
    docs = loader.load()

    text_splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=chunk_size,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )
    texts = text_splitter.split_documents(docs)
    return texts

def save_to_disk(texts):
    # save to disk
    vectorstore = Chroma.from_documents(
        documents=texts,
        embedding=OpenAIEmbeddings(),
        persist_directory="./chroma_db"
    )

if __name__ == "__main__":
    save_to_disk()