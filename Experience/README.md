<h1 id="sujet1"> <strong> IIHM - Programmation d'une expérience contrôlée </strong> </h1>

## **Membres**

* [**Antoine Nollet**](mailto:antoine.nollet.etu@univ-lille.fr)

---

## **Sujet**

Le sujet suivant a guidé le travail effectué :

* [**Sujet**](https://thomaspietrzak.com/teaching/IHM/TP-expe.html)

---

## **Sommaire**

* [**Contenu**](#contenu)
* [**Utilisation**](#Utilisation)
* [**Réponses aux Questions**](#réponses)
    * [**Boîte de dialogue de setup**](#11)
    * [**Génération aléatoire des cibles**](#12)
    * [**Le gestionnaire d'expérience**](#13)
    * [**Déroulement de l'expérience contrôlée**](#14)

---

<h2 id="contenu"> <strong> Contenu </strong> </h2>

* [**media**](./media/) : le dossier contenant des medias ressources utilisées lors du travail effectué
  * [**logo.png**](./media/logo.png) : le logo de l'application
  * [**resultats**](./media/resultats/) : le dossier contenant les resultats des expériences
    * **experience_(method)_(densite)_(size)_(minspace).csv** : fichier de résultat d'expérience de la méthode (method) avec une densitée (densite) de cibles de taille (size) espacées d'une distance d'au moins (minspace)
  * [**sequences**](./media/sequences/) : le dossier contenant les sequences d'execution des cibles
    * **sequence_(densite)_(size)_(minspace).csv** : sequence d'execution des cibles
  * [**terrains**](./media/terrains/) : le dossier contenant les terrains de cibles
    * **cibles_(densite)_(size)_(minspace).csv** : terrain de cibles d'une densitée (densite) de taille (size) espacées d'une distance d'au moins (minspace)
* [**src**](./src) : le dossier contenant les codes sources utilisées lors du travail effectué
  * [**Cursor**](./src/Cursor/) : dossier contenant les fichiers sources permettant d'effectuer l'expérience de curseur
  * [**Experience**](./src/Experience/) : dossier contenant les fichiers sources permettant de contrôler les expériences
  * [**mainWindow.py**](./src/mainWindow.py) : la fenêtre principale
* [**readme.md**](./readme.md) : le fichier que vous lisez actuellement
* [**compte-rendu.md**](compte-rendu.md) : le fichier de compte-rendu de l'expérience contrôlée
* [**compte-rendu.pdf**](compte-rendu.pdf) : le fichier de compte-rendu de l'expérience contrôlée
* [**main.py**](./main.py) : le code principal à exécuter pour constater le travail effectué.

---


<h2 id="Utilisation"> <strong> Utilisation </strong>  <a href="#init"> ↩️  </a> </h2>

Il y a 4 manières d'utiliser ce programme :

* avec aucun paramètre : cela mettra les paramètres de base (dimension 1024x800 et nom de fenêtre "BubbleCursor")
* avec 1 paramètre  : permet de choisir le nom de la fenêtre
* avec 2 paramètres : permet de choisir les dimensions de la fenêtre
* avec 3 paramètres : permet de choisir le nom de la fenêtre et les dimensions de la fenêtre



---

<h2 id="réponses"> <strong> Réponses aux Questions </strong>  <a href="#init"> ↩️  </a> </h2>

---

Vous pouvez consulter le [**compte-rendu.md**](compte-rendu.md) pour obtenir les réponses aux questions.

