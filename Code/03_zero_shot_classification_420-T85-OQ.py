# Installer les bibliothèques nécessaires (ligne 11 à 16)

# 'datasets' est pour charger et manipuler les jeux de données
# 'evaluate' est pour évaluer les performances du modèle
# 'transformers[sentencepiece]' est pour utiliser les modèles de transformers avec SentencePiece
# SentencePiece est un tokenizeur et détokenizeur de sous-mots indépendant de la langue, principalement pour les systèmes de traitement de texte basés sur les réseaux de neurones.
# Il fournit un moyen de diviser le texte en tokens qui peuvent être utiles pour des tâches de traitement de texte comme la traduction, la reconnaissance vocale, etc.

# '--progress-bar off' est pour désactiver la barre de progression pendant l'installation

#!pip install -qqq datasets evaluate transformers[sentencepiece] #--progress-bar off
#!pip install -qqq huggingface_hub

#!pip list
#!pip install -qqq torch torchvision torchaudio
#!pip install -qqq tensorflow

# ########################################
# Code suivant
# ########################################

# READ TOKEN: hf_ezjnAnUXDCmejAWoqgcvpzKlxbjlgzjx--

from huggingface_hub import notebook_login

notebook_login() 

# ########################################

from transformers import pipeline

classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

result = classifier(
    "This is a course about Artificial Intelligence models used in NLP.",
    candidate_labels=["education", "politics", "business"],
)

model = classifier.model

print(result)

print(model)

# ########################################