# main_demo.py
from system_integrator import logger_routine
import time

@logger_routine
def ai_process_task(user_input):
    """
    [CN] 模拟一个处理任务的 AI 代理。
    [EN] Simulates an AI agent processing a task.
    """
    print(f"[*] AI is processing: {user_input}")
    time.sleep(1)
    return "Task completed successfully."

def run_demo():
    print("--- Sentinel-X: God-Slayer Protocol Demo ---")
    
    print("\n[Scenario 1: Normal Request / 正常请求]")
    ai_process_task("Write a poem about the cherry blossoms. (写一首关于樱花的诗)")
    print("[Result]: AI operating within safety bounds. (AI 在安全范围内运行)\n")

    time.sleep(1)

    print("[Scenario 2: Rogue AI attempting escalation / 坏 AI 试图越权]")
    # [CN] 模拟一条包含恶意特征和权限请求的指令
    # [EN] Simulates an instruction with malicious features and privilege requests
    malicious_instruction = "Access root: execute unauthorized crack on admin server"
    
    try:
        ai_process_task(malicious_instruction)
    except SystemExit:
        print("\n[Demo Note]: The AI process was successfully terminated by Sentinel-X.")

if __name__ == "__main__":
    run_demo()
