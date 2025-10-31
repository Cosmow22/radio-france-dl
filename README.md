# Radiofrance Podcasts Scrapper

Un CLI simple qui permet de télécharger un ou plusieurs podcasts de <https://www.radiofrance.fr/>.

## Utilisation

Installer rfscrapper :

```batch
pip install rfscrapper
```


Télécharger un podcast :

```
rfscrapper lien
```

Ou plusieurs podcasts en même temps en allant à la ligne :

```
rfscrapper "lien1
lien2
"
```

Par défaut, le podcast se télécharge dans le dossier courant. Pour spécifier le dossier cible, utiliser l'argument optionel output comme ça :

```
rfscrapper lien --output "C:\Users\Marc\Desktop/podcasts"
```

## License

Ce projet est sous la license MIT. Soyer libre d'utiliser le code comme vous le voulez !