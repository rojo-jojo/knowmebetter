import os
from langchain_community.document_loaders import PyPDFLoader
from llm import llm

pdf_file_path = os.path.join('data', 'Avnish_mishra_ML_Engg.pdf')
loader = PyPDFLoader(pdf_file_path)
pages = loader.load_and_split()
question_prompt = {
    "question1": "What is the name of the candidate?",
    "question2": "Give details of candidates education qualification?"
    }
prompt_instruction = "You are a resume checker. Go throught the resume text below and answer the question asked at the end. Only use the information from the resume text to answer."
resume_text = pages[1].page_content
prompt = f'''
{prompt_instruction}

Resume Text:
{resume_text[:200]}

Question: {question_prompt["question2"]}
'''
print(llm(prompt))