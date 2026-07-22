from openai import OpenAI
from openai import InternalServerError
import ast
import dotenv
dotenv.load_dotenv()
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
logpath = BASE_DIR/'logs.txt'
client = OpenAI(
    api_key=os.getenv('API'),
    base_url="https://api.gapgpt.app/v1"
)
def load_logs():
    logs = []
    with open(logpath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            logs.append(ast.literal_eval(line))
    return logs
def analyze_logs():
    logs = load_logs()
    results = []
    for log in logs:
        PROMPT = f"""You are an AI model analyzing and evaluating network logs. You will be fed the log number, timestamp of the log, source ip and log type with a raw log being the description of what the log is more definitively.
You must take this information, evaluate and give me the information i need in a dictionary format. I have provided the information and the format you need to follow below, be sure to follow it and do not say anything else. just give me the dictionary:
        {{
            "timestamp": "2026-07-21 14:32:01",
            "source_ip": "192.168.1.45",
            "log_type": "failed_login",
            "raw_log": "Failed password for root from 192.168.1.45 port 51321 ssh2",
            "severity": "high",
            "ai_summary": "Repeated failed root logins from a single IP",
            "ai_reasoning": "5 failed attempts within 2 minutes targeting the root account matches a brute-force pattern.",
            "recommended_action": "Block the IP and confirm root SSH login is disabled"
        }}
        this is the format you must follow. and here is the data you need to read and evaluate:
        {log}
"""
        response = client.responses.create(model='gapgpt-qwen-3.5', input=PROMPT)
        text = response.output_text.strip()
        try:
            parsed = ast.literal_eval(text)
            results.append(parsed)
        except (ValueError, SyntaxError):
            print(f"Couldn't parse.")
    return results