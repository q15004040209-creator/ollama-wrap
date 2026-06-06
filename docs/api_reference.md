# Ollama API 鍙傝€冩枃妗?
## 鍩虹淇℃伅

- **Base URL**: `http://localhost:11434`
- **Content-Type**: `application/json`

---

## 绔偣璇﹁В

### 1. `/api/chat` - 瀵硅瘽鐢熸垚

**鏂规硶**: `POST`

**璇锋眰浣?*:
```json
{
  "model": "gemma3",
  "messages": [
    {"role": "system", "content": "浣犳槸涓€涓湁甯姪鐨勫姪鎵?},
    {"role": "user", "content": "浣犲ソ锛岃浠嬬粛涓€涓嬩綘鑷繁"}
  ],
  "stream": false,
  "options": {
    "temperature": 0.7,
    "num_predict": 256
  }
}
```

**鍝嶅簲**:
```json
{
  "model": "gemma3",
  "message": {
    "role": "assistant",
    "content": "浣犲ソ锛佹垜鏄?.."
  },
  "done": true
}
```

---

### 2. `/api/generate` - 鏂囨湰鐢熸垚

**鏂规硶**: `POST`

**璇锋眰浣?*:
```json
{
  "model": "gemma3",
  "prompt": "鍐欎竴涓叧浜嶢I鐨勬晠浜?,
  "stream": false,
  "options": {
    "temperature": 0.8,
    "num_predict": 512
  }
}
```

**鍝嶅簲**:
```json
{
  "model": "gemma3",
  "response": "浠庡墠鏈変竴涓狝I...",
  "done": true
}
```

---

### 3. `/api/tags` - 妯″瀷鍒楄〃

**鏂规硶**: `GET`

**鍝嶅簲**:
```json
{
  "models": [
    {
      "name": "gemma3:latest",
      "size": 5000000000,
      "modified_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

---

### 4. `/api/show` - 妯″瀷淇℃伅

**鏂规硶**: `POST`

**璇锋眰浣?*:
```json
{
  "name": "gemma3"
}
```

---

### 5. `/api/create` - 鍒涘缓妯″瀷

**鏂规硶**: `POST`

浠?Modelfile 鍒涘缓妯″瀷銆?
---

### 6. `/api/pull` - 鎷夊彇妯″瀷

**鏂规硶**: `POST`

**璇锋眰浣?*:
```json
{
  "name": "llama3"
}
```

---

### 7. `/api/delete` - 鍒犻櫎妯″瀷

**鏂规硶**: `DELETE`

**璇锋眰浣?*:
```json
{
  "name": "llama3"
}
```

---

### 8. `/api/embeddings` - 鍚戦噺宓屽叆

**鏂规硶**: `POST`

**璇锋眰浣?*:
```json
{
  "model": "gemma3",
  "prompt": "瑕佸祵鍏ョ殑鏂囨湰"
}
```

---

## 閫氱敤閫夐」 (options)

| 鍙傛暟 | 绫诲瀷 | 榛樿鍊?| 璇存槑 |
|------|------|--------|------|
| temperature | float | 0.8 | 閲囨牱娓╁害锛岃秺楂樿秺闅忔満 |
| num_predict | int | 256 | 鏈€澶?token 鏁?|
| top_p | float | 0.9 | 鏍搁噰鏍锋鐜?|
| top_k | int | 40 | top-k 閲囨牱 |
| stop | string/array | - | 鍋滄璇?|
| repeat_penalty | float | 1.1 | 閲嶅鎯╃綒 |

---

## 娴佸紡鍝嶅簲

灏?`stream` 璁句负 `true`锛屾湇鍔″櫒灏嗚繑鍥?Server-Sent Events (SSE) 鏍煎紡鐨勬祦寮忔暟鎹€?
```
curl http://localhost:11434/api/chat -d '{
  "model": "gemma3",
  "messages": [{"role": "user", "content": "Hello"}],
  "stream": true
}'
```

娴佸紡鍝嶅簲鏍煎紡锛?```
data: {"model":"gemma3","message":{"role":"assistant","content":"He"},"done":false}
data: {"model":"gemma3","message":{"role":"assistant","content":"llo"},"done":false}
data: {"model":"gemma3","message":{"role":"assistant","content":""},"done":true}
```