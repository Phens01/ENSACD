from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Adresse e-mail')

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmer le mot de passe', widget=forms.PasswordInput)
    email = forms.EmailField(label='Adresse e-mail')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Les mots de passe ne correspondent pas.")
            
            
            
class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['NumModule', 'Title', 'Auteur']
        labels = {
            'NumModule': 'Numéro du module',
            'Title': 'Titre du module',
            'Auteur': 'Auteur'
        }

class ObjectifForm(forms.ModelForm):
    class Meta:
        model = Objectif
        fields = ['Libelle']
        labels = {
            'Libelle': 'Objectif'
        }

class UAForm(forms.ModelForm):
    class Meta:
        model = UA
        fields = ['NumUA', 'Objectifs', 'Auteur']
        labels = {
            'NumUA': 'Numéro UA',
            'Objectifs': 'Les objectifs UA',
            'Auteur': 'Auteur'
        }

class NiveauForm(forms.ModelForm):
    class Meta:
        model = Niveau
        fields = ['NumNiveau', 'Cycle', 'Auteur']
        labels = {
            'NumNiveau': 'Numéro du Niveau',
            'Cycle': 'Cycle du Niveau',
            'Auteur': 'Auteur'
        }

class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ['CodeMatiere', 'Intitule', 'Auteur']
        labels = {
            'CodeMatiere': 'Code de la Matiere',
            'Intitule': 'Intitulé de la Matiere',
            'Auteur': 'Auteur'
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['Module', 'UA', 'Niveau', 'Matiere', 'NumCourse', 'Titre', 'Objectifs', 'Nature', 'Duree', 'Auteur']
        labels = {
            'Module': 'Module ',
            'UA': 'UA',
            'Niveau': 'Niveau ',
            'Matiere': 'Matiere',
            'NumCourse': 'Numéro de la leçon',
            'Titre': 'Titre de la leçon',
            'Objectifs': 'Les objectifs de l\'UA',
            'Nature': 'Nature de la leçon',
            'Duree': 'Durée de la leçon',
            'Auteur': 'Auteur'
        }

class KitForm(forms.ModelForm):
    class Meta:
        model = Kit
        fields = ['NumKit', 'Nom', 'Quantite', 'Auteur']
        labels = {
            'NumKit': 'Numéro du kit',
            'Nom': 'Nom de l\'équipement',
            'Quantite': 'Quantité',
            'Auteur': 'Auteur'
        }

class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ['Code', 'Effectif']
        labels = {
            'Code': 'Code de la salle',
            'Effectif': 'Effectif'
        }

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['Code', 'Intitule', 'Effectif']
        labels = {
            'Code': 'Code du département',
            'Intitule': 'Intitulé du Département',
            'Effectif': 'Effectif'
        }

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['Departement', 'Matricule', 'Nom', 'Prenom', 'lieu_de_naissance', 'genre', 'password']
        labels = {
            'Departement': 'Département associé',
            'Matricule': 'Matricule de l\'enseignant',
            'Nom': 'Nom de l\'enseignant',
            'Prenom': 'Prenom de l\'enseignant',
            'lieu_de_naissance': 'Date de naissance',
            'genre': 'Genre',
            'password': 'Mot de passe'
        }

class AdministrateurForm(forms.ModelForm):
    class Meta:
        model = Administrateur
        fields = ['Matricule', 'Nom', 'Prenom', 'Lieu_de_naissance', 'genre', 'Status', 'password']
        labels = {
            'Matricule': 'Matricule de l\'enseignant',
            'Nom': 'Nom de l\'enseignant',
            'Prenom': 'Prenom de l\'enseignant',
            'Lieu_denaissance': 'Lieu de naissance',
            'genre': 'Genre',
            'Status': 'Statut',
            'password': 'Mot de passe'
        }


class DigCourseForm(forms.ModelForm):
    class Meta:
        model = DigCourse
        fields = ['Course', 'Classe', 'Enseignant', 'Kitdig', 'Niveau', 'Titre']
        labels = {
            'Course': 'Leçon',
            'Classe': 'Classe',
            'Niveau': 'Niveau',
            'Kitdig': 'Kit de digitalisation',
            'Enseignant': 'Nom enseignant',
            'Titre': 'Titre de la leçon'
        }