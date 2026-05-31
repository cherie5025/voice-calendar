# 通事舍人 · 语音历
通尔之言，舍人掌历 —— 语音驱动的智能日历助手

## 功能

| 功能 | 说明 | 示例 |
|:---|:---|:---|
| 语音输入 | 说出指令自动识别 | "明天下午3点开会" |
| 文字输入 | 键盘输入指令 | "今天有什么安排" |
| 添加日程 | 自动识别时间+事件 | "明天下午3点开会" |
| 删除日程 | 关键词匹配删除 | "删掉开会" |
| 查询日程 | 查看指定日期 | "今天有什么安排" |
| 一周预览 | 未来7天日程 | "查看一周" |
| 历史上的今天 | 返回历史事件 | "历史上的今天" |
| 农历信息 | 农历日期+节气 | "农历" |

## 技术栈

- Python 3.10 + Gradio（界面）
- Whisper（语音识别）
- DeepSeek API（意图解析）
- 本地JSON（数据存储）

## 运行

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置API Key（app.py中替换）
DEEPSEEK_API_KEY = "你的Key"

# 3. 运行
python app.py

# 4.项目结构
voice-calendar/
├── app.py           # 主程序
├── agent.py         # AI解析
├── calendar_api.py  # 日历操作
├── styles.css       # 样式
└── events.json      # 数据存储

# 5.开发周期
2026年5月29日 - 5月31日

# 6.Demo视频
链接: https://pan.baidu.com/s/1KxP-un_cKyDs5jlmUqgLEQ?pwd=1234 提取码: 1234 
