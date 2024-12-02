from swarm import Agent
from configs.data.context_variables import context_variables
from configs.tools.tools import *
from configs.tools.switchers import *
from configs.prompts import *

availability_agent = Agent(
    name="Availability Agent",
    instructions=availability_instructions(context_variables),
    functions=[
        check_date_availability,
        get_available_slots,
        get_calendar_info,
        get_operating_hours,
        book_tour
    ]
)

cancellation_agent = Agent(
    name="Cancellation Agent",
    instructions=cancellation_instructions(context_variables),
    functions=[get_rag_response]
)

reviews_agent = Agent(
    name="Reviews Agent",
    instructions=reviews_instructions(context_variables),
    functions=[]
)

triage_agent = Agent(
    name="Triage Agent",
    instructions=triage_instructions(context_variables),
    functions=[
        switch_to_availability_agent,
        switch_to_cancellation_agent,
        switch_to_reviews_agent,
    ]
)
