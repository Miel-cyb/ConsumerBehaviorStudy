# 🛒 Consumer Behavior and Online Shopping Preference Analysis

This project explores **consumer decision behavior** — specifically how **external factors** such as discounts, trends, and availability affect people's shopping choices, and how these choices relate to **Human–Computer Interaction (HCI)** and user trust in e-commerce systems. Main goal is to ensure effective decision making particularly for FMCG distribution companies to understand features that may affect purchasing behavior and how to manage stock movement based on both historic sales data and human factors.
---

# Problem Statement
In modern organizations, decisions increasingly rely on insights derived from data visualization and predictive modeling. However, when analysts fail to select the appropriate features or define the correct target variables, visualizations can become misleading, and models may produce unreliable outcomes. This misalignment between chosen variables and actual decision objectives can result in flawed conclusions, ultimately affecting strategic and operational decision-making. This is an extended study of understanding overstocking and understocking, the initial project evaluated historical sales but the question is: What if consumer behavior does not follow past trends? Prediction can falter when expected results deviate from outcome.

## 📊 Project Overview

The dataset was collected through an **online survey** to examine:
- What influences consumer purchasing decisions
- How consumers respond to price increases or discounts
- Which factors predict whether someone prefers **online** or **in-person** shopping
- How user experience (UX/HCI) factors might explain online adoption gaps

---

## 🧠 Objective

> To model consumer decision-making patterns and analyze the human–computer interaction elements influencing **online shopping adoption**.

---

## 🧩 Dataset

| Source | Description |
|--------|--------------|
| Self-collected survey | Responses from 34 participants on shopping preferences, behavior influences, and attitudes toward online shopping. |
| Columns | 51 (including demographics, behavior patterns, and perception questions) |
| Target Variable | `Which shopping mode do you prefer most often?_Online(Ecommerce)` |

---

## ⚙️ Workflow

### 1. **Data Cleaning and Encoding**
- Removed empty or inconsistent responses
- Encoded categorical variables into numeric format
- Saved to `outputs/cleaned_data_encoded.csv`

### 2. **Exploratory Data Analysis (`analysis.py`)**
- Visualized the distribution of shopping preferences
- Generated a correlation heatmap
- Found that **in-person shopping dominated (82%)** compared to online (18%)

### 3. **Modeling (`modeling.py`)**
- Trained a **Logistic Regression** model to predict online shopping preference  
- Accuracy: **85.7%**
- Top predictive features included:
  - Perceived quality of online experience
  - Past brand loyalty changes
  - Month of highest spending
  - Occupation (students showed higher online adoption)
  - Main influences on purchasing behavior

### 4. **Interpretation and HCI Insights**
- Analyzed UX-related factors influencing shopping behavior
- Discussed usability, trust, and digital experience gaps in e-commerce

---

## 📈 Key Results

| Metric | Score |
|--------|-------|
| Accuracy | **0.86** |
| Precision (Offline) | **1.00** |
| Precision (Online) | **0.50** |
| F1-Score (Average) | **0.87** |

### 🔍 Top 10 Features Influencing Online Shopping
1. Rating of online shopping experience  
2. Loyalty shifts unrelated to quality  
3. Month of peak spending  
4. Occupation (students)  
5. Social or promotional influence factors  

---

## 💡 HCI Interpretation

Despite widespread digital access, most consumers **still prefer in-person shopping**.  
The analysis suggests:
- **Trust and usability** concerns limit online adoption.
- **Cognitive load** (too many steps, unclear feedback) deters users.
- **Lack of sensory experience** and social interaction affects satisfaction.
- **Design Implication:** Online shopping interfaces must emphasize **clarity, transparency, and user control**.

---

## 📦 Outputs
- `outputs/feature_importance.png` — Top predictive features  
- `outputs/shopping_mode_preference.png` — Shopping mode distribution  
- `outputs/correlation_heatmap.png` — Variable relationships  
- `outputs/analysis_summary.txt` — Full analytical and HCI report  

---
## Future Work
More data can be added to get in depth overview of patterns for better visualization. Furthermore, behavioural sciences should continue to be explored to understand ways decision making can be adaptive to different user groups.

## 🧰 Tech Stack
- **Python** (pandas, numpy, sklearn, matplotlib, seaborn)
- **Scikit-learn** for modeling
- **Matplotlib/Seaborn** for visualization

---


