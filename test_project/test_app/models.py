from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255)
    persons = models.ManyToManyField(Person, through="PersonSkill")  
    categories = models.ManyToManyField("Category", through="SkillCategory")  

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Through Table for Person <-> Skill
class PersonSkill(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.name} - {self.skill.name}"

# Through Table for Skill <-> Category
class SkillCategory(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.skill.name} belongs to {self.category.name}"
