from utils.skills import SKILLS

def extract_skills(text):
    found_skills[]

    # Convert text to lowercase
    text = text.lower()

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills)) # Removing duplicates

