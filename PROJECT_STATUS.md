# AIS 30 經典論文更新專案狀態

## 專案目標
採用 NotebookLM 四張筆記卡方法，系統化整理 AIS 30 篇經典論文

## 更新格式
每篇論文包含：
- 📌 第一張：核心觀點卡（關鍵數據、理論架構、核心論點）
- ✍️ 第二張：Paraphrase 卡（白話解釋、IS 研究影響）
- ❓ 第三張：問答卡（3 個核心問題深入探討）
- 🤔 第四張：例外卡（3 個疑點與批判性思考）
- 📊 研究方法
- 🔍 理論影響
- ⚠️ 理論限制
- 🎯 實務啟示
- 📚 延伸閱讀

## 完成進度

### ✅ Batch 1 (已完成 - 2025-01-XX)
1. **AIS-01: 計劃行為理論 (TPB)** - Ajzen (1991)
2. **AIS-02: 技術接受模型 (TAM)** - Davis et al. (1989)
3. **AIS-03: 整合科技接受模型 (UTAUT)** - Venkatesh et al. (2003)
4. **AIS-04: 目標導向行為模型** - Perugini & Bagozzi (2001)

### ✅ Batch 2 (已完成 - 2025-01-04)
5. **AIS-05: 整體構念測試方法** - Bagozzi & Yi (1988)
   - 主題：SEM 方法論、反映性 vs 形成性指標
   - 字數：~8,000 字
   
6. **AIS-06: 使用者滿意度測量工具** - Bailey & Pearson (1983)
   - 主題：39 因素 UIS 量表、IS 評估
   - 字數：~13,000 字
   
7. **AIS-07: 自我效能理論** - Bandura (1977)
   - 主題：行為改變理論、電腦自我效能
   - 字數：~14,000 字
   
8. **AIS-08: 協同控制理論** - Barker (1993)
   - 主題：自我管理團隊、組織控制
   - 字數：~15,000 字

### 🔄 Batch 3 (進行中 - 4/5 完成)
9. **AIS-09: 使用者參與 vs 參加** - Barroudi et al. (1986) ✅
   - 主題：User Involvement vs Participation 概念區辨
   - 字數：~17,000 字
   - 完成日期：2025-01-04

10. **AIS-10: IS 持續使用模型 (ECM)** - Bhattacherjee (2001) ✅
    - 主題：期望確認理論、持續使用意圖
    - 字數：~20,000 字
    - 完成日期：2025-01-04

11. **AIS-11: MTMM 效度驗證** - Campbell & Fiske (1959) ✅
    - 主題：多特質多方法矩陣、收斂與區辨效度
    - 字數：~19,000 字
    - 完成日期：2025-01-04

12. **AIS-12: IS 成功模型** - DeLone & McLean (1992) ✅
    - 主題：六維度 IS 成功模型
    - 字數：~19,000 字
    - 完成日期：2025-01-04

13. **AIS-13: IS 成功模型十年更新** - DeLone & McLean (2003) ⏳
    - 主題：更新版 D&M 模型、服務品質維度
    - 狀態：待完成

### ⏳ Batch 4 (待完成)
14-18. 待規劃

### ⏳ Batch 5 (待完成)
19-23. 待規劃

### ⏳ Batch 6 (待完成)
24-30. 待規劃

## 總進度統計
- **已完成**: 12/30 篇 (40%)
- **進行中**: 1/30 篇 (AIS-13)
- **待完成**: 17/30 篇 (57%)

## 技術細節

### Repository
- GitHub: https://github.com/Flgh139/docusaurus
- 網站: https://Flgh139.github.io/docusaurus/

### 部署方式
- 使用 GitHub Actions 自動部署
- 每次推送到 main 分支會自動觸發部署

### 已知問題與解決方案
1. **Broken Links 問題**: 
   - 問題：連結到尚未完成的論文會導致 build 失敗
   - 解決：移除指向未完成論文的連結，改為純文字引用

2. **Token 使用管理**:
   - 每個 session 有 200K token 限制
   - 建議每 4-6 篇論文推送一次（約使用 60-80K tokens）

### Session 1 工作記錄 (2025-01-04 早)
- 完成 AIS-05 到 AIS-08 共 4 篇論文 (Batch 2)
- Token 使用: ~64K/200K (32%)
- 修復 1 個 broken link 問題
- 成功部署到 GitHub Pages

### Session 2 工作記錄 (2025-01-04 晚)
- 完成 AIS-09 到 AIS-12 共 4 篇論文 (Batch 3 部分)
- 額外完成：AIS-11 (MTMM) 取代原本的 AIS-11 檔案
- Token 使用: ~62K/200K (31%)
- 發現檔案命名差異：
  - ais-11-convergent-discriminant.md → Campbell & Fiske (1959) MTMM
  - ais-12-is-success.md → DeLone & McLean (1992)
  - ais-13-is-success-update.md → DeLone & McLean (2003) 待完成
- 成功推送 4 次到 GitHub

### 輸出長度限制問題
- 在完成 AIS-13 時遇到 Claude 32000 token 輸出限制
- 解決方案：下次 session 分段完成 AIS-13

## 下次繼續工作重點
1. ⚠️ **優先完成 AIS-13** (DeLone & McLean 2003 更新版)
2. 完成 Batch 3 後推送並更新專案狀態
3. 開始規劃 Batch 4 (AIS-14 到 AIS-18)
4. 注意輸出長度：每篇論文控制在 15,000-20,000 字

## 聯絡資訊
- 專案負責人: YOUTA
- 最後更新: 2025-01-04 (Session 2)
