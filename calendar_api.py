"""
日历操作模块：增、删、查（使用本地JSON文件存储）
"""

import json
import os
from datetime import datetime

CALENDAR_FILE = "events.json"

def load_events():
    """加载所有事件"""
    if not os.path.exists(CALENDAR_FILE):
        return []
    with open(CALENDAR_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_events(events):
    """保存事件"""
    with open(CALENDAR_FILE, 'w', encoding='utf-8') as f:
        json.dump(events, f, indent=2, ensure_ascii=False)

def add_event(start_time: str, summary: str) -> str:
    """添加事件"""
    events = load_events()

    # 生成唯一ID
    event_id = str(int(datetime.now().timestamp() * 1000))

    event = {
        "id": event_id,
        "summary": summary,
        "start_time": start_time
    }

    events.append(event)
    save_events(events)

    print(f"[日历] 已添加: {summary} 在 {start_time}")
    return f"✅ 已添加：{summary} 在 {start_time}"

def delete_event_by_keyword(keyword: str) -> str:
    """根据关键词删除事件"""
    events = load_events()

    # 找出包含关键词的事件
    matched = [e for e in events if keyword.lower() in e["summary"].lower()]

    if not matched:
        return f"❌ 没有找到包含「{keyword}」的事件"

    # 删除匹配的事件
    for event in matched:
        events.remove(event)

    save_events(events)

    deleted_names = [e["summary"] for e in matched]
    return f"✅ 已删除：{', '.join(deleted_names)}"

def query_events(date: str) -> str:
    """查询某一天的所有事件"""
    events = load_events()

    # 筛选出当天的事件
    matched = [e for e in events if e["start_time"].startswith(date)]

    if not matched:
        return f"📅 {date} 没有安排任何事件"

    result = f"📅 {date} 有 {len(matched)} 个事件：\n"
    for i, e in enumerate(matched, 1):
        time_part = e["start_time"].split(" ")[1][:5]
        result += f"  {i}. {time_part} - {e['summary']}\n"

    return result

def search_events_by_keyword(keyword: str) -> list:
    """根据关键词搜索事件"""
    events = load_events()
    return [e for e in events if keyword.lower() in e["summary"].lower()]

def get_all_events() -> list:
    """获取所有事件"""
    return load_events()


# 测试代码（直接运行 python calendar_api.py 时执行）
if __name__ == "__main__":
    print("=== 测试日历功能 ===\n")

    # 测试添加
    print("1. 添加事件：")
    print(add_event("2026-05-31 15:00:00", "和产品组开会"))

    # 测试查询
    print("\n2. 查询事件：")
    print(query_events("2026-05-31"))

    # 测试删除
    print("\n3. 删除事件：")
    print(delete_event_by_keyword("开会"))

    # 再次查询确认
    print("\n4. 删除后查询：")
    print(query_events("2026-05-31"))