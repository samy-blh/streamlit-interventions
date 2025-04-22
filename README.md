[README.md](https://github.com/user-attachments/files/19857992/README.md)[Uploading READM
# 🛠 Outil de Gestion des Interventions Free

Cette application Streamlit permet de suivre, planifier et analyser les interventions des techniciens Free (via AboRacco). Elle regroupe plusieurs scripts Python dans une interface simple à utiliser.

## ⚙️ Fonctions disponibles

1. ✅ **Interventions à suivre aujourd’hui**
   - Suivi des interventions en retard ou non démarrées.
   - Génère un fichier Excel avec statut de démarrage.

2. 📁 **Planning des interventions (demain)**
   - Affiche les interventions prévues pour demain.
   - Génère un fichier Excel du planning technicien par technicien.

3. 📆 **Interventions terminées à une date précise**
   - À partir d’une date choisie, récupère toutes les interventions clôturées.
   - Ajoute l’état de la box (OK / NOK).
   - Produit un Excel.

## 🧑‍💻 Utilisation

Lancer l’interface :
```bash
streamlit run streamlit_app.py
```

> ⚠️ Assurez-vous d’avoir un fichier `liste_techniciens.xlsx` dans le dossier (non fourni ici pour des raisons de sécurité).
> Il doit contenir les colonnes : `nom`, `login`, `password`.

## 📦 Dépendances

Toutes les dépendances sont listées dans `requirements.txt`.  
Installation recommandée :
```bash
pip install -r requirements.txt
```

---

Projet développé par Samy B. dans le cadre de la gestion de la conduite d'activité Free.
E.md…]()
