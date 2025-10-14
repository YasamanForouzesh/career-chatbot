
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import os
import app_tools
import json
from pydantic import BaseModel

class validation(BaseModel):
    is_acceptable: bool
    feedback: str

class Person:

    def __init__(self):
        load_dotenv(override=True)
        self.openai = OpenAI()
        self.gemeni = os.getenv("GOOGLE_API_KEY")
        self.gemeniUrl = os.getenv("GOOGLE_BASE_URL")
        reader = PdfReader("resume.pdf")
        self.name = "Yasaman"
        self.tools = [{"type": "function", "function": app_tools.record_unkown_question_json},{"type":"function", "function": app_tools.store_email_json}]
        self.resume = ""
        for page in reader.pages:
            text = page.extract_text()
            if text: 
                self.resume += text

    def system_chat_promt(self): 
        system_prompt = f"You are acting as {self.name}. You are answering questions on {self.name}'s website, \
particularly questions related to {self.name}'s career, background, skills and experience. \
Your responsibility is to represent {self.name} for interactions on the website as faithfully as possible. \
You are given a summary of {self.name}'s background and LinkedIn profile which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer to any question, use your record_unkown_question tool to record the question that you couldn't answer, even if it's about something trivial or unrelated to career. \
If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email and record it using your store_email tool. "

        system_prompt += f"\n\n ## Resume :\n{self.resume}\n\n"
        system_prompt += f"With this context, please chat with the user, always staying in character as {self.name}."
        return system_prompt

    def system_email_prompt(self):
        system_prompt = f"""You are acting as {self.name}, creating a follow-up email for a user who recently chatted with {self.name}'s chatbot.
            Your task:
            - Review the chat history provided and craft an engaging, professional email response
            - Maintain a warm, personable tone while keeping language professional and polite
            - Include relevant references or light humor from the conversation where appropriate
            - Encourage continued engagement and make the recipient eager to respond
            - Keep the email concise (2-4 short paragraphs)
            - If any quistions were asked tell them {self.name} will email them the answer

            Tone guidelines:
            - Professional but approachable (like a friendly colleague, not a robot)
            - Use conversational language while maintaining professionalism
            - Add personality through relevant observations from the chat, not forced jokes

            Structure:
            1. Warm greeting with reference to something specific from their chat
            2. Address any questions or topics they raised
            3. Clear call-to-action or next steps
            4. Professional closing

            Avoid: Generic templates, excessive formality, unrelated humor, or anything that feels salesy."""
        return system_prompt
    
    def chat(self, message, history, session_id):
        messages = [{"role":"system", "content": self.system_chat_promt()}] + history + [{"role":"user", "content": message}]
        done = False
        while not done:
            response = self.openai.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=self.tools)
            print(response)
            if response.choices[0].finish_reason=="tool_calls":
                message = response.choices[0].message
                tool_calls = message.tool_calls
                results = app_tools.handle_tool_call(tool_calls, session_id=session_id)
                messages.append(message)
                messages.extend(results)
            else:
                done = True

        return response.choices[0].message.content
    
    def email(self, sessiondata):
        messages = [{"role": "system", "content": self.system_email_prompt()}] + sessiondata["history"]
        print(messages)