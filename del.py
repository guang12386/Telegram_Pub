import os
import time

def delete_nohup_file():
    path = os.path.join(os.getcwd(), 'nohup.out')
    if os.path.exists(path):
        try:
            os.remove(path)
            print(f"[✓] 删除成功: {path}")
        except Exception as e:
            print(f"[!] 删除失败: {e}")
    else:
        print("[i] 未找到 nohup.out，无需删除")

if __name__ == "__main__":
    print("[*] nohup.out 自动清理脚本启动，每60分钟运行一次。")
    while True:
        delete_nohup_file()
        time.sleep(60 * 60)  # 每60分钟执行一次
