from django.shortcuts import render
from .models import Person, Skill, Category

def skill_view(request):
    persons = Person.objects.all()
    skills = Skill.objects.all()
    categories = Category.objects.all()

    person_skills = {person.id: list(Skill.objects.filter(persons=person).values("id", "name")) for person in persons}
    category_skills = {category.id: list(Skill.objects.filter(categories=category).values("id", "name")) for category in categories}
    skill_persons = {skill.id: list(skill.persons.values("id", "name")) for skill in skills}
    skill_categories = {skill.id: list(skill.categories.values("id", "name")) for skill in skills}

    return render(request, "skill_view.html", {
        "persons": persons,
        "skills": skills,
        "categories": categories,
        "person_skills": person_skills,
        "category_skills": category_skills,
        "skill_persons": skill_persons,
        "skill_categories": skill_categories
    })
