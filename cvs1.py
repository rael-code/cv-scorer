import tkinter as tk
from tkinter import Scrollbar, Text


class CVScorer:
    def __init__(self, job_description):
        self.job_description = job_description.lower()
        self.skills = {}

    def add_skill(self, skill, weight):
        self.skills[skill.lower()] = weight

    def score_cv(self, cv_text):
        cv_text = cv_text.lower()
        total_score = 0
        matched_skills = []
        unmatched_skills = []

        for skill, weight in self.skills.items():
            if skill in cv_text:
                total_score += weight
                matched_skills.append(skill)
            else:
                unmatched_skills.append(skill)

        return total_score, matched_skills, unmatched_skills


def calculate_score():
    job_description = job_description_text.get("1.0", "end-1c")
    cv_text = cv_text_box.get("1.0", "end-1c")

    scorer = CVScorer(job_description)

    for skill, weight in skills_list:
        scorer.add_skill(skill, weight)

    cv_score, matched_skills, unmatched_skills = scorer.score_cv(cv_text)

    result_label.config(text=f"CV Score: {cv_score} out of {len(skills_list)}")


    summary_text.delete(1.0, tk.END)
    summary_text.insert(tk.END, f"CV Score: {cv_score} out of {len(skills_list)}\n")
    summary_text.insert(tk.END, f"Matched Skills: {', '.join(matched_skills)}\n")
    summary_text.insert(tk.END, f"Unmatched Skills: {', '.join(unmatched_skills)}\n")


def clear_fields():
    job_description_text.delete("1.0", tk.END)
    cv_text_box.delete("1.0", tk.END)
    summary_text.delete(1.0, tk.END)


skills_list = [
    ("Customer Service", 1),
    ("Project Management", 1),
    ("Customer Communication", 2),
    ("Interpersonal Skills", 2),
    ("Willingness to Learn", 1),
    ("Communication Skills", 2),
    ("Problem-Solving", 2),
    ("Adaptability", 1),
    ("Attention to Detail", 1),
    ("Critical Thinking",2),

]

# main window (GUI)
root = tk.Tk()
root.title("CV Scorer")

# "Job description" text box
job_description_label = tk.Label(root, text="Job Description:")
job_description_label.pack()
job_description_text = Text(root, wrap=tk.WORD, width=40, height=10)
job_description_text.pack()

#"CV text" box
cv_text_label = tk.Label(root, text="CV Text:")
cv_text_label.pack()
cv_text_box = Text(root, wrap=tk.WORD, width=40, height=10)
cv_text_box.pack()

# "Calculate Score" Button
calculate_button = tk.Button(root, text="Calculate CV Score", command=calculate_score)
calculate_button.pack()

# CV score Display Label
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.pack()

# Scrollable text area
summary_text = Text(root, wrap=tk.WORD, width=40, height=10)
summary_text.pack()
scrollbar = Scrollbar(root, command=summary_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
summary_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
