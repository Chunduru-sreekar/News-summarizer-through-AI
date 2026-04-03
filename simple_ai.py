from langchain.chat_models import init_chat_model
GOOGLE_API_KEY = "AIzaSyAAqNfxR8wboVywpI4xns1G5IDYBG51U-w"
model = init_chat_model(model="gemini-2.5-flash",
                        model_provider="google-genai",
                        api_key=GOOGLE_API_KEY
                        )
response = model.invoke("hey,how're you today?")
response_str = response.content
print(response_str)