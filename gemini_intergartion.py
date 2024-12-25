import google.generativeai as genai

genai.configure(api_key="AIzaSyB857ReOQDQXse3gtHtK0358g2IHKnO7ao")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)