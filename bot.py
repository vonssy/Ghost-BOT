import requests
import json
import urllib.parse
import os
from colorama import *
from datetime import datetime
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class GHOST:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Host': '1002867-cb36460.tmweb.ru',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }
        self.base_url = 'https://1002867-cb36460.tmweb.ru'

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}GHOST - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    
    def load_data(self, query: str):
        query_params = urllib.parse.parse_qs(query)
        query = query_params.get('user', [None])[0]

        if query:
            user_data_json = urllib.parse.unquote(query)
            user_data = json.loads(user_data_json)
            user_id = user_data['id']
            return user_id
        else:
            raise ValueError("User data not found in query.")
        
    def user_data(self, query: str):
        url = f'{self.base_url}/data?{query}'
        self.headers.update({
            'Referer': 'https://1002867-cb36460.tmweb.ru/dist/?tgWebAppStartParam=1493482017',
        })

        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def ghost_combo(self, query: str, combo: str):
        url = f'{self.base_url}/complete_combo?answer={combo}&{query}'
        self.headers.update({
            'Origin': 'https://1002867-cb36460.tmweb.ru',
            'Referer': 'https://1002867-cb36460.tmweb.ru/earn',
        })

        response = self.session.get(url, headers=self.headers)
        if response.text.strip().lower() == "true":  
            return True
        else:
            return False
        
    def complete_tasks(self, query: str, task_name: str):
        url = f'{self.base_url}/complete_task?name={task_name}&{query}'
        self.headers.update({
            'Content-Length': '0',
            'Origin': 'https://1002867-cb36460.tmweb.ru',
            'Referer': 'https://1002867-cb36460.tmweb.ru/earn',
        })

        response = self.session.post(url, headers=self.headers)
        if response.text.strip().lower() == "true":  
            return True
        else:
            return False
        
    def get_ads(self, user_id: str):
        url = f'https://api.adsgram.ai/adv?blockId=2629&tg_id={user_id}&top_domain=1002867-cb36460.tmweb.ru'
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'api.adsgram.ai',
            'Origin': 'https://1002867-cb36460.tmweb.ru',
            'Referer': 'https://1002867-cb36460.tmweb.ru/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

        response = self.session.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def watch_ads(self, url: str):
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'api.adsgram.ai',
            'Origin': 'https://1002867-cb36460.tmweb.ru',
            'Referer': 'https://1002867-cb36460.tmweb.ru/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

        response = self.session.get(url, headers=headers)
        if response.text == {}:
            return True
        else:
            return False
        
    def process_query(self, query: str):
        user_id = self.load_data(query)
        user = self.user_data(query)
        if not user:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED + Style.BRIGHT} Query ID Isn't Valid {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return

        if user:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {user['username']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {user['balance']} $GHOST {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
            time.sleep(1)

            combo = user["about_app"]["combo"]
            play_ghostcombo = self.ghost_combo(query, combo)
            if play_ghostcombo:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Ghost Combo{Style.RESET_ALL}"
                    f"{Fore.GREEN + Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} 10000 $GHOST {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Ghost Combo{Style.RESET_ALL}"
                    f"{Fore.YELLOW + Style.BRIGHT} Is Already Completed {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            tasks_status = user["tasks"]
            tasks_list = user["about_app"]["tasks"]
            for task in tasks_list:
                task_name = task[0]
                if tasks_status.get(task_name) == "True":
                    complete = self.complete_tasks(query, task_name)
                    if complete:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {task[1]} {Style.RESET_ALL}"
                            f"{Fore.GREEN + Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {task[3]} $GHOST {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {task[1]} {Style.RESET_ALL}"
                            f"{Fore.RED + Style.BRIGHT}Isn't Completed{Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                        )
                    time.sleep(1)

            count = 0
            while count < 20:
                ads = self.get_ads(user_id)
                trackings = ads["banner"]["trackings"]
                urls = [tracking["value"] for tracking in trackings if tracking["name"] in ["render", "click", "reward"]]
                for url in urls:
                    if url:
                        self.watch_ads(url)
                        
                count += 1
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Watch Short Video {Style.RESET_ALL}"
                    f"{Fore.GREEN + Style.BRIGHT}Is Succes{Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT} ] [ Count{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} {count}/20 {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
                if count == 20:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Task{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} Watch Short Video {Style.RESET_ALL}"
                        f"{Fore.GREEN + Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} 5000 $GHOST {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                    break

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        time.sleep(3)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] GHOST - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    bot = GHOST()
    bot.main()