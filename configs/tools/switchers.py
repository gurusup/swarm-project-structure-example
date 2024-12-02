from configs.agents.types import *

def switch_to_availability_agent():
    from configs.agents.types import availability_agent
    return availability_agent

def switch_to_cancellation_agent():
    from configs.agents.types import cancellation_agent
    return cancellation_agent

def switch_to_reviews_agent():
    from configs.agents.types import reviews_agent
    return reviews_agent