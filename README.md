# 🔐 MAC Address Changer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey)
![License](https://img.shields.io/badge/License-Educational-green)

A professional Python script that allows you to **change the MAC address** of any network interface on **Linux systems** using the command line.

This tool is designed for **educational, security, and penetration testing purposes**.

---

## 🚀 Features

- Change MAC address of any network interface
- Display current MAC address before modification
- Verify MAC address after change
- Simple and user-friendly CLI
- Clean, readable, and beginner-friendly code
- Useful for:
  - Penetration Testing
  - Privacy protection
  - Network security labs
  - Ethical hacking practice

---

## 🛠️ Requirements

- Linux Operating System
- Python 3.x
- Root privileges (sudo)
- `ifconfig` command

Install required tools if missing:

```bash
sudo apt update
sudo apt install net-tools
```

---

## 📌 Usage

```bash
sudo python3 mac_changer.py -e <interface> -m <new_mac>
```

---

## 🔎 Example

```bash
sudo python3 mac_changer.py -e eth0 -m 00:11:22:33:44:55
```

---

## 🧠 How It Works

1. Parses command-line arguments (`-e` for interface, `-m` for MAC address)
2. Reads the current MAC address using `ifconfig`
3. Disables the network interface
4. Assigns the new MAC address
5. Re-enables the interface
6. Verifies whether the MAC address was changed successfully

---

## 📂 Project Structure

```text
.
├── mac_changer.py
└── README.md
```

---

## ⚠️ Disclaimer

This project is intended **for educational and legal purposes only**.

- Do NOT use this tool on networks you do not own
- Do NOT use without proper authorization
- The author is NOT responsible for any misuse or illegal activity

---

## 📚 Python Libraries Used

- subprocess
- optparse
- re

---

## 👨‍💻 Author

Developed for learning and cybersecurity practice.  
The script is fully customizable and can be extended with additional features.

---

## ⭐ Future Improvements

- Random MAC address generator
- Replace `optparse` with `argparse`
- NetworkManager support
- GUI version
- Automatic interface detection

---

## 🌟 Support

If you find this project helpful:

- ⭐ Star the repository
- 🍴 Fork it
- 🧠 Learn and improve it

Happy hacking 🚀
