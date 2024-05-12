from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Module(models.Model):
    "Représente le module d'une leçon"
    NumModule = models.PositiveIntegerField(verbose_name = "Numéro du module", null=False, default = 0)
    Title = models.CharField(max_length = 255, verbose_name = "Intitulé du module", null = False)
    date_publiee = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    Auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.NumModule} : {self.Title}"
    


class Objectif(models.Model):
    Libelle = models.CharField(max_length = 100, verbose_name = "Objectif")
    
    def __str__(self):
        return self.Libelle
    
class UA(models.Model):
    "Représente l'UA d'une leçon"
    NumUA = models.PositiveIntegerField(verbose_name = "Numéro du UA", null=False)
    Objectifs = models.ManyToManyField(Objectif,blank=True, verbose_name = "Les objectifs de l'UA")
    date_publiee = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    Auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.NumUA} : {self.Objectifs}"
    
    
class Niveau(models.Model):
    "Représente le Niveau d'une leçon"
    CYCLE_CHOICE = (
        ('Observation', 'Observation'),
        ('Orientation', 'Orientation'),
    )
    NumNiveau = models.PositiveIntegerField(verbose_name = "Numéro du Niveau", null=False)
    Cycle = models.CharField(max_length = 20, choices = CYCLE_CHOICE, verbose_name = "Cycle du Niveau", null = False)
    date_publiee = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    Auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.NumNiveau} : {self.Cycle}"
    
class Matiere(models.Model):
    "Représente le Matiere d'une leçon"
    CodeMatiere = models.CharField(max_length = 10,verbose_name = "Code de la Matiere", null=False)
    Intitule = models.CharField(max_length = 255,  verbose_name = "Intitulé de la Matiere", null = False)
    date_publiee = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    Auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.CodeMatiere} : {self.Intitule}"
    
class Course(models.Model):
    "Représente une leçon"
    NATURE = (
        ('Pratique', 'Pratique'),
        ('Theorique', 'Theorique'),
        ('Hybride', 'Hybride'),
    )
    Module = models.ForeignKey(Module, on_delete = models.CASCADE, verbose_name = "Module associé")
    UA = models.ForeignKey(UA, on_delete = models.CASCADE, verbose_name = "UA associée")
    Niveau = models.ForeignKey(Niveau, on_delete = models.CASCADE, verbose_name = "Niveau associé")
    Matiere = models.ForeignKey(Matiere, on_delete = models.CASCADE, verbose_name = "Matiere associée")
    NumCourse = models.PositiveIntegerField(verbose_name = "Numéro de la leçon", null=False)
    Titre = models.CharField(max_length = 50, verbose_name = "Titre de la leçon", null = False)
    Objectifs = models.ManyToManyField(Objectif,blank=True, verbose_name = "Les objectifs de l'UA")
    Nature = models.CharField(max_length = 20, choices = NATURE, verbose_name = "Nature de la leçon", null = False)
    Duree = models.DurationField(blank=True, null=True, verbose_name="Durée de la leçon")
    date_publiee = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    Auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.NumCourse} : {self.Titre}"
    
    
class Kit(models.Model):
    "Représente les équipements utilisés lors de la dispensation des cours"
    NumKit = models.PositiveIntegerField(null = False)
    Nom = models.CharField(max_length = 50, verbose_name = "Nom de l'équipement")
    Quantite = models.PositiveIntegerField(default = 1, verbose_name = "Qauntité")   
    date_publiee = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    Auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.NumKit} : {self.Quantite}"
    

class Classe(models.Model):
    "Représente la classe liée à la matière"
    Code = models.CharField(max_length = 10, verbose_name = "Code de la salle", null=False)
    Effectif = models.PositiveIntegerField(default = 0)
    
    
    def __str__(self) -> str:
        return f"{self.Code} : {self.Effectif}"
    

class Departement(models.Model):
    "Représente le département lié à la matière"
    Code = models.CharField(max_length = 10, verbose_name = "Code du département", null=False)
    Intitule = models.CharField(max_length = 20, verbose_name = "Intitulé du Département")
    Effectif = models.PositiveIntegerField(default = 0)
    
    
    def __str__(self) -> str:
        return f"{self.Code} : {self.Intitule}"
    
class Enseignant(models.Model):
    "Représente un enseignant"
    Departement = models.ForeignKey(Departement, on_delete = models.CASCADE, verbose_name = "Département associé")
    Matricule = models.CharField(max_length=20, verbose_name = "Matricule de l'enseignant", null = False)
    Nom = models.CharField(max_length=100, verbose_name = "Nom de l'enseignant", null = False)
    Prenom = models.CharField(max_length=100, verbose_name = "Prenom de l'enseignant", null = False)
    lieu_de_naissance = models.DateTimeField(verbose_name = "Date de naissance")
    genre_choices = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    genre = models.CharField(max_length=1, choices=genre_choices)
    password = models.CharField(max_length=100)
    
    
    def __str__(self) -> str:
        return f"{self.Nom} {self.IPrenom}"


class Administrateur(models.Model):
    "Représente un administrateur"
    Matricule = models.CharField(max_length=20, verbose_name = "Matricule de l'enseignant", null = False)
    Nom = models.CharField(max_length=100, verbose_name = "Nom de l'enseignant", null = False)
    Prenom = models.CharField(max_length=100, verbose_name = "Prenom de l'enseignant", null = False)
    Lieu_de_naissance = models.DateTimeField(verbose_name = "Date de naissance")
    genre_choices = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    genre = models.CharField(max_length=1, choices=genre_choices)
    status_choices = [
        ('P', 'Proviseur'),
        ('C', 'Censeur'),
    ]
    Status = models.CharField(max_length=1, choices=status_choices)
    password = models.CharField(max_length=100)
    
    
    def __str__(self) -> str:
        return f"{self.Nom} : {self.Prenom}"
    
    
class KitDig(models.Model):
    "Représente le Kit de digitalisation"
    Admin = models.ForeignKey(Administrateur, on_delete = models.CASCADE, verbose_name = "Administrateur qui l'a ajouté")
    CodeK = models.CharField(max_length = 10, verbose_name = "Code du kit", null = False )
    
    def __str__(self) -> str:
        return f"{self.CodeK}"
    
    

class DigCourse(models.Model):
    "Représente une leçon digitalisée"
    Course = models.ForeignKey(Course, on_delete = models.CASCADE, verbose_name = "Leçon à digitaliser")
    Classe = models.ForeignKey(Classe, on_delete = models.CASCADE, verbose_name = "Classe du cours")
    Enseignant = models.ForeignKey(Enseignant, on_delete = models.CASCADE, verbose_name = "Enseignant qui dispense la leçon")
    Kitdig = models.ForeignKey(KitDig, on_delete = models.CASCADE, verbose_name = "L'équipement utilisé")
    Niveau = models.ForeignKey(Niveau, on_delete = models.CASCADE, verbose_name = "Niveau de la leçon")
    Titre = models.CharField(max_length = 100, null = False, verbose_name = "Titre de la leçon digitalisée")
    Debut = models.DateTimeField(auto_now = True)
    
    
    def __str__(self) -> str:
        return f"{self.Course} : {self.Titre}"