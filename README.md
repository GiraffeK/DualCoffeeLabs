# DualCoffeeLabs ☕🫖

> 義式濃縮與手沖咖啡參數動態模擬與金杯萃取實驗室 (Espresso & Pour-Over Dialing-in Lab)

[![Firebase Hosting](https://img.shields.io/badge/Demo-Firebase%20Hosting-orange?style=flat-square&logo=firebase)](https://dualcoffeelabs.web.app)
[![GitHub Pages](https://img.shields.io/badge/Demo-GitHub%20Pages-blue?style=flat-square&logo=github)](https://giraffek.github.io/DualCoffeeLabs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

**DualCoffeeLabs** 是一款專為咖啡師與咖啡愛好者打造的互動式萃取物理模擬器，結合流體力學模型、溶解動力學與 SCA 金杯準則（Golden Cup Standard），提供直覺、即時的參數調校與風味預測。

---

## 🌟 核心特色

### ☕ 1. 義式濃縮實驗室 (Espresso Dialing-in Lab)
- **物理動力學模擬**：模擬研磨粗細、粉餅阻力、預浸透水（Pre-infusion）、萃取水壓（Bar）、水溫對流速與萃取率的影響。
- **通道效應（Channeling）偵測**：即時預測過細研磨或布粉不均導致的噴濺與穿孔風險。
- **即時數值與金杯圖**：
  - 總溶解固體量（TDS %）
  - 萃取率（Extraction Yield, EY %）
  - 流速（Flow Rate, g/s）
  - 即時感官風味雷達圖（酸質、甜感、醇厚度、苦味、餘韻）
- **經典食譜預設**：一鍵套用標準平衡黃金萃取、研磨過細/通道效應、研磨過粗/萃取不足、高溫苦澀等預設進行對比學習。

### 🫖 2. 手沖咖啡實驗室 (Pour-Over Coffee Lab)
- **多種濾杯系統**：支援 Hario V60、Kalita Wave 蛋糕濾杯、Origami 摺紙濾杯、Kono 等不同流速特性的濾杯模型。
- **進階沖煮手法與名家預設**：
  - 粕谷哲 4:6 法五段變溫沖煮
  - 三段式中心注水
  - 低溫濃厚浸潤法
- **莊園精品豆風味庫**：內建祕魯桑托斯藝伎黑蜜、衣索比亞西達摩日曬、肯亞日曬藝伎、薩爾瓦多聖依蓮娜蜜處理等多款精品咖啡豆特性模擬。
- **水溫衰減與攪拌擾動模擬**：模擬注水過程中的熱流流失與粉層擾動程度對芳香物質萃取的動態影響。

### 📱 3. 現代化沉浸體驗
- **多端適配（RWD）**：針對行動裝置最佳化的觸控步進器（Touch Steppers）與視圖快速切換塢（Live Telemetry Dock）。
- **環境音效**：內建萃取滴濾音效與水流聲，增強調校沉浸感。
- **零外部伺服器依賴**：純靜態 Web 應用（HTML5 + TailwindCSS + Web Audio API + Canvas），無須安裝任何依賴，雙擊即可執行。

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
├── index.html            # 主應用入口（支援 GitHub Pages）
├── dual_coffee_lab.html  # 完整功能原始檔
├── README.md             # 專案介紹文件
└── .gitignore            # Git 忽略配置
```

---

## 📄 授權協議

本專案基於 [MIT License](LICENSE) 開源。
