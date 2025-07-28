# 🧪 Web Automation: Playwright vs Selenium

A quick comparative overview of two leading browser automation tools — **Playwright** and **Selenium** — highlighting their features, strengths, and sample usage in Python.

---

## ⚙️ Overview

| Feature                        | **Playwright**                              | **Selenium**                            |
|-------------------------------|---------------------------------------------|------------------------------------------|
| **Initial Release**           | 2020                                        | 2004                                     |
| **Maintained By**             | Microsoft                                   | OpenJS Foundation                        |
| **Language Support**          | Python, JavaScript, TypeScript, Java, C#    | Python, Java, JavaScript, Ruby, C#, Kotlin |
| **Browser Support**           | Chromium, Firefox, WebKit                   | Chrome, Firefox, Edge, Safari, IE        |
| **Headless Mode**             | Built-in and optimized                      | Supported                                |
| **Auto-Waiting**              | ✅ Built-in intelligent wait system         | ❌ Manual waits usually required         |
| **Cross-Browser Testing**     | ✅ Native support for all major engines     | ✅ With setup and drivers                |
| **Parallel Execution**        | ✅ Built-in (Playwright Test)               | ⚠️ Requires external test runners        |
| **Network Interception**      | ✅ Fully supported                          | ⚠️ Limited or with workarounds           |
| **Mobile Emulation**          | ✅ Supported                                | ⚠️ Limited                               |
| **Shadow DOM Support**        | ✅ Yes                                      | ✅ Yes (manual effort)                   |

---

## 🚀 When to Use What?

### ✅ Choose **Playwright** if:
- You need fast and modern test automation.
- Your app is built with modern frameworks like React/Vue/Angular.
- You need smooth multi-browser, multi-context testing.
- You want a developer-friendly testing experience with fewer waits.

### ✅ Choose **Selenium** if:
- You're maintaining or extending legacy automation scripts.
- You need Internet Explorer or Safari support on native devices.
- Your organization already has strong Selenium expertise and infrastructure.

---

## 📚 References 

Playwright: https://playwright.dev/ <br>
Selenium: https://www.selenium.dev/

---
## 🛠️ Built-in Code: GeeksforGeeks Automation

This project includes simple automation scripts using both **Playwright** and **Selenium** to perform UI interactions on [GeeksforGeeks.org](https://www.geeksforgeeks.org). It demonstrates logging in, menu navigation using hover, click, scroll, and text extraction actions for both frameworks.

**Playwright based Automation** - pw_geeksforgeeks.py
<br>
**Selenium based Automation** - sl_geeksforgeeks.py

```
Install Dependencies and Start Automating
Happy Automation 😊
