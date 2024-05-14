1. Installation de Python
2. Environnement virtuel
    - Ajouter un environnemennt:
        - Windows :
            >>> mkdir myproject
            >>> cd myproject
            >>> py -3 -m venv .venv
        - Mac Os:
            $ mkdir myproject
            $ cd myproject
            $ python3 -m venv .venv
    - Activer l'environnement:
        - Windows :
            >>> .venv\Scripts\activate
        - Mac Os:
            $ . .venv/bin/activate
    - Desactiver l'environnement:
        >>> deactivate
3. Installation de Flask:
    >>> pip install Flask