# TokenizeArt

## Introduction

La blockchain est une technologie qui permet d'enregistrer des transactions de manière immuable et transparente, assurant ainsi sécurité et confiance dans les échanges. Elle repose sur plusieurs principes fondamentaux qui en font un outil puissant pour divers secteurs.

Les bases de la blockchain reposent sur la cryptographie à clé publique, qui garantit la confidentialité des transactions, ainsi qu’un réseau décentralisé qui favorise l’indépendance vis-à-vis d’autorités centrales. Chaque transaction est intégrée dans un bloc, et chaque bloc est lié au précédent par une référence cryptographique (hash), formant ainsi une chaîne continue et sécurisée.

Le caractère décentralisé de la blockchain est essentiel : au lieu d'être stockée sur des serveurs contrôlés par une seule entité, elle est répartie sur un grand nombre de nœuds dans le réseau. Cela renforce la confiance des utilisateurs, car aucune entité unique ne détient le contrôle total des données.

Grâce à cette décentralisation et à la distribution des informations sur plusieurs serveurs, chaque transaction est enregistrée de manière immuable. Une fois validée et intégrée dans un bloc, l'information ne peut plus être modifiée.

Pasted image 20241029133410.png

Initialement développée pour faciliter les transactions financières avec le Bitcoin, la technologie blockchain a évolué pour inclure des concepts innovants tels que les smart contracts avec Ethereum. Aujourd'hui, d'autres blockchains émergent, chacune apportant des caractéristiques et des solutions uniques.

Les blockchains partagent plusieurs caractéristiques clés :
- Immutabilité : une fois qu'une transaction est inscrite, elle ne peut pas être altérée.
- Décentralisation et distribution : les données sont conservées sur un réseau maillé de serveurs, rendant la manipulation des informations très difficile.

En matière de gouvernance, il existe différents types de blockchains :
- Ouvertes : tout le monde peut lire et écrire sur la blockchain.
- Semi-fermées : la lecture est libre, mais l’écriture est limitée à un organisme central.
- Fermées : accès restreint pour la lecture et l'écriture.

Les applications de la blockchain sont variées et prometteuses, notamment :
- Les cryptomonnaies
- Les contrats intelligents
- La chaîne d'approvisionnement
- Le secteur de la santé
- ...

En somme, la blockchain représente une avancée majeure dans la manière dont nous gérons et sécurisons les données, offrant des solutions innovantes dans de nombreux domaines.

## Les applications de la blockchain

### Les cryptomonnaies

Une cryptomonnaie est une monnaie électronique (actif numérique) émise de pair à pair, sans nécessité de banque ou de banque centrale ni d'intermédiaire humain, utilisable au moyen d'un réseau informatique décentralisé basé sur une blockchain intégrant des technologies de cryptographie pour les processus d'émission et de règlement des transactions.

Apparus en 2009 avec le bitcoin et sa blockchain (ou chaine de blocs), des centaines d'autres cryptoactifs se sont ensuite développés, aussi dits Altcoins (mot valise combinant deux mots anglais, “alt” qui signifie alternatif et “coin” qui fait référence aux pièces de monnaie ; désignant toutes les cryptomonnaies créées après le Bitcoin, comme alternatives au Bitcoin, utilisant généralement le même type de technologie de chaîne de blocs, mais avec des algorithmes de consensus différents, des fonctionnalités et des objectifs plus ou moins proches, moins consommateurs de ressources informatiques et énergétiques, comme l'Ethereum, ou augmentant encore la confidentialité des échanges, etc.

Les cryptomonnaies les plus connues et les plus utilisées sont le Bitcoin (BTC) et l'Ethereum (ETH).

### Les NFT

La blockchain n'est pas reservee a l'echange de cryptomonnaies. Les Tokens Non Fongibles sont des actifs numeriques qui sont stockés sur la blockchain. Ces actifs peuvent etre des fichiers (images, sons ...), des données ...

Dans l’écosystème blockchain, on appelle token ou jeton numérique tout actif transférable numériquement entre deux personnes.

Les tokens fongibles sont des actifs qui ont des caracteristiques et des valeurs identiques entre eux. Par exemple les cryptomonnaies sont des tokens fongibles, le Bitcoin est echangeable contre un autre bitcoin, il n'y a pas de differences entre deux Bitcoins.

Les tokens non-fongibles ont des caracteristiques qui les rendent differents les uns des autres, comme par exemple leurs images, leurs token_id ... Ils representent tous quelque chose de different et ont donc des valeurs differentes. On n'echange pas un NFT contre un autre. Ils sont uniques et bases sur la blockchain.


## Le projet Tokenizer

Dans le cadre du projet Tokenizer, j'ai décidé de créer un NFT sur une blockchain de test similaire à Euthereum. On va donc créer et déployer un smart-contract ERC-721 sur la blockchain de test Sepolia.

Pour pouvoir interagir avec notre smart-contract via une API et avoir du monitoring, on a utilisé [Alchemy](https://alchemy.com). On récupère une API_KEY alchemy en créant une app. Cette clé permet de communiquer avec l'API.

Pour stocker nos tokens on utilise un portefeuille virtuel. Chaque transaction sur la blockchain est associée à des frais de gas. On a donc besoin de SepoliaETH, la cryptomonnaie associée à la blockchain Sepolia pour pouvoir déployer notre smart-contract dessus. Sepolia est un réseau de test, on peut récupérer gratuitement des SepoliaETH sur notre portefeuille en utilisant des faucets.

Une fois que l'on a notre clé API et notre wallet, on peut commencer à écrire notre smart-contract. Notre smart contract va etre utilisé au moment de la création d'un NFT. C'est un script, écrit en Solidity, qui régit la création, l'ownership et les fonctions associées aux NFT que l'on veut créer.

Pour assurer toutes les fonctions de notre collection d'NFT, le smart-contract que l'on va déployer hérite de classes vérifiées et approuvées ERC (Ethereum Request for Comment).

Pour les _**jetons non-fongibles (NFT, uniques et non divisibles),**_ la norme **ERC-721** est la plus utilisée. Elle définit un **ensemble de fonctions permettant la création**, la **propriété** et le **transfert de NFT** et, comme susmentionné, le **fait d’être unique au monde**. **Chaque NFT est représenté par un identifiant unique (“_tokenId_”)** et **peut être associé à des métadonnées**, telles qu’un nom, une description et une image. Leur **propriété est stockée sur la blockchain Ethereum**, ce qui signifie qu’elle peut être facilement vérifiée et transférée entre individus.

[Interface definition of ERC-721](https://eips.ethereum.org/EIPS/eip-721)

Une fois le contrat ecrit, l'objectif est de pouvoir l'utiliser. On le deploie donc sur la blockchain. Pour cela on utilise hardhat, un framework de développement Ethereum. On peut deployer notre smart-contract sur la blockchain Sepolia en utilisant notre wallet et notre clé API alchemy. On recupere une adresse qui correspond a notre contrat. Elle est utile pour appeler les fonctions de notre contrat.

Pour pouvoir interagir avec notre smart-contract, on a utilisé un script en javascript. On a utilisé l'API alchemy pour communiquer avec notre smart-contract. On a pu ainsi créer un NFT, le transferer, le recuperer, le supprimer ...

Pour finir, on a créé une documentation pour expliquer comment utiliser notre smart-contract et comment interagir avec lui.

## Conclusion

Le projet TokenizeArt m'a permis de découvrir le monde des NFT et de la blockchain. J'ai pu apprendre à créer un smart-contract ERC-721 et à le déployer sur une blockchain de test. J'ai pu aussi apprendre à interagir avec un smart-contract en utilisant une API. J'ai pu aussi apprendre à utiliser un wallet pour stocker des cryptomonnaies et à utiliser des faucets pour récupérer des cryptomonnaies sur une blockchain de test. Avec ces cryptomonnaies, j'ai pu déployer mon smart-contract et interagir avec lui.


## Liens
Comprendre le fonctionnement de la Blockchain
Créer et vendre un NFT : https://docs.alchemy.com/docs/how-to-create-an-nft
ERC-20 Token : https://docs.alchemy.com/docs/how-to-create-an-erc-20-token-4-steps
