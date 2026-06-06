#!/usr/bin/env python3
"""
Ollama Python Demo
鏈湴澶фā鍨嬭皟鐢ㄧず渚?
渚濊禆: pip install requests
杩愯: python demo.py
"""

import requests
import json

OLLAMA_BASE_URL = "http://localhost:11434"


def chat(model: str, message: str, stream: bool = False) -> str:
    """
    鍙戦€佸璇濊姹傚埌 Ollama

    Args:
        model: 妯″瀷鍚嶇О (濡?gemma3, llama3, mistral)
        message: 鐢ㄦ埛娑堟伅
        stream: 鏄惁娴佸紡杩斿洖

    Returns:
        妯″瀷鍥炲鍐呭
    """
    url = f"{OLLAMA_BASE_URL}/api/chat"
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": message}
        ],
        "stream": stream
    }

    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()
    result = response.json()
    return result["message"]["content"]


def generate(model: str, prompt: str, stream: bool = False) -> str:
    """
    鍙戦€佹枃鏈敓鎴愯姹傚埌 Ollama

    Args:
        model: 妯″瀷鍚嶇О
        prompt: 鎻愮ず璇?        stream: 鏄惁娴佸紡杩斿洖

    Returns:
        鐢熸垚鏂囨湰
    """
    url = f"{OLLAMA_BASE_URL}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }

    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()
    result = response.json()
    return result["response"]


def list_models() -> list:
    """
    鍒楀嚭鎵€鏈夊凡涓嬭浇鐨勬ā鍨?
    Returns:
        妯″瀷鍒楄〃
    """
    url = f"{OLLAMA_BASE_URL}/api/tags"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    result = response.json()
    return result.get("models", [])


def show_model_info(model: str) -> dict:
    """
    鑾峰彇妯″瀷璇︾粏淇℃伅

    Args:
        model: 妯″瀷鍚嶇О

    Returns:
        妯″瀷淇℃伅瀛楀吀
    """
    url = f"{OLLAMA_BASE_URL}/api/show"
    payload = {"name": model}

    response = requests.post(url, json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print("=" * 50)
    print("Ollama Python Demo")
    print("=" * 50)

    # 1. 鍒楀嚭宸蹭笅杞芥ā鍨?    print("\n[1] 宸蹭笅杞芥ā鍨嬪垪琛?")
    try:
        models = list_models()
        if models:
            for m in models:
                print(f"  - {m['name']} ({m.get('size', 'unknown') / 1e9:.1f}GB)")
        else:
            print("  鏆傛棤妯″瀷锛岃杩愯: ollama run gemma3")
    except Exception as e:
        print(f"  鏃犳硶鑾峰彇妯″瀷鍒楄〃: {e}")
        print("  璇风‘淇?Ollama 鏈嶅姟宸插惎鍔?(杩愯: ollama serve)")

    # 2. 瀵硅瘽绀轰緥
    print("\n[2] 瀵硅瘽娴嬭瘯 (gemma3):")
    try:
        response = chat("gemma3", "鐢ㄤ竴鍙ヨ瘽瑙ｉ噴閲忓瓙璁＄畻")
        print(f"  妯″瀷鍥炲: {response}")
    except Exception as e:
        print(f"  瀵硅瘽澶辫触: {e}")

    # 3. 鏂囨湰鐢熸垚绀轰緥
    print("\n[3] 鏂囨湰鐢熸垚娴嬭瘯 (gemma3):")
    try:
        text = generate("gemma3", "鍐欎竴棣栧叧浜庝汉宸ユ櫤鑳界殑灏忚瘲")
        print(f"  鐢熸垚缁撴灉: {text}")
    except Exception as e:
        print(f"  鐢熸垚澶辫触: {e}")

    print("\n" + "=" * 50)
    print("Demo 瀹屾垚!")