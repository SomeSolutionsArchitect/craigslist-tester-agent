import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent, ChatOpenAI

async def main():
    file_path = 'boats-for-sale.feature.md'  # Replace with the actual path to your file

    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    agent = Agent(
        task=(
            "You are a QA Analyst helping your employer: Craigslist. "
            "Validate the following feature file and report your results. "
            "If you run into a failure, take a screenshot and include it in your report. "
            f"Here is the feature file:\n{file_content}"
        ),
        llm=ChatOpenAI(model="o3", temperature=0),
        use_vision=False
    )
    await agent.run()

asyncio.run(main())