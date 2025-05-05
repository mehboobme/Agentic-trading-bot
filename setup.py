from setuptools import find_packages,setup

setup(name="agentic-trading-system",
       version="0.0.1",
       author="Mahboob",
       author_email="mehboobmeo@gmail.com",
       packages=find_packages(),
       install_requires=['pineconedb','langchain','langgraph','tavily-python','polygon']
       )