#!/usr/bin/env python3
"""GSC Indexing API — 使用系统代理批量提交 URL"""
import json
import time
import sys
import ssl
import urllib.request

# ===== 代理配置 =====
PROXY = "http://127.0.0.1:17891"

# ===== GSC 凭据 =====
CRED = json.loads(open("/Users/mac/WorkBuddy/Claw/SEO/subao-seo-service-account.json").read())
TOKEN_URI = "https://oauth2.googleapis.com/token"
INDEXING_API = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPE = "https://www.googleapis.com/auth/indexing"

URLS = [
    "https://subao.tw/blog/mooncake-shipping-guide-2026",
    "https://subao.tw/blog/clothes-shipping-guide",
    "https://subao.tw/blog/tw-to-cn-food-restrictions-2026",
    "https://subao.tw/sitemap.xml",
]


def urlopen_with_proxy(req, timeout=15):
    """通过系统代理发请求"""
    ctx = ssl.create_default_context()
    https_handler = urllib.request.HTTPSHandler(context=ctx)
    proxy_handler = urllib.request.ProxyHandler({
        "http": PROXY,
        "https": PROXY,
    })
    opener = urllib.request.build_opener(proxy_handler, https_handler)
    return opener.open(req, timeout=timeout)


def create_jwt():
    """手动创建 JWT"""
    import base64
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding

    header = {"alg": "RS256", "typ": "JWT"}
    now = int(time.time())
    claim = {
        "iss": CRED["client_email"],
        "scope": SCOPE,
        "aud": TOKEN_URI,
        "exp": now + 3600,
        "iat": now,
    }

    def b64url(data):
        return base64.urlsafe_b64encode(data).rstrip(b"=").decode()

    h = b64url(json.dumps(header).encode())
    c = b64url(json.dumps(claim).encode())
    signing_input = f"{h}.{c}".encode()

    key = serialization.load_pem_private_key(CRED["private_key"].encode(), password=None)
    sig = key.sign(signing_input, padding.PKCS1v15(), hashes.SHA256())
    return f"{h}.{c}.{b64url(sig)}"


def get_access_token():
    """用 JWT 换取 access token"""
    jwt = create_jwt()
    data = urllib.parse.urlencode({
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwt,
    }).encode()

    req = urllib.request.Request(TOKEN_URI, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")

    resp = urlopen_with_proxy(req)
    result = json.loads(resp.read())
    return result["access_token"]


def submit_url(token, url):
    """提交单个 URL"""
    import urllib.error as ue
    body = json.dumps({"url": url, "type": "URL_UPDATED"}).encode()
    req = urllib.request.Request(INDEXING_API, data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {token}")

    try:
        resp = urlopen_with_proxy(req)
        return resp.status, json.loads(resp.read())
    except ue.HTTPError as e:
        err_body = e.read().decode() if e.fp else str(e)
        return e.code, json.loads(err_body) if err_body else {"error": str(e)}


def main():
    print(f"GSC Indexing API — 提交 {len(URLS)} 个 URL")
    print(f"代理: {PROXY}\n")

    # 测试连通性
    try:
        token = get_access_token()
        print(f"✅ Token 获取成功\n")
    except Exception as e:
        print(f"❌ Token 获取失败: {e}")
        sys.exit(1)

    results = {"success": [], "error": [], "quota": []}

    for i, url in enumerate(URLS, 1):
        tag = f"[{i:02d}/{len(URLS)}]"
        try:
            status, data = submit_url(token, url)

            if status == 200:
                results["success"].append(url)
                print(f"  ✅ {tag} {url}")
            elif status == 429:
                results["quota"].extend(URLS[i-1:])
                print(f"  🟡 {tag} {url} → 配额用尽")
                print(f"  ⚠️ 剩余 {len(URLS)-i} 个未提交")
                break
            elif status == 403:
                err = data.get("error", {}).get("message", str(data))
                results["error"].append((url, err))
                print(f"  ❌ {tag} {url} → 403 权限不足")
                print(f"  💡 需在 GSC 添加 {CRED['client_email']} 为拥有者")
                break
            else:
                err = data.get("error", {}).get("message", str(data))
                results["error"].append((url, err))
                print(f"  ❌ {tag} {url} → {status} {err[:80]}")
        except Exception as e:
            results["error"].append((url, str(e)))
            print(f"  ❌ {tag} {url} → {e}")

        time.sleep(0.5)

    print(f"\n{'='*50}")
    print(f"📊 结果: ✅{len(results['success'])} 🟡{len(results['quota'])} ❌{len(results['error'])} / {len(URLS)}")

    if results["quota"]:
        print(f"\n🟡 明天重试:")
        for u in results["quota"][:5]:
            print(f"  - {u}")

    sys.exit(1 if results["error"] else 0)


if __name__ == "__main__":
    main()
