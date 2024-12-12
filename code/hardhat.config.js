require("@nomicfoundation/hardhat-toolbox");

// Ensure your configuration variables are set before executing the script
const { vars } = require("hardhat/config");

// Go to https://alchemy.com, sign up, create a new App in
// its dashboard, and add its key to the configuration variables
const ALCHEMY_URL = process.env.ALCHEMY_URL;

// Add your Sepolia account private key to the configuration variables
// To export your private key from Coinbase Wallet, go to
// Settings > Developer Settings > Show private key
// To export your private key from Metamask, open Metamask and
// go to Account Details > Export Private Key
// Beware: NEVER put real Ether into testing accounts
const METAMASK_PRIVATE_KEY = process.env.METAMASK_PRIVATE_KEY;

task("mint", "Mint a NFT")
    .addParam("to", "The address to mint the NFT to")
    .addParam("uri", "The URI of the token")
    .setAction(async (taskArgs) => {

        const { to, uri } = taskArgs;
        if (to === undefined || uri === undefined) {
            console.error("Missing arguments");
            return;
        }

        const API_KEY = process.env.ALCHEMY_API_KEY;
        const PRIVATE_KEY = process.env.METAMASK_PRIVATE_KEY;

        // Get the contract address from the deployed contract file in the ignitions folder
        // ../ignition/deployments/chain-11155111/deployed_addresses.json
        const fs = require('fs');
        const path = require('path');

        function getContractAddress(
            chainId = 11155111,
            ignitionModule = "NFT42Module",
            contractName = "NFT42"
        ) {
            const filePath = path.join(__dirname, `ignition/deployments/chain-${chainId}/deployed_addresses.json`);
            const content = fs.readFileSync(filePath, 'utf-8');
            const deployed = JSON.parse(content);
            const key = `${ignitionModule}#${contractName}`;
            return deployed[key];
        }

        const CONTRACT_ADDRESS = getContractAddress();
        if (CONTRACT_ADDRESS === undefined) {
            console.error("Contract not deployed");
            return;
        }

        // The contract ABI (Application Binary Interface) is the interface to interact
        // with our smart contract
        const contract = require(path.join(__dirname, "artifacts/contracts/NFT42.sol/NFT42.json"));

        // To interact with our contract, we need to create an instance of it in our code.
        // To do so with Ethers.js, we'll need to work with three concepts:
        const ethers = require('ethers');

        // 1. A provider: a connection to the Sepolia network
        const alchemyProvider = new ethers.AlchemyProvider("sepolia", API_KEY);

        // 2. A signer: an Seplia account that can sign transactions
        const signer = new ethers.Wallet(PRIVATE_KEY, alchemyProvider);

        // 3. A contract instance: an object in our code that represents our deployed smart contract
        const nft42 = new ethers.Contract(CONTRACT_ADDRESS, contract.abi, signer);

        // Now we can interact with our contract by calling its functions

        // Mint a new NFT
        const transaction = await nft42.mint(to, uri);
        const tx = await transaction.wait();
        console.log("NFT minted:", tx);
    });

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
    solidity: "0.8.28",
    networks: {
        sepolia: {
            url: ALCHEMY_URL,
            accounts: [METAMASK_PRIVATE_KEY]
        }
    }
};
