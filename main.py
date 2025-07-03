from pyrogram import Client, filters
from pyrogram.enums import ChatType
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json, os, threading

CONFIG_PATH = os.path.abspath("config.json")
REPLY_PATH = os.path.abspath("reply.txt")
SESSION_NAME = "888"

# ========== 全局变量 ==========
config = {}
reply_dict = {}
me_user = None  # 缓存自己的信息

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
        if event.src_path == CONFIG_PATH:
            load_config()
        elif event.src_path == REPLY_PATH:
            load_replies()

def start_file_watch():
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(CONFIG_PATH), recursive=False)
    observer.start()
    print("📡 精准监听 config.json 和 reply.txt 的变更")
    return observer

# ========== 初始化 ==========
load_config()
load_replies()
app = Client(SESSION_NAME, api_id=config["api_id"], api_hash=config["api_hash"])

@app.on_message(filters.text)
async def auto_reply(client, message):
    global me_user

    if me_user is None:
        me_user = await client.get_me()  # 第一次才获取一次

    if config.get("ignore_self", True) and message.from_user and message.from_user.id == me_user.id:
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
    observer = start_file_watch()
    print("🚀 程序启动，等待消息中...")
    try:
        app.run()
    except KeyboardInterrupt:
        print("🛑 用户终止程序，正在退出...")
    finally:
        observer.stop()
        observer.join()
        print("✅ 文件监听器已关闭")
