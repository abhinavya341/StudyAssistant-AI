def zero_shot_prompt(question):
    return f"""
Answer the following student question clearly and simply.

Question:
{question}
"""


def few_shot_prompt(question):
    return f"""
You are a study assistant.

Follow the style shown in these examples.

Example 1:
Question: What is RAM?
Answer: RAM is temporary memory used by a computer to store
data and programs that are currently being used.

Example 2:
Question: What is ROM?
Answer: ROM is memory that stores data permanently and
keeps its contents even when the computer is turned off.

Now answer this question in the same simple style:

Question: {question}
"""


def role_prompt(question):
    return f"""
You are an experienced college professor helping a beginner.

Rules:
- Use simple English.
- Explain the concept clearly.
- Give a small real-life example when useful.
- Avoid unnecessary technical words.
- Make the answer easy for a student to understand.

Student question:
{question}
"""


def mock_llm(prompt):
    """
    Temporary LLM simulation.

    Later this function will be replaced by
    a real LLM API call.
    """
    return (
        "This is a temporary AI response.\n\n"
        "The selected prompt technique was successfully "
        "processed by the Study Assistant."
    )


def answer_question(question, prompt_type):
    if prompt_type == "zero-shot":
        prompt = zero_shot_prompt(question)

    elif prompt_type == "few-shot":
        prompt = few_shot_prompt(question)

    elif prompt_type == "role":
        prompt = role_prompt(question)

    else:
        prompt = zero_shot_prompt(question)

    answer = mock_llm(prompt)

    return answer