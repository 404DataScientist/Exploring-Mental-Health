## 🧠 Mental Health Analysis Based on Lifestyle, Academic, and Professional Factors

This project explores mental health patterns among students and professionals using a dataset from Kaggle. The analysis focuses on academic pressure, professional stress, lifestyle factors, and personal history — with a goal of understanding key indicators that correlate with mental health conditions.


### 📂 Dataset

* **Source:** [Kaggle Mental Health Dataset](https://www.kaggle.com/datasets/adilshamim8/exploring-mental-health-data)
* **Key Features:**

  * **Demographics:** Gender, Profession
  * **Lifestyle:** Sleep Score, Dietary Habits
  * **Academic/Work Pressure:** Academic Pressure, Work Pressure, CGPA
  * **Mental Health History:** Have you ever had suicidal thoughts, Family History of Mental Illness	
  * **Satisfaction Metrics:** Study Satisfaction, Job Satisfaction


### 🛠️ Preprocessing Workflow

Data preprocessing was done using **scikit-learn pipelines** for clean, modular, and leak-proof handling.

#### ✔ Label Encoding (`OrdinalEncoder`):

* `gender`
* `working professional or student`
* `Have you ever had suicidal thoughts ?`
* `Family History of Mental Illness`

#### ✔ One-Hot Encoding:

* `dietary habits`
* `fieldofstudy`
* `professionalfield` (combined from `degree` and `profession`)
* `sleepscore` (transformed from `sleep duration`)

#### ✔ Simple Imputation (`SimpleImputer`):

* `academic pressure`
* `work pressure`
* `cgpa`
* `study satisfaction`
* `job satisfaction`

All steps were composed using **`ColumnTransformer`** and applied within a structured **train-test split** without data leakage.

### Note: During Feature engineering following columns were changed to reduce dimensions
* `Degree` -> `FieldOfStudy`
* `Profession` -> `ProfessionalField`
* `Sleep Duration` -> `SleepScore`

### 📊 Visualizations & Insights

A range of **exploratory data visualizations** was created to support the findings, including:

* **Distribution Plots:** Academic Pressure, Sleep Score, CGPA
* **Bar Charts:** Suicidal Thoughts by Gender, Job Satisfaction across Fields
* **Correlation Heatmap:** To identify significant numeric relationships
* **Boxplots/Violin Plots:** Comparing mental health responses across categorical groups
* **Countplots/Pie Charts:** Showing mental health condition frequency by demographic and lifestyle factors

All visualizations are styled for clarity and support interpretability.


### 📈 Goals of Analysis

* Identify lifestyle and professional factors linked to mental health issues
* Examine the prevalence of suicidal thoughts and familial mental illness history
* Explore how academic/work pressure impacts satisfaction and mental wellness


### 📦 Libraries Used

* `pandas`, `numpy`
* `matplotlib`, `seaborn`
* `scikit-learn`


### 🚀 How to Run

1. Clone the repository.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter notebook:

   ```bash
   jupyter notebook mental_health_analysis.ipynb
   ```


### 📄 License

### 📄 License & Dataset Usage

This project uses data provided under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license.

You are free to:
- Share — copy and redistribute the material
- Adapt — remix, transform, and build upon the material

**Under the following terms:**
- **Attribution** — You must give appropriate credit to the dataset creator.
- **NonCommercial** — You may not use the material for commercial purposes.

🔗 License Details: [CC BY-NC 4.0 Deed](https://creativecommons.org/licenses/by-nc/4.0/)

📊 Dataset Source: *[Mental Health Dataset on Kaggle](https://www.kaggle.com/datasets)*  
- **Author/Uploader:** Adil Shamim


