#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Subterfuge - The Ultimate Hacker Simulator
Make it look like you're doing something incredibly important!
"""

import random
import time
import sys
import threading
from datetime import datetime

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import locale
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')

class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

class HackerSimulator:
    def __init__(self):
        self.running = True

        # ASCII Art Gallery
        self.ascii_art = {
            'wopr': """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║   ██╗    ██╗ ██████╗ ██████╗ ██████╗                        ║
    ║   ██║    ██║██╔═══██╗██╔══██╗██╔══██╗                       ║
    ║   ██║ █╗ ██║██║   ██║██████╔╝██████╔╝                       ║
    ║   ██║███╗██║██║   ██║██╔═══╝ ██╔══██╗                       ║
    ║   ╚███╔███╔╝╚██████╔╝██║     ██║  ██║                       ║
    ║    ╚══╝╚══╝  ╚═════╝ ╚═╝     ╚═╝  ╚═╝                       ║
    ║                                                              ║
    ║          WAR OPERATION PLAN RESPONSE SYSTEM                 ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
            """,
            'skull': """
                       .--.
                      /.-. '----------.
                      \\'-' .--"--""-"-'
                       '--'

                   ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗
                   ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
                   ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
                   ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
                   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
                   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
            """,
            'matrix': """
            ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗
            ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝
            ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝
            ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗
            ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
            """,
            'cyber': """
    ╔═══════════════════════════════════════════════════════════╗
    ║  ___  _  _  ___  ___  ___    __   ___  __  ___  ___      ║
    ║ / __|| || || _ )|   || _ \\  /  \\ / _ \\/ _|| __||   \\     ║
    ║( (__  \\_. || _ \\| - || v / ( () )  _/\\_ \\| _| | - |     ║
    ║ \\___|  |__||___/|___||_|_\\  \\__/|_|  |__/|___||_|_|     ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
            """
        }

        self.code_snippets = [
            "def decrypt_mainframe(payload):\n    return hashlib.sha256(payload).hexdigest()",
            "async function bypasFirewall() {\n    const encrypted = await crypto.subtle.encrypt(...);\n}",
            "SELECT * FROM users WHERE access_level > 9000;",
            "import neural_network\nmodel.train(epochs=1000, learning_rate=0.001)",
            "docker build -t quantum-compiler:latest .",
            "git commit -m 'Refactored the flux capacitor'",
            "npm install --save @hacker/elite-tools",
            "class QuantumEncryptor:\n    def __init__(self, key):\n        self.cipher = AES.new(key)",
            "curl -X POST https://api.mainframe.corp/inject",
            "terraform apply -auto-approve",
            "kubectl scale deployment/critical-systems --replicas=100",
            "pipeline {\n    agent any\n    stages { ... }\n}",
        ]

        self.operations = [
            "Compiling neural pathways",
            "Decrypting blockchain ledger",
            "Bypassing firewall",
            "Injecting payload",
            "Establishing secure tunnel",
            "Optimizing quantum algorithms",
            "Synchronizing distributed nodes",
            "Analyzing packet streams",
            "Cracking encryption keys",
            "Deploying stealth protocols",
            "Mapping network topology",
            "Initializing AI modules",
            "Calibrating flux capacitors",
            "Mining cryptocurrency",
            "Refactoring legacy systems",
            "Compiling kernel modules",
            "Training deep learning models",
            "Scanning for vulnerabilities",
            "Establishing VPN tunnels",
            "Reticulating splines",
        ]

        self.files = [
            "mainframe_access.py", "neural_net.cpp", "blockchain.rs",
            "encryption_keys.dat", "firewall_bypass.sh", "payload.bin",
            "quantum_compiler.go", "ai_trainer.py", "network_map.json",
            "secret_data.enc", "exploit.c", "backdoor.asm",
        ]

        self.ips = [
            f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            for _ in range(20)
        ]

    def matrix_rain(self, duration=3):
        """Matrix-style falling characters"""
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()_+-=[]{}|;:,.<>?"
        start = time.time()
        while time.time() - start < duration:
            line = ''.join(random.choice(chars) for _ in range(80))
            color = random.choice([Colors.GREEN, Colors.CYAN])
            print(f"{color}{line}{Colors.RESET}")
            time.sleep(0.05)

    def progress_bar(self, operation, duration=None):
        """Animated progress bar"""
        if duration is None:
            duration = random.uniform(2, 6)

        steps = 50
        delay = duration / steps

        print(f"\n{Colors.CYAN}[*] {operation}...{Colors.RESET}")

        for i in range(steps + 1):
            percent = (i / steps) * 100
            filled = int(i * 40 / steps)
            bar = '█' * filled + '░' * (40 - filled)

            # Random status messages
            if i % 10 == 0 and i > 0:
                status = random.choice([
                    "Processing...", "Analyzing...", "Computing...",
                    "Validating...", "Optimizing...", "Executing..."
                ])
                print(f"\r{Colors.GREEN}  [{bar}] {percent:.1f}% - {status}{Colors.RESET}", end='', flush=True)
            else:
                print(f"\r{Colors.GREEN}  [{bar}] {percent:.1f}%{Colors.RESET}", end='', flush=True)

            time.sleep(delay)

        print(f"\n{Colors.GREEN}  [✓] Complete!{Colors.RESET}\n")

    def typing_effect(self, text, speed=0.03):
        """Simulate typing"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()

    def scroll_code(self):
        """Scroll random code snippets"""
        print(f"\n{Colors.YELLOW}{'='*80}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}>>> EXECUTING CODE BLOCK{Colors.RESET}")
        print(f"{Colors.YELLOW}{'='*80}{Colors.RESET}\n")

        snippet = random.choice(self.code_snippets)
        for line in snippet.split('\n'):
            print(f"{Colors.GREEN}{line}{Colors.RESET}")
            time.sleep(0.3)

        print(f"\n{Colors.GREEN}[✓] Execution successful{Colors.RESET}")
        time.sleep(1)

    def fake_logs(self):
        """Generate fake log messages"""
        log_types = ["INFO", "DEBUG", "WARN", "SUCCESS"]
        messages = [
            "Connection established to remote server",
            "Authentication token refreshed",
            "Data packet received",
            "Checksum verified",
            "Cache invalidated",
            "Resource allocated",
            "Process forked successfully",
            "Memory optimization complete",
            "Thread pool expanded",
            "Lock acquired on critical section",
        ]

        for _ in range(random.randint(5, 10)):
            log_type = random.choice(log_types)
            message = random.choice(messages)
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            ip = random.choice(self.ips)

            color = {
                "INFO": Colors.CYAN,
                "DEBUG": Colors.DIM,
                "WARN": Colors.YELLOW,
                "SUCCESS": Colors.GREEN
            }[log_type]

            print(f"{Colors.DIM}[{timestamp}]{Colors.RESET} {color}[{log_type}]{Colors.RESET} {message} ({ip})")
            time.sleep(random.uniform(0.1, 0.5))

    def system_stats(self):
        """Display fake system statistics"""
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}╔════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.MAGENTA}║       SYSTEM STATUS MONITOR          ║{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.MAGENTA}╚════════════════════════════════════════╝{Colors.RESET}\n")

        cpu = random.randint(60, 99)
        mem = random.randint(70, 95)
        net = random.randint(100, 9999)
        threads = random.randint(500, 2000)

        print(f"{Colors.CYAN}  CPU Usage:        {Colors.GREEN}{cpu}%{Colors.RESET}")
        print(f"{Colors.CYAN}  Memory Usage:     {Colors.GREEN}{mem}%{Colors.RESET}")
        print(f"{Colors.CYAN}  Network Traffic:  {Colors.GREEN}{net} Mb/s{Colors.RESET}")
        print(f"{Colors.CYAN}  Active Threads:   {Colors.GREEN}{threads}{Colors.RESET}")
        print(f"{Colors.CYAN}  Processes:        {Colors.GREEN}{random.randint(200, 500)}{Colors.RESET}\n")

    def file_operations(self):
        """Simulate file operations"""
        operations = ["Encrypting", "Decrypting", "Compiling", "Analyzing", "Transferring"]
        op = random.choice(operations)
        file = random.choice(self.files)

        print(f"\n{Colors.YELLOW}[*] {op} {file}...{Colors.RESET}")

        for i in range(random.randint(3, 8)):
            status = random.choice(["Reading blocks", "Writing sectors", "Validating checksums", "Applying transformations"])
            print(f"{Colors.DIM}  {status}... {random.randint(1000, 9999)} bytes{Colors.RESET}")
            time.sleep(0.3)

        print(f"{Colors.GREEN}[✓] {op} complete: {file}{Colors.RESET}")

    def network_scanner(self):
        """Simulate network scanning and port discovery"""
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}  NETWORK SCANNER v3.2.1 - ACTIVE RECONNAISSANCE{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}\n")

        # Target selection
        target = random.choice(self.ips)
        print(f"{Colors.YELLOW}[*] Target acquired: {target}{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Initiating port scan...{Colors.RESET}\n")
        time.sleep(0.5)

        # Common ports to "scan"
        ports = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
            53: "DNS", 80: "HTTP", 443: "HTTPS", 3306: "MySQL",
            3389: "RDP", 5432: "PostgreSQL", 8080: "HTTP-ALT",
            27017: "MongoDB", 6379: "Redis", 9200: "Elasticsearch"
        }

        open_ports = random.sample(list(ports.keys()), random.randint(3, 7))

        print(f"{Colors.CYAN}PORT     STATE    SERVICE{Colors.RESET}")
        print(f"{Colors.DIM}{'─'*40}{Colors.RESET}")

        for port in sorted(open_ports):
            time.sleep(random.uniform(0.1, 0.3))
            service = ports[port]
            state_color = Colors.GREEN if random.random() > 0.3 else Colors.YELLOW
            state = "OPEN" if random.random() > 0.2 else "FILTERED"
            print(f"{Colors.GREEN}{port:<8}{Colors.RESET} {state_color}{state:<8}{Colors.RESET} {Colors.CYAN}{service}{Colors.RESET}")

        print(f"\n{Colors.GREEN}[✓] Scan complete: {len(open_ports)} ports discovered{Colors.RESET}")

        # Vulnerability check
        if random.random() > 0.5:
            time.sleep(0.5)
            print(f"\n{Colors.YELLOW}[*] Running vulnerability assessment...{Colors.RESET}")
            time.sleep(1)
            vulns = random.randint(0, 3)
            if vulns > 0:
                print(f"{Colors.RED}[!] {vulns} potential vulnerabilities detected{Colors.RESET}")
                vuln_types = ["SQL Injection", "XSS", "Outdated SSL/TLS", "Weak credentials", "Directory traversal"]
                for i in range(vulns):
                    print(f"{Colors.RED}  └─ {random.choice(vuln_types)} (CVE-2024-{random.randint(1000,9999)}){Colors.RESET}")
            else:
                print(f"{Colors.GREEN}[✓] No critical vulnerabilities found{Colors.RESET}")

    def terminal_breach(self):
        """Simulate a movie-style terminal hacking sequence"""
        print(f"\n{Colors.BOLD}{Colors.RED}{'='*80}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.RED}  BREACH PROTOCOL INITIATED - UNAUTHORIZED ACCESS ATTEMPT{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.RED}{'='*80}{Colors.RESET}\n")

        target = f"MAINFRAME-{random.randint(100,999)}"
        print(f"{Colors.YELLOW}[*] Target system: {target}{Colors.RESET}")
        time.sleep(0.5)

        # Access levels
        levels = [
            "PUBLIC ACCESS",
            "USER LEVEL",
            "ADMIN LEVEL",
            "ROOT ACCESS",
            "KERNEL MODE"
        ]

        for i, level in enumerate(levels):
            time.sleep(0.5)
            print(f"\n{Colors.CYAN}[{i+1}/5] Attempting {level}...{Colors.RESET}")

            # Random "attempts"
            attempts = random.randint(2, 5)
            for attempt in range(attempts):
                time.sleep(random.uniform(0.2, 0.5))
                if attempt < attempts - 1:
                    method = random.choice([
                        "Brute force attack",
                        "Dictionary attack",
                        "Rainbow table lookup",
                        "Hash collision",
                        "Token injection"
                    ])
                    print(f"{Colors.DIM}  [{attempt+1}] {method}... {Colors.RED}FAILED{Colors.RESET}")
                else:
                    method = random.choice([
                        "Exploiting buffer overflow",
                        "SQL injection bypass",
                        "Session hijacking",
                        "Privilege escalation",
                        "Zero-day exploit"
                    ])
                    print(f"{Colors.DIM}  [{attempt+1}] {method}... {Colors.GREEN}SUCCESS{Colors.RESET}")

            print(f"{Colors.GREEN}  [✓] {level} GRANTED{Colors.RESET}")

        # Final access
        print(f"\n{Colors.BOLD}{Colors.GREEN}{'='*80}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.GREEN}  ACCESS GRANTED - FULL SYSTEM CONTROL ACHIEVED{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.GREEN}{'='*80}{Colors.RESET}\n")
        time.sleep(1)

        # Show "system info"
        print(f"{Colors.CYAN}System Information:{Colors.RESET}")
        print(f"{Colors.DIM}  OS: {random.choice(['Linux 5.15.0', 'Windows Server 2022', 'FreeBSD 13.1'])}{Colors.RESET}")
        print(f"{Colors.DIM}  Architecture: {random.choice(['x86_64', 'ARM64', 'RISC-V'])}{Colors.RESET}")
        print(f"{Colors.DIM}  Users: {random.randint(10, 500)}{Colors.RESET}")
        print(f"{Colors.DIM}  Uptime: {random.randint(1, 365)} days{Colors.RESET}")

    def glitch_effect(self):
        """Create a glitch/distortion effect"""
        chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        glitch_text = random.choice([
            "SYSTEM COMPROMISED",
            "FIREWALL BREACHED",
            "ENCRYPTION BROKEN",
            "ACCESS GRANTED",
            "ALERT: INTRUSION DETECTED"
        ])

        print(f"\n{Colors.BOLD}", end='')
        for _ in range(5):
            # Glitchy version
            glitched = ''.join(random.choice([c, random.choice(chars)]) for c in glitch_text)
            color = random.choice([Colors.RED, Colors.GREEN, Colors.CYAN, Colors.YELLOW])
            print(f"\r{color}{glitched}{Colors.RESET}", end='', flush=True)
            time.sleep(0.1)

        # Final clear version
        print(f"\r{Colors.GREEN}{glitch_text}{Colors.RESET}")
        time.sleep(0.5)

    def data_stream(self):
        """Simulate high-speed data streaming"""
        print(f"\n{Colors.CYAN}[*] Intercepting data stream...{Colors.RESET}\n")

        data_types = ["PACKET", "FRAME", "BLOCK", "CHUNK", "SEGMENT"]
        for _ in range(random.randint(10, 20)):
            dtype = random.choice(data_types)
            size = random.randint(64, 4096)
            checksum = ''.join(random.choices('0123456789ABCDEF', k=8))
            status = random.choice([Colors.GREEN + "OK", Colors.YELLOW + "WARN", Colors.DIM + "INFO"])

            print(f"{Colors.DIM}[{dtype}] {size:04d}B | CRC:{checksum} | {status}{Colors.RESET}")
            time.sleep(random.uniform(0.05, 0.15))

        print(f"\n{Colors.GREEN}[✓] Stream captured: {random.randint(100, 999)} KB{Colors.RESET}")

    def binary_cascade(self):
        """Falling binary numbers effect"""
        print(f"\n{Colors.GREEN}")
        for _ in range(10):
            line = ' '.join(''.join(random.choices('01', k=8)) for _ in range(10))
            print(line)
            time.sleep(0.1)
        print(Colors.RESET)

    def wopr_dialogue(self):
        """WarGames WOPR dialogue sequence"""
        # Display WOPR ASCII art
        print(f"\n{Colors.CYAN}{self.ascii_art['wopr']}{Colors.RESET}")
        time.sleep(1)

        # WOPR boot sequence
        print(f"\n{Colors.GREEN}WOPR SYSTEM INITIALIZING...{Colors.RESET}")
        time.sleep(0.5)

        boot_messages = [
            "LOADING PRIMARY FUNCTIONS",
            "CONNECTING TO NORAD MAINFRAME",
            "ACCESSING DEFENSE SYSTEMS",
            "RUNNING DIAGNOSTICS",
            "ALL SYSTEMS OPERATIONAL"
        ]

        for msg in boot_messages:
            print(f"{Colors.DIM}> {msg}...{Colors.RESET}")
            time.sleep(0.4)

        print(f"\n{Colors.BOLD}{Colors.CYAN}GREETINGS PROFESSOR FALKEN.{Colors.RESET}")
        time.sleep(1)
        print()
        self.typing_effect(f"{Colors.YELLOW}SHALL WE PLAY A GAME?{Colors.RESET}", 0.05)
        time.sleep(1)

        # List of "games"
        games = [
            "FIGHTER COMBAT",
            "GUERRILLA ENGAGEMENT",
            "DESERT WARFARE",
            "AIR-TO-GROUND ACTIONS",
            "THEATERWIDE TACTICAL WARFARE",
            "THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE",
            "GLOBAL THERMONUCLEAR WAR"
        ]

        print(f"\n{Colors.CYAN}AVAILABLE GAMES:{Colors.RESET}\n")
        for i, game in enumerate(games, 1):
            print(f"{Colors.DIM}  {i}. {game}{Colors.RESET}")
            time.sleep(0.2)

        time.sleep(1)
        print(f"\n{Colors.BOLD}{Colors.RED}> LAUNCHING GLOBAL THERMONUCLEAR WAR...{Colors.RESET}")
        time.sleep(0.5)

        # Launch sequence
        print(f"\n{Colors.YELLOW}DEFCON STATUS: 5 → 4 → 3 → 2 → 1{Colors.RESET}")
        time.sleep(1)

        print(f"\n{Colors.RED}MISSILE LAUNCH DETECTED{Colors.RESET}")
        for _ in range(3):
            print(f"{Colors.RED}{'!' * 60}{Colors.RESET}")
            time.sleep(0.3)

        time.sleep(0.5)
        print(f"\n{Colors.CYAN}A STRANGE GAME.{Colors.RESET}")
        time.sleep(0.8)
        print(f"{Colors.CYAN}THE ONLY WINNING MOVE IS NOT TO PLAY.{Colors.RESET}\n")
        time.sleep(1.5)

    def radar_sweep(self):
        """Animated radar sweep display"""
        print(f"\n{Colors.BOLD}{Colors.GREEN}[RADAR SYSTEM ACTIVE]{Colors.RESET}\n")

        # Radar display
        radius = 10
        center_x, center_y = radius, radius

        # Create radar grid
        for sweep in range(12):  # 12 sweeps (like a clock)
            angle = sweep * 30  # 30 degrees per sweep

            print(f"\n{Colors.CYAN}╔{'═' * 44}╗{Colors.RESET}")
            print(f"{Colors.CYAN}║{Colors.RESET}  RADAR SWEEP - SECTOR {sweep + 1:02d}/12  {Colors.DIM}[{angle}°]{Colors.RESET}  {Colors.CYAN}║{Colors.RESET}")
            print(f"{Colors.CYAN}╚{'═' * 44}╝{Colors.RESET}\n")

            # Draw radar circle
            for y in range(radius * 2 + 1):
                line = ""
                for x in range(radius * 2 + 1):
                    dx = x - center_x
                    dy = y - center_y
                    distance = (dx**2 + dy**2) ** 0.5

                    # Center point
                    if dx == 0 and dy == 0:
                        line += f"{Colors.RED}⊕{Colors.RESET}"
                    # Radar ring
                    elif abs(distance - radius) < 0.8:
                        line += f"{Colors.GREEN}○{Colors.RESET}"
                    # Sweep line (approximate angle)
                    elif abs(dx) < 1 and dy < 0 and sweep % 3 == 0:
                        line += f"{Colors.YELLOW}│{Colors.RESET}"
                    # Random blips
                    elif random.random() > 0.95:
                        line += f"{Colors.RED}•{Colors.RESET}"
                    else:
                        line += f"{Colors.DIM}·{Colors.RESET}"

                print(f"  {line}")

            # Contact info
            if random.random() > 0.6:
                contacts = random.randint(1, 3)
                print(f"\n{Colors.YELLOW}  CONTACTS DETECTED: {contacts}{Colors.RESET}")
                for i in range(contacts):
                    bearing = random.randint(0, 359)
                    distance_km = random.randint(10, 500)
                    speed = random.randint(100, 900)
                    print(f"{Colors.DIM}  └─ Bearing {bearing}° | Range {distance_km}km | Speed {speed}kt{Colors.RESET}")

            time.sleep(0.4)

        print(f"\n{Colors.GREEN}[✓] Radar sweep complete{Colors.RESET}\n")

    def spinner_demo(self):
        """Demonstrate various loading spinners"""
        spinners = {
            'dots': ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'],
            'line': ['|', '/', '-', '\\'],
            'arrow': ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
            'dots_pulse': ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷'],
            'box': ['◰', '◳', '◲', '◱'],
            'circle': ['◐', '◓', '◑', '◒'],
            'blocks': ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃', '▂'],
        }

        operations = [
            "Initializing quantum processors",
            "Establishing satellite uplink",
            "Decrypting intercepted transmissions",
            "Compiling exploit framework",
            "Synchronizing network nodes"
        ]

        for op in random.sample(operations, 3):
            spinner_name, frames = random.choice(list(spinners.items()))
            duration = random.uniform(2, 4)
            iterations = int(duration / 0.1)

            print(f"\n{Colors.CYAN}[*] {op}...{Colors.RESET}")

            for i in range(iterations):
                frame = frames[i % len(frames)]
                percent = int((i / iterations) * 100)
                print(f"\r  {Colors.YELLOW}{frame}{Colors.RESET} {Colors.DIM}{percent}%{Colors.RESET}", end='', flush=True)
                time.sleep(0.1)

            print(f"\r  {Colors.GREEN}✓{Colors.RESET} {Colors.GREEN}Complete{Colors.RESET}" + " " * 20)

        print()

    def ascii_art_display(self):
        """Display random ASCII art from gallery"""
        art_name = random.choice(list(self.ascii_art.keys()))
        art = self.ascii_art[art_name]

        colors = [Colors.GREEN, Colors.CYAN, Colors.YELLOW, Colors.MAGENTA]
        color = random.choice(colors)

        print(f"\n{color}{art}{Colors.RESET}")
        time.sleep(2)

    def themed_scenario_wargames(self):
        """Run a complete WarGames-themed scenario"""
        # WOPR intro
        self.wopr_dialogue()
        time.sleep(1)

        # Launch detection
        print(f"\n{Colors.RED}{Colors.BOLD}╔{'═' * 78}╗{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}║  NORAD ALERT: MULTIPLE MISSILE LAUNCHES DETECTED                            ║{Colors.RESET}")
        print(f"{Colors.RED}{Colors.BOLD}╚{'═' * 78}╝{Colors.RESET}\n")

        # Radar tracking
        self.radar_sweep()

        # System analysis
        self.system_stats()
        time.sleep(1)

        # Outcome
        print(f"\n{Colors.YELLOW}{Colors.BOLD}SIMULATION TERMINATED{Colors.RESET}")
        print(f"{Colors.CYAN}Joshua has learned that thermonuclear war cannot be won.{Colors.RESET}\n")

    def themed_scenario_matrix(self):
        """Run a Matrix-themed scenario"""
        # Matrix banner
        print(f"{Colors.GREEN}{self.ascii_art['matrix']}{Colors.RESET}")
        time.sleep(1)

        print(f"\n{Colors.GREEN}Wake up, Neo...{Colors.RESET}")
        time.sleep(1.5)
        self.typing_effect(f"{Colors.GREEN}The Matrix has you...{Colors.RESET}", 0.05)
        time.sleep(1)
        print(f"{Colors.GREEN}Follow the white rabbit.{Colors.RESET}\n")
        time.sleep(1.5)

        # Matrix rain
        self.matrix_rain(duration=4)

        # Red pill / blue pill moment
        print(f"\n{Colors.CYAN}This is your last chance. After this, there is no turning back.{Colors.RESET}\n")
        time.sleep(1)
        print(f"{Colors.BLUE}  You take the blue pill - the story ends, you wake up in your bed.{Colors.RESET}")
        time.sleep(1)
        print(f"{Colors.RED}  You take the red pill - you stay in Wonderland.{Colors.RESET}\n")
        time.sleep(2)

        # Taking red pill
        print(f"{Colors.RED}[TAKING RED PILL...]{Colors.RESET}\n")
        self.spinner_demo()

        # Reality breaking
        self.glitch_effect()
        time.sleep(0.5)
        self.binary_cascade()

        print(f"\n{Colors.GREEN}Welcome to the Real World.{Colors.RESET}\n")

    def themed_scenario_cyberpunk(self):
        """Run a cyberpunk/Mr. Robot-themed scenario"""
        # Cyber banner
        print(f"{Colors.MAGENTA}{self.ascii_art['cyber']}{Colors.RESET}")
        time.sleep(1)

        print(f"\n{Colors.YELLOW}[ENCRYPTED TRANSMISSION RECEIVED]{Colors.RESET}")
        time.sleep(0.5)
        self.typing_effect(f"{Colors.CYAN}Hello, friend. Time to take down Evil Corp.{Colors.RESET}", 0.04)
        time.sleep(1)

        # Network infiltration
        print(f"\n{Colors.RED}[PHASE 1: RECONNAISSANCE]{Colors.RESET}")
        self.network_scanner()

        print(f"\n{Colors.RED}[PHASE 2: EXPLOITATION]{Colors.RESET}")
        self.terminal_breach()

        print(f"\n{Colors.RED}[PHASE 3: DATA EXFILTRATION]{Colors.RESET}")
        self.data_stream()

        # Mission complete
        print(f"\n{Colors.GREEN}{Colors.BOLD}╔{'═' * 78}╗{Colors.RESET}")
        print(f"{Colors.GREEN}{Colors.BOLD}║  MISSION ACCOMPLISHED - EVIL CORP ACCOUNTS ZEROED                           ║{Colors.RESET}")
        print(f"{Colors.GREEN}{Colors.BOLD}╚{'═' * 78}╝{Colors.RESET}\n")
        time.sleep(1)

        print(f"{Colors.DIM}bonsoir, elliot{Colors.RESET}\n")

    def run_themed_scenario(self):
        """Randomly select and run a themed scenario"""
        scenarios = [
            ("WarGames", self.themed_scenario_wargames),
            ("The Matrix", self.themed_scenario_matrix),
            ("Cyberpunk", self.themed_scenario_cyberpunk),
        ]

        theme_name, scenario_func = random.choice(scenarios)
        print(f"\n{Colors.BOLD}{Colors.YELLOW}>>> LOADING SCENARIO: {theme_name} <<<{Colors.RESET}\n")
        time.sleep(1)
        scenario_func()

    def run_sequence(self):
        """Run a random sequence of operations"""
        operations_list = [
            self.matrix_rain,
            lambda: self.progress_bar(random.choice(self.operations)),
            self.scroll_code,
            self.fake_logs,
            self.system_stats,
            self.file_operations,
            self.network_scanner,
            self.terminal_breach,
            self.glitch_effect,
            self.data_stream,
            self.binary_cascade,
            self.wopr_dialogue,
            self.radar_sweep,
            self.spinner_demo,
            self.ascii_art_display,
        ]

        # Header
        print(f"\n{Colors.BOLD}{Colors.GREEN}{'='*80}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.GREEN}  SUBTERFUGE v3.0.0 - ELITE HACKER SIMULATOR{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.GREEN}  Initialization Complete - All Systems Operational{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.GREEN}  New: WarGames WOPR | Radar Sweep | Themed Scenarios{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.GREEN}{'='*80}{Colors.RESET}\n")

        time.sleep(1)

        # Run random operations
        operation_count = 0
        while True:
            try:
                # Every 10-15 operations, run a themed scenario instead
                if operation_count > 0 and operation_count % random.randint(10, 15) == 0:
                    self.run_themed_scenario()
                else:
                    operation = random.choice(operations_list)
                    operation()

                operation_count += 1
                time.sleep(random.uniform(0.5, 2))
            except KeyboardInterrupt:
                print(f"\n\n{Colors.RED}[!] Emergency shutdown initiated...{Colors.RESET}")
                print(f"{Colors.YELLOW}[*] Cleaning up traces...{Colors.RESET}")
                time.sleep(1)
                print(f"{Colors.GREEN}[✓] All systems secured. Goodbye.{Colors.RESET}\n")
                break

if __name__ == "__main__":
    simulator = HackerSimulator()
    simulator.run_sequence()
