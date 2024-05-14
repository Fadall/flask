1. __Structure:__
    - les templates sont dans un dossier nommés *templates*
    - les vues retourne *render_template('vue.html')*
2. __Variable de template:__
    -> dans le fichier .py
    >>> render_template('vue,html',varName=value )
    -> dans le template:
    >>> {{ varName }}
3. __Boucle & Condition:__
    - Utilisation de la syntaxe *{%...%}*
        - FOR :
        >>>{%for item in items%}
        >>>...
        >>>{%endfor%}
        - IF :
        >>>{%if ...%}
        >>>...
        >>>{%endif%}
4. __Heritage de template:__
    - Utilisation des sythaxes : *{% extend "..." %}* & *{% block %}*
    - Include : 
            - {% include "...." %}
            - {% include "...." ignore missing %}
            - {% include ["...","...","..."] ignore missing %}
5. __url_for():__
    - url_for('routeFunctionName')
        Ex: <a href="{{ url_for('routeFunctionName') }}"></a>
    - Fichier statique (image par exemple):
        - url_for('static',filename='file.jpeg')
        Ex: <a href="{{ url_for('static',filename='toto.png ') }}"></a>
6. __Formulaire de template:__
    -> Dans le fichier template:
        - Nommer les champs 
        - action="{{url_for('...')}}"
    -> Dans le fichier .py:
    >>>from flask import Flask, render_template, request
    >>>fieldValue = request.args.get('fieldName')
7. __Page 404:__
    >>>@app.errorhandler(404)
    >>>def page_not_found(e):
    >>>    return render_template('404.html'), 404
 



