# 🎯 Smart Career Path Advisor

The **Smart Career Advisor** is an intelligent machine learning-based system that helps students or professionals discover suitable career paths based on their **skills**, **interests**, and **education background**.

Built using **Python**, **NLP**, and a **Streamlit web interface**, it compares user input to a large dataset of 2000 unique career profiles using **TF-IDF vectorization** and **cosine similarity** to recommend the top 3 most relevant careers.

---

## 🌟 Features

- ✅ Takes input in simple text (skills, interests, education)
- 🧠 Uses NLP to understand and process user input
- 📊 Recommends top 3 career roles from 2000+ real-world job profiles
- 🧾 Shows career descriptions and match confidence scores
- 🌐 Streamlit app with clean and responsive UI

---

## 🛠️ Tech Stack Used

| Tool/Library      | Purpose                             |
|-------------------|-------------------------------------|
| Python            | Main programming language           |
| Streamlit         | To build the web application        |
| scikit-learn      | For TF-IDF and cosine similarity    |
| Custom Python Modules | For organizing logic and dataset |

---

## 📂 Project Structure

```
smart_career_advisor/
│
├── app.py             # Main Streamlit app
├── recommend.py       # Contains career matching logic
├── career_data.py     # Contains job roles data (hardcoded dataset)
└── README.md          # You're reading this!
```

---

## 💻 How to Run the Project

### Step 1: download the project folder

### Step 2: Install the dependencies

streamlit
pandas
scikit-learn

### Step 3: Run the Streamlit app
```bash
streamlit run app.py
```

This will open the app in your web browser.

---

## 🧠 How It Works

1. User fills out a simple form:
   - Skills (e.g. python, teamwork, SQL)
   - Interests (e.g. design, marketing, AI)
   - Education level (e.g. Bachelor's)

2. The app combines this input into a single string.

3. It compares this string with each career in the dataset using **TF-IDF** (Term Frequency-Inverse Document Frequency).

4. It calculates **cosine similarity** between user input and each career profile.

5. Returns the top 3 most relevant matches, along with:
   - Career name
   - Brief description
   - Confidence score (% match)

---

## 📈 Example Input/Output

### 🧾 Input:
```
Skills: python, machine learning, statistics
Interests: data, ai, problem solving
Education: Bachelor's
```

### ✅ Output:
```
1. Data Scientist (Match: 93.5%)
   Work with data, build ML models, and draw insights.

2. AI Researcher (Match: 90.3%)
   Explore and invent cutting-edge AI algorithms and models.

3. Business Analyst (Match: 84.2%)
   Bridge business and technology with data-driven decisions.
```

---

## 🎯 Use Cases

- 💼 College students seeking career clarity
- 👨‍💻 Entry-level professionals switching domains
- 🧑‍🏫 Career counseling tools
- 🎓 Academic projects or portfolio demos

---

## 🔮 Future Improvements

- Resume parser to auto-extract skills and education
- More accurate suggestions using sentence embeddings
- Add filters: remote, domain, salary, etc.
- Integrate a chatbot for Q&A and career exploration
- Deploy live on Streamlit Cloud or Hugging Face Spaces

---

## 👨‍💻 Author

**Vaibhav Jain**  
_BSc Data Science Student | Python & ML Enthusiast_  
🔗 [LinkedIn](https://www.linkedin.com/in/vaibhav-jain-84274826b) • 📧 vaibhavjie1@gmail.com

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
