
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

df = pd.read_excel("liste_techniciens.xlsx")

options = Options()
options.add_argument("--start-maximized")

interventions_demain = []

def extraire_interventions(driver, nom, login, onglet_type):
    try:
        driver.find_element(By.LINK_TEXT, onglet_type).click()
        time.sleep(4)

        while True:
            cards = driver.find_elements(By.CLASS_NAME, "intervention")
            if not cards:
                break

            total = len(cards)
            for i in range(total):
                try:
                    cards = driver.find_elements(By.CLASS_NAME, "intervention")
                    card = cards[i]
                    text = card.text
                    lines = text.split("\n")
                    date_line = next((l for l in lines if "Date du RDV" in l), None)
                    if not date_line:
                        continue
                    date_str = date_line.split(":")[1].strip()
                    if len(date_str) == 13:
                        date_str += ":00"
                    rdv_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                    now = datetime.now()
                    demain = now + timedelta(days=1)

                    if rdv_time.date() != demain.date():
                        continue

                    card.click()
                    time.sleep(2)

                    statut = "Prévue"
                    debut_intervention = ""
                    jeton_val = ""
                    adresse_client = ""

                    labels = driver.find_elements(By.CLASS_NAME, "label")
                    for label in labels:
                        try:
                            b = label.find_element(By.TAG_NAME, "b")
                            label_title = b.text.strip().lower()
                            texte_complet = label.text.strip()

                            if "début de l'intervention" in label_title:
                                parts = texte_complet.split(":")
                                if len(parts) > 1:
                                    debut_intervention = parts[1].strip()
                                    statut = f"Démarrée à {debut_intervention}"

                            elif "jeton" in label_title:
                                parts = texte_complet.split(":")
                                if len(parts) > 1:
                                    jeton_val = parts[1].strip()

                            elif "adresse" in label_title:
                                try:
                                    adresse_client = label.find_element(By.TAG_NAME, "a").text.strip()
                                except:
                                    adresse_client = texte_complet.split(":")[1].strip()

                        except:
                            continue

                    interventions_demain.append({
                        "technicien": nom,
                        "login": login,
                        "jeton": jeton_val,
                        "adresse": adresse_client,
                        "rdv": rdv_time.strftime("%Y-%m-%d %H:%M"),
                        "statut": statut,
                        "heure_actuelle": now.strftime("%Y-%m-%d %H:%M"),
                        "type": onglet_type
                    })

                    driver.back()
                    time.sleep(2)

                except Exception as e:
                    print(f"Erreur sur une intervention : {e}")
                    continue
            break

    except Exception as e:
        print(f"Erreur pour {nom} dans l’onglet {onglet_type} : {e}")

for index, row in df.iterrows():
    nom = row["nom"]
    login = str(row["login"])
    password = str(row["password"])

    print(f"Connexion pour {nom}...")

    driver = webdriver.Chrome(options=options)
    driver.get("https://aboracco.pub.app.ftth.iliad.fr/")
    time.sleep(3)

    inputs = driver.find_elements(By.TAG_NAME, "input")
    inputs[0].send_keys(login)
    inputs[1].send_keys(password)

    time.sleep(1)
    bouton_connexion = driver.find_element(By.XPATH, "//button[contains(text(), 'Connexion')]")
    bouton_connexion.click()
    time.sleep(4)

    extraire_interventions(driver, nom, login, "Production")
    extraire_interventions(driver, nom, login, "Post-Production / SAV")

    driver.quit()

if interventions_demain:
    df_result = pd.DataFrame(interventions_demain)
    df_result.to_excel("planification_demain.xlsx", index=False)
    print("\nFichier 'planification_demain.xlsx' généré avec succès.")
else:
    print("\nAucune intervention détectée pour demain.")
