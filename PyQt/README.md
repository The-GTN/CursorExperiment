<h1 id="init"> <strong> IIHM - TP PyQt </strong> </h1>

## **Membres**

* [**Antoine Nollet**](mailto:antoine.nollet.etu@univ-lille.fr)

---

## **Sujets**

Les sujets suivants ont guidé le travail effectué :

* [**Sujet 1**](https://www.thomaspietrzak.com/teaching/IHM/TP-pyqt1.html)
* [**Sujet 2**](https://www.thomaspietrzak.com/teaching/IHM/TP-pyqt2.html)

---

## **Sommaire**

* [**Contenu**](#contenu)
* [**Réponses aux Questions**](#réponses)
    * [**Sujet 1**](#sujet1)
        * [**1e Etape: Démarrage**](#11)
        * [**2e Etape: Créer une classe MainWindow**](#12)
        * [**3e Etape: rajouter des widgets à MainWindow**](#13)
        * [**4e Etape: définir et connecter les slots**](#14)
        * [**5e Etape: ouvrir une boîte de dialogue pour sélectionner un fichier**](#15)
        * [**6e Etape: ouvrir / sauver une page HTML**](#16)
        * [**7e Etape: ouvrir une boîte de dialogue pour demander confirmation**](#17)
        * [**8e Etape: demander confirmation dans tous les cas**](#18)
    * [**Sujet 2**](#sujet2)
        * [**Exercice 1 : dessiner un bouton**](#21)
            * [**1e Etape: Démarrage**](#211)
            * [**2e Etape: Classe CanvasButton**](#212)
            * [**3e Etape: Classe ButtonModel**](#213)
            * [**4e Etape: synchroniser ButtonModel et CanvasButton**](#214)
        * [**Exercice 2 : Zone de dessin**](#22)
            * [**1e Etape: Créer un nouveau projet affichant une zone de dessin**](#221)
            * [**2e Etape: créer une classe Trace**](#222)
            * [**3e Etape: dessiner un tracé interactivement**](#223)
            * [**4e Etape: spécifier des attributs graphiques**](#224)
            * [**5e Etape: choisir interactivement les attributs graphiques**](#225)
            * [**6e Etape: mettre à jour l'affichage du bouton qui permet de choisir la couleur**](#226)

---

<h2 id="contenu"> <strong> Contenu </strong> </h2>

* [**media**](./media/) : le dossier contenant des medias ressources utilisées lors du travail effectué
    * [**logo.png**](./media/logo.png) : image logo de l'application
    * [**copy.png**](./media/copy.png) : image de copie
    * [**cut.png**](./media/cut.png) : image de coupage
    * [**new.png**](./media/new.png) : image de création
    * [**open.png**](./media/open.png) : image d'ouverture
    * [**paste.png**](./media/paste.png) : image de collage
    * [**quit.png**](./media/quit.png) : image de sortie
    * [**save.png**](./media/save.png) : image de sauvegarde
* [**src**](./src) : le dossier contenant les codes sources utilisées lors du travail effectué
    * [**dessin.py**](./src/dessin.py) : le dessin effectué (facultatif)
    * [**mainWindow.py**](./src/mainWindow.py) : la fenêtre principale
* [**readme.md**](./readme.md) : le fichier que vous lisez actuellement
* [**main.py**](./main.py) : le code principal à exécuter pour constater le travail effectué.

---

<h2 id="Utilisation"> <strong> Utilisation </strong>  <a href="#init"> ↩️  </a> </h2>

Il y a 4 manières d'utiliser ce programme :

* avec aucun paramètre : cela mettra les paramètres de base (dimension 1024x800 et nom de fenêtre "TPs PyQts")
* avec 1 paramètre  : permet de choisir le nom de la fenêtre
* avec 2 paramètres : permet de choisir les dimensions de la fenêtre
* avec 3 paramètres : permet de choisir le nom de la fenêtre et les dimensions de la fenêtre

---

<h2 id="réponses"> <strong> Réponses aux Questions </strong>  <a href="#init"> ↩️  </a> </h2>

---

<h3 id="sujet1"> <strong> Sujet 1 </strong>  <a href="#init"> ↩️  </a> </h3>

---

<h4 id="11">  <strong> 1e Etape: Démarrage </strong>  <a href="#sujet1"> ↩️  </a> </h4>

Je ne comprend pas la question de ce qu'il faut rajouter pour exécuter le programme. Le print affiche : "['mainWindow.py']" , ce qui correspond à la liste des arguments passées à la commande python3. Il n'y a pas eu d'options entrées, donc cette liste n'est constituée que du nom du fichier exécuté par la commande python3. 

---

<h4 id="12">  <strong> 2e Etape: Créer une classe MainWindow </strong>  <a href="#sujet1"> ↩️ </a> </h4>

Classe MainWindow créée dans le fichier [mainWindow.py](./src/mainWindow.py). Attention : il faut penser à appeler le constructeur de la super classe !

---

<h4 id="13"> <strong> 3e Etape: rajouter des widgets à MainWindow </strong>  <a href="#sujet1"> ↩️ </a> </h4>

Ajout des QActions et des Bars (menuBar, toolBar et statusBar)

---

<h4 id="14"> <strong> 4e Etape: définir et connecter les slots </strong>  <a href="#sujet1"> ↩️ </a> </h4>

Ajout des fonctions associées aux QActions. Les QActions ont déjà un pyqtSignal qui est self.triggered, il faut donc appeler self.triggered.connect aux fonctions auxquelles on veut associer les QActions. 

---

<h4 id="15"> <strong> 5e Etape: ouvrir une boîte de dialogue pour sélectionner un fichier </strong>  <a href="#sujet1"> ↩️ </a> </h4>

Boite de dialogue OK.

---

<h4 id="16"> <strong> 6e Etape: ouvrir / sauver une page HTML </strong>  <a href="#sujet1"> ↩️ </a> </h4>

Utilisation boite de dialogue OK. Pour pouvoir accéder au textEdit il suffir de le mettre en attribut de la window.

---

<h4 id="17"> <strong> 7e Etape: ouvrir une boîte de dialogue pour demander confirmation </strong>  <a href="#sujet1"> ↩️ </a> </h4>

Utilisation de QMessageBox OK.

---

<h4 id="18"> <strong> 8e Etape: demander confirmation dans tous les cas </strong>  <a href="#sujet1"> ↩️ </a> </h4>

Au final la fonction quit ne fera qu'un self.close(), et c'est dans la redéfinition de la fonction closeEvent qu'on 
utilisera un QMessageBox pour ignorer ou non l'évènement.

---


<h3 id="sujet2"> <strong> Sujet 2 </strong> <a href="#init"> ↩️  </a> </h3>

Non fait pour le moment...

---

<h4 id="21"> <strong> Exercice 1 : dessiner un bouton </strong>  <a href="#sujet2"> ↩️ </a> </h4>

---

<h5 id="211"> <strong> 1e Etape: Démarrage </strong>  <a href="#sujet2"> ↩️ </a> </h5>

---

<h5 id="212"> <strong> 2e Etape: Classe CanvasButton </strong>  <a href="#sujet2"> ↩️ </a> </h5>

---

<h5 id="213"> <strong> 3e Etape: Classe ButtonModel </strong>  <a href="#sujet2"> ↩️ </a> </h5>

---

<h5 id="214"> <strong> 4e Etape: synchroniser ButtonModel et CanvasButton </strong>  <a href="#sujet2"> ↩️ </a> </h5>

---


<h4 id="22"> <strong> Exercice 2 : Zone de dessin </strong>  <a href="#sujet2"> ↩️ </a> </h4>

---

<h5 id="221"> <strong> 1e Etape: Créer un nouveau projet affichant une zone de dessin </strong>  <a href="#sujet2"> ↩️ </a> </h5>

---

<h5 id="222"> <strong> 2e Etape: créer une classe Trace </strong>  <a href="#sujet2"> ↩️ </a> </h5>

---

<h5 id="223"> <strong> 3e Etape: dessiner un tracé interactivement </strong>  <a href="#sujet2"> ↩️ </a> </h5>

---

<h5 id="224"> <strong> 4e Etape: spécifier des attributs graphiques </strong>  <a href="#sujet2"> ↩️ </a> </h5>

---

<h5 id="225"> <strong> 5e Etape: choisir interactivement les attributs graphiques </strong>  <a href="#sujet2"> ↩️ </a> </h5>

---

<h5 id="226"> <strong> 6e Etape: mettre à jour l'affichage du bouton qui permet de choisir la couleur </strong>  <a href="#sujet2"> ↩️ </a> </h5>

---


