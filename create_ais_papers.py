#!/usr/bin/env python3
"""批次建立 AIS 30篇經典論文的 markdown 檔案"""

import os

# 論文資料（編號 4-30）
papers = [
    {
        "num": 4,
        "file": "ais-04-goal-behavior",
        "title": "目標導向行為預測",
        "en_title": "Prediction of goal-directed behavior: Attitudes, intentions, and perceived behavioral control",
        "authors": "Ajzen, I., & Madden, T. J.",
        "year": 1986,
        "journal": "Journal of Experimental Social Psychology",
        "volume": "22(5), 453–474",
        "doi": "10.1016/0022-1031(86)90045-4"
    },
    {
        "num": 5,
        "file": "ais-05-holistic-construal",
        "title": "組織理論的表徵與測試",
        "en_title": "Representing and testing organizational theories: A holistic construal",
        "authors": "Bagozzi, R. P., & Phillips, L. W.",
        "year": 1982,
        "journal": "Administrative Science Quarterly",
        "volume": "27(3), 459–489",
        "doi": "10.2307/2392322"
    },
    {
        "num": 6,
        "file": "ais-06-user-satisfaction",
        "title": "電腦使用者滿意度測量工具",
        "en_title": "Development of a tool for measuring and analyzing computer user satisfaction",
        "authors": "Bailey, J. E., & Pearson, S. W.",
        "year": 1983,
        "journal": "Management Science",
        "volume": "29(5), 530–545",
        "doi": "10.1287/mnsc.29.5.530"
    },
    {
        "num": 7,
        "file": "ais-07-self-efficacy",
        "title": "自我效能：行為改變的統一理論",
        "en_title": "Self-efficacy: Toward a unifying theory of behavioral change",
        "authors": "Bandura, A.",
        "year": 1977,
        "journal": "Psychological Review",
        "volume": "84(2), 191–215",
        "doi": "10.1037/0033-295X.84.2.191"
    },
    {
        "num": 8,
        "file": "ais-08-self-managing-teams",
        "title": "自我管理團隊中的協同控制",
        "en_title": "Tightening the iron cage: Concertive control in self-managing teams",
        "authors": "Barker, J. R.",
        "year": 1993,
        "journal": "Administrative Science Quarterly",
        "volume": "38(3), 408–437",
        "doi": "10.2307/2393374"
    },
    {
        "num": 9,
        "file": "ais-09-user-involvement",
        "title": "使用者參與對系統使用的實證研究",
        "en_title": "An empirical study of the impact of user involvement on system usage and user satisfaction",
        "authors": "Baroudi, J. J., Olson, M. H., & Ives, B.",
        "year": 1986,
        "journal": "Communications of the ACM",
        "volume": "29(3), 232–238",
        "doi": "10.1145/5666.5669"
    },
    {
        "num": 10,
        "file": "ais-10-is-continuance",
        "title": "資訊系統持續使用模型",
        "en_title": "Understanding information systems continuance: An expectation-confirmation model",
        "authors": "Bhattacherjee, A.",
        "year": 2001,
        "journal": "MIS Quarterly",
        "volume": "25(3), 351–370",
        "doi": "10.2307/3250921"
    },
    {
        "num": 11,
        "file": "ais-11-convergent-discriminant",
        "title": "多特質多方法矩陣的收斂與區辨效度",
        "en_title": "Convergent and discriminant validation by the multitrait-multimethod matrix",
        "authors": "Campbell, D. T., & Fiske, D. W.",
        "year": 1959,
        "journal": "Psychological Bulletin",
        "volume": "56(2), 81–105",
        "doi": "10.1037/h0046016"
    },
    {
        "num": 12,
        "file": "ais-12-is-success",
        "title": "資訊系統成功模型",
        "en_title": "Information systems success: The quest for the dependent variable",
        "authors": "DeLone, W. H., & McLean, E. R.",
        "year": 1992,
        "journal": "Information Systems Research",
        "volume": "3(1), 60–95",
        "doi": "10.1287/isre.3.1.60"
    },
    {
        "num": 13,
        "file": "ais-13-is-success-update",
        "title": "資訊系統成功模型十年更新",
        "en_title": "The DeLone and McLean model of information systems success: A ten-year update",
        "authors": "DeLone, W. H., & McLean, E. R.",
        "year": 2003,
        "journal": "Journal of Management Information Systems",
        "volume": "19(4), 9–30",
        "doi": "10.1080/07421222.2003.11045748"
    },
    {
        "num": 14,
        "file": "ais-14-privacy-calculus",
        "title": "電子商務交易的擴展隱私計算模型",
        "en_title": "An extended privacy calculus model for e-commerce transactions",
        "authors": "Dinev, T., & Hart, P.",
        "year": 2006,
        "journal": "Information Systems Research",
        "volume": "17(1), 61–80",
        "doi": "10.1287/isre.1060.0080"
    },
    {
        "num": 15,
        "file": "ais-15-eucs-validation",
        "title": "終端使用者滿意度量表驗證",
        "en_title": "A confirmatory factor analysis of the end-user computing satisfaction instrument",
        "authors": "Doll, W. J., Xia, W., & Torkzadeh, G.",
        "year": 1994,
        "journal": "MIS Quarterly",
        "volume": "18(4), 453–461",
        "doi": "10.2307/249524"
    },
    {
        "num": 16,
        "file": "ais-16-trust-tam-online",
        "title": "線上購物的信任與TAM整合模型",
        "en_title": "Trust and TAM in online shopping: An integrated model",
        "authors": "Gefen, D., Karahanna, E., & Straub, D. W.",
        "year": 2003,
        "journal": "MIS Quarterly",
        "volume": "27(1), 51–90",
        "doi": "10.2307/30036519"
    },
    {
        "num": 17,
        "file": "ais-17-user-participation",
        "title": "使用者參與在資訊系統使用中的角色",
        "en_title": "Explaining the role of user participation in information system use",
        "authors": "Hartwick, J., & Barki, H.",
        "year": 1994,
        "journal": "Management Science",
        "volume": "40(4), 440–465",
        "doi": "10.1287/mnsc.40.4.440"
    },
    {
        "num": 18,
        "file": "ais-18-consumer-trust-internet",
        "title": "網路商店的消費者信任",
        "en_title": "Consumer trust in an Internet store",
        "authors": "Jarvenpaa, S. L., Tractinsky, N., & Vitale, M.",
        "year": 2000,
        "journal": "Information Technology and Management",
        "volume": "1(1–2), 45–71",
        "doi": "10.1023/A:1019104520776"
    },
    {
        "num": 19,
        "file": "ais-19-habit-limits",
        "title": "習慣如何限制意圖的預測力",
        "en_title": "How habit limits the predictive power of intentions: The case of IS continuance",
        "authors": "Limayem, M., Hirt, S. G., & Cheung, C. M. K.",
        "year": 2007,
        "journal": "MIS Quarterly",
        "volume": "31(4), 705–737",
        "doi": "10.2307/25148817"
    },
    {
        "num": 20,
        "file": "ais-20-organizational-trust",
        "title": "組織信任的整合模型",
        "en_title": "An integrative model of organizational trust",
        "authors": "Mayer, R. C., Davis, J. H., & Schoorman, F. D.",
        "year": 1995,
        "journal": "The Academy of Management Review",
        "volume": "20(3), 709–734",
        "doi": "10.2307/258792"
    },
    {
        "num": 21,
        "file": "ais-21-social-capital",
        "title": "社會資本、智慧資本與組織優勢",
        "en_title": "Social capital, intellectual capital, and the organizational advantage",
        "authors": "Nahapiet, J., & Ghoshal, S.",
        "year": 1998,
        "journal": "The Academy of Management Review",
        "volume": "23(2), 242–266",
        "doi": "10.2307/259373"
    },
    {
        "num": 22,
        "file": "ais-22-satisfaction-decisions",
        "title": "滿意度決策的認知模型",
        "en_title": "A cognitive model of the antecedents and consequences of satisfaction decisions",
        "authors": "Oliver, R. L.",
        "year": 1980,
        "journal": "Journal of Marketing Research",
        "volume": "17(4), 460–469",
        "doi": "10.2307/3150499"
    },
    {
        "num": 23,
        "file": "ais-23-institution-trust",
        "title": "以制度為基礎建立有效的線上市場",
        "en_title": "Building effective online marketplaces with institution-based trust",
        "authors": "Pavlou, P. A., & Gefen, D.",
        "year": 2004,
        "journal": "Information Systems Research",
        "volume": "15(1), 37–59",
        "doi": "10.1287/isre.1040.0015"
    },
    {
        "num": 24,
        "file": "ais-24-common-method-bias",
        "title": "共同方法偏誤：文獻回顧與補救建議",
        "en_title": "Common method biases in behavioral research: A critical review of the literature and recommended remedies",
        "authors": "Podsakoff, P. M., MacKenzie, S. B., Lee, J.-Y., & Podsakoff, N. P.",
        "year": 2003,
        "journal": "Journal of Applied Psychology",
        "volume": "88(5), 879–903",
        "doi": "10.1037/0021-9010.88.5.879"
    },
    {
        "num": 25,
        "file": "ais-25-tra-meta-analysis",
        "title": "理性行為理論的後設分析",
        "en_title": "The theory of reasoned action: A meta-analysis of past research with recommendations",
        "authors": "Sheppard, B. H., Hartwick, J., & Warshaw, P. R.",
        "year": 1988,
        "journal": "Journal of Consumer Research",
        "volume": "15(3), 325–343",
        "doi": "10.1086/209170"
    },
    {
        "num": 26,
        "file": "ais-26-validating-instruments",
        "title": "MIS研究中的工具驗證",
        "en_title": "Validating instruments in MIS research",
        "authors": "Straub, D. W.",
        "year": 1989,
        "journal": "MIS Quarterly",
        "volume": "13(2), 147–169",
        "doi": "10.2307/248922"
    },
    {
        "num": 27,
        "file": "ais-27-what-theory-not",
        "title": "什麼不是理論",
        "en_title": "What theory is not",
        "authors": "Sutton, R. I., & Staw, B. M.",
        "year": 1995,
        "journal": "Administrative Science Quarterly",
        "volume": "40(3), 371–384",
        "doi": "10.2307/2393788"
    },
    {
        "num": 28,
        "file": "ais-28-satisfaction-acceptance",
        "title": "使用者滿意度與技術接受的理論整合",
        "en_title": "A theoretical integration of user satisfaction and technology acceptance",
        "authors": "Wixom, B. H., & Todd, P. A.",
        "year": 2005,
        "journal": "Information Systems Research",
        "volume": "16(1), 85–102",
        "doi": "10.1287/isre.1050.0042"
    },
    {
        "num": 29,
        "file": "ais-29-case-study-research",
        "title": "從個案研究建立理論",
        "en_title": "Building theories from case study research",
        "authors": "Eisenhardt, K. M.",
        "year": 1989,
        "journal": "Academy of Management Review",
        "volume": "14(4), 532–550",
        "doi": "10.5465/amr.1989.4308385"
    },
    {
        "num": 30,
        "file": "ais-30-grounded-theory",
        "title": "紮根理論研究：程序、準則與評估標準",
        "en_title": "Grounded theory research: Procedures, canons, and evaluative criteria",
        "authors": "Strauss, A., & Corbin, J.",
        "year": 1990,
        "journal": "Qualitative Sociology",
        "volume": "13(1), 3–21",
        "doi": "10.1007/BF00988593"
    }
]

# 模板
template = """---
sidebar_position: {num}
---

# AIS經典論文 {num}：{title}

**English Title**: {en_title}
**中文標題**: {title}
**作者**: {authors}
**年份**: {year}
**期刊**: {journal}
**卷期**: {volume}
**DOI**: [{doi}](https://doi.org/{doi})

---

## 📌 核心觀點

（本論文的主要貢獻與核心論點）

---

## 💡 理論貢獻

### 主要創新

1. **理論發展**
2. **方法論貢獻**
3. **實證發現**

---

## 📊 研究方法

### 研究設計

- 研究類型：
- 資料來源：
- 分析方法：

---

## 🎯 在資訊系統領域的應用

### 應用領域

1.
2.
3.

---

## ⚠️ 理論限制

1.
2.
3.

---

## 📚 延伸閱讀

### 相關論文

-
-
-

### 引用次數

此論文在 Google Scholar 上有大量引用，是 IS 領域的經典文獻。

---

## 🔗 參考資源

- AIS Electronic Library: [搜尋此論文](https://aisel.aisnet.org/)
- Google Scholar: [查看引用](https://scholar.google.com/)

---

*註：本頁面提供論文概要，詳細內容請參閱原文。*
"""

# 建立檔案
output_dir = "docs/ais-classic-30"

for paper in papers:
    file_path = f"{output_dir}/{paper['file']}.md"
    content = template.format(**paper)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ 建立檔案: {file_path}")

print(f"\n🎉 完成！共建立 {len(papers)} 個檔案")
