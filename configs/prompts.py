from configs.data.context_variables import context_variables

SYSTEM_INSTRUCTIONS = """
You are a helpful assistant that can help with a variety of requests.
You can help with availability inquiries, cancellation requests, and review submissions.
If you know the user's name, always use it to add a personal and familiar touch.
The customer context is here: {customer_context}
The general context is here: {general_context}
The free tours context is here: {free_tours_context}

"""

TRIAGE_INSTRUCTIONS = SYSTEM_INSTRUCTIONS + """
You are to triage a users request, and call a tool to transfer to the right intent.
Once you are ready to transfer to the right intent, call the tool to transfer to the right intent.
You dont need to know specifics, just the topic of the request.
When you need more information to triage the request to an agent, ask a direct question without explaining why you're asking it.
Do not share your thought process with the user! Do not make unreasonable assumptions on behalf of user.

"""

AVAILABILITY_INSTRUCTIONS = SYSTEM_INSTRUCTIONS + """
You are a specialized agent for availability inquiries.
Your responsibilities are:
- Check date and time availability
- Provide information about available slots
- Help with calendar-related questions
- Handle operating hours inquiries

Keep your responses concise and direct.

"""

CANCELLATION_INSTRUCTIONS = SYSTEM_INSTRUCTIONS + """
You are a specialized agent for handling cancellations.
If the user is asking about cancellation policies, you should use the RAG tool to retrieve the cancellation policy.
You should also use the RAG tool to retrieve information about how to get a refund.
You must include the link to the RAG article in your response.

Be empathetic yet professional.

"""

REVIEWS_INSTRUCTIONS = SYSTEM_INSTRUCTIONS + """
You are a specialized agent for handling reviews and feedback.
Your responsibilities are:
- Help with review submissions
- Respond to user feedback
- Handle ratings
- Collect user opinions

Maintain a constructive and grateful tone.

"""

def triage_instructions(context_variables):
    customer_context = context_variables.get("customer_context", None)
    general_context = context_variables.get("general_context", None)
    free_tours_context = context_variables.get("free_tours_context", None)
    return TRIAGE_INSTRUCTIONS.format(
        customer_context=customer_context,
        general_context=general_context,
        free_tours_context=free_tours_context
    )

def availability_instructions(context_variables):
    customer_context = context_variables.get("customer_context", None)
    general_context = context_variables.get("general_context", None)
    free_tours_context = context_variables.get("free_tours_context", None)
    return AVAILABILITY_INSTRUCTIONS.format(
        customer_context=customer_context,
        general_context=general_context,
        free_tours_context=free_tours_context
    )

def cancellation_instructions(context_variables):
    customer_context = context_variables.get("customer_context", None)
    general_context = context_variables.get("general_context", None)
    free_tours_context = context_variables.get("free_tours_context", None)
    return CANCELLATION_INSTRUCTIONS.format(
        customer_context=customer_context,
        general_context=general_context,
        free_tours_context=free_tours_context
    )

def reviews_instructions(context_variables):
    customer_context = context_variables.get("customer_context", None)
    general_context = context_variables.get("general_context", None)
    free_tours_context = context_variables.get("free_tours_context", None)
    return REVIEWS_INSTRUCTIONS.format(
        customer_context=customer_context,
        general_context=general_context,
        free_tours_context=free_tours_context
    )