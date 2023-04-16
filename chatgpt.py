from revChatGPT.V3 import Chatbot


chatbot = Chatbot(api_key="<api_key>")


def sync_ask(message) -> str:
    for response in chatbot.ask(message):
        responseMessage = response["message"]

    return responseMessage
