# ToDoList_SN

## Description

ToDoList_SN est une application de gestion de tâches réalisée avec Django. Elle permet aux utilisateurs de créer, modifier et supprimer des tâches à faire.

## Installation

1. Assurez-vous d'avoir Python installé sur votre système. Vous pouvez le télécharger depuis [python.org](https://www.python.org/).

2. Clonez ce dépôt sur votre machine locale en exécutant la commande suivante dans votre terminal :
    ```
    git clone https://github.com/Moisekonan/TodoList_SN.git
    ```

3. Accédez au répertoire de l'application ToDoList_SN :
    ```
    cd ToDoList_SN
    ```

4. Créez un environnement virtuel pour l'application :
    ```
    python3 -m venv venv
    ```

5. Activez l'environnement virtuel :
- Sur Windows :
  ```
  venv\Scripts\activate
  ```
- Sur macOS et Linux :
  ```
  source venv/bin/activate
  ```

6. Installez les dépendances requises :
    ```
    pip3 install -r requirements.txt
    ```


## Configuration
1. Assurez-vous que votre base de données est configurée dans le fichier `settings.py`. Par défaut, l'application est configurée pour utiliser SQLite.

2. Appliquez les migrations pour créer les tables de la base de données :
    ```
    python3 manage.py migrate
    ```

## Lancement de l'application
1. Lancez le serveur de développement Django en exécutant la commande suivante :
    ```
    python3 manage.py runserver
    ```