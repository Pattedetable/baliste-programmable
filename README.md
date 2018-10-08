# Baliste programmable

![screenshot](https://raw.githubusercontent.com/Pattedetable/baliste-programmable/master/screenshot.png)

Le fichier utilisé pour démarrer le programme est ```baliste.py```.

## Utilisation

Afin d'utiliser ce programme, vous aurez besoin des logiciels suivants :

  * Python 3
  * Arduino IDE

Si vous utilisez Linux, Python sera généralement déjà installé.  Si ce n'est pas déjà fait, vous pouvez installer Python 3 à partir des dépôts de logiciels de votre distribution.  Que vous utilisiez Linux, MacOS ou Windows, vous pouvez aussi installer Python à partir du [site officiel](https://www.python.org/).  Sélectionnez ensuite le paquet correspondant à votre système d'exploitation.

Arduino IDE est peut-être disponible dans les dépôts de votre distribution Linux.  Sinon, il est aussi disponible sur le [site web d'Arduino](https://www.arduino.cc/en/Main/Software), que ce soit pour Linux, MacOS ou Windows.

Vous aurez aussi besoin des modules Python suivants :

  * PyQt5

Si vous utilisez Linux, il est fort probable qu'ils se trouvent dans les dépôts logiciels de votre distribution.

Pour tous les systèmes d'exploitation supportés, à partir de la version 3.4, Python inclus de plus `pip`, un gestionnaire de paquet qui permet d'installer des modules pour Python.  Pour vérifer la version de Python installée sur votre système, ouvrez un terminal (Linux, MacOS) ou une invite de commande (Windows) et tappez :

```python --version```

Si le numéro de version affiché à l'écran commence par 2, dans tout ce qui suit, utilisez `python3` au lieu de `python`, et `pip3` au lieu de `pip`.

Vous pouvez vous servir de `pip` pour installer les divers modules nécessaires.  Par exemple, pour installer PyQt5, entrez dans un terminal (ou invite de commande) :

```pip install PyQt5```

Une fois ces modules installés, dans le terminal sous Linux et MacOS ou l'invite de commande sous Windows, entrez :

```python baliste.py```

Sous Windows, vous pouvez aussi double-cliquer sur le fichier ```baliste.py```.

### License

Le programme est distribué sous la licence GNU GPLv3.  Pour le texte complet, référez-vous au fichier `LICENSE`.
La version courte de cette licence est que vous êtes libre d'utiliser ce logiciel, d'en modifier le code source, ainsi que de le redistribuer, que ce soit sous sa version originale ou modifiée.  Cependant, vous devez donner ces mêmes droits aux personnes qui utiliseront votre logiciel redistribué.

Le code source est disponible sur [GitHub](https://github.com/Pattedetable/baliste-programmable).
