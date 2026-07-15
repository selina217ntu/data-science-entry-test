# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer: Prompt B

# Q8b: Give TWO reasons to support your choice.
# Your answer (Reason 1): 
# Prompt B clearly separates the task into a structured format (Role, Task, Data, 
# Steps, Audience, Constraints), which makes it easier for the AI to identify exactly 
# what is expected at each stage, reducing the chance of missing a requirement.

# Your answer (Reason 2):
# Prompt B explicitly numbers the steps (1, 2, 3), which encourages the AI to address 
# each part sequentially and completely, rather than potentially glossing over one 
# aspect (like the complaints analysis) while focusing heavily on another.

# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer:
# Prompt A provides richer context and a natural narrative (e.g., who the user is, 
# why the analysis is needed, and the real-world stakes of presenting to the CEO), 
# which can help the AI calibrate tone and relevance more naturally than a purely 
# structured prompt.


# Task 2
# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.

prompt_b_improved = """
Role: You are a data analyst helping a retail marketing team.
Context: I am a marketing manager at a retail company and we have just finished 
a three-month campaign. This analysis will be presented to our CEO next Friday, 
so it needs to be clear, credible, and easy for a non-technical executive audience 
to understand.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""

# Your answer:
# I borrowed the "Context" element from Prompt A (the background story about being a 
# marketing manager and the purpose of the CEO presentation) and added it into Prompt B's 
# structured format. This strengthens Prompt B because the AI now understands not just 
# WHAT to do, but WHY it matters and WHO it's for, which helps it calibrate the tone, 
# framing, and level of detail appropriately for a CEO audience, while still keeping 
# the clarity and organisation of Prompt B's structured steps.
