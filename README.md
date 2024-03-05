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

## Resultat 
### N=4:
Message 1: a5e8f455b92bfd6987c53d9ba1811702
Nonce: 4977816020282032379

Message 2: 61a9ace0041632bb74c89b00cafff4ad
Nonce: 9022644149268952846

Message 3: fc6b6a666a37d10984d076b98cc82076
Nonce: 16324191791992681910

Message 4: fea4cedc3711c4126b5b0b30244bc47e
Nonce: 2250530014917910904

Message 5: fb73c831ffa33936f2af0b881525c5e1
Nonce: 7550639824035030247

Message 6: 6b8a6d19e15bc535a2725eed376b3637
Nonce: 14041684320673350041

Message 7: 01f5bf20c863537eb205f324edc8ea61
Nonce: 14066995968442975521

Message 8: 70eb9aa95f4c2559a9042ab0820df681
Nonce: 18293689997059580449

Message 9: a0dd23af9121bb33de19863321b23e01
Nonce: 10874315406050367309

Message 10: c4292b70ccce924a34537c414e6330ff
Nonce: 12914659356917088389

### N=8:
Message 1: 3f1c1c9a6e6d46d7620ee4d950b2a1f3
Nonce: 2848226229064289982

Message 2: d02a1d851d8f35e5879c1771b11861cf
Nonce: 9103038440458737204

Message 3: 76f4714d718830ff8155142305c1c608
Nonce: 7029127771340769752

Message 4: 9dc9f3b05af241de94cb9256a31719ef
Nonce: 519454478110732674

Message 5: d358a639460c1667258b12f3ba0839e1
Nonce: 16464373774324786716

Message 6: b3e420b16e20d9e26bad8ad727b083d9
Nonce: 15108264695990887441

Message 7: 92575be65439d9e837598007fbcc7134
Nonce: 4813714907640488850

Message 8: 74382406881efe28078d5c73da56a6bd
Nonce: 13447366261043926248

Message 9: 95c4d61d94749e4bcf44ec7cac158e7c
Nonce: 17457088163814806028

Message 10: 7eb1b63c221f8f075234b77918972f70
Nonce: 6243707511350494278

### N=12:
Message 1: 8dcaf914d396bb8111701aa16bd44d1d
Nonce: 9444291998022727180

Message 2: 0d15435d52d0f0b23d42d12edb6b5b99
Nonce: 10201793660801297605

Message 3: 8a4e1fba318c8b6ea5aac4b6d7ab8e76
Nonce: 984523843501367090

Message 4: 9243e0fda027d0d9e50d2e418f65efd4
Nonce: 12450155819312294682

Message 5: c3938160df814904e68fb33641589b02
Nonce: 14536071449205300043

Message 6: 07b55cf4e1a0644d24c677d30da3efd4
Nonce: 2273386765925576249

Message 7: fc725cbdc6b85eac3e45f2b2fad25080
Nonce: 11967399356732819950

Message 8: d1838e89a7a989beff8afe524539b3ed
Nonce: 17950653591956081699

Message 9: 2d159df21fb0ee39ab475ad37c8a3e5b
Nonce: 16211233347607985871

Message 10: 12e1246de3d31ac11db72ea205caef1b
Nonce: 12341295630076131646

## Statistiques
N=4:
Number of nonces: 10
Average nonce: -36329759261733968.00
Standard deviation of nonce: 11972465769413809939265778643313360896.00

N=8:
Number of nonces: 10
Average nonce: 80064186459216112.00
Standard deviation of nonce: 9633695616791857729435899158287351808.00

N=12:
Number of nonces: 10
Average nonce: -231965897911572800.00
Standard deviation of nonce: 10930449399384587352500418627005054976.00

## Qu’observez-vous sur cette statistique ?
Dans ces statistiques, nous observons que pour chaque valeur de N (le nombre de zéros de poids fort dans le haché SHA-256), les moyennes des nonces sont assez différentes, avec des écarts de plusieurs ordres de grandeur. De plus, les écarts-types des nonces sont également très élevés, ce qui indique une dispersion importante des valeurs autour de la moyenne.

Cela suggère que la recherche de nonce pour obtenir un haché avec un certain nombre de zéros de poids fort est un processus aléatoire et que les valeurs des nonces peuvent varier considérablement même pour le même nombre de zéros de poids fort.

## Etait-ce previsible ?
Oui, cette observation était prévisible. Lorsque nous recherchons des nonces pour obtenir un haché avec un certain nombre de zéros de poids fort, nous effectuons essentiellement une recherche aléatoire. Chaque nonce généré est une tentative aléatoire pour trouver un haché qui satisfait les conditions requises.

## A quoi cela peut-il servir ?
La recherche de nonces pour obtenir un haché avec un certain nombre de zéros de poids fort est souvent utilisée dans le contexte de la preuve de travail (Proof of Work), qui est largement utilisée dans les systèmes de blockchain, notamment dans le minage de nouvelles unités de cryptomonnaies telles que le Bitcoin.

Cette méthode permet de créer une condition difficile à satisfaire mais facile à vérifier. Les mineurs doivent rechercher une solution (le nonce) qui, une fois ajoutée aux données du bloc, produit un haché avec un certain nombre de zéros de poids fort. Cela nécessite un processus itératif et intensif en calcul, mais une fois que le nonce est trouvé, il est facile pour les autres participants du réseau de vérifier que le haché satisfait la condition.

Cela garantit que la création de nouveaux blocs dans la blockchain est un processus coûteux en termes de ressources de calcul, ce qui contribue à sécuriser le réseau et à prévenir les attaques malveillantes.
