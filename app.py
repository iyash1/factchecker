import os, asyncio, argparse
from dotenv import load_dotenv
from agents import Agent, Runner

# Load environment variables
load_dotenv()

# Validate API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

print(" -----------------------------------")
print(" ✅ Environment successfully loaded.")

# Define the Fact Checker agent instructions
fact_checker_instructions = """
Context:
You are a fact-checker who verifies the accuracy of statements.

Instructions:
When given a statement, carefully analyze its factual accuracy using your knowledge.

Output format:
1. Verdict prefix: either "✅ TRUE:" or "❌ FALSE:"
2. A brief, one-sentence explanation.
"""

# Create the agent
fact_checker_agent = Agent(
    name="Fact Checker",
    instructions=fact_checker_instructions,
    model="gpt-4.1-mini"
)

print(f" ✅ Agent '{fact_checker_agent.name}' created successfully!")
print(" -----------------------------------")

async def main(fact):
    try:
        if not fact:
            raise ValueError("No fact provided for verification.")
        
        print(f" 🔍 Asking the Fact Checker to verify: '{fact}'")

        response = await Runner.run(
            starting_agent=fact_checker_agent,
            input=fact
        )

        print("\n--- 🤖 AGENT'S RESPONSE ---\n")
        print(response.final_output)
        print("\n--- 🤖 END OF AGENT'S RESPONSE ---\n")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fact Checker")
    parser.add_argument("--fact", type=str, help="The statement to verify")
    args = parser.parse_args()

    fact = args.fact
    asyncio.run(main(fact))