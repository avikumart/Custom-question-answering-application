import openai

# define a prompt
def prompt(context, query):
    header = "Answer the question as truthfully as possible using the provided context, and if the answer is not contained within the text and requires some latest information to be updated, print 'Sorry Not Sufficient context to answer query' \n"
    return header + context + "\n\n" + query + "\n"   

# feed the prompt to the model to return the answer using openai's compleation api
def get_answer(promt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=promt,
        temperature=0.5,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    return response.choices[0].text
