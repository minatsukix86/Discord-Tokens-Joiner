import tls_client
import ctypes
import time
from colorama import Fore, Style, init

init(autoreset=True)  
banner = """
                                         .,,cccd$$$$$$$$$$$ccc,
                                    ,cc$$$$$$$$$$$$$$$$$$$$$$$$$cc,
                                  ,d$$$$$$$$$$$$$$$$"J$$$$$$$$$$$$$$c,
                                d$$$$$$$$$$$$$$$$$$,$" ,,`?$$$$$$$$$$$$L
                              ,$$$$$$$$$$$$$$$$$$$$$',J$$$$$$$$$$$$$$$$$b
                             ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i `$h
                             $$$$$$$$$$$$$$$$$$$$$$$$$P'  "$$$$$$$$$$$h $$              Version : 1.O
                            ;$$$$$$$$$$$$$$$$$$$$$$$$F,$$$h,?$$$$$$$$$$h$F              Discord Token Joiner 2024
                            `$$$$$$$$$$$$$$$$$$$$$$$F:??$$$:)$$$$P",. $$F               it can't be used to boost servers right now 
                             ?$$$$$$$$$$$$$$$$$$$$$$(   `$$ J$$F"d$$F,$F                if u use more than 5k tokens add time to timesleep
                              ?$$$$$$$$$$$$$$$$$$$$$h,  :P'J$$F  ,$F,$"
                               ?$$$$$$$$$$$$$$$$$$$$$$$ccd$$`$h, ",d$
                                "$$$$$$$$$$$$$$$$$$$$$$$$",cdc $$$$"
                       ,uu,      `?$$$$$$$$$$$$$$$$$$$$$$$$$$$c$$$$h
                   .,d$$$$$$$cc,   `$$$$$$$$$$$$$$$$??$$$$$$$$$$$$$$$,
                 ,d$$$$$$$$$$$$$$$bcccc,,??$$$$$$ccf `"??$$$$??$$$$$$$
                d$$$$$$$$$$$$$$$$$$$$$$$$$h`?$$$$$$h`:...  d$$$$$$$$P
               d$$$$$$$$$$$$$$$$$$$$$$$$$$$$`$$$$$$$hc,,cd$$$$$$$$P"
           =$$?$$$$$$$$P' ?$$$$$$$$$$$$$$$$$;$$$$$$$$$???????",,
              =$$$$$$F       `"?????$$$$$$$$$$$$$$$$$$$$$$$$$$$$$bc
              d$$F"?$$k ,ccc$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
       .     ,ccc$$c`""u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",$$$$$$$$$$$$h
    ,d$$$L  J$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" `""$$$??$$$$$$$
  ,d$$$$$$c,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F       `?J$$$$$$$'
 ,$$$$$$$$$$h`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F           ?$$$$$$$P""=,
,$$$F?$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F              3$$$$II"?$h,
$$$$$`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P"               ;$$$??$$$,"?"
$$$$F ?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",z'                3$$h   ?$F
       `?$$$$$$$$$$$$$$$??$$$$$$$$$PF"',d$P"                  "?$F
          """""""         ,z$$$$$$$$$$$$$P
                         J$$$$$$$$$$$$$$F
                        ,$$$$$$$$$$$$$$F
                        :$$$$$c?$$$$PF'
                        `$$$$$$$P
                         `?$$$$F

"""

print(Fore.BLUE + banner + Style.RESET_ALL)
class DiscordJoiner():
    def __init__(self, token_file):
        
        self.joined = 0
        self.failed = 0
        
       
        proxy_host = '198.23.239.134'
        proxy_port = '6540'
        proxy_user = 'zjdocglq'
        proxy_pass = 'vk0fd3rv0v9f'
        self.proxy = f"{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"  
        
        self.session = tls_client.Session(client_identifier="chrome_124", random_tls_extension_order=True)
        self.session.proxies = {
            "http": f"http://{self.proxy}",
            "https": f"https://{self.proxy}"
        }
        
        
        self.invite = 'bataclan' 
        
        # Load Tokens
        self.tokens = self.load_tokens(token_file)
        if not self.tokens:
            print(Fore.RED + "No tokens found in the file. Exiting." + Style.RESET_ALL)
            exit()
    
    def load_tokens(self, token_file):
        """Load tokens from a file."""
        try:
            with open(token_file, 'r') as f:
                tokens = [line.strip() for line in f if line.strip()]
                return tokens
        except FileNotFoundError:
            print(Fore.RED + f"Token file '{token_file}' not found. Exiting." + Style.RESET_ALL)
            return []
    
  
    
    def get_discord_cookies(self):
        
        try:            
            response = self.session.get("https://discord.com")
            if response.status_code == 200:
                return "; ".join(
                    [f"{cookie.name}={cookie.value}" for cookie in response.cookies]
                ) + "; locale=en-US"
            else:
                return "__dcfduid=4e0a8d504a4411eeb88f7f88fbb5d20a; locale=en-US"
        except Exception as e:
            print(e)
    
    def headers_joiner(self, token):
        """Generate headers for joining."""
        return {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'pt-BR,pt;q=0.6',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'authorization': token,
            'content-type': 'application/json',
            'cookie': self.get_discord_cookies(),
            'Dnt': '1',
            'Origin': 'https://discord.com',
            'Priority': 'u=1, i',
            'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjExMzM1MDYzMjU2MDM2ODQ1MzQiLCJsb2NhdGlvbl9jaGFubmVsX2lkIjoiMTEzMzU3Nzk4OTQxODkyNjEyMSIsImxvY2F0aW9uX2NoYW5uZWxfdHlwZSI6MH0=',
            'x-discord-timezone': 'America/Sao_Paulo',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InB0LUJSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI5MTk2MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
        }
    
    def joiner(self, token):
        
        try:
            print(f"{Fore.CYAN}(+) Starting Joiner{Style.RESET_ALL}  --->  {Fore.CYAN}Token:{Style.RESET_ALL} {token[:40]}  --->  {Fore.CYAN}Server:{Style.RESET_ALL} {self.invite}")
            headers = self.headers_joiner(token)
            joiner = self.session.post(f"https://discord.com/api/v9/invites/{self.invite}", headers=headers, json={})
            if joiner.status_code != 200:
                print(f"{Fore.RED}(-) Join Failed Error:{Style.RESET_ALL} {joiner.text}")
                self.failed += 1
            else:
                print(f"{Fore.GREEN}(+) Token Joined:{Style.RESET_ALL} {token[:40]}  --->  {Fore.GREEN}Server:{Style.RESET_ALL} {self.invite}")
                self.joined += 1
            
            time.sleep(5)
        except Exception as e:
            print(f"Function Exit - Error: {e}")
    
    def main(self):
        """Main loop to iterate through tokens."""
        
        for token in self.tokens:
            self.joiner(token)

if __name__ == "__main__":
    token_file = "tokens.txt"  
    joiner = DiscordJoiner(token_file)
    joiner.main()
