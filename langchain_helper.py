from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

def generate_resume_descriptor(Key_words):
    #1. create model
    model = ChatOpenAI(temperature=0.7)
    #2. create parser
    parser = StrOutputParser()
    #3. Create prompt template
    prompt_template_name = ChatPromptTemplate([
            ('user', "Create Job Desciption with given key words. I have input of keywords {Key_words}. I want a resume description with the sections: Job Description, Key Responsibilities, What are the Mandatory skills and skill proficiencies required for this position, What are the Optional skills and skill proficiencies for this position. Any other if needed")
        #('human', "I have a Role {Role} with Mondatory_skills {Mondatory_skills} and Optional skills {Optional_skills} and I want a resume description for this")

            ])
    name_chain = prompt_template_name | model | parser

    #response = name_chain.invoke({'Role':Role}, {'Mondatory_skills':Mondatory_skills}, {'Optional_skills':Optional_skills})
    response = name_chain.invoke({'Key_words':Key_words})


    return response

