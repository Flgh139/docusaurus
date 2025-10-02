---
sidebar_position: 8
---

# 文獻 8：Comparative Diagnostic Performance of a Multimodal Large Language Model Versus a Dedicated Electrocardiogram AI

**English Title**: Comparative Diagnostic Performance of a Multimodal Large Language Model Versus a Dedicated Electrocardiogram AI

**中文標題**: 多模態大型語言模型與專用心電圖 AI 的診斷性能比較
**PMID**: 40961357
**期刊**: JMIR AI
**評分**: 8
**應用領域**: 門診/急診
**DOI**: https://doi.org/10.2196/75910

---

## 📌 第一張：核心觀點卡

### 主要發現
通用AI與專用AI的效能比較

### 文獻摘要（Abstract）
BACKGROUND: Accurate and timely electrocardiogram (ECG) interpretation is critical for diagnosing myocardial infarction (MI) in emergency settings. Recent advances in multimodal large language models (LLMs), such as ChatGPT (OpenAI) and Gemini (Google DeepMind), have shown promise in clinical interpretation for medical imaging. However, whether these models analyze waveform patterns or simply rely on text cues remains unclear, underscoring the need for direct comparisons with dedicated ECG artificial intelligence (AI) tools. OBJECTIVE: This study aimed to evaluate the diagnostic performance of ChatGPT and Gemini, a general-purpose LLM, in detecting MI from ECG images and to compare its performance with that of ECG Buddy (ARPI Inc), a dedicated AI-driven ECG analysis tool. METHODS: This retrospective study evaluated and compared AI models for classifying MI using a publicly available 12-lead ECG dataset from Pakistan, categorizing cases into MI-positive (239 images) and MI-negative (689 images). ChatGPT (GPT-4o, version November 20, 2024) and Gemini (Gemini 2.5 pro) were queried with 5 MI confidence options, whereas ECG Buddy for Microsoft Windows analyzed the images based on ST-elevation MI, acute coronary syndrome, and myocardial injury biomarkers. RESULTS: Among 928 ECG recordings (239/928, 25.8% MI-positive), ChatGPT achieved an accuracy of 65.95% (95% CI 62.80-69.00), area under the curve (AUC) of 57.34% (95% CI 53.44-61.24), sensitivity of 36.40% (95% CI 30.30-42.85), and specificity of 76.2% (95% CI 72.84-79.33). With Gemini 2.5 Pro, accuracy dropped to 29.63% (95% CI 26.71-32.69), AUC to 51.63% (95% CI 50.22-53.04), and sensitivity rose to 97.07% (95% CI 94.06-98.81), but specificity fell sharply to 6.24% (95% CI 4.55-8.31). However, ECG Buddy reached an accuracy of 96.98% (95% CI 95.67-97.99), AUC of 98.8% (95% CI 98.3-99.43), sensitivity of 96.65% (95% CI 93.51-98.54), and specificity of 97.10% (95% CI 95.55-98.22). DeLong test confirmed that ECG Buddy significantly outperformed ChatGPT (all P&lt;.001). In a qualitative error analysis of LLMs' diagnostic explanations, GPT-4o produced fully accurate explanations in only 5% of cases (2/40), was partially accurate in 38% (15/40), and completely inaccurate in 58% (23/40). By contrast, Gemini 2.5 Pro yielded fully accurate explanations in 32% of cases (12/37), was partially accurate in 14% (5/37), and completely inaccurate in 54% (20/37). CONCLUSIONS: LLMs, such as ChatGPT and Gemini, underperform relative to specialized tools such as ECG Buddy in ECG image-based MI diagnosis. Further training may improve LLMs; however, domain-specific AI remains essential for clinical accuracy. The high performance of ECG Buddy underscores the importance of specialized models for achieving reliable and robust diagnostic outcomes.

### 中文摘要
**背景**：在急診環境中，準確且及時的心電圖（ECG）判讀對於診斷心肌梗塞（MI）至關重要。多模態大型語言模型（LLMs）如 ChatGPT（OpenAI）和 Gemini（Google DeepMind）在醫學影像的臨床判讀方面已顯示出潛力。然而，這些模型是分析波形模式還是僅依賴文字提示仍不明確，突顯出與專用心電圖人工智能（AI）工具進行直接比較的必要性。**目的**：本研究旨在評估 ChatGPT 和 Gemini 這類通用 LLM 從心電圖影像檢測心肌梗塞的診斷性能，並將其與專用 AI 驅動的心電圖分析工具 ECG Buddy（ARPI Inc）進行比較。**方法**：本回溯性研究使用來自巴基斯坦的公開 12 導聯心電圖資料集，評估並比較 AI 模型對心肌梗塞的分類能力，將病例分為心肌梗塞陽性（239 張影像）和陰性（689 張影像）。ChatGPT（GPT-4o，2024 年 11 月 20 日版本）和 Gemini（Gemini 2.5 pro）提供 5 個心肌梗塞信心選項進行查詢，而 ECG Buddy for Microsoft Windows 則基於 ST 段抬高型心肌梗塞、急性冠狀動脈症候群和心肌損傷生物標記進行分析。**結果**：在 928 份心電圖記錄中（239/928，25.8% 為心肌梗塞陽性），ChatGPT 達到 65.95% 的準確率（95% CI 62.80-69.00）、57.34% 的曲線下面積（AUC）（95% CI 53.44-61.24）、36.40% 的敏感度（95% CI 30.30-42.85）和 76.2% 的特異度（95% CI 72.84-79.33）。Gemini 2.5 Pro 的準確率降至 29.63%（95% CI 26.71-32.69），AUC 降至 51.63%（95% CI 50.22-53.04），敏感度上升至 97.07%（95% CI 94.06-98.81），但特異度大幅下降至 6.24%（95% CI 4.55-8.31）。然而，ECG Buddy 達到 96.98% 的準確率（95% CI 95.67-97.99）、98.8% 的 AUC（95% CI 98.3-99.43）、96.65% 的敏感度（95% CI 93.51-98.54）和 97.10% 的特異度（95% CI 95.55-98.22）。DeLong 檢定證實 ECG Buddy 顯著優於 ChatGPT（所有 P&lt;.001）。在 LLMs 診斷解釋的質性錯誤分析中，GPT-4o 僅在 5% 的病例（2/40）中產生完全準確的解釋，38%（15/40）部分準確，58%（23/40）完全不準確。相比之下，Gemini 2.5 Pro 在 32% 的病例（12/37）中產生完全準確的解釋，14%（5/37）部分準確，54%（20/37）完全不準確。**結論**：在基於心電圖影像的心肌梗塞診斷中，ChatGPT 和 Gemini 等 LLMs 的表現不如 ECG Buddy 等專用工具。進一步訓練可能改善 LLMs；然而，領域特定的 AI 對於臨床準確性仍然至關重要。ECG Buddy 的高性能強調了專用模型對於實現可靠且穩健診斷結果的重要性。

### 關鍵數據
- **研究類型**: 未分類
- **國家/地區**: 待查
- **發表年份**: 待查
- **ROI 數值**: 無數值

### 核心創新點
本研究的主要創新在於：通用AI與專用AI的效能比較

---

## ✍️ 第二張：Paraphrase 卡

### 研究目的與方法
本研究聚焦於門診/急診領域，旨在探討 AI 技術在醫療場景中的應用。

### 主要貢獻
研究提出了通用AI與專用AI的效能比較，為臨床實踐提供了新的解決方案。

### 技術特點
- 應用場景：門診/急診
- 創新程度：評分 8/10
- 期刊影響：發表於 JMIR AI

---

## ❓ 第三張：問答卡

### Q1: 這項研究解決了什麼問題？
A: 本研究針對門診/急診領域的挑戰，提出了基於 AI 的解決方案。

### Q2: 採用了什麼技術方法？
A: 通用AI與專用AI的效能比較

### Q3: 研究的主要成果是什麼？
A: 研究獲得了 8 分的專家評分，證明了其在門診/急診領域的應用價值。

### Q4: 有哪些實際應用場景？
A: 主要應用於門診/急診，可用於改善醫療服務品質和效率。

---

## 🤔 第四張：例外卡

### 潛在限制
1. **研究範圍**: 研究評分為 8/10，可能存在改進空間
2. **地區差異**: 研究來自待查，其他地區適用性需驗證
3. **ROI 數據**: 無數值，經濟效益評估可能不完整

### 需要進一步探討的問題
1. 該技術在不同規模醫院的適用性如何？
2. 長期使用的效果和穩定性是否經過驗證？
3. 與現有系統整合時可能面臨哪些挑戰？

### 批判性思考
- **技術成熟度**: 需要評估從研究到實際部署的距離
- **成本效益**: 無數值，需要更詳細的經濟分析
- **倫理考量**: AI 在門診/急診應用時的倫理和隱私問題
- **可推廣性**: 研究結果在其他醫療場景的適用性

---

## 📚 參考資訊
- **PMID**: [40961357](https://pubmed.ncbi.nlm.nih.gov/40961357/)
- **DOI**: https://doi.org/10.2196/75910
- **期刊**: JMIR AI
