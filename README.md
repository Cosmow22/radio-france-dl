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

Par exemple : 

```
rfdl https://www.radiofrance.fr/franceculture/podcasts/la-conversation-scientifique/faut-il-bouleverser-l-organisation-de-la-recherche-scientifique-7688303
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