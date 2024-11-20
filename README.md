
# Discord Token Joiner 2024

![Banner](https://cdn.dfg.com.br/itemimages/963948375-token-joiner-discord-AKNT.webp)

## Introduction

Welcome to **Discord Token Joiner 2024**, a Python-based script that automates joining Discord servers using tokens. This project is designed with ease of use and dynamic functionality in mind.

> **Note:** This script cannot be used to boost servers right now. For usage with over 5,000 tokens, increase the sleep time to prevent issues.
> **Help** For This script we need proxies on this format : {proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port} we can find it here ![PROXY](https://www.webshare.io/features/free-proxy)

---

## Features

- **Dynamic Proxy Support:** Easily configure proxies for secure and anonymous connections.
- **Token Management:** Load multiple tokens from a file.
- **Error Handling:** Tracks and logs both successful and failed attempts.
- **Customizable:** Edit the invite link and settings as per your requirements.
- **Real-time Logging:** Color-coded logs for better visibility of status.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/minatsukix86/Discord-Token-Joiner.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Discord-Token-Joiner
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Create a `tokens.txt` file in the root directory and add your tokens, one per line.
2. Edit the invite link in the script (`self.invite = 'your-invite-code'`) to the desired server. [ only code ]
3. Run the script:
   ```bash
   python discord_token_joiner.py
   ```

---

## Configuration

### Proxy Setup
Update the proxy configuration in the script:
```python
proxy_host = 'your-proxy-host'
proxy_port = 'your-proxy-port'
proxy_user = 'your-proxy-username'
proxy_pass = 'your-proxy-password'
```

### Invite Link
Set the desired server invite link:
```python
self.invite = 'your-server-invite' ( on line 67 ) 
```

---

## Logging

- **Success:** Tokens that successfully joined the server are logged with a green status.
- **Failure:** Tokens that failed to join the server are logged with a red status.

---

## Troubleshooting

- Ensure all dependencies are installed using the provided `requirements.txt`.
- Use a valid invite link and tokens.
- For large-scale operations, increase the sleep time to avoid rate limits.

---

## Legal Disclaimer

This tool is intended for educational purposes only. The use of this tool to bypass Discord's Terms of Service is strictly prohibited. The author is not responsible for any misuse or damages caused by this script.

---

## Contribution

Feel free to fork this repository and submit pull requests for improvements.

---

## Author

Developed by **Minatsuki**. For questions or support, contact me on discord => **__minatsukix86__**.

---

### Version

**Discord Token Joiner 2024** - Version 1.0
