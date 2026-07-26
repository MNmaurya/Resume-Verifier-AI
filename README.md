# 💼 AI Resume Analyzer with ATS Score Prediction

An AI-powered Resume Analyzer built using **Python, Streamlit, and Machine Learning** that evaluates resumes based on skills, experience, and education. The application calculates an ATS (Applicant Tracking System) score, predicts whether a resume is likely to be shortlisted, and provides an estimated selection probability.

--- 

## 📌 Features
 
- ✅ ATS Score Calculation (Out of 100)
- ✅ Intelligent Skill Matching
- ✅ Resume Shortlisting Prediction
- ✅ Selection Probability Estimation
- ✅ Interactive Streamlit Dashboard
- ✅ Machine Learning-Based Prediction
- ✅ Real-Time Resume Analysis

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Logistic Regression

---

## 📂 Project Structure

```
AI-Resume-Analyzer/
│
├── app.py              # Streamlit Frontend
├── model.py            # Machine Learning Model & Backend Logic
└── README.md
```

---

## 🚀 How It Works

### Step 1: Enter Details

The user provides:

- Skills (comma separated)
- Years of Experience
- Education Level

---

### Step 2: Skill Matching

The application compares the entered skills with predefined industry-relevant skills such as:

- Python
- SQL
- Machine Learning
- Flask
- Git
- AWS
- HTML
- CSS
- MongoDB
- and many more.

It then calculates the total number of matched skills.

---

### Step 3: ATS Score Calculation

The ATS Score is calculated using:

- Skill Match
- Experience
- Education Level

The score is normalized to a scale of **100**.

---

### Step 4: Machine Learning Prediction

A **Logistic Regression** model predicts whether the resume is likely to be:

- ✅ Shortlisted
- ❌ Rejected

---

### Step 5: Selection Probability

The application also estimates the candidate's probability of getting shortlisted:

| Skill Match | Selection Chance |
|-------------|------------------|
| 5 or more | High (80%) |
| 3–4 | Moderate (50%) |
| Less than 3 | Low (20%) |

---

## 📊 Output

The application displays:

- Skills Matched
- ATS Score
- Selection Probability
- Matched Skills List
- Resume Status
- Personalized Feedback

---

## 📷 User Interface

The application provides an interactive dashboard where users can:

- Enter resume details
- Analyze their resume
- View ATS score
- Check matched skills
- Predict shortlisting status
- Estimate selection probability

---

## 📖 Machine Learning Model

The project uses **Logistic Regression**, a supervised machine learning classification algorithm, to predict resume shortlisting based on:

- Skill Match
- Experience
- Education
- ATS Score

---

## 🎯 Future Enhancements

- 📄 Upload Resume (PDF/DOCX)
- 🤖 NLP-Based Resume Parsing
- ☁️ Cloud Deployment
- 📈 Advanced ATS Scoring
- 💡 Personalized Resume Improvement Suggestions
- 🧠 AI-Based Resume Feedback
- 📊 Recruiter Dashboard

---

## 💡 Learning Outcomes

Through this project, I learned:

- Streamlit Web Application Development
- Machine Learning Model Training
- Logistic Regression
- Feature Engineering
- ATS Score Calculation
- Rule-Based Recommendation Systems
- Data Preprocessing
- Frontend and Backend Integration
- Python Application Development

---

## 👩‍💻 Author

**Muskan Maurya**

AI/ML Engineering Student
---

⭐ If you found this project helpful, don't forget to star the repository! 
