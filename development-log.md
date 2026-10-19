# DualCoffeeLabs 開發歷程記錄 (Development Log)

本文件依據 [AI Agent 行動準則](file:///.antigravityrules) 建立，完整記錄專案的每一次使用者需求 (User Prompt)、AI 的理解分析 (Understanding)、思考與技術解法 (Thoughts & Solutions)、實作修改 (Implementation) 與驗證部署 (Verification & Deployment)。

---

## 2026-10-19 22:13 | 建立 AI Agent 行動準則與自動化規範

### 1. 接收需求 (User Prompt)
使用者提供 AI Agent 專屬行動規範，要求建立標準規範文件並落實於日常開發：
1. 每次任務結尾必須告知使用者「已使用此準則」。
2. 從頭到尾記錄程式開發歷程至 `development-log.md`。
3. 建立 `Bulletin.json` 作為跨 Agent / Tools / MCP 支援看板。
4. 授權此 Workspace 下的所有檔案管理操作。
5. 終端機防打斷規範：
   - 嚴禁透過終端機進行檔案與字串搜尋（禁止 `Select-String`, `Get-ChildItem`, `git grep` 等），一律使用內建工具。
   - 所有單行測試與動態查詢一律覆寫至 `test_safe_command.py` 後執行 `python test_safe_command.py`。
6. 可與使用者對話持續修改此規範文件使其更完整。

### 2. AI 理解與架構設計 (Understanding & Strategy)
- **規則持久化**：將規範寫入專案根目錄之 `.antigravityrules`，使 Antigravity 系統能將其作為 System Rules 永久加載。
- **支援公佈欄**：初始化 `Bulletin.json`，提供結構化的需求堆疊格式（含 id, timestamp, requestor, needed_resource_type, description, status）。
- **歷程追蹤**：建立 `development-log.md`，並將先前重要里程碑（SCA 萃取率保底修正、LINE 預覽 OG 標籤修正、階段卡片重構）一併彙整入檔以保持完整脈絡。
- **測試隔離**：建立範本 `test_safe_command.py`，作為日後所有終端測試指令的唯一執行入口。

### 3. 實作變更 (Implementation)
- 新增檔案：
  - [`.antigravityrules`](file:///.antigravityrules)：包含 6 大核心規範。
  - [`Bulletin.json`](file:///Bulletin.json)：跨資源支援公告板。
  - [`development-log.md`](file:///development-log.md)：開發全歷程記錄檔案。
  - [`test_safe_command.py`](file:///test_safe_command.py)：安全執行單行/多行查詢腳本。

---

## 2026-10-19 21:24 | 修復 Switch 浸泡時間 40s 至 56s 時 SCA 數值未動態響應問題

### 1. 接收需求 (User Prompt)
使用者回報在 Switch 聰明杯模式下，將第 3 段止水浸泡時間從 40 秒調整為 56 秒時，上方 KPI 顯示的手沖萃取率 (EY 13.2%) 與濃度 (TDS 1.00%) 完全沒有變化。

### 2. AI 理解與根因分析 (Root Cause Analysis)
- 透過物理公式與截圖比對發現：右側明細面板中「濾杯與接觸時間」倍率確實有正常提升（從 `×1.050` 上升至 `×1.072`），未保底之原始計算萃取率 `rawEY` 實際上是從 `12.61%` 增加至 `12.89%`。
- 根因：程式碼第 6452 行設有 `Math.max(13.2, Math.min(25.2, rawEY))` 硬截斷保底。在使用者偏粗研磨 (7.0)、低溫 (70°C)、淺焙豆等組合下，兩個原始數值皆小於 13.2%，因此皆被強制夾斷至 `13.2%`，造成介面完全沒有數值變化反饋。

### 3. 技術解法與修改 (Solution & Code Changes)
- 在 [`index.html`](file:///index.html) 與 [`dual_coffee_lab.html`](file:///dual_coffee_lab.html)：
  - 將萃取率下限保底放寬至真實極端低萃取物理範圍：`Math.max(8.0, Math.min(28.0, rawEY))`。
  - 增強 Switch 浸泡擴散動力學：依據菲克擴散定律，將 `immersionSynergy` 改為非線性平方根時間模型（`1 + Math.min(0.08, Math.pow(totalImmersionSec / 60, 0.6) * 0.055)`）。
  - 將金杯圖譜（Gold Cup Chart）座標軸下限自 14% 延伸至 11%，支援低萃取率落點完整呈現。
- 驗證：執行語法檢查通過，推送到 GitHub（commit `7aa9ea8`）並完成 Firebase Hosting 部署。

---

## 2026-10-18 22:33 | 解決 LINE 連結預覽抓取 noscript 警語問題

### 1. 接收需求 (User Prompt)
將站點網址分享至 LINE 聊天室時，預覽縮圖下方文字抓取到了 `<noscript>` 的黃色驚嘆號警告（「⚠️ 您的手機檔案預覽器目前已禁用 JavaScript...」）。

### 2. AI 理解與根因分析 (Root Cause Analysis)
- LINE 等通訊軟體的爬蟲抓取預覽時不執行 JavaScript，且專案原始 `<head>` 中缺乏 Open Graph (OG) 與 `<meta name="description">` 標籤，導致爬蟲直接抓取 `<body>` 內第一段可見的純文字（即 `<noscript>` 內的文字）。

### 3. 技術解法與修改 (Solution & Code Changes)
- 在 [`index.html`](file:///index.html) 與 [`dual_coffee_lab.html`](file:///dual_coffee_lab.html) 的 `<head>` 補上完整的 `<meta name="description">`、`og:title`、`og:description`、`og:url`、`og:type`、`og:site_name` 及 `twitter:card`。
- 將 `<noscript>` 內容重構，於第一行放上「CoffeeLabs 咖啡全維度實驗室」正向標題作為雙重防護。
- 驗證：語法檢查通過，推送到 GitHub（commit `789c2be`）並部署至 Firebase。

---

## 2026-10-18 22:15 | 手沖各階段注水卡片 4 欄步進器重構與紅框緊湊化

### 1. 接收需求 (User Prompt)
黃框（注水階段卡片容器）內容過於擁擠、左右橫向滑動操作不便；紅框（沖煮粉重/粉水比/攪拌手法）留白過多顯得鬆散。

### 2. AI 理解與架構設計 (Understanding & Strategy)
- 黃框：卡片內塞入兩條滑動拉桿與流速調整，造成寬度超載與橫向捲動軸。需徹底移除卡片內微型 Slider，改為固定 4 欄格點微型按鈕佈局（水量、流速、水溫、時長）。
- 紅框：縮減 padding 與 margin，將攪拌手法精簡為膠囊型按鈕，流派摘要橫幅進行緊湊化處理。

### 3. 技術解法與修改 (Solution & Code Changes)
- 更新 [`index.html`](file:///index.html) 與 [`dual_coffee_lab.html`](file:///dual_coffee_lab.html) 中的參數區域與 `renderPourStagesUI()` 模板。
- 加入 `overflow-x-hidden` 徹底杜絕橫向位移與溢出。
- 驗證：語法檢查通過，推送到 GitHub（commit `f29c8a3`）並部署至 Firebase。
