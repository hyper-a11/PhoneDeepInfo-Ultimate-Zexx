# 📞 PhoneDeepInfo Ultimate Zexx

A Python tool for advanced phone number, IP, and OSINT lookup.  
Made by **hyper-a11** 🚀  


=== Phone Info ===
Country      : IN
Valid        : True
Possible     : True
Carrier      : Airtel
Time Zones   : ('Asia/Kolkata',)
Geo (approx) : India

=== NumVerify Lookup ===
Location : Maharashtra (India)
Carrier  : Airtel
---

## 🔥 Features
| Feature | Description |
|---------|-------------|
| 📱 Phone Lookup | Country, carrier, timezone, validity |
| 🌍 NumVerify API | Advanced location & carrier info |
| 🔍 Social Media Search | Google Dorking for Facebook, LinkedIn, Instagram, Twitter |
| 💬 Telegram Search | Find Telegram profiles |
| 🔐 Breach Lookup | Check Scylla.sh & Dehashed for leaked data |
| 🌐 IP Lookup | Geolocation (City, ISP, Lat/Lon) |
| ✉️ Email/Username OSINT | Search social media & GitHub |

---

## 🖼 Screenshot
*(Example of running the tool in Termux)*  
![PhoneDeepInfo Screenshot](https://via.placeholder.com/800x300.png?text=PhoneDeepInfo+Ultimate+Zexx)

---

## ⚡ Installation
```bash
git clone https://github.com/hyper-a11/PhoneDeepInfo-Ultimate-Zexx.git
cd PhoneDeepInfo-Ultimate-Zexx
pip install -r requirements.txt

---

### **📜 setup.sh**
```bash
#!/bin/bash

echo "📲 Setting up PhoneDeepInfo-Ultimate-Zexx..."
pkg update -y && pkg upgrade -y
pkg install python git -y
pip install -r requirements.txt
echo "✅ Setup Complete! Run: python phone_deep_info_ultimate.py +911234567890"
