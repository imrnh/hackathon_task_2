import os, json
from dotenv import load_dotenv
from gradio_client import Client
import requests

load_dotenv()

HF_TOKEN = os.getenv('HF_TOKEN')

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
 
def chatbot(user_prompt, sys_msg):   
    output = query({
        "inputs": f"""
            System Message: {sys_msg}
            User Message: {user_prompt}."""
    })
    
    out_res = output[0]['generated_text'].replace("name': '", "")
    out_res = out_res.replace("'", "")
    return {
        "User Message": user_prompt,
        "AI Message": "You can cook " + out_res
    }
