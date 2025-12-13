import uuid
import boto3
from datetime import datetime
from strands import Agent
from bedrock_agentcore.memory.integrations.strands.config import AgentCoreMemoryConfig
from bedrock_agentcore.memory.integrations.strands.session_manager import (
    AgentCoreMemorySessionManager,
)

MEM_ID = "test_memory_e4a0y-ssn9eWBXio"
ACTOR_ID = "test_actor_id_%s" % datetime.now().strftime("%Y%m%d%H%M%S")
SESSION_ID = "test_session_id_%s" % datetime.now().strftime("%Y%m%d%H%M%S")


def main():
    print("Hello from agent!")

    agentcore_memory_config = AgentCoreMemoryConfig(
        memory_id=MEM_ID, session_id=SESSION_ID, actor_id=ACTOR_ID
    )

    # Create session manager
    session_manager = AgentCoreMemorySessionManager(
        agentcore_memory_config=agentcore_memory_config, region_name="ap-northeast-1"
    )

    # Create agent with session manager
    agent = Agent(
        system_prompt="You are a helpful assistant. Use all you know about the user to provide helpful responses.",
        session_manager=session_manager,
    )

    # Use the agent - conversations are automatically persisted
    agent("I like sushi with tuna")
    agent("What should I buy for lunch today?")


if __name__ == "__main__":
    main()
