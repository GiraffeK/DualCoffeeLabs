# CoffeeLabs ☕🫖🔥

> 咖啡全維度物理模擬實驗室：烘豆熱力動力學、手沖滴濾與義式高壓萃取 (Roasting, Pour-Over & Espresso Dialing-in Lab)

[![Firebase Hosting](https://img.shields.io/badge/Demo-Firebase%20Hosting-orange?style=flat-square&logo=firebase)](https://dualcoffeelabs.web.app)
[![GitHub Pages](https://img.shields.io/badge/Demo-GitHub%20Pages-blue?style=flat-square&logo=github)](https://giraffek.github.io/DualCoffeeLabs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**CoffeeLabs** 是一款專為烘豆師、咖啡師與咖啡愛好者打造的跨階段互動式物理模擬實驗室，從**生豆熱力烘焙動力學**、到**手沖滴濾滲透流體力學**、再到**義式高壓濃縮萃取**，實現從生豆到一杯完美咖啡的一站式模擬與風味預測。

---

## 🌟 三棲核心實驗室

### 🔥 1. 烘豆實驗室 (Kaleido Sniper M10 & 熱門烘豆機)
- **物理與化學動力學模型**：精確模擬入豆溫（Charge Temp）、回溫點（Turnaround Point, TP）、脫水轉黃點（Dry End）、梅納反應期、一爆（First Crack）與發展時間（Development Time）。
- **即時熱力曲線與 RoR 升溫率**：
  - 豆溫（BT, Bean Temp）與環境溫（ET, Env Temp）
  - 實時 RoR（Rate of Rise）升溫速率曲線
  - 發展時間比（DTR %）與焦糖化指數
  - 烘焙度預測：Agtron Commercial / Gourmet 色值、烘焙失重率（%）
- **化學成分動力學演變**：實時追蹤有機酸質分解、綠原酸降解、梅納香氣化合物積累、熱裂解苦味物質與醇厚度發展。
- **熱門機型與莊園豆曲線庫**：
  - 支援 Kaleido Sniper M10、Aillio Bullet R1、Stronghold S7 Pro 等機型熱力特徵。
  - 內建祕魯藝伎黑蜜、肯亞辛巴日曬藝伎、西達摩溫妮公主、卡法森林金寶村、義式配方深焙等實戰階梯式烘焙曲線。
- **跨實驗室參數連動**：烘焙完成後可一鍵將熟豆 Agtron 色度與風味特徵**「帶入熟豆參數至手沖實驗室」**或**「帶入熟豆參數至義式實驗室」**，自動推薦對應之水溫與研磨度！

### 🫖 2. 手沖咖啡實驗室 (Pour-Over Coffee Lab)
- **多種濾杯系統**：支援 Hario V60、Kalita Wave 蛋糕濾杯、Origami 摺紙濾杯、Kono 等不同流速特性的濾杯模型。
- **進階沖煮手法與名家預設**：
  - 粕谷哲 4:6 法五段變溫沖煮
  - 三段式中心注水
  - 低溫濃厚浸潤法
- **莊園精品豆風味庫**：內建祕魯桑托斯藝伎黑蜜、衣索比亞西達摩日曬、肯亞日曬藝伎、薩爾瓦多聖依蓮娜蜜處理等多款精品咖啡豆特性模擬。
- **水溫衰減與攪拌擾動模擬**：模擬注水過程中的熱流流失與粉層擾動程度對芳香物質萃取的動態影響。

### ☕ 3. 義式濃縮實驗室 (Espresso Dialing-in Lab)
- **物理動力學模擬**：模擬研磨粗細、粉餅阻力、預浸透水（Pre-infusion）、萃取水壓（Bar）、水溫對流速與萃取率的影響。
- **通道效應（Channeling）偵測**：即時預測過細研磨或布粉不均導致的噴濺與穿孔風險。
- **即時數值與金杯圖**：
  - 總溶解固體量（TDS %）
  - 萃取率（Extraction Yield, EY %）
  - 流速（Flow Rate, g/s）
  - 即時感官風味雷達圖（酸質、甜感、醇厚度、苦味、餘韻）
- **經典食譜預設**：一鍵套用標準平衡黃金萃取、研磨過細/通道效應、研磨過粗/萃取不足、高溫苦澀等預設進行對比學習。

---

## 📱 現代化體驗與行動端最佳化

- **不遮擋操作視窗**：頂部選單針對行動裝置自適應流暢滾動，不佔據半螢幕空間；預設食譜單行橫向滑動。
- **多端適配（RWD）**：針對行動裝置最佳化的觸控步進器（Touch Steppers）與底部浮動數據列（可隨時一鍵收合/展開）。
- **環境音效**：內建水流聲、滴濾聲與一爆二爆爆裂音效模擬。
- **零外部伺服器依賴**：純前端靜態 Web 應用（HTML5 + TailwindCSS + Web Audio API + Canvas），無須安裝任何後端依賴，雙擊即可執行。

---

## 🚀 快速開始

### 線上體驗
- **Firebase Hosting**：👉 [https://dualcoffeelabs.web.app/](https://dualcoffeelabs.web.app/)
- **GitHub Pages**：👉 [https://giraffek.github.io/DualCoffeeLabs/](https://giraffek.github.io/DualCoffeeLabs/)

### 本地執行
1. 複製本儲存庫：
   ```bash
   git clone https://github.com/GiraffeK/DualCoffeeLabs.git
   ```
2. 直接使用任意現代瀏覽器開啟 `index.html` 或 `dual_coffee_lab.html` 即可使用。

---

## 📂 專案結構

```
DualCoffeeLabs/
├── index.html            # 主應用入口（支援 GitHub Pages 與 Firebase Hosting）
├── dual_coffee_lab.html  # 完整功能原始檔（三棲實驗室整合版）
├── README.md             # 專案介紹文件
├── firebase.json         # Firebase Hosting 部署設定
└── .gitignore            # Git 忽略配置
```

---

## 📄 授權協議

本專案基於 [MIT License](LICENSE) 開源。
