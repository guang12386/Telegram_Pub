<p align="center">
  <img src="[阿强的酒馆](https://img.st/image/photo-2025-06-16-02-42-32.jV0s)" width="400"/>
</p>

# 🍺 Pub酒馆 - 打造你的 Telegram 账号助手

> 基于 Python 的 Telegram 用户自动回复系统，关键词监听 + 实时热更新，快速打造你的专属账号助手！本项目完全开源不会有任何风险，请放心食用！

---

## 📖 项目介绍

本项目基于 Python 编写，是一个用于 Telegram 的自动回复项目。通过关键词监听，实现你的账号自动响应用户消息，适合打造客服账号、自动聊天助手、互动回复机器人等。

---

## 🛠️ 准备工作

1. **准备一台 Linux 系统的服务器**  
   推荐使用 **香港或海外 VPS**，不要选择中国大陆的服务器，因为大陆地区无法直连 Telegram。

2. **申请 Telegram API ID 与 Hash**  
   - 申请地址：[https://my.telegram.org](https://my.telegram.org)  
   - 若申请失败，请联系开发者获取帮助：[@guang8886667](http://t.me/guang8886667)

3. **具备复制粘贴基础操作能力**  
   所有命令均已提供，按步骤执行即可。

---

## 📦 使用文档

### 🔽 第一步：下载项目源码

- 将本项目压缩包下载后上传至服务器（推荐使用 [FinalShell](https://www.hostbuf.com/) 远程连接），直接拖动文件夹即可。

> ❗ 不会在服务器上解压也没关系，可以在本地解压后上传到服务器。
> 
```bash
cd 项目目录
```
---

### 🐍 第二步：安装 Python 环境（建议 Python 3.10+）

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip -y
```

---

### 🧪 第三步：创建并激活虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate
```

> 📌 **提示：每次启动前都需要激活虚拟环境：**

```bash
cd
source venv/bin/activate
```

---

### 📚 第四步：安装依赖

```bash
pip install -r requirements.txt
```

---

### 📝 第五步：配置关键词与参数

#### config.json 示例：

```json
{
  "api_id": 12345678,
  "api_hash": "your_api_hash_here",
  "enable_group": true,
  "ignore_self": true,
  "excluded_user_ids": []
}
```

#### reply.txt 示例：

```
你好=好你木不会说事吗
在吗=我在的~
天气=今天天气晴朗 ☀️
```

---

## 🚀 启动主程序

```bash
python main.py
```

首次运行将提示：

- 输入你的手机号
- 输入验证码
- 如果开启二级验证，请输入密码
- 登录成功后将自动保存 `.session` 文件并开始监听消息

---

## ✅ 测试效果

用另一个 Telegram 账号向当前账号发送关键词：

```text
你好
```

如果配置正确，将自动回复：

```text
好你木不会说事吗
```

---

## 🛡️ 守护进程运行（后台）

按下 `Ctrl + C` 会结束程序。推荐使用后台运行方式保持持续监听：

```bash
nohup python main.py &
nohup python del.py &
```

> `del.py` 是辅助文件，自动清理缓存防止内存过大。

---

## 📬 联系我们

- Telegram 联系人：[http://t.me/guang8886667](http://t.me/guang8886667)
- 如需更多功能请私信联系，功能都可以定制
- 邮箱地址：`guang8886667@gmail.com`

---

## 💖 如果你觉得本项目不错，欢迎 Star 🌟 支持我继续开发更多实用功能！
