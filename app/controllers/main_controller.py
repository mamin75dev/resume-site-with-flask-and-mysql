from flask import render_template
from models.profile import Profile
from models.experience import Experience
from models.education import Education
from models.skill import Skill


class MainController:
    @staticmethod
    def main():
        profile = Profile()
        profile.get_proflie_from_db()
        experiences = Experience.get_expriences_from_db()
        educations = Education.get_educations_from_db()
        skills = Skill.get_skills_from_db()
        return render_template("index.html",
                               data={"profile": profile, "experiences": experiences,
                                     "educations": educations, "skills": skills})
