# CMPE 255 — Assignment 1: Do Data Science with ChatGPT

> Semester: Fall 2025   
> Date: 2025-09-13

## 🎯 Objective
Use **ChatGPT as a copilot** to complete an end-to-end data science workflow on a dataset from **Kaggle**.

## ✅ Dataset Chosen (Newbie-friendly)
- **Dataset**: *Titanic — Machine Learning from Disaster* (Kaggle)  
- **Target (目標欄位)**: `Survived`（0=未存活, 1=存活）  
- **Task**: Binary Classification  
- **Suggested features**: Drop identifiers like `PassengerId`, `Name`, `Ticket`, `Cabin` for the baseline.

## 📁 Repo Layout
```
assignment-1/
  ├─ README.md
  ├─ prompts.md
  ├─ transcript.md
  ├─ requirements.txt
  ├─ .gitignore
  ├─ data/
  ├─ notebooks/
  │   ├─ assignment1.ipynb             ← generic
  │   └─ assignment1_titanic.ipynb     ← prefilled with target & steps
  ├─ src/
  │   └─ utils.py
  ├─ artifacts/
  └─ results/
```

## 🛠️ Steps (High-level)
1. Data Understanding → 2. Data Preparation → 3. Modeling → 4. Evaluation → 5. Iteration → 6. Report & Artifacts

## ▶️ How to run (Colab)
- Open `notebooks/assignment1_titanic.ipynb` in **Google Colab**.
- Option A: Upload `train.csv` manually；Option B: use Kaggle API to download the Titanic dataset.
- Run cells top-to-bottom; artifacts/metrics will be saved into `artifacts/` and `results/`.

## 🧪 Reproducibility
- Python: 3.10+
- Install deps: `pip install -r requirements.txt`
- Use a fixed `random_state` for splits.

## 📈 Fill after you run
- Best Model: …  
- Metrics: Accuracy=…, F1(macro)=…, ROC-AUC=…  
- Takeaways: …  

## ✅ Submission Checklist
- [ ] Public GitHub repo
- [ ] README updated with results
- [ ] Transcript in `transcript.md`
- [ ] Notebook runs end-to-end
- [ ] Artifacts saved to `artifacts/` or `results/`
