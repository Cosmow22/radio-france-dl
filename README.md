# Radiofrance Podcast Downloader

Un CLI simple qui permet de télécharger un ou plusieurs podcasts de <https://www.radiofrance.fr/>.

## Utilisation

Installer radio-france-dl :

```batch
pip install rfdl
```


Télécharger un podcast :

```
rfdl lien
```

Ou plusieurs podcasts en même temps en allant à la ligne :

```
rfdl "lien1
lien2
"
```

Par défaut, le podcast se télécharge dans le dossier courant. Pour spécifier le dossier cible, utiliser l'argument optionel output comme ça :

```
rfdl lien --output "C:\Users\Marc\Desktop/podcasts"
```

## Licence

Ce projet est sous la license MIT. Soyer libre d'utiliser le code comme vous le voulez !