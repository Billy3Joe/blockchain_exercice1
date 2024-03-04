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
Pour
N=4:
Nonce values: [33758243466888279705828089888309479652595586169484381006374058978548197436730, 24866815114152202846915193371796421574632798908860705089610775857560223813105, 104631843221669048065967907324211032004241577607539153572450888958808276786271, 11998129597221911751413740809087911975624790050356329959498507740509759771468, 102630109954800677648835614269497316920159362154999081857845683233442287621204, 55257113997024033325167375489183170291324251253753620091009248711311856771986, 112122414971820790864792122798520041657947693546181297701076580464176293532324, 45509898320682839106644878261273440751457999751230559500708084194823626808333, 74980838719931592521856239668375054227600821251901660241250126294949884710486, 58089948727522973485906819111423116678422061650666502476074918200762959790278]
Number of nonces: 10
Average nonce: 6.238453560917143e+76
Standard deviation of nonce: 3.520873567922268e+76

## Statistiques
Pour
N=4
Nombre de nonces : 10
Moyenne du nonce : 6.238453560917143e+76
Écart type du nonce : 3.520873567922268e+76

## Qu’observez-vous sur cette statistique ?
Sur la statistique pour N=4, on observe ce qui suit :

Nonce values : Les nonces générés sont des entiers très grands, représentés en notation scientifique. Cela est dû à la conversion des nonces hexadécimales en entiers pour cette valeur de N.

Nombre de nonces : Il y a 10 nonces générés dans cet exemple.

Moyenne du nonce : La moyenne du nonce est un nombre extrêmement grand en notation scientifique. Cela montre la distribution des nonces générés, qui sont généralement très dispersés compte tenu de la nature aléatoire de la génération de nonces.

Écart type du nonce : L'écart type du nonce est également très élevé en notation scientifique, indiquant la dispersion ou la variabilité des nonces générés par rapport à la moyenne. Cela signifie que les nonces sont très dispersés autour de la moyenne.

En résumé, pour N=4, les nonces générés ont une distribution très large et sont dispersés sur une plage de valeurs très étendue. Cela est attendu car la génération de nonces est un processus aléatoire, et les nonces générés peuvent être très grands en raison de la taille de l'espace de recherche.

## Etait-ce previsible ?
Oui, il était prévisible que les nonces générés pour N=4 auraient une grande dispersion et seraient des nombres très grands. Voici pourquoi :

▪Nature aléatoire de la recherche du nonce : La recherche d'un nonce valide implique un processus aléatoire où des nonces sont générés de manière aléatoire jusqu'à ce qu'un nonce valide soit trouvé. Comme la recherche est aléatoire, les nonces générés peuvent être très dispersés sur une plage de valeurs.

▪Taille de l'espace de recherche : Pour N=4, le nombre de combinaisons possibles de nonces est très grand en raison de la longueur du nonce. Cela signifie qu'il existe un grand nombre de nonces potentiels parmi lesquels choisir, ce qui augmente la probabilité d'obtenir des nonces très grands et dispersés.

▪Effet de la taille du nonce : Pour cette implémentation, les nonces sont convertis en entiers à partir de leur représentation hexadécimale. Comme les nonces sont des chaînes hexadécimales de 32 caractères, leur conversion en entiers conduit à des nombres très grands.

En résumé, étant donné la nature aléatoire de la recherche du nonce, la taille de l'espace de recherche et la méthode de conversion des nonces en entiers, il était prévisible que les nonces générés pour N=4 seraient des nombres très grands et auraient une grande dispersion.

## A quoi cela peut-il servir ?
La génération de nonces avec des contraintes de preuve de travail, telles que trouver un nonce produisant un haché avec un certain nombre de bits de poids forts égaux à zéro, est une composante essentielle des systèmes de blockchain et de cryptomonnaie comme Bitcoin. Voici quelques utilisations et implications de cette pratique :

▪Sécurité du réseau : La preuve de travail est utilisée pour sécuriser le réseau en rendant la création de nouveaux blocs de transaction coûteuse en termes de temps et de ressources informatiques. Cela rend difficile pour les attaquants de modifier rétroactivement les blocs précédents, garantissant ainsi l'intégrité de la blockchain.

▪Consensus distribué : La preuve de travail permet d'atteindre un consensus distribué sur l'état du registre dans un réseau décentralisé. Les mineurs travaillent pour résoudre des problèmes de preuve de travail afin de valider et d'ajouter de nouveaux blocs à la blockchain, ce qui nécessite un consensus sur l'ensemble du réseau.

▪Récompense des mineurs : Les mineurs qui réussissent à trouver un nonce valide et à résoudre le problème de preuve de travail sont récompensés par l'attribution de nouvelles unités de cryptomonnaie, ainsi que par les frais de transaction associés aux transactions incluses dans le bloc.

▪Contrôle de l'émission monétaire : Dans certaines cryptomonnaies, comme Bitcoin, la génération de nouveaux blocs est également associée à la création de nouvelles unités de cryptomonnaie, ce qui permet de contrôler l'offre totale de monnaie et d'implémenter une politique monétaire déflationniste.

▪Résistance aux attaques sybil : La preuve de travail rend difficile pour un attaquant de créer de multiples identités (nœuds) sur le réseau et de prendre le contrôle de la majorité du pouvoir de calcul, ce qui pourrait compromettre la sécurité du réseau.

En résumé, la génération de nonces avec des contraintes de preuve de travail est un mécanisme crucial pour garantir la sécurité, la résistance aux attaques et le consensus distribué dans les systèmes de blockchain et de cryptomonnaie.
