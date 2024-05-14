0. __Rappel:__
    - Les Fonctions :
        >>>Definir une fonction dans une fonction
        >>>Retourner une fonction
        >>>Passer une fonction en parametre
    - Les decorateurs :
        - fonction a decorer est passee a une fonction (A) qui prend en parametre une fonction,
        - La fonction (A) definie une fonction (B) qui :
            - Excecute du code
            - Appel la fonction passee en parametre
            - Execute du code
        - La fonction (A) retourne la fonction (B) 
    - Les modules :
    - Les Packages :



1. __Hello world application__
2. __Les routes:__
    - Route simple:
        >>> @app.route('/endPoint')
    - Route dynamique: 
        >>> @app.route('/endPoint/<param>')
            def function(param):
                pass
    - Exercice : y-iful
    - Les converters:
        >>> @app.route('/post/<TYPE:variable>')
        TYPE => - int
                - float
                - string
                - path
                - uuid





