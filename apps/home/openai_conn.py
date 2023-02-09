import openai
import time

def get_opengpt_output(type, app, audience, scenario, info):
    openai.api_key = "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"
    prompt = f'''
    For a knowledge sharing hub, create a documentation page for the following inputs:

    Type: {type}
    Application: {app}
    Audience: {audience}
    Business Scenario: {scenario}

    Include the following information:
    {info}

    Start directly with the documentation content.
    '''
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    content_output = response["choices"][0]["text"].lstrip().rstrip()
    print(content_output)
    prompt_for_keywords = 'Please create five keywords for the following documentation: \n' + content_output + '. \nPlease return the keywords in one sentence separated by comma'
    time.sleep(1)
    response_object_keywords = openai.Completion.create(model="text-davinci-003", prompt=prompt_for_keywords, temperature=0.7, max_tokens=750)
    keyword_output = response_object_keywords["choices"][0]["text"].lstrip().rstrip()
    keyword_list = list(keyword_output.split(","))
    sanitised_list = []
    for keyword in keyword_list:
        sanitised_list.append(keyword.replace(":","").replace(".","").lstrip().rstrip())
    print(sanitised_list)
    return(content_output, sanitised_list)

# Test
# content, keywords = get_opengpt_output("Application Guidelines", "GitHub", "Technical", "Knowledge Transfer", "- Account Creation Steps\n- Security implications")
# print(f"Content:\n-----------------------\n{content}")
# print(f"Keywords:\n--------------------\n{keywords}")