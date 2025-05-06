import requests

API_KEY = '118cb6be32f9cd477ff6439ae7b42a7381a3e0b6dc06fdcd149df31de216e46f5088be67d71ec22f' 
ABUSE_CATEGORIES = {
    3: 'Fraud Orders',
    4: 'DDoS Attack',
    5: 'FTP Brute-Force',
    6: 'Ping of Death',
    7: 'Phishing',
    8: 'Fraud VoIP',
    9: 'Open Proxy',
    10: 'Web Spam',
    11: 'Email Spam',
    12: 'Blog Spam',
    13: 'VPN IP',
    14: 'Port Scan',
    15: 'Hacking',
    16: 'SQL Injection',
    17: 'Spoofing',
    18: 'Brute-Force',
    19: 'Bad Web Bot',
    20: 'Exploited Host',
    21: 'Web App Attack',
    22: 'SSH',
    23: 'IoT Targeted'
}

def check_ip(ip):
    url = 'https://api.abuseipdb.com/api/v2/check'
    headers = {
        'Key': API_KEY,
        'Accept': 'application/json'
    }
    params = {
        'ipAddress': ip,
        'maxAgeInDays': 90,
        'verbose': True
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"[!] Failed to check IP {ip}: {response.status_code}")
        return

    data = response.json().get('data', {})

    print(f"\n=== Result for {ip} ===")
    print(f"IP: {data.get('ipAddress')}")
    print(f"Country: {data.get('countryCode', '-')}")
    print(f"Domain: {data.get('domain', '-')}")
    print(f"ISP: {data.get('isp', '-')}")
    print(f"Abuse Score: {data.get('abuseConfidenceScore')} / 100")
    print(f"Total Reports: {data.get('totalReports')}")
    print(f"Last Reported: {data.get('lastReportedAt', '-')}")

    print("\nTop Reports:")
    reports = data.get('reports', [])
    if not reports:
        print(" - No recent reports found.")
    else:
        for i, report in enumerate(reports[:5], start=1):
            date = report['reportedAt'][:19].replace("T", " ")
            country = report.get('reporterCountryCode', 'UNK')
            categories = report.get('categories', [])
            category_names = [ABUSE_CATEGORIES.get(cat_id, f"Unknown({cat_id})") for cat_id in categories]
            category_str = ", ".join(category_names)
            comment = report.get('comment', '-').replace("\n", " ").strip()
            if len(comment) > 60:
                comment = comment[:57] + "..."
            print(f"#{i:<2} | {date} | {country:<3} | {category_str:<40} | {comment}")

    print(f"\n📄 Source: https://www.abuseipdb.com/check/{ip}")

if __name__ == '__main__':
    while True:
        ip_to_check = input("Enter an IP address to check (or 'exit' to quit): ")
        if ip_to_check.lower() == 'exit':
            break
        check_ip(ip_to_check)
        print("\n" + "="*40 + "\n")
        print("Press Enter to check another IP address or type 'exit' to quit.")
