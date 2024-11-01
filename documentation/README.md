Build your own token

## Chapter I - Preamble
This subject is the production of a partnership between 42 and BNB Chain.
Build N Build (BNB) Chain is a distributed blockchain network upon which developers and innovators can build decentralised applications (DApps) as part of the move to Web3. As of October 2022, BNB Chain is the world’s largest smart-contract blockchain in terms of transaction volume and daily active users. At the time of writing, it has processed 3 billion transactions from 232 million unique addresses, and has an ecosystem of more than 1,500 active DApps. The decentralised nature of the network means anyone can build a product on BNB Chain without having to ask for permission, and potentially reach a massive audience.

## Chapter II - Introduction
Welcome to the exciting world of blockchain technology!
Have you ever dreamed of creating your own digital token?
Now is your chance to make that dream a reality.
Blockchain technology allows for the creation and distribution of unique digital assets, known as tokens. These tokens can represent a wide range of things, from a simple representation of currency to more complex assets like artwork or even a real-world asset.
The process of creating your own token is not without its challenges, but with the right
knowledge and resources, it can be a rewarding and fulfilling experience.
So why wait?
Start your journey towards creating your very own token on the blockchain today!

## Chapter III - Objectives

As a participant in this project, you will have the opportunity to contribute to the creation of a digital asset on the blockchain. This project is designed to challenge you in several areas, including your ability to master multiple programming languages and your familiarity with public blockchain technology.
While a strong background in cryptography is not required for this project, you should be prepared to learn and adapt as you work towards creating your own digital asset. This project will require you to think critically and creatively, as well as to push yourself out of your comfort zone as you navigate the complexities of blockchain technology.
Ultimately, your participation in this project will not only help you develop valuable skills and knowledge, but it will also allow you to be a part of something truly innovative and exciting. Are you ready to take on the challenge?
Let’s get started!

## Chapter IV - Mandatory part

In order to create a token, there are several technical requirements that must be met.
You are free to choose the name of your token.
Your only constraint is to have 42 in it.
It is of course forbidden to use insulting terms under penalty of punishment.

You must therefore create a README.md file at the root of your repository explaining the choices you had to make and the reasons why you made these choices.

The language used is of course free.

First and foremost, you will need to choose a blockchain platform that supports the creation of tokens. There are many different options to choose from, each with its own unique features and capabilities.

Once you have selected a platform, you will need to become proficient in the programming language used by that platform in order to develop your token. Different platforms use different programming languages, so you will need to ensure that you have the necessary skills to work with the language of your chosen platform such as IDE, Truffle, Remix or Hardhat.

Make sure you understand what you are doing. You will never be asked to use real money to do this project. There are test chains to avoid this problem.

You must submit the code used to create your token in a code folder located at the root of your repository. You should be careful to comment out your code and to use readable and explicit variable/function names. During your evaluation there will be a code review. You must be very careful about how you demonstrate the operation of your token. You must be able to perform minimalist actions to demonstrate its operation. You need to think about all aspects of security such as ownership or privileges.

You should also put all the things you need for the deployment part of your token in a second folder with the name you want. 

After deploying your token on a public blockchain. You will define its ticker and publish it on a blockchain explorer (ex: blockscan or bscscan). Please mention the smart contract address and the network used, in your Git repository.

Finally, you should have a folder containing the documentation for this project. This folder is called documentation and should be at the root of your repository. It should be possible to understand how it works and what is needed to use your token.

You will need to have a clear understanding of how your token will be used and what it will represent. This may require the development of a white-paper or other documentation outlining the features and functionality of your token.
You must take the time to make a clear and explicit documentation.
This will be reviewed during your evaluation.
Consider also creating a demo video to showcase your token and its features to potential users and investors.
If you want to make a video demo you don’t have to push the video on your repository but a simple link will do!
Creating a demo video is not required.
You will not get a better grade by creating this video.

Below is an example of the expected directory structure:
$> ls -al
total XX
drwxrwxr-x 3 wil wil 4096 avril 42 20:42 .
drwxrwxrwt 17 wil wil 4096 avril 42 20:42 ..
-rw-rw-r-- 1 wil wil XXXX avril 42 20:42 README.md
drwxrwxr-x 3 wil wil 4096 avril 42 20:42 code
drwxrwxr-x 3 wil wil 4096 avril 42 20:42 deployment
drwxrwxr-x 3 wil wil 4096 avril 42 20:42 documentation

## Chapter V - Bonus part
To ensure the security of your token and prevent fraudulent activity, you may want to consider implementing a multisignature system, also known as a multisig.
This feature requires multiple parties to sign off on a transaction before it can be executed, providing an extra layer of protection for high-value assets or sensitive financial transactions.
Setting up a multisig system is easy using your preferred programming language by creating a smart contract that mandates multiple signatures for every transaction. Determine the number of signatures required and who is authorized to sign to enhance security and gain the trust of your token’s users.
You must adapt this bonus to the mandatory part of this project.
The bonus part will only be assessed if the mandatory part is PERFECT. Perfect means the mandatory part has been integrally done and works without malfunctioning.
If you have not passed ALL the mandatory requirements, your bonus part will not be evaluated at all.

## Chapter VI - Submission and peer-evaluation
Turn in your assignment in your Git repository as usual. Only the work inside your repository will be evaluated during the defense. Don’t hesitate to double check the names of your folders and files to ensure they are correct.
Exceptionally for this project, we recommend that you share your project via your personal git account when your project is valid. Feel free to use different hashtags depending on the programming language used, but also web3 etc...










# Tokenizer

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

On le fait également hériter de l'interface Ownable. Cette classe met en place des règles qui  permettent de restreindre le minage du NFT qu'au détenteur du smart-contract.














## Liens
Comprendre le fonctionnement de la Blockchain
Créer et vendre un NFT : https://docs.alchemy.com/docs/how-to-create-an-nft
