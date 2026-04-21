# 🎯 MCTiers Ultimate QueueSniper

A high-speed Discord client built to monitor queue-based systems, instantly secure a spot via button interaction, and optionally solve captcha challenges using OCR — with an added **sound alert system for instant join feedback**.

---

## ⚡ Features

- 🚀 Instant queue joining (auto button click)
- 🎯 Queue position detection from embeds
- 🤖 Captcha solving using OCR
- 🔄 Handles live message edits (real-time queue updates)
- 🔊 Sound alarm when successfully joining
- ⚙️ Fully asynchronous and fast execution

---

## 📦 Requirements

- Python 3.8+
- Windows (for sound alerts via winsound)
- Discord account token *(see warning below)*

### Install dependencies

pip install discord.py ddddocr requests python-dotenv

---

## ⚙️ Setup

### 1. Clone the Repository

```git clone https://github.com/jayaplayz12/MCTiers-Queue-Sniper.git```  
```cd MCTiers-Queue-Sniper``` 

---

### 2. Create `.env`

Create a file named `.env` in the project folder:

DISCORD_TOKEN=your_token_here  
GUILD_ID=your_server_id  
CHANNEL_ID=target_channel_id  
BOT_ID=target_bot_id  

---

### 3. Run the Bot

python main.py  

---

## 🔑 Environment Variables Explained

### DISCORD_TOKEN
- Your Discord account token used for login  
- Gives full access to your account session  
- ⚠️ Never share it with anyone  

---

### GUILD_ID
- The Discord server ID where the system runs  
- The bot only works inside this server  

👉 “Which server should I monitor?”

---

### CHANNEL_ID
- The specific channel ID where queue messages appear  
- All automation is restricted to this channel  

👉 “Where should the bot watch messages?”

---

### BOT_ID
- The ID of the bot that controls the queue system  
- This bot:
  - Sends queue updates  
  - Shows tester availability  
  - Displays Join buttons  

👉 The script ignores all other users and only reacts to this bot  

👉 “Which bot should I listen to?”

---

## 🧠 How It Works

1. Logs into Discord using your token  
2. Watches a specific channel for messages from the target bot  
3. Detects and clicks the **Join** button instantly  
4. Plays a **ringing sound alert** on successful join  
5. Fetches updated message and extracts queue position  
6. If captcha appears:
   - Downloads image
   - Uses OCR to solve it
   - Sends solution automatically  

---

## 🤖 Captcha System

Some queue systems use captcha images to prevent automation.

This bot handles them automatically:

- Detects captcha image attachments in messages  
- Downloads the image instantly  
- Uses OCR (Optical Character Recognition) to read the text  
- Sends the detected solution back into the chat  
- Continues the queue process automatically  

If OCR succeeds → captcha is solved instantly  
If OCR fails → it waits for the next attempt  

---

## 🔊 Sound Feature

When a successful join happens:
- A high-pitched alert sound is played
- Helps you instantly notice successful queue entry

(Windows only — falls back to beep if unavailable)

---

## 📸 Example Output

════════════════════════════════════════  
        MCTIERS AUTO-JOINER ACTIVE      
════════════════════════════════════════  
User:         ExampleUser  
Server:       Example Server  
Channel:      queue-channel  
════════════════════════════════════════  
[-] STATUS: NO TESTER AVAILABLE  
════════════════════════════════════════  

[!] JOIN SUCCESS - ALARM RINGING  

⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
Tester Name:    QueueBot  
Timestamp:      14:32:10  
My Queue Pos:   2  
⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  

---

## 💸 Free & Open

Most tools like this are paid or locked behind subscriptions.  
This project is completely free.

If you want to support development:

- LTC: `ltc1qdfd50nwfs2h2u8l2cama668xf705nfvxty8je4`  
- BTC: `bc1qzjauvt0fytmf9asgsdxgt7z7clhtv8mvzltg0l`  
- ETH: `0x404169F9dF7FC7117C6d76Af08f5390c4B3cCd33`  
- SOL: `62fvBjbwegn397KQJYphBfVjqkZrWbbyyAjzor8tF4oi`  
- USDT (ERC20): `0x404169F9dF7FC7117C6d76Af08f5390c4B3cCd33`  

Donations are optional but appreciated ❤️

---

## ⚠️ Disclaimer

This project is for educational purposes only.

- Self-bots violate Discord Terms of Service  
- Automation may breach platform rules  
- Use can result in account restriction or banning  

Use at your own risk.

---

## 🛠️ Customization

- Change beep sound frequency in `play_ring()`  
- Adjust OCR timing delay  
- Modify queue detection regex  
- Extend for other queue systems  

---

## 🤝 Contributing

Pull requests and improvements are welcome.

---

## ⭐ Support

If you like this project, consider starring the repository ⭐
