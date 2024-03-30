from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate       #for promptTemplate -how you want user inputs to the model to look like
from langchain.chains import LLMChain              #for langchain chains - used to assemble components
from langchain.agents import load_tools            #these 3 are for agents
from langchain.agents import initialize_agent
from langchain.agents import AgentType

load_dotenv()
# client = OpenAI(organization="org-Y3ZqZ6B28R9LPLcEuqFzLJdZ")

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7)
    prompt_tempate_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="\
            I have a {animal_type} pet and i want a cool name for it, it is {pet_color} in color.\
            Suggest for me five cool names for my pet."
    )


    name_chain = LLMChain(llm=llm, prompt=prompt_tempate_name, output_key="pet_name")
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})
    return response

def langchain_agent():
    llm = OpenAI(temperature=0.5)

    # load some tools that will perform given actions and state llm to be used
    # llm-math - math function to perform calculation on llm responses
    # wikipedia  
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    # initiate agent, specialize tools that will be providing it, llm to be used and agent type
    # verbose=True will show reasoning in the console
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    # run the agent and specify tasks to perform with this agent
    result = agent.run(
        "What is the average age of a dog? Multiply the age by 3"
    )
    print(result)


if __name__ == "__main__":
    # print(generate_pet_name("cat", "black"))
    langchain_agent()