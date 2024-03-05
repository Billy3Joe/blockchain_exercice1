# Travail à effectuer
▌Ecrire une fonction qui calcule le haché SHA-256 d’un message
▌Etendre la fonction précédente pour une prendre un “nonce” de 32 bits en
paramètre (la valeur du nonce est concaténée à la suite du message avant
de hacher le résultat)
▌Produire une fonction qui recherche un nonce produisant un haché dont les
N bits de poids fort sont tous égaux à 0
▪ Executer cette fonction au moins 10 fois avec les valeurs N=4, 8 et 12 pour un même
message, avec un nonce évoluant de façon incrémentale à partir de 0
▪ Etablir une statististique sur la valeur du nonce obtenu pour chaque N
▪ Qu’observez-vous sur cette statistique ?
▪ Etait-ce previsible ?
▪ A quoi cela peut-il servir ?

## Resultats
N=4:
Nonce values: [2784046573, 3041036670, 2555091487, 1191571167, 3040054679, 4015047471, 4008083049, 2867578734, 1856260566, 4194916056]
Number of nonces: 10
Average nonce: 2955368645.2
Standard deviation of nonce: 960232355.3533636

## Statistiques
Pour
N=4
Nombre de nonces : 10
Moyenne du nonce : 2955368645.2
Écart type du nonce : 960232355.3533636

## Qu’observez-vous sur cette statistique ?
Dans cette

statistique, nous observons les valeurs des nonces générées pour N=4, ainsi que des mesures de centralité et de dispersion, à savoir la moyenne et l'écart-type.

-->Nonce values: Il s'agit des valeurs des nonces générées pour N=4 lors de l'exécution de l'algorithme de recherche de nonce. Chaque nonce est un entier qui satisfait la condition spécifiée, où les 4 bits de poids fort sont égaux à zéro.

-->Number of nonces: Il indique le nombre total de nonces générées pour N=4, dans ce cas, il y en a 10.

-->Average nonce: C'est la moyenne des valeurs des nonces. Dans ce cas, la moyenne est d'environ 2955368645.2. Cela signifie que, en moyenne, les nonces générés ont une valeur proche de cette moyenne.

-->Standard deviation of nonce: C'est une mesure de la dispersion des valeurs des nonces par rapport à la moyenne. Dans ce cas, l'écart-type est d'environ 960232355.3533636. Cela indique la variabilité des valeurs des nonces autour de la moyenne. Plus l'écart-type est élevé, plus les valeurs des nonces sont dispersées autour de la moyenne.

En résumé, cette statistique nous fournit des informations sur la distribution des valeurs des nonces générées pour N=4, ainsi que sur la tendance centrale (moyenne) et la dispersion (écart-type) de ces valeurs.

## Etait-ce previsible ?
La prévisibilité dépend de la manière dont l'algorithme de recherche de nonce est conçu et de la nature aléatoire des nonces générés. Dans le cadre de cet exercice, l'algorithme utilise la fonction secrets.token_bytes() pour générer des nonces aléatoires de 32 octets (256 bits). Cependant, la fonction de hachage SHA-256 utilisée est déterministe, ce qui signifie que pour une paire donnée de message et de nonce, le haché généré sera toujours le même.

Cependant, la distribution des valeurs des nonces générés peut ne pas être uniforme en raison de la nature de la génération de nombres aléatoires. Dans certains cas, certaines valeurs de nonce peuvent être plus fréquentes que d'autres, ce qui peut affecter la moyenne et l'écart-type des nonces générés.

En résumé, bien que le comportement précis des nonces générés puisse ne pas être prévisible dans chaque exécution, il est raisonnable de s'attendre à ce que la moyenne et l'écart-type des nonces générés fluctuent autour de certaines valeurs, en fonction de la distribution des nombres aléatoires générés par la fonction secrets.token_bytes().

## A quoi cela peut-il servir ?
La génération de nonces avec des bits de poids fort égaux à zéro est un élément clé dans de nombreux protocoles cryptographiques et systèmes décentralisés, en particulier dans le domaine de la blockchain. Voici quelques utilisations courantes de cette technique :

1. **Preuve de travail (Proof of Work) :** Dans les blockchains comme Bitcoin et Ethereum, les mineurs doivent résoudre un problème de preuve de travail pour ajouter un nouveau bloc à la chaîne. Ce problème implique de trouver un nonce de sorte que le haché du bloc satisfasse une condition spécifique, généralement que les N bits de poids fort soient nuls. Cette preuve de travail garantit que l'ajout de blocs à la chaîne nécessite un travail computationnel important, ce qui rend difficile la modification de l'historique des transactions.

2. **Cryptographie :** La génération de nonces avec des bits de poids fort égaux à zéro est utilisée dans de nombreux protocoles cryptographiques pour garantir la sécurité et l'intégrité des données. Par exemple, dans le protocole de signature numérique DSA (Digital Signature Algorithm), des valeurs aléatoires appelées "k" sont utilisées dans le calcul de la signature, et il est important que ces valeurs ne soient pas prévisibles.

3. **Sécurité des communications :** Dans certains protocoles de communication sécurisée, des nonces sont utilisés pour éviter la répétition des messages et pour assurer l'authenticité et l'intégrité des données échangées entre les parties.

En résumé, la génération de nonces avec des bits de poids fort égaux à zéro est un mécanisme fondamental dans de nombreux domaines de la cryptographie et des systèmes décentralisés, et elle est essentielle pour assurer la sécurité et la fiabilité des systèmes.
