# Ollama Wrapper - 鏈湴澶фā鍨嬭繍琛屽伐鍏峰皝瑁?
[English](#english) | [涓枃](#涓枃)

---

## 馃搶 涓枃

### 椤圭洰绠€浠?
**Ollama** 鏄竴涓紑婧愮殑鏈湴澶ц瑷€妯″瀷 (LLM) 杩愯宸ュ叿锛屾敮鎸佷竴閿儴缃插拰杩愯鍚勭被寮€婧愭ā鍨嬶紙濡?Llama 3銆丟emma 3銆丮istral 绛夛級銆傛湰椤圭洰 (`ollama-wrap`) 鎻愪緵 Python 鍜?curl 璋冪敤灏佽锛屾柟渚垮揩閫熼泦鎴愬埌鍚勭被搴旂敤涓€?
> 猸?GitHub 鏄熸爣 82,000+锛屾湰鍦?LLM 杩愯鏍囨潌宸ュ叿

### 鏍稿績鐗规€?
- 馃枼锔?**璺ㄥ钩鍙?*锛氭敮鎸?macOS銆乄indows銆丩inux銆丏ocker
- 馃殌 **涓€閿繍琛?*锛氫竴鏉″懡浠ゅ嵆鍙惎鍔ㄦā鍨?- 馃寪 **REST API**锛氳交閲忕骇 API 鎺ュ彛锛屾柟渚块泦鎴?- 馃摝 **妯″瀷甯傚満**锛氬唴缃ā鍨嬪簱锛屾寔缁洿鏂?- 馃捇 **缁堢鑱婂ぉ**锛氱洿鎺ュ湪缁堢涓庢ā鍨嬪璇?
### 蹇€熷紑濮?
#### 1. 瀹夎 Ollama

```powershell
# Windows
irm https://ollama.com/install.ps1 | iex

# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Docker
docker run -d -p 11434:11434 ollama/ollama
```

#### 2. 杩愯妯″瀷

```powershell
# 鎷夊彇骞惰繍琛?Gemma 3
ollama run gemma3

# 鎷夊彇骞惰繍琛?Llama 3
ollama run llama3

# 鎷夊彇骞惰繍琛?Mistral
ollama run mistral
```

#### 3. API 璋冪敤绀轰緥

**Python 璋冪敤锛?*

```python
import requests

url = "http://localhost:11434/api/chat"
headers = {"Content-Type": "application/json"}
data = {
    "model": "gemma3",
    "messages": [
        {"role": "user", "content": "涓轰粈涔堝ぉ绌烘槸钃濊壊鐨勶紵"}
    ],
    "stream": False
}

response = requests.post(url, json=data, headers=headers)
print(response.json()["message"]["content"])
```

**curl 璋冪敤锛?*

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma3",
  "messages": [{"role": "user", "content": "涓轰粈涔堝ぉ绌烘槸钃濊壊鐨勶紵"}],
  "stream": false
}'
```

### API 绔偣涓€瑙?
| 绔偣 | 鏂规硶 | 璇存槑 |
|------|------|------|
| `/api/chat` | POST | 瀵硅瘽鐢熸垚 |
| `/api/generate` | POST | 鏂囨湰鐢熸垚 |
| `/api/tags` | GET | 鍒楀嚭宸蹭笅杞芥ā鍨?|
| `/api/show` | POST | 妯″瀷淇℃伅 |
| `/api/create` | POST | 鍒涘缓妯″瀷 |
| `/api/pull` | POST | 鎷夊彇妯″瀷 |
| `/api/push` | POST | 鎺ㄩ€佹ā鍨?|
| `/api/delete` | DELETE | 鍒犻櫎妯″瀷 |
| `/api/embeddings` | POST | 鍚戦噺宓屽叆 |

### 妯″瀷搴撴帹鑽?
| 妯″瀷 | 鍛戒护 | 鍙傛暟閲?|
|------|------|--------|
| Llama 3 | `ollama run llama3` | 8B |
| Gemma 3 | `ollama run gemma3` | 12B |
| Mistral | `ollama run mistral` | 7B |
| Qwen 2.5 | `ollama run qwen2.5` | 7B |
| DeepSeek Coder | `ollama run deepseek-coder` | 6.7B |

### 椤圭洰缁撴瀯

```
ollama-wrap/
鈹溾攢鈹€ README.md           # 鏈枃浠?鈹溾攢鈹€ demo/
鈹?  鈹溾攢鈹€ demo.py         # Python 璋冪敤绀轰緥
鈹?  鈹斺攢鈹€ demo.sh         # curl 璋冪敤绀轰緥
鈹斺攢鈹€ docs/
    鈹斺攢鈹€ api_reference.md # API 鍙傝€冩枃妗?```

### 鐩稿叧璧勬簮

- 馃寪 瀹樼綉锛歨ttps://ollama.com
- 馃摎 鏂囨。锛歨ttps://docs.ollama.com
- 馃挰 Discord锛歨ttps://discord.gg/ollama
- 馃悪 GitHub锛歨ttps://github.com/ollama/ollama

---

## 馃搶 English

### Project Introduction

**Ollama** is an open-source local large language model (LLM) runtime that supports one-command deployment and running of various open-source models (such as Llama 3, Gemma 3, Mistral, etc.). This project (`ollama-wrap`) provides Python and curl call wrappers for easy integration into various applications.

> 猸?82,000+ GitHub stars, the benchmark for local LLM runtime

### Key Features

- 馃枼锔?**Cross-platform**: Supports macOS, Windows, Linux, Docker
- 馃殌 **One-command run**: Start a model with a single command
- 馃寪 **REST API**: Lightweight API for easy integration
- 馃摝 **Model Library**: Built-in model hub with regular updates
- 馃捇 **Terminal Chat**: Chat with models directly in terminal

### Quick Start

#### 1. Install Ollama

```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows
irm https://ollama.com/install.ps1 | iex

# Docker
docker run -d -p 11434:11434 ollama/ollama
```

#### 2. Run a Model

```bash
# Pull and run Gemma 3
ollama run gemma3

# Pull and run Llama 3
ollama run llama3

# Pull and run Mistral
ollama run mistral
```

#### 3. API Call Examples

**Python:**

```python
import requests

url = "http://localhost:11434/api/chat"
headers = {"Content-Type": "application/json"}
data = {
    "model": "gemma3",
    "messages": [
        {"role": "user", "content": "Why is the sky blue?"}
    ],
    "stream": False
}

response = requests.post(url, json=data, headers=headers)
print(response.json()["message"]["content"])
```

**curl:**

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma3",
  "messages": [{"role": "user", "content": "Why is the sky blue?"}],
  "stream": false
}'
```

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/chat` | POST | Chat completion |
| `/api/generate` | POST | Text generation |
| `/api/tags` | GET | List downloaded models |
| `/api/show` | POST | Model info |
| `/api/create` | POST | Create model |
| `/api/pull` | POST | Pull model |
| `/api/push` | POST | Push model |
| `/api/delete` | DELETE | Delete model |
| `/api/embeddings` | POST | Text embeddings |

### Recommended Models

| Model | Command | Parameters |
|-------|---------|------------|
| Llama 3 | `ollama run llama3` | 8B |
| Gemma 3 | `ollama run gemma3` | 12B |
| Mistral | `ollama run mistral` | 7B |
| Qwen 2.5 | `ollama run qwen2.5` | 7B |
| DeepSeek Coder | `ollama run deepseek-coder` | 6.7B |

### Project Structure

```
ollama-wrap/
鈹溾攢鈹€ README.md           # This file
鈹溾攢鈹€ demo/
鈹?  鈹溾攢鈹€ demo.py         # Python demo
鈹?  鈹斺攢鈹€ demo.sh         # curl demo
鈹斺攢鈹€ docs/
    鈹斺攢鈹€ api_reference.md # API reference
```

### Resources

- 馃寪 Website锛歨ttps://ollama.com
- 馃摎 Docs锛歨ttps://docs.ollama.com
- 馃挰 Discord锛歨ttps://discord.gg/ollama
- 馃悪 GitHub锛歨ttps://github.com/ollama/ollama

---

## License

MIT License - See [Ollama](https://github.com/ollama/ollama) for original project.