import pandas as pd
from sklearn.linear_model import LogisticRegression

# Expanded required skills
required_skills = [
    "python", "java", "c++", "c",
    "sql", "mongodb",
    "machine learning", "deep learning", "data analysis", "data science",
    "html", "css", "javascript", "react", "nodejs",
    "flask", "django",
    "git", "github",
    "excel", "power bi",
    "cloud", "aws"
]

# Dataset for taining the model  
data = {
    'SkillMatch': [1,2,3,0,4,2,1,5,0,3],
    'Experience': [1,2,3,0,4,2,1,5,0,3],
    'Education': [2,3,3,1,3,2,2,3,1,3],  #school=1,UG=2,PG=3 >>>FEATURE ENCODING
    'ATS_Score': [40,60,80,20,95,70,50,110,10,85],
    'Result': [0,1,1,0,1,1,0,1,0,1]
}

df = pd.DataFrame(data)

X = df[['SkillMatch','Experience','Education','ATS_Score']]
y = df['Result']

# Train model
model = LogisticRegression()
model.fit(X, y) # training the model:x = given input, y = expexted o/p

# Skill matching (smart matching)
def match_skills(user_skills):
    user_skills = [skill.strip().lower() for skill in user_skills.split(",")]
    
    matched = 0
    matched_list = []
    
    for user_skill in user_skills:
        for req_skill in required_skills:
            if user_skill in req_skill or req_skill in user_skill:
                matched += 1
                matched_list.append(req_skill)
                break

    return matched, list(set(matched_list))

# ATS Score calculation
def calculate_ats(skill_match, experience, education):
    raw_score = (skill_match * 15) + (experience * 5) + (education * 10) #Weights assigned to each feature acc to priority
    
    # Normalize to 100
    max_possible = (7 * 15) + (10 * 5) + (3 * 10)  # max inputs
    normalized_score = (raw_score / max_possible) * 100
    
    return round(normalized_score, 2)

# Rule-based probability
def get_probability(skill_match):
    if skill_match >= 5:
        return 80, "High chances of getting shortlisted"
    elif skill_match >= 3:
        return 50, "Moderate chances of getting shortlisted"
    else:
        return 20, "Low chances of getting shortlisted"

# Final prediction
def predict_resume(skills, experience, education):
    skill_match, matched_list = match_skills(skills)
    ats = calculate_ats(skill_match, experience, education)

    # ML prediction give o/p as (0 or 1) BINARY CLASSIFICATION PROBLEM
    prediction = model.predict([[skill_match, experience, education, ats]])[0]

    # Rule-based probability
    probability, message = get_probability(skill_match)

    return skill_match, matched_list, ats, prediction, probability, message