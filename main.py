from pyrogram import Client, filters
from pyrogram.enums import ChatType
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json, os, time, threading

CONFIG_PATH = "config.json"
REPLY_PATH = "reply.txt"
SESSION_NAME = "hello_Pub"

# ========== 全局变量 ==========
config = {}
reply_dict = {}

# ========== 加载配置 ==========
def load_config():
    global config
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
    print("✅ 配置文件已重新加载")

# ========== 加载自动回复规则 ==========
def load_replies():
    global reply_dict
    reply_dict = {}
    with open(REPLY_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                reply_dict[key.strip()] = value.strip()
    print(f"✅ 自动回复规则已重新加载，共 {len(reply_dict)} 条")

# ========== 监听文件变化 ==========
class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("config.json"):
            load_config()
        elif event.src_path.endswith("reply.txt"):
            load_replies()

def start_file_watch():
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    observer.start()
    print("📡 开始监听 config.json 和 reply.txt 变更")
    threading.Thread(target=observer.join).start()

# ========== 初始化 ==========
load_config()
load_replies()
app = Client(SESSION_NAME, api_id=config["api_id"], api_hash=config["api_hash"])

@app.on_message(filters.text)
async def auto_reply(client, message):
    if message.edit_date is not None:
        return

    me = await client.get_me()
    if config.get("ignore_self", True) and message.from_user and message.from_user.id == me.id:
        return

    if message.from_user and message.from_user.id in set(config.get("excluded_user_ids", [])):
        return

    chat_type = message.chat.type.value
    if chat_type == "private" or (config.get("enable_group", True) and chat_type in ["group", "supergroup"]):
        text = message.text.strip()
        for keyword, reply in reply_dict.items():
            if keyword in text:
                await message.reply(reply)
                break

# ========== 启动 ==========
if __name__ == "__main__":
    start_file_watch()
    print("🚀 程序启动，等待消息中...")
    app.run()
