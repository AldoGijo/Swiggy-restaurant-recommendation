# 🍽️ Swiggy Restaurant Recommendation System

A **machine learning–based recommendation system** that suggests restaurants to users based on similarity in features such as cuisine, city, and ratings.
The project mimics the logic behind popular food delivery platforms like **Swiggy** by analyzing restaurant data and recommending the most relevant options.

---

## 📘 Project Overview

This project demonstrates a **data-driven recommendation engine** built using Python.
It covers every stage of a real-world data science workflow — from **data cleaning and encoding** to **clustering, similarity computation, and dashboard visualization**.

The model leverages both **Cosine Similarity** and **K-Means Clustering** techniques to deliver restaurant recommendations efficiently.

---

## 🚀 Key Features

✅ Cleaned and preprocessed real Swiggy restaurant dataset
✅ Encoded categorical columns (`city`, `cuisine`) using `OneHotEncoder`
✅ Scaled numerical features using `MinMaxScaler`
✅ Generated recommendations using **Cosine Similarity**
✅ Built an alternative **K-Means Clustering–based** model
✅ Developed an interactive **Streamlit dashboard**
✅ Stored and managed data in local CSV files for reproducibility

---

## 🧠 Machine Learning Techniques Used

| Technique              | Purpose                                                               |
| ---------------------- | --------------------------------------------------------------------- |
| **One-Hot Encoding**   | Converts categorical columns (`city`, `cuisine`) into numeric vectors |
| **Min-Max Scaling**    | Normalizes numerical columns for uniform distance calculations        |
| **Cosine Similarity**  | Measures similarity between restaurant feature vectors                |
| **K-Means Clustering** | Groups similar restaurants into clusters for fast recommendations     |

---

## 🧩 Project Workflow

### **1. Data Cleaning**

* Dropped unnecessary columns (e.g., `lic_no`)
* Removed duplicates
* Reset index
* Saved cleaned data → `cleaned_data/cleaned_data.csv`

### **2. Data Encoding**

* Applied OneHotEncoder to `city` and `cuisine`
* Saved encoded output → `cleaned_data/encoded_data.csv`

### **3. Recommendation Engine**

* **Cosine Similarity–based model:** Recommends restaurants most similar to the selected one
* **K-Means Clustering model:** Groups restaurants and recommends within the same cluster

### **4. Streamlit Dashboard**

* Interactive web app (`swigdash.py`)
* Allows users to select a restaurant and get top N recommendations
* Displays restaurant details and similarity scores visually

---

## 🧰 Tech Stack

| Category            | Tools                                          |
| ------------------- | ---------------------------------------------- |
| **Language**        | Python 3.10+                                   |
| **Libraries**       | Pandas, NumPy, Scikit-learn, Streamlit, Pickle |
| **Visualization**   | Streamlit                                      |
| **Storage**         | CSV Files (Local)                              |
| **Version Control** | Git & GitHub                                   |

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/swiggy-recommendation-system.git
cd swiggy-recommendation-system
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run swigdash.py
```

### 4️⃣ View in Browser

Your app will open automatically at:
👉 `http://localhost:8501`

---

## 📊 Sample Output

**Dashboard Features:**

* Restaurant Selection Dropdown
* Similar Restaurant Recommendations
* Cuisine and City Filters
* Top N Similarity Results
* Clustering Visual Insights

---

## 📈 Future Enhancements

🔹 Integrate live restaurant data from Swiggy API
🔹 Deploy the model on Streamlit Cloud or HuggingFace Spaces
🔹 Add user-based collaborative filtering
🔹 Include sentiment analysis of restaurant reviews

---

## 👨‍💻 Author

**Asaf**
Data Science Enthusiast | Python Developer | ML Learner
📧 *Contact:* [[your.email@example.com](mailto:aldogijo123@gmail.com)]
🌐 *GitHub:* [https://github.com/yourusername](https://github.com/AldoGijo/Swiggy-restaurant-recommendation/new/main?filename=README.md)

---

⭐ *If you like this project, consider giving it a star on GitHub!*
