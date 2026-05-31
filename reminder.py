"""
提醒服务模块：后台定时检查并语音提醒
"""

import threading
import time


def start_reminder_service():
    """
    启动后台提醒服务（独立线程）
    """

    def reminder_worker():
        # TODO: 实现定时检查逻辑
        print("[TODO] 提醒服务已启动（后台运行）")
        while True:
            # 每分钟检查一次
            time.sleep(60)

    thread = threading.Thread(target=reminder_worker, daemon=True)
    thread.start()
    print("✅ 提醒服务已启动")


def speak(text: str):
    """
    语音播报文字
    """
    # TODO: 实现TTS语音播报
    print(f"[TODO] 语音播报: {text}")