from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

# Target URLs
urls = ["https://github.com/6t9xstar/6t9/tree/main"] * 1000
# ⚠️ Keep this realistic (1000, not 10k)

# Linux User Agent (Real Chrome on Linux)
LINUX_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

options = Options()

# Headless (modern)
options.add_argument("--headless=new")

# Stealth / anti-detection flags
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# User Agent
options.add_argument(f"--user-agent={LINUX_UA}")

# Window size (important)
options.add_argument("--window-size=1920,1080")

# Remove automation flag
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)

# Extra stealth (JS)
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        """
    },
)

try:
    for i, url in enumerate(urls, 1):
        driver.get(url)
        print(f"[{i}/{len(urls)}] Opened")

        # Human-like delay (VERY IMPORTANT)
        time.sleep(random.uniform(2.5, 5.0))

finally:
    driver.quit()
    print("Done ✅ Browser closed.")