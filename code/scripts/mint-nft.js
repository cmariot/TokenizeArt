require("dotenv").config();

const ethers = require("ethers");

// Get Alchemy App URL
const API_KEY = process.env.API_KEY;

// Define an Alchemy Provider
const provider = new ethers.AlchemyProvider("sepolia", API_KEY);

// Get contract ABI file
const contract = require("../artifacts/contracts/GER42.sol/Gertrude42.json");

// Create a signer
const privateKey = process.env.PRIVATE_KEY;
const signer = new ethers.Wallet(privateKey, provider);

// Get contract ABI and address
const abi = contract.abi;
const contract_address = require("../contract-address.json");
if (!contract_address) {
  throw new Error("Contract address not found");
}

const contractAddress = contract_address.contractAddress;

// Create a contract instance
const Gertrude42Contract = new ethers.Contract(contractAddress, abi, signer);

// Get the NFT Metadata IPFS URL
const tokenUri = "https://gateway.pinata.cloud/ipfs/QmfAzgKqq9XdeXB6DN9taSf7Fqo46Jrp4URNctpHVmBtcA";

// Call mintNFT function
const mintNFT = async () => {
  let nftTxn = await Gertrude42Contract.mintNFT(signer.address, tokenUri);
  await nftTxn.wait();
  console.log(
    `NFT Minted! Check it out at: https://sepolia.etherscan.io/tx/${nftTxn.hash}`
  );
};

mintNFT()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
