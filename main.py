from browser_use import Agent, ChatGoogle
from dotenv import load_dotenv
load_dotenv()

# this is the automation part where once you run it after you configure the prompt.md file according to your use case
# it will generate a csv file with the papers and the pdf links which is used to download the pdfs according to the csv format specified
# change the prompt.md file accordingly before the execution
# the csv file will be made in the temp directory in filesystem open it from there and save it here with desired name
# the csv file will be used to download the pdfs from the downloadpdfs.py file to download all the pdfs

with open("prompt.md", "r", encoding="utf-8") as f:
    prompt = f.read()

agent = Agent(
    task=f"{prompt}",
    llm=ChatGoogle(model="gemini-flash-latest")
)
agent.run_sync()