<h1 id="sujet1"> <strong> IIHM - TP Cursor </strong> </h1>

## **Membres**

* [**Antoine Nollet**](mailto:antoine.nollet.etu@univ-lille.fr)

---

## **Sujet**

Le sujet suivant a guidé le travail effectué :

* [**Sujet**](https://www.thomaspietrzak.com/teaching/IHM/TP-pyqt3.html)

---

## **Sommaire**

* [**Contenu**](#contenu)
* [**Utilisation**](#Utilisation)
* [**Réponses aux Questions**](#réponses)
    * [**1e Etape: Démarrage**](#11)
    * [**2e Etape: classe Target**](#12)
    * [**3e Etape: classe BubbleWidget**](#13)
    * [**4e Etape: classe BubbleCursor**](#14)
    * [**5e Etape: programmer l'interaction**](#15)
    * [**6e Etape: Mesure du temps de selection de cible**](#16)
    * [**7e Etape: Selection "classique"**](#17)
    * [**8e Etape: RopeCursor**](#18)

---

<h2 id="contenu"> <strong> Contenu </strong> </h2>

* [**media**](./media/) : le dossier contenant des medias ressources utilisées lors du travail effectué
  * [**logo.png**](./media/logo.png) : le logo de l'application
  * [**src_tp_buble.csv**](media/src_tp_bubble.csv) : ressource permettant de créer le terrain de base
* [**src**](./src) : le dossier contenant les codes sources utilisées lors du travail effectué
  * [**mainWindow.py**](./src/mainWindow.py) : la fenêtre principale
  * [**NormalCursor.py**](./src/NormalCursor.py) : Curseur de base 
  * [**BubbleCursor.py**](./src/BubbleCursor.py) : Curseur Bulle, héritant de Curseur de base
  * [**RopeCursor.py**](./src/RopeCursor.py) : Curseur Corde, héritant de Curseur de base
  * [**HighLightCursor.py**](./src/HighLightCursor.py) : Curseur Distance (dans dessin pour relier la plus proche cible), héritant de Curseur de base
  * [**BubbleWidget.py**](./src/BubbleWidget.py) : fenêtre Bulle, utilisant le curseur bulle
  * [**NormalWidget.py**](./src/NormalWidget.py) : fenêtre utilisant le curseur de base, héritant de fenêtre bulle
  * [**Target.py**](./src/Target.py) : les cibles
* [**readme.md**](./readme.md) : le fichier que vous lisez actuellement
* [**main.py**](./main.py) : le code principal à exécuter pour constater le travail effectué.

---


<h2 id="Utilisation"> <strong> Utilisation </strong>  <a href="#init"> ↩️  </a> </h2>

Il y a 4 manières d'utiliser ce programme :

* avec aucun paramètre : cela mettra les paramètres de base (dimension 1024x800 et nom de fenêtre "BubbleCursor")
* avec 1 paramètre  : permet de choisir le nom de la fenêtre
* avec 2 paramètres : permet de choisir les dimensions de la fenêtre
* avec 3 paramètres : permet de choisir le nom de la fenêtre et les dimensions de la fenêtre

Une fois utilisé, vous pouvez switcher entre les modes d'utilisation grâce à la touche **ESPACE** ou la touche **M**. Il y a 3 modes : BubbleCursor, RopeCursor et NormalCursor. Dans les trois modes, un chronomètre est déclenché pour mesurer le temps mis pour cliquer sur la bulle rose parmi les bulles bleues.

---

<h2 id="réponses"> <strong> Réponses aux Questions </strong>  <a href="#init"> ↩️  </a> </h2>

---

<h3 id="11">  <strong> 1e Etape: Démarrage </strong>  <a href="#sujet1"> ↩️  </a> </h4>

Création de [**main.py**](main.py) et de [**./src/mainWindow.py**](./src/mainWindow.py) 

---

<h3 id="12">  <strong> 2e Etape: classe Target </strong>  <a href="#sujet1"> ↩️ </a> </h4>

Création de [**./src/Target.py**](./src/Target.py)

---

<h4 id="13"> <strong> 3e Etape: classe BubbleWidget </strong>  <a href="#sujet1"> ↩️ </a> </h4>


Création de [**./src/BubbleWidget**](./src/BubbleWidget)

---

<h3 id="14"> <strong> 4e Etape: classe BubbleCursor </strong>  <a href="#sujet1"> ↩️ </a> </h4>

Création de [**./src/BubbleCursor**](./src/BubbleCursor) (il héritera plus tard de NormalCursor)

---

<h3 id="15"> <strong> 5e Etape: programmer l'interaction </strong>  <a href="#sujet1"> ↩️ </a> </h4>

Ici [**./src/BubbleWidget**](./src/BubbleWidget) est modifié afin de pouvoir utiliser un cursor pour cliquer sur les cibles.

---

<h3 id="16"> <strong> 6e Etape: Mesure du temps de selection de cible </strong>  <a href="#sujet1"> ↩️ </a> </h4>

Ici [**./src/BubbleWidget**](./src/BubbleWidget) est modifié, quand on le crée on conserve le temps courant qu'on modifiera à chaque click de cible qui était à sélectionner. Le temps mis pour le click sera affiché en console. 

---

<h3 id="17"> <strong> 7e Etape: Selection "classique" </strong>  <a href="#sujet1"> ↩️ </a> </h4>

Création de [**./src/NormalWidget**](./src/NormalWidget) et de [**./src/NormalCursor**](./src/NormalCursor). NormalWidget a le même comportement que BubbleWidget (car nous voulons également pour mesurer le temps mis pour les clicks). Le code de BubbleCursor est transférer dans NormalCursor afin que BubbleCursor puisse hériter de NormalCursor et qu'il n'y ait plus que la fonction d'affichage qui soit à redéfinir.


---

<h3 id="18"> <strong> 8e Etape: RopeCursor </strong>  <a href="#sujet1"> ↩️ </a> </h4>


Création de [**./src/RopeCursor**](./src/RopeCursor) qui hérite de NormalCursor.

---


