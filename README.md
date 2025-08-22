
# Real-Time Object Alert 🚨

This project uses **YOLOv11n** for real-time object detection and sends an **instant WhatsApp alert** when a specific object (like a mobile phone, person, etc.) is detected in the video stream.

## 🔧 Features

* Real-time object detection with **YOLOv11n**
* Detects custom or pre-trained objects
* Sends **WhatsApp messages automatically** when a target object is detected
* Works with webcam or video files

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/arif124713/realtime-object-alert.git
cd realtime-object-alert
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the script:

```bash
python main.py
```

Customize the target object and WhatsApp number in the code:

```python
target_object = "cell phone"
phone_number = "+8801XXXXXXXXX"
```

## 📂 Project Structure

```
realtime-object-alert/
│── main.py               # Main script
│── requirements.txt      # Dependencies
│── README.md             # Documentation
```

## ✅ Example Output

* Detects "cell phone" in webcam stream
* Instantly sends a WhatsApp message:
  *“Alert 🚨: Mobile phone detected!”*

## 💡 Use Cases

* 🔒 **Security Systems** – Get alerts when suspicious objects (like weapons) are detected.
* 📱 **Workplace Monitoring** – Receive notifications if employees use mobile phones in restricted areas.
* 🏠 **Home Safety** – Detect and alert if unknown persons enter through a CCTV feed.
* 🎒 **School/Exam Monitoring** – Detect mobile phones during examinations and send alerts.
* 🚗 **Parking/Traffic Monitoring** – Detect vehicles and send alerts to authorities.

---



---

## 🚀 Future Improvements

* Support for multiple objects → multiple numbers.
* Telegram/Email integration.
* Push notifications instead of browser-based WhatsApp.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss your ideas.

---

## 📜 License

This project is licensed under the MIT License.

---

👨‍💻 Developed by [Arif Hussain](https://github.com/arif124713)


