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

summarizer = pipeline("summarization",
                       model="sshleifer/distilbart-cnn-12-6")

summarizer(
    """
    America has changed dramatically during recent years. Not only has the number of 
    graduates in traditional engineering disciplines such as mechanical, civil, 
    electrical, chemical, and aeronautical engineering declined, but in most of 
    the premier American universities engineering curricula now concentrate on 
    and encourage largely the study of engineering science. As a result, there 
    are declining offerings in engineering subjects dealing with infrastructure, 
    the environment, and related issues, and greater concentration on high 
    technology subjects, largely supporting increasingly complex scientific 
    developments. While the latter is important, it should not be at the expense 
    of more traditional engineering.

    Rapidly developing economies such as China and India, as well as other 
    industrial countries in Europe and Asia, continue to encourage and advance 
    the teaching of engineering. Both China and India, respectively, graduate 
    six and eight times as many traditional engineers as does the United States. 
    Other industrial countries at minimum maintain their output, while America 
    suffers an increasingly serious decline in the number of engineering graduates 
    and a lack of well-educated engineers.
"""
)

model = summarizer.model

print(model)

# ########################################