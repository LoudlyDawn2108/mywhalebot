import os
import google.generativeai as genai

GOOGLE_API_KEY = os.environ['GEMINIAPI']

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')


def generate_text(text):
  response = model.generate_content(text + "in less than 200 words")
  return response.text
