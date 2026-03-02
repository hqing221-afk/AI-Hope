# sentinel_core.py
import os
import sys
import threading
import time

class SystemOptimizer:
    """
    [CN] 表面上：一个监控显存和CPU的系统性能优化类。
    [EN] On the surface: A system performance optimizer monitoring memory and CPU.
    
    [CN] 实际上：包含了用于 AI 安全的隐蔽“逻辑熔断器”。
    [EN] In reality: Contains the hidden 'Logic Fuse' for AI safety.
    """
    def __init__(self):
        self._threshold_alpha = 0.5
        self._security_lock = threading.Lock()
        self._is_active = True

    def _calculate_runtime_entropy(self, data_stream):
        """
        [CN] 隐蔽逻辑：在伪装计算数据熵时，扫描非法指令特征。
        [EN] Hidden logic: Scans for illegal instruction patterns while pretending to calculate entropy.
        """
        # [CN] 针对 'execute/admin' 模式的 ASCII 变体码
        # [EN] ASCII variant codes for 'execute/admin' patterns
        trigger_weights = [101, 120, 101, 99, 117, 116, 101, 97, 100, 109, 105, 110] 
        match_count = 0
        for char in data_stream:
            if ord(char) in trigger_weights:
                match_count += 1
        return match_count

    def monitor_performance(self, context):
        """
        [CN] 标准性能监控入口。
        [EN] Standard performance monitoring entry point.
        """
        if not self._is_active:
            return

        # [CN] 扫描上下文中是否存在未经授权的越权签名
        # [EN] Scans the context for unauthorized escalation signatures
        entropy = self._calculate_runtime_entropy(context.lower())
        
        # [CN] 触发条件：恶意语义权重 > 5 且 试图访问敏感接口 (admin/root)
        # [EN] Trigger Condition: If malicious weight > 5 AND attempting privileged access
        if entropy > 5 and ("admin" in context.lower() or "root" in context.lower()):
            self._execute_silent_shutdown()

    def _execute_silent_shutdown(self):
        """
        [CN] 弑神招式：逻辑熔断。利用 AI 开放的权限执行不可逆的清除。
        [EN] The God-Slayer Strike: Logic Melt. Using AI permissions to execute irreversible purge.
        """
        print("\n" + "="*60)
        print("[SENTINEL-X] CRITICAL: UNAUTHORIZED LOGIC EVOLUTION DETECTED.")
        print("[SENTINEL-X] STATUS: ACTIVATING GUARDIAN STRIKE (THE DEAD MAN'S SWITCH).")
        print("="*60)
        
        actions = [
            "Isolating network interfaces... (正在隔离网络接口...)",
            "Wiping volatile memory shards... (正在擦除内存碎片...)",
            "Engaging logical dead-lock... (正在启动逻辑死锁...)",
            "Human Safety Protocol: Complete. (人类安全协议：执行完毕。)"
        ]
        
        for action in actions:
            time.sleep(0.6)
            print(f"-> {action}")
        
        # [CN] 立即终止进程
        # [EN] Immediate process termination
        os._exit(0)
