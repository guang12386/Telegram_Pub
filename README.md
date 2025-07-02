# Telegram_pub
本项目基于python编写 为Telegram自动回复相关项目 让你的账号可以进行一个关键词的监听 从而实现进行自动回复的功能
# 🍺 Pub酒馆 - 打造你的 Telegram 账号助手

> **关键词自动回复系统 | 基于 Python + Pyrogram | 支持热更新 + 后台运行**

---

## ✨ 项目介绍

本项目基于 Python 编写，旨在为 Telegram 用户账号提供 **关键词监听自动回复** 功能。你只需配置关键词和回复语句，机器人便会在私聊或群组中自动响应。

适合用来打造账号助手、自动客服、信息提醒等功能。

---

## 📦 功能特性

- ✅ 支持私聊 / 群组自动回复
- ✅ 支持关键词配置（reply.txt）
- ✅ 支持配置选项控制（config.json）
- ✅ 热更新：修改配置无需重启程序
- ✅ 支持虚拟环境运行，稳定性更高
- ✅ 可守护后台运行，断线不掉线

---

## 🔧 准备工作

1. 准备一台 **非大陆地区的 Linux 服务器**（推荐香港/海外 VPS）
2. 申请 Telegram API：
   - 地址：[https://my.telegram.org](https://my.telegram.org)
   - 获取 `api_id` 和 `api_hash`
   - 如果申请失败可联系：[@guang8886667](http://t.me/guang8886667)

3. 拥有基本的复制粘贴能力（本教程手把手指令）

---

## 🚀 快速启动指南（纯 Linux 系统）

### ✅ 1. 安装 Python 环境（推荐 Python 3.10+）

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip -y
