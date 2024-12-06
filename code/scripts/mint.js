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
    const filePath = path.join(__dirname, `../ignition/deployments/chain-${chainId}/deployed_addresses.json`);
    const content = fs.readFileSync(filePath, 'utf-8');
    const deployed = JSON.parse(content);
    const key = `${ignitionModule}#${contractName}`;
    return deployed[key];
}

const CONTRACT_ADDRESS = getContractAddress();

// The contract ABI (Application Binary Interface) is the interface to interact
// with our smart contract
const contract = require("../artifacts/contracts/NFT42.sol/NFT42.json");

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
const to = "0x9500A4b4164BaDf7d03050112F2cbE1592B7A483";
const tokenUri = "https://gateway.pinata.cloud/ipfs/QmY2sAjivJSGzsnVJ7AGLSTYKQHA1on8wZB9KrxC6NopkQ";
async function mintNFT(to, tokenUri) {
  const transaction = await nft42.mint(to, tokenUri);
  const tx = await transaction.wait();
  console.log("NFT minted:", tx);
}
mintNFT(to, tokenUri);