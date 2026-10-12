
import tkinter as tk
import webbrowser
import os
from urllib.parse import quote
from html import escape

WHATSAPP = "2250564076055"
DOSSIER_SITE = os.path.abspath("WUA_SITE_WEB")


SERVICES = [
    {
        "nom": "Création de QR codes",
        "prix": "À partir de 1 000 FCFA",
        "description": "QR codes pour WhatsApp, Facebook, liens et entreprises.",
        "details": (
            "Facilitez l'accès à vos informations grâce à un QR code. "
            "Vos clients pourront scanner votre code pour découvrir votre "
            "entreprise, ouvrir votre WhatsApp ou accéder à un lien."
        ),
        "prestations": [
            "QR code pour WhatsApp",
            "QR code pour les réseaux sociaux",
            "QR code pour un site Internet ou un lien",
            "QR code pour une activité commerciale"
        ],
        "image": "https://images.unsplash.com/photo-1595079676339-1534801ad6cf?auto=format&fit=crop&w=1000&q=85"
    },
    {
        "nom": "Affiches publicitaires",
        "prix": "À partir de 2 000 FCFA",
        "description": "Des affiches attrayantes pour présenter vos produits et promotions.",
        "details": (
            "Mettez votre activité en valeur avec une affiche publicitaire "
            "adaptée à votre communication. Présentez vos produits, vos "
            "promotions, vos coordonnées et les informations importantes "
            "de votre entreprise."
        ),
        "prestations": [
            "Affiches pour promotions",
            "Visuels pour produits et services",
            "Affiches pour événements",
            "Visuels adaptés aux réseaux sociaux"
        ],
        "image": "https://images.unsplash.com/photo-1541701494587-cb58502866ab?auto=format&fit=crop&w=1000&q=85"
    },
    {
        "nom": "Catalogues WhatsApp",
        "prix": "À partir de 3 000 FCFA",
        "description": "Présentez vos produits, leurs photos, leurs noms et leurs prix.",
        "details": (
            "Présentez votre boutique et vos produits dans un catalogue "
            "facile à consulter et à partager sur WhatsApp. Chaque produit "
            "peut être présenté avec une image, un nom, une description "
            "et un prix communiqué par votre entreprise."
        ),
        "prestations": [
            "Présentation de vos produits",
            "Ajout des photos fournies",
            "Affichage des noms et des prix",
            "Mise en page facile à partager"
        ],
        "image": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=1000&q=85"
    },
    {
        "nom": "CV et lettres de motivation",
        "prix": "À partir de 1 500 FCFA",
        "description": "Des CV clairs et des lettres de motivation au format numérique.",
        "details": (
            "Préparez vos candidatures avec des documents bien structurés. "
            "Votre CV peut présenter votre parcours, vos compétences, "
            "vos expériences et votre formation. La lettre de motivation "
            "est adaptée au poste ou à la formation visée."
        ),
        "prestations": [
            "Mise en page de CV",
            "Création de lettre de motivation",
            "Organisation des informations",
            "Préparation de documents numériques"
        ],
        "image": "https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&w=1000&q=85"
    },
    {
        "nom": "Menus numériques",
        "prix": "À partir de 5 000 FCFA",
        "description": "Des menus pour restaurants et maquis avec plats et tarifs.",
        "details": (
            "Présentez votre carte de restauration de manière claire et "
            "professionnelle. Vos clients peuvent consulter les plats, "
            "les catégories et les prix à partir d'un menu numérique "
            "facile à partager."
        ),
        "prestations": [
            "Présentation des plats et boissons",
            "Organisation par catégories",
            "Ajout des prix communiqués",
            "Menu numérique à partager avec vos clients"
        ],
        "image": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?auto=format&fit=crop&w=1000&q=85"
    }
]


def creer_page_accueil():
    cartes = ""

    for i, service in enumerate(SERVICES):
        nom = escape(service["nom"])
        description = escape(service["description"])
        prix = escape(service["prix"])
        image = escape(service["image"], quote=True)

        cartes += f"""
        <article class="carte">
            <a class="lien-carte" href="service_{i}.html">
                <img src="{image}"
                     alt="{nom}"
                     loading="lazy">
                <div class="contenu">
                    <h3>{nom}</h3>
                    <p>{description}</p>
                    <div class="prix">{prix}</div>
                    <span class="bouton">Voir les détails →</span>
                </div>
            </a>
        </article>
        """

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>WUA SERVICE DIGITAL | Catalogue</title>
<style>
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: #08111f;
    color: white;
    line-height: 1.6;
}}
header {{
    padding: 20px 6%;
    background: #101d30;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    border-bottom: 2px solid #22d3ee;
}}
.logo {{ font-size: 22px; font-weight: bold; }}
.logo span {{ color: #22d3ee; }}
nav a {{
    color: white;
    text-decoration: none;
    margin: 8px;
}}
.hero {{
    padding: 65px 7%;
    text-align: center;
    background: linear-gradient(135deg, #16375a, #08111f);
}}
.hero h1 {{ font-size: clamp(32px, 6vw, 54px); line-height: 1.2; }}
.hero h1 span {{ color: #ffda48; }}
.hero p {{ color: #d0d9e7; max-width: 680px; margin: 15px auto; }}
.bouton {{
    display: inline-block;
    border-radius: 9px;
    background: #25d366;
    color: #06220f;
    padding: 12px 17px;
    font-weight: bold;
    text-decoration: none;
}}
section {{ padding: 35px 7%; }}
.intro {{ color: #bac7da; }}
.catalogue {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(245px, 1fr));
    gap: 20px;
}}
.carte {{
    overflow: hidden;
    background: #14243c;
    border: 1px solid #304765;
    border-radius: 15px;
    transition: transform 0.2s;
}}
.carte:hover {{ transform: translateY(-5px); }}
.lien-carte {{ color: inherit; text-decoration: none; display: block; height: 100%; }}
.carte img {{
    width: 100%;
    height: 190px;
    object-fit: cover;
    display: block;
    background: #24354c;
}}
.contenu {{ padding: 18px; }}
.contenu h3 {{ color: #22d3ee; margin-top: 0; }}
.contenu p {{ color: #d0d9e7; }}
.prix {{ color: #ffda48; font-weight: bold; margin: 15px 0; }}
footer {{
    padding: 25px;
    border-top: 1px solid #304765;
    text-align: center;
    color: #bac7da;
}}
@media(max-width:600px) {{
    header {{ gap: 10px; }}
    section {{ padding: 28px 5%; }}
}}
</style>
</head>
<body>
<header>
    <div class="logo">WUA <span>SERVICE DIGITAL</span></div>
    <nav>
        <a href="#services">Services</a>
        <a href="#contact">Contact</a>
    </nav>
</header>

<div class="hero">
    <h1>Bienvenue chez<br><span>WUA SERVICE DIGITAL</span></h1>
    <p>
        Des solutions numériques pour les particuliers, les commerçants,
        les restaurants et les entrepreneurs.
        Choisissez un service pour découvrir tous ses détails.
    </p>
    <a class="bouton" href="#services">Découvrir nos services</a>
</div>

<section id="services">
    <h2>Notre catalogue de services</h2>
    <p class="intro">
        Cliquez sur une carte ou sur « Voir les détails » pour découvrir
        la présentation complète de chaque prestation.
    </p>
    <div class="catalogue">
        {cartes}
    </div>
    <p class="intro">
        Les prix affichés sont des prix de départ.
        Le tarif final est confirmé avant le début du travail.
    </p>
</section>

<section id="contact">
    <h2>Besoin d'informations ?</h2>
    <p class="intro">Contactez directement WUA SERVICE DIGITAL.</p>
    <a class="bouton"
       href="https://wa.me/{WHATSAPP}"
       target="_blank" rel="noopener">
       Nous écrire sur WhatsApp
    </a>
    <p>WhatsApp : 05 64 07 60 55</p>
</section>

<footer>
    WUA SERVICE DIGITAL — Services numériques
</footer>
</body>
</html>
"""


def creer_page_detail(service, index):
    nom = escape(service["nom"])
    description = escape(service["description"])
    prix = escape(service["prix"])
    image = escape(service["image"], quote=True)

    liste = "".join(
        f"<li>{escape(prestation)}</li>"
        for prestation in service["prestations"]
    )

    message = (
        "Bonjour WUA SERVICE DIGITAL, je souhaite commander : "
        + service["nom"]
    )
    lien_whatsapp = (
        "https://wa.me/" + WHATSAPP + "?text=" + quote(message)
    )

    precedent = f"service_{index - 1}.html" if index > 0 else "index.html"
    suivant = (
        f"service_{index + 1}.html"
        if index < len(SERVICES) - 1
        else "index.html"
    )

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{nom} | WUA SERVICE DIGITAL</title>
<style>
* {{ box-sizing: border-box; }}
body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: #08111f;
    color: white;
    line-height: 1.7;
}}
header {{
    padding: 20px 6%;
    background: #101d30;
    border-bottom: 2px solid #22d3ee;
}}
.logo {{ font-size: 22px; font-weight: bold; }}
.logo span {{ color: #22d3ee; }}
main {{ max-width: 1000px; margin: auto; padding: 30px 20px 50px; }}
.retour {{ color: #22d3ee; text-decoration: none; }}
h1 {{ color: #22d3ee; line-height: 1.25; }}
.photo {{
    width: 100%;
    max-height: 440px;
    object-fit: cover;
    border-radius: 15px;
    margin: 18px 0;
    background: #14243c;
}}
.panel {{
    background: #14243c;
    border: 1px solid #304765;
    border-radius: 15px;
    padding: 22px;
    margin-top: 22px;
}}
.prix {{ color: #ffda48; font-weight: bold; font-size: 22px; }}
li {{ margin: 8px 0; }}
.bouton {{
    display: inline-block;
    margin: 10px 8px 10px 0;
    padding: 12px 17px;
    border-radius: 9px;
    background: #25d366;
    color: #06220f;
    font-weight: bold;
    text-decoration: none;
}}
.secondaire {{ background: #243b59; color: white; }}
footer {{
    padding: 25px;
    text-align: center;
    border-top: 1px solid #304765;
    color: #bac7da;
}}
</style>
</head>
<body>
<header>
    <div class="logo">WUA <span>SERVICE DIGITAL</span></div>
</header>

<main>
    <a class="retour" href="index.html">← Retour au catalogue</a>

    <h1>{nom}</h1>
    <img class="photo" src="{image}" alt="Illustration : {nom}">

    <div class="panel">
        <h2>Présentation du service</h2>
        <p>{description}</p>
        <p>{escape(service["details"])}</p>
    </div>

    <div class="panel">
        <h2>Ce que nous proposons</h2>
        <ul>{liste}</ul>
        <p class="prix">{prix}</p>
        <p>
            Le prix final dépend de votre demande.
            Nous le confirmerons avant de commencer le travail.
        </p>
        <a class="bouton"
           href="{lien_whatsapp}"
           target="_blank" rel="noopener">
           Commander sur WhatsApp
        </a>
    </div>

    <p>
        <a class="bouton secondaire" href="{precedent}">
            ← Service précédent
        </a>
        <a class="bouton secondaire" href="{suivant}">
            Service suivant →
        </a>
    </p>
</main>

<footer>
    WUA SERVICE DIGITAL — WhatsApp : 05 64 07 60 55
</footer>
</body>
</html>
"""


def creer_site():
    os.makedirs(DOSSIER_SITE, exist_ok=True)

    # Créer la page d'accueil
    chemin_accueil = os.path.join(DOSSIER_SITE, "index.html")
    with open(chemin_accueil, "w", encoding="utf-8") as fichier:
        fichier.write(creer_page_accueil())

    # Créer une page de détails pour chaque service
    for index, service in enumerate(SERVICES):
        chemin = os.path.join(DOSSIER_SITE, f"service_{index}.html")
        with open(chemin, "w", encoding="utf-8") as fichier:
            fichier.write(creer_page_detail(service, index))

    # Ouvrir le catalogue dans le navigateur
    webbrowser.open("file://" + chemin_accueil)


def lancer():
    fenetre = tk.Tk()
    fenetre.title("WUA SERVICE DIGITAL")
    fenetre.geometry("440x280")
    fenetre.configure(bg="#08111f")

    tk.Label(
        fenetre,
        text="WUA SERVICE DIGITAL",
        font=("Arial", 20, "bold"),
        fg="#22d3ee",
        bg="#08111f"
    ).pack(pady=28)

    tk.Label(
        fenetre,
        text="Catalogue et pages détaillées des services",
        font=("Arial", 10),
        fg="white",
        bg="#08111f"
    ).pack(pady=5)

    tk.Button(
        fenetre,
        text="LANCER MON SITE",
        command=creer_site,
        bg="#25d366",
        fg="#06220f",
        font=("Arial", 13, "bold"),
        padx=15,
        pady=10
    ).pack(pady=22)

    fenetre.mainloop()


if __name__ == "__main__":
    lancer()
