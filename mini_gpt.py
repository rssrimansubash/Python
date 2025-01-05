import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_FOR_GEMINI")
model = genai.GenerativeModel("gemini-1.5-flash")

qn = input("Message for GPT : ")
response = model.generate_content(qn)
print(response.text)
