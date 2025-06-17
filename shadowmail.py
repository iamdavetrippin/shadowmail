#!/usr/bin/env python3
import requests
import re
import json
import time
import random
from colorama import init, Fore, Style
import os
import sys
from datetime import datetime

# Initialize colorama
init(autoreset=True)

# Common user agents for stealth
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
]

class ShadowMailUltimate:
    def __init__(self):
        self.email = ""
        self.results = {}
        self.platforms = {
            "Social": [
                {"name": "Facebook", "url": "facebook.com", "method": "password_reset"},
                {"name": "Twitter", "url": "twitter.com", "method": "password_reset"},
                {"name": "Instagram", "url": "instagram.com", "method": "signup_check"},
                {"name": "LinkedIn", "url": "linkedin.com", "method": "password_reset"},
                {"name": "Reddit", "url": "reddit.com", "method": "profile_check"},
                {"name": "TikTok", "url": "tiktok.com", "method": "signup_check"},
                {"name": "Pinterest", "url": "pinterest.com", "method": "password_reset"},
                {"name": "Snapchat", "url": "snapchat.com", "method": "signup_check"},
                {"name": "Tumblr", "url": "tumblr.com", "method": "profile_check"},
                {"name": "VK", "url": "vk.com", "method": "password_reset"}
            ],
            "Crypto": [
                {"name": "Binance", "url": "binance.com", "method": "signup_check"},
                {"name": "Coinbase", "url": "coinbase.com", "method": "profile_check"},
                {"name": "KuCoin", "url": "kucoin.com", "method": "signup_check"},
                {"name": "Crypto.com", "url": "crypto.com", "method": "password_reset"},
                {"name": "Kraken", "url": "kraken.com", "method": "profile_check"},
                {"name": "Gemini", "url": "gemini.com", "method": "signup_check"},
                {"name": "FTX", "url": "ftx.com", "method": "password_reset"},
                {"name": "Bybit", "url": "bybit.com", "method": "profile_check"}
            ],
            "Finance": [
                {"name": "PayPal", "url": "paypal.com", "method": "password_reset"},
                {"name": "Venmo", "url": "venmo.com", "method": "signup_check"},
                {"name": "CashApp", "url": "cash.app", "method": "profile_check"},
                {"name": "Revolut", "url": "revolut.com", "method": "password_reset"},
                {"name": "Chime", "url": "chime.com", "method": "signup_check"},
                {"name": "Wise", "url": "wise.com", "method": "profile_check"}
            ],
            "Email": [
                {"name": "Gmail", "url": "gmail.com", "method": "password_reset"},
                {"name": "Yahoo", "url": "yahoo.com", "method": "password_reset"},
                {"name": "Outlook", "url": "outlook.com", "method": "password_reset"},
                {"name": "ProtonMail", "url": "protonmail.com", "method": "signup_check"},
                {"name": "Zoho", "url": "zoho.com", "method": "profile_check"}
            ],
            "Developer": [
                {"name": "GitHub", "url": "github.com", "method": "profile_check"},
                {"name": "GitLab", "url": "gitlab.com", "method": "password_reset"},
                {"name": "Bitbucket", "url": "bitbucket.org", "method": "signup_check"},
                {"name": "StackOverflow", "url": "stackoverflow.com", "method": "profile_check"},
                {"name": "DigitalOcean", "url": "digitalocean.com", "method": "password_reset"}
            ]
        }
        
    def display_banner(self):
        print(Fore.CYAN + r"""
   _____ __                        __  ___      __       _       __ 
  / ___// /_____  _________  ____/ / / / |    / /___   | |     / / 
  \__ \/ __/ __ \/ ___/ __ \/ __  / / /| |   / / __ \  | | /| / /  
 ___/ / /_/ /_/ / /__/ /_/ / /_/ / / / | |  / / /_/ /  | |/ |/ /   
/____/\__/\____/\___/\____/\__,_/ /_/  |_| /_/\____/   |__/|__/    
        """ + Style.RESET_ALL)
        print(Fore.YELLOW + "🔐 ShadowMail Ultimate Edition - Email Intelligence Scanner")
        print(Fore.MAGENTA + "👤 Created by iamdavetrippin" + Style.RESET_ALL)
        print("\n")

    def show_disclaimer(self):
        print(Fore.RED + """
DISCLAIMER:
This tool is for educational and authorized penetration testing only.
Unauthorized use against systems you don't own is illegal.
The developer assumes no liability for misuse.
        """ + Style.RESET_ALL)
        input("Press Enter to acknowledge and continue...")

    def main_menu(self):
        while True:
            print(Fore.GREEN + "\n[+] Main Menu" + Style.RESET_ALL)
            print("1. Basic Scan (Fast)")
            print("2. Full Ultimate Scan (Comprehensive)")
            print("3. GitHub Recon")
            print("4. Username Pattern Generator")
            print("5. Dark Web Leak Check")
            print("6. Exit")
            
            choice = input("\nSelect an option: ")
            
            if choice == "1":
                self.basic_scan()
            elif choice == "2":
                self.full_scan()
            elif choice == "3":
                self.github_recon()
            elif choice == "4":
                self.username_patterns()
            elif choice == "5":
                self.darkweb_check()
            elif choice == "6":
                print(Fore.YELLOW + "\n[!] Exiting ShadowMail Ultimate..." + Style.RESET_ALL)
                sys.exit(0)
            else:
                print(Fore.RED + "\n[!] Invalid choice. Please try again." + Style.RESET_ALL)

    def get_email(self):
        self.email = input(Fore.BLUE + "\n[?] Enter target email: " + Style.RESET_ALL).strip()
        if not self.validate_email(self.email):
            print(Fore.RED + "[!] Invalid email format. Please try again." + Style.RESET_ALL)
            return False
        return True
    
    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email)
    
    def basic_scan(self):
        if not self.get_email():
            return
            
        print(Fore.YELLOW + f"\n[*] Starting basic scan for {self.email}..." + Style.RESET_ALL)
        
        # Check major platforms
        self.check_platforms(quick_mode=True)
        
        # Display results
        self.display_results()
        
        # Save results
        self.save_results("basic")
    
    def full_scan(self):
        if not self.get_email():
            return
            
        print(Fore.YELLOW + f"\n[*] Starting FULL ULTIMATE scan for {self.email}..." + Style.RESET_ALL)
        
        # Check all platforms
        self.check_platforms(quick_mode=False)
        
        # Additional recon
        self.github_recon()
        self.username_patterns()
        self.darkweb_check()
        
        # Display results
        self.display_results(verbose=True)
        
        # Save results
        self.save_results("full")
    
    def stealth_request(self, url, method="GET", data=None):
        """Makes requests appear more human-like"""
        time.sleep(random.uniform(1, 3))  # Random delay
        headers = {
            'User-Agent': random.choice(USER_AGENTS),
            'Accept-Language': 'en-US,en;q=0.9'
        }
        
        try:
            if method == "GET":
                return requests.get(url, headers=headers, timeout=10)
            else:
                return requests.post(url, headers=headers, data=data, timeout=10)
        except Exception as e:
            return None

    def check_platform(self, platform):
        """Check if email exists on a specific platform"""
        result = "Error"
        
        try:
            if platform["method"] == "password_reset":
                # Try password reset flow
                url = f"https://{platform['url']}/account/begin_password_reset"
                resp = self.stealth_request(url)
                if resp and resp.status_code == 200:
                    result = "Found"
                else:
                    result = "Not Found"
                    
            elif platform["method"] == "signup_check":
                # Try signup availability
                url = f"https://{platform['url']}/signup/check_email"
                data = {'email': self.email}
                resp = self.stealth_request(url, method="POST", data=data)
                if resp and "already in use" in resp.text.lower():
                    result = "Found"
                else:
                    result = "Not Found"
                    
            elif platform["method"] == "profile_check":
                # Check public profile
                username = self.email.split('@')[0]
                url = f"https://{platform['url']}/{username}"
                resp = self.stealth_request(url)
                if resp and resp.status_code == 200:
                    result = "Found"
                else:
                    result = "Not Found"
                    
        except Exception as e:
            result = f"Error: {str(e)}"
            
        return result
    
    def check_platforms(self, quick_mode=True):
        categories = list(self.platforms.keys())
        if quick_mode:
            categories = categories[:3]  # Only check first 3 categories in quick mode
            
        for category in categories:
            self.results[category] = {}
            print(Fore.CYAN + f"\n[*] Checking {category} platforms..." + Style.RESET_ALL)
            
            for platform in self.platforms[category]:
                status = self.check_platform(platform)
                
                if "Found" in status:
                    print(Fore.GREEN + f"[+] {platform['name']}: {status}" + Style.RESET_ALL)
                elif "Not Found" in status:
                    print(Fore.RED + f"[-] {platform['name']}: {status}" + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + f"[!] {platform['name']}: {status}" + Style.RESET_ALL)
                
                self.results[category][platform['name']] = status
    
    def github_recon(self):
        print(Fore.CYAN + "\n[*] Scanning GitHub commits..." + Style.RESET_ALL)
        
        try:
            # Search public commits (no API key needed)
            url = f"https://github.com/search?q={self.email}&type=commits"
            resp = self.stealth_request(url)
            
            if not resp or "We couldn't find any commits matching" in resp.text:
                self.results['GitHub'] = {"commits": 0}
            else:
                # Extract approximate count from page
                count = re.search(r"(\d+) commit results", resp.text)
                count = int(count.group(1)) if count else "Several"
                self.results['GitHub'] = {
                    "commits": count,
                    "profile": f"https://github.com/search?q={self.email}"
                }
                
        except Exception as e:
            self.results['GitHub'] = {"error": str(e)}
    
    def username_patterns(self):
        print(Fore.CYAN + "\n[*] Generating username patterns..." + Style.RESET_ALL)
        local_part = self.email.split('@')[0]
        patterns = [
            local_part,
            local_part + "123",
            local_part + "_",
            local_part + "1",
            local_part[:3] + "x",
            local_part.upper(),
            local_part.replace('.', ''),
            local_part.split('.')[0]  # For first.last@ emails
        ]
        self.results['Username_Patterns'] = list(set(patterns))  # Remove duplicates
    
    def darkweb_check(self):
        print(Fore.MAGENTA + "\n[*] Checking known breach databases..." + Style.RESET_ALL)
        
        try:
            # Check HaveIBeenPwned (free tier)
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{self.email}"
            headers = {
                'User-Agent': 'ShadowMailUltimate',
                'hibp-api-key': ''  # Leave empty for free tier (limited)
            }
            
            resp = requests.get(url, headers=headers)
            
            if resp.status_code == 200:
                breaches = json.loads(resp.text)
                self.results['Breaches'] = {
                    "count": len(breaches),
                    "sources": [b['Name'] for b in breaches]
                }
            elif resp.status_code == 404:
                self.results['Breaches'] = {"count": 0}
            else:
                self.results['Breaches'] = {"error": "API limit reached"}
                
        except Exception as e:
            self.results['Breaches'] = {"error": str(e)}
    
    def display_results(self, verbose=False):
        print(Fore.GREEN + "\n[+] SCAN RESULTS" + Style.RESET_ALL)
        print(f"Email: {self.email}")
        print(f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        for category, data in self.results.items():
            print(Fore.YELLOW + f"\n=== {category.upper()} ===" + Style.RESET_ALL)
            if isinstance(data, dict):
                for platform, status in data.items():
                    if "Found" in str(status):
                        color = Fore.GREEN
                    elif "Not Found" in str(status):
                        color = Fore.RED
                    else:
                        color = Fore.YELLOW
                    print(f"{platform}: {color}{status}{Style.RESET_ALL}")
            elif isinstance(data, list):
                for item in data:
                    print(f"- {item}")
    
    def save_results(self, scan_type):
        filename = f"shadowmail_ultimate_{scan_type}_results.txt"
        with open(filename, 'w') as f:
            f.write(f"ShadowMail Ultimate Edition - Scan Results\n")
            f.write(f"Email: {self.email}\n")
            f.write(f"Scan Type: {scan_type}\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for category, data in self.results.items():
                f.write(f"\n=== {category.upper()} ===\n")
                if isinstance(data, dict):
                    for platform, status in data.items():
                        f.write(f"{platform}: {status}\n")
                elif isinstance(data, list):
                    for item in data:
                        f.write(f"- {item}\n")
        
        print(Fore.GREEN + f"\n[+] Results saved to {filename}" + Style.RESET_ALL)

if __name__ == "__main__":
    tool = ShadowMailUltimate()
    tool.display_banner()
    tool.show_disclaimer()
    tool.main_menu()
