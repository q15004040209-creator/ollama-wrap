#!/bin/bash
# Ollama curl Demo
# 鏈湴澶фā鍨?curl 璋冪敤绀轰緥
# 杩愯: bash demo.sh 鎴?./demo.sh

OLLAMA_URL="http://localhost:11434"

echo "=================================================="
echo "Ollama curl Demo"
echo "=================================================="

# 1. 妫€鏌ユ湇鍔＄姸鎬?echo ""
echo "[1] 妫€鏌?Ollama 鏈嶅姟鐘舵€?.."
curl -s --max-time 5 "${OLLAMA_URL}/" | head -c 100 || echo "鏈嶅姟鏈搷搴旓紝璇疯繍琛? ollama serve"

# 2. 鍒楀嚭宸蹭笅杞芥ā鍨?echo ""
echo "[2] 宸蹭笅杞芥ā鍨嬪垪琛?"
curl -s "${OLLAMA_URL}/api/tags" | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    models = data.get('models', [])
    if models:
        for m in models:
            name = m.get('name', 'unknown')
            size = m.get('size', 0)
            print(f'  - {name} ({size/1e9:.1f}GB)')
    else:
        print('  鏆傛棤妯″瀷锛岃杩愯: ollama run gemma3')
except:
    print('  鏃犳硶鑾峰彇妯″瀷鍒楄〃')
" 2>/dev/null || echo "  鏃犳硶鑾峰彇妯″瀷鍒楄〃"

# 3. 瀵硅瘽娴嬭瘯
echo ""
echo "[3] 瀵硅瘽娴嬭瘯 (gemma3):"
echo "   闂: 鐢ㄤ竴鍙ヨ瘽瑙ｉ噴閲忓瓙璁＄畻"
echo -n "   鍥炲: "
response=$(curl -s "${OLLAMA_URL}/api/chat" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "gemma3",
        "messages": [{"role": "user", "content": "鐢ㄤ竴鍙ヨ瘽瑙ｉ噴閲忓瓙璁＄畻"}],
        "stream": false
    }' 2>/dev/null | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    print(data.get('message', {}).get('content', '鏃犲洖澶?))
except:
    print('璇锋眰澶辫触')
" 2>/dev/null)
echo "$response"

# 4. 鏂囨湰鐢熸垚娴嬭瘯
echo ""
echo "[4] 鏂囨湰鐢熸垚娴嬭瘯 (gemma3):"
echo "   鎻愮ず璇? 鍐欎竴棣栧叧浜庝汉宸ユ櫤鑳界殑灏忚瘲"
echo -n "   缁撴灉: "
text=$(curl -s "${OLLAMA_URL}/api/generate" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "gemma3",
        "prompt": "鍐欎竴棣栧叧浜庝汉宸ユ櫤鑳界殑灏忚瘲",
        "stream": false
    }' 2>/dev/null | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    print(data.get('response', '鏃犲洖澶?))
except:
    print('璇锋眰澶辫触')
" 2>/dev/null)
echo "$text"

echo ""
echo "=================================================="
echo "Demo 瀹屾垚!"
echo "=================================================="