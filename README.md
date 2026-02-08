# Web Vulnerability Scanner – Flask UI

**Author:** Teshan  
**Specialization:** Cybersecurity (Undergraduate, Sri Lanka)

---

## 1️⃣ Project Purpose
The Web Vulnerability Scanner is a **Python-based security tool** designed to analyze websites for **common vulnerabilities and missing security headers**.  
It helps developers, students, and security enthusiasts identify **potential risks** in web applications before they can be exploited.

---

## 2️⃣ Key Features

- **Web-based Interface**: Modern HTML/CSS dashboard built with Flask.  
- **Automated Security Checks**: Detects missing HTTP security headers (`X-Frame-Options`, `X-XSS-Protection`, `Content-Security-Policy`).  
- **HTTPS Verification**: Checks if the site uses secure HTTPS connections.  
- **Form Detection**: Counts input forms that may be potential attack vectors.  
- **Severity Classification**: Risk level assigned as **Low / Medium / High** based on security posture.  
- **PDF Reporting**: Generates professional PDF reports of scan results.  
- **Scan History**: Tracks the last 10 scans in JSON for reference and review.

---

## 3️⃣ Technology Stack

- **Backend:** Python 3.x  
- **Web Framework:** Flask  
- **Web Scraping:** BeautifulSoup4  
- **PDF Reporting:** ReportLab  
- **Frontend:** HTML5, CSS3 (modern cyber-themed UI)  
- **Data Storage:** JSON (`history.json`)  

---

## 4️⃣ How It Works

1. User enters a URL in the web interface.  
2. The scanner sends an HTTP/HTTPS request with **browser-like headers**.  
3. Parses HTML to check:  
   - Missing security headers  
   - Number of forms  
   - HTTPS availability  
4. Assigns **severity level**: Low / Medium / High  
5. Stores results in **history.json**  
6. Generates a **PDF report** for download.

---

## 5️⃣ Example Scan Report

