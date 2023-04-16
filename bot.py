from pyrogram import Client, filters
from chatgpt import sync_ask

app = Client("my_account", api_id=123, api_hash="123")

romantic_list = []


@app.on_message(filters.command(["add", "del"], prefixes=".") & filters.outgoing)
def add_handler(client, msg):
    msg.delete()
    if msg.text == ".add" and msg.chat.id not in romantic_list:
        romantic_list.append(msg.chat.id)
        app.send_message("me", "%s added to romantic list" % msg.chat.id)
    elif msg.text == ".del" and msg.chat.id in romantic_list:
        romantic_list.remove(msg.chat.id)
        app.send_message("me", "%s deleted from romantic list" % msg.chat.id)


@app.on_message(filters.private & filters.incoming)
def from_users(client, msg):
    if msg.chat.id in romantic_list:
        answer = sync_ask(
            "Imagine that you are a romantic guy who communicates with a girl\nAll subsequent messages will be supposedly from a girl, answer them as you need to\nFirst message: %s"
            % msg.text
        )
        msg.reply(answer)


app.run()
