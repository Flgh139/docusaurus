---
sidebar_position: 41
---

# 文獻 41：Enhancing Oncology-Specific Question Answering With Large Language Models Through Fine-Tuned Embeddings With Synthetic Data

**English Title**: Enhancing Oncology-Specific Question Answering With Large Language Models Through Fine-Tuned Embeddings With Synthetic Data

**中文標題**: 通過合成數據的微調嵌入增強大型語言模型的腫瘤學特定問答
**PMID**: 40911811
**期刊**: JCO clinical cancer informatics
**評分**: 8
**應用領域**: 門診/腫瘤科
**DOI**: https://doi.org/10.1200/CCI-25-00011

---

## 📌 第一張：核心觀點卡

### 主要發現
腫瘤學專門檢索編碼器

### 文獻摘要（Abstract）
PURPOSE: The recent advancements of retrieval-augmented generation (RAG) and large language models (LLMs) have revolutionized the extraction of real-world evidence from unstructured electronic health records (EHRs) in oncology. This study aims to enhance RAG's effectiveness by implementing a retriever encoder specifically designed for oncology EHRs, with the goal of improving the precision and relevance of retrieved clinical notes for oncology-related queries. METHODS: Our model was pretrained with more than six million oncology notes from 209,135 patients at City of Hope. The model was subsequently fine-tuned into a sentence transformer model using 12,371 query-passage training pairs. Specifically, the passages were obtained from actual patient notes, whereas the query was synthesized by an LLM. We evaluated the retrieval performance of our model by comparing it with six widely used embedding models on 50 oncology questions across 10 categories based on Normalized Discounted Cumulative Gain (NDCG), Precision, and Recall. RESULTS: In our test data set comprising 53 patients, our model exceeded the performance of the runner-up model by 9% for NDCG (evaluated at the top 10 results), 7% for Precision (top 10), and 6% for Recall (top 10). Our model showed exceptional retrieval performance across all metrics for oncology-specific categories, including biomarkers assessed, current diagnosis, disease status, laboratory results, tumor characteristics, and tumor staging. CONCLUSION: Our findings highlight the effectiveness of pretrained contextual embeddings and sentence transformers in retrieving pertinent notes from oncology EHRs. The innovative use of LLM-synthesized query-passage pairs for data augmentation was proven to be effective. This fine-tuning approach holds significant promise in specialized fields like health care, where acquiring annotated data is challenging.

### 中文摘要
**目的**：檢索增強生成（RAG）和大型語言模型（LLMs）的最新進展徹底改變了從腫瘤學非結構化電子健康記錄（EHRs）中提取真實世界證據。本研究旨在通過實施專門為腫瘤學 EHRs 設計的檢索編碼器來增強 RAG 的有效性，目標是提高腫瘤學相關查詢檢索臨床記錄的精確度和相關性。**方法**：我們的模型使用希望之城 209,135 名患者的超過 600 萬份腫瘤學記錄進行預訓練。隨後使用 12,371 個查詢段落訓練對將模型微調為句子轉換器模型。具體而言，段落來自實際患者記錄，而查詢由 LLM 合成。我們通過將模型與六個廣泛使用的嵌入模型在 10 個類別的 50 個腫瘤學問題上進行比較，基於歸一化折扣累積增益（NDCG）、精確度和召回率評估檢索性能。**結果**：在包含 53 名患者的測試數據集中，我們的模型在 NDCG（在前 10 個結果中評估）上超過第二名模型 9%，精確度（前 10）7%，召回率（前 10）6%。我們的模型在腫瘤學特定類別的所有指標上表現出卓越的檢索性能，包括評估的生物標記、當前診斷、疾病狀態、實驗室結果、腫瘤特徵和腫瘤分期。**結論**：我們的研究結果強調了預訓練上下文嵌入和句子轉換器在從腫瘤學 EHRs 檢索相關記錄方面的有效性。創新使用 LLM 合成的查詢段落對進行數據增強被證明是有效的。這種微調方法在醫療保健等專業領域具有重大前景，因為在這些領域獲取標註數據具有挑戰性。

### 關鍵數據
- **研究類型**: 未分類
- **國家/地區**: 待查
- **發表年份**: 待查
- **ROI 數值**: 無數值

### 核心創新點
本研究的主要創新在於：腫瘤學專門檢索編碼器

---

## ✍️ 第二張：Paraphrase 卡

### 研究目的與方法
本研究聚焦於門診/腫瘤科領域，旨在探討 AI 技術在醫療場景中的應用。

### 主要貢獻
研究提出了腫瘤學專門檢索編碼器，為臨床實踐提供了新的解決方案。

### 技術特點
- 應用場景：門診/腫瘤科
- 創新程度：評分 8/10
- 期刊影響：發表於 JCO clinical cancer informatics

---

## ❓ 第三張：問答卡

### Q1: 這項研究解決了什麼問題？
A: 本研究針對門診/腫瘤科領域的挑戰，提出了基於 AI 的解決方案。

### Q2: 採用了什麼技術方法？
A: 腫瘤學專門檢索編碼器

### Q3: 研究的主要成果是什麼？
A: 研究獲得了 8 分的專家評分，證明了其在門診/腫瘤科領域的應用價值。

### Q4: 有哪些實際應用場景？
A: 主要應用於門診/腫瘤科，可用於改善醫療服務品質和效率。

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
- **倫理考量**: AI 在門診/腫瘤科應用時的倫理和隱私問題
- **可推廣性**: 研究結果在其他醫療場景的適用性

---

## 📚 參考資訊
- **PMID**: [40911811](https://pubmed.ncbi.nlm.nih.gov/40911811/)
- **DOI**: https://doi.org/10.1200/CCI-25-00011
- **期刊**: JCO clinical cancer informatics
