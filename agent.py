"""
AI智能体模块：调用DeepSeek API，将用户输入的文字解析为操作指令
"""

import json
from datetime import datetime, timedelta
from openai import OpenAI

# ===== 在这里直接填入你的 API Key =====
DEEPSEEK_API_KEY = "sk-106446aace5344de8f57d2416d923d7d"  # 把这一串换成你真实的Key
# ====================================

# 初始化DeepSeek客户端
client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

def parse_user_input(user_text: str) -> dict:
    """解析用户输入，返回结构化指令"""
    print(f"[Agent] 正在解析: {user_text}")

    # 计算日期
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    day_after = today + timedelta(days=2)

    # 使用双花括号来转义JSON中的花括号，避免format()冲突
    SYSTEM_PROMPT = f"""
你是一个智能日历助手。将用户的输入解析成JSON格式的操作指令。

当前时间：{today.strftime("%Y-%m-%d %H:%M:%S")}
今天：{today.strftime("%Y-%m-%d")}
明天：{tomorrow.strftime("%Y-%m-%d")}
后天：{day_after.strftime("%Y-%m-%d")}

输出格式（只输出JSON，不要有其他内容）：

添加事件：{{"action": "add", "time": "YYYY-MM-DD HH:MM:SS", "summary": "事件名称"}}
删除事件：{{"action": "delete", "keyword": "关键词"}}
查询事件：{{"action": "query", "date": "YYYY-MM-DD"}}

示例：
用户："明天下午3点开会"
输出：{{"action": "add", "time": "{tomorrow.strftime("%Y-%m-%d")} 15:00:00", "summary": "开会"}}

用户："删掉明天的会"
输出：{{"action": "delete", "keyword": "会"}}

用户："今天有什么安排"
输出：{{"action": "query", "date": "{today.strftime("%Y-%m-%d")}"}}
"""

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ],
            temperature=0.1
        )

        result_text = response.choices[0].message.content
        print(f"[Agent] AI返回: {result_text}")

        # 去掉可能的markdown代码块标记
        result_text = result_text.replace("```json", "").replace("```", "").strip()

        return json.loads(result_text)

    except Exception as e:
        print(f"[Agent] 错误: {e}")
        return {"action": "error", "message": str(e)}


# 测试
if __name__ == "__main__":
    test = "明天下午3点开会"
    result = parse_user_input(test)
    print(f"解析结果: {json.dumps(result, ensure_ascii=False, indent=2)}")