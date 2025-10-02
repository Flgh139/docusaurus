---
sidebar_position: 59
---

# 文獻 59：Rapidly Benchmarking Large Language Models for Diagnosing Comorbid Patients

**English Title**: Rapidly Benchmarking Large Language Models for Diagnosing Comorbid Patients

**中文標題**: 快速基準測試大型語言模型診斷共病患者
**PMID**: 40880236
**期刊**: JMIRx med
**評分**: 8.5
**應用領域**: 多科醫療
**DOI**: https://doi.org/10.2196/67661

---

## 📌 第一張：核心觀點卡

### 主要發現
LLM診斷能力快速評估

### 文獻摘要（Abstract）
BACKGROUND: On average, 1 in 10 patients die because of a diagnostic error, and medical errors represent the third largest cause of death in the United States. While large language models (LLMs) have been proposed to aid doctors in diagnoses, no research results have been published comparing the diagnostic abilities of many popular LLMs on a large, openly accessible real-patient cohort. OBJECTIVE: In this study, we set out to compare the diagnostic ability of 18 LLMs from Google, OpenAI, Meta, Mistral, Cohere, and Anthropic, using 3 prompts, 2 temperature settings, and 1000 randomly selected Medical Information Mart for Intensive Care-IV (MIMIC-IV) hospital admissions. We also explore improving the diagnostic hit rate of GPT-4o 05-13 with retrieval-augmented generation (RAG) by utilizing reference ranges provided by the American Board of Internal Medicine. METHODS: We evaluated the diagnostic ability of 21 LLMs, using an LLM-as-a-judge approach (an automated, LLM-based evaluation) on MIMIC-IV patient records, which contain final diagnostic codes. For each case, a separate assessor LLM ("judge") compared the predictor LLM's diagnostic output to the true diagnoses from the patient record. The assessor determined whether each true diagnosis was inferable from the available data and, if so, whether it was correctly predicted ("hit") or not ("miss"). Diagnoses not inferable from the patient record were excluded from the hit rate analysis. The reported hit rate was defined as the number of hits divided by the total number of hits and misses. The statistical significance of the differences in model performance was assessed using a pooled z-test for proportions. RESULTS: Gemini 2.5 was the top performer with a hit rate of 97.4% (95% CI 97.0%-97.8%) as assessed by GPT-4.1, significantly outperforming GPT-4.1, Claude-4 Opus, and Claude Sonnet. However, GPT-4.1 ranked the highest in a separate set of experiments evaluated by GPT-4 Turbo, which tended to be less conservative than GPT-4.1 in its assessments. Significant variation in diagnostic hit rates was observed across different prompts, while changes in temperature generally had little effect. Finally, RAG significantly improved the hit rate of GPT-4o 05-13 by an average of 0.8% (P&lt;.006). CONCLUSIONS: While the results are promising, more diverse datasets and hospital pilots, as well as close collaborations with physicians, are needed to obtain a better understanding of the diagnostic abilities of these models.

### 關鍵數據
- **研究類型**: 未分類
- **國家/地區**: 待查
- **發表年份**: 待查
- **ROI 數值**: 無數值

### 核心創新點
本研究的主要創新在於：LLM診斷能力快速評估

---

## ✍️ 第二張：Paraphrase 卡

### 研究目的與方法
本研究聚焦於多科醫療領域，旨在探討 AI 技術在醫療場景中的應用。

### 主要貢獻
研究提出了LLM診斷能力快速評估，為臨床實踐提供了新的解決方案。

### 技術特點
- 應用場景：多科醫療
- 創新程度：評分 8.5/10
- 期刊影響：發表於 JMIRx med

---

## ❓ 第三張：問答卡

### Q1: 這項研究解決了什麼問題？
A: 本研究針對多科醫療領域的挑戰，提出了基於 AI 的解決方案。

### Q2: 採用了什麼技術方法？
A: LLM診斷能力快速評估

### Q3: 研究的主要成果是什麼？
A: 研究獲得了 8.5 分的專家評分，證明了其在多科醫療領域的應用價值。

### Q4: 有哪些實際應用場景？
A: 主要應用於多科醫療，可用於改善醫療服務品質和效率。

---

## 🤔 第四張：例外卡

### 潛在限制
1. **研究範圍**: 研究評分為 8.5/10，可能存在改進空間
2. **地區差異**: 研究來自待查，其他地區適用性需驗證
3. **ROI 數據**: 無數值，經濟效益評估可能不完整

### 需要進一步探討的問題
1. 該技術在不同規模醫院的適用性如何？
2. 長期使用的效果和穩定性是否經過驗證？
3. 與現有系統整合時可能面臨哪些挑戰？

### 批判性思考
- **技術成熟度**: 需要評估從研究到實際部署的距離
- **成本效益**: 無數值，需要更詳細的經濟分析
- **倫理考量**: AI 在多科醫療應用時的倫理和隱私問題
- **可推廣性**: 研究結果在其他醫療場景的適用性

---

## 📚 參考資訊
- **PMID**: [40880236](https://pubmed.ncbi.nlm.nih.gov/40880236/)
- **DOI**: https://doi.org/10.2196/67661
- **期刊**: JMIRx med
