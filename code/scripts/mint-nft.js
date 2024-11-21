require("dotenv").config();
const ethers = require('ethers');

const ALCHEMY_API_KEY = process.env.ALCHEMY_API_KEY;
const METAMASK_PRIVATE_KEY = process.env.METAMASK_PRIVATE_KEY;


// Create an Alchemy Provider using ethers
const provider = new ethers.AlchemyProvider(
    'sepolia', ALCHEMY_API_KEY
);


// Grab your contract ABI
const contract = require(
    "../artifacts/contracts/GER42.sol/Gertrude42.json"
);
const abi = contract.abi;

const contractAddress = require("../contract-address.json").contractAddress;
if (!contractAddress) {
  throw new Error("Contract address not found");
}

// Create a signer
const signer = new ethers.Wallet(METAMASK_PRIVATE_KEY, provider);

// Create a contract instance
const Gertrude42Contract = new ethers.Contract(contractAddress, abi, signer);

const main = async () => {
    const tokenUri = "https://gateway.pinata.cloud/ipfs/QmUnFdjEZhS9zsrKycMNhGs71ejjMvXHPYqvaQ3PJpvgMp";
    if (!tokenUri) {
        throw new Error("Token URI not found, please provide the token URI as an argument");
    }
    // process.exit(1);
    let nftTxn = await Gertrude42Contract.mintNFT(signer.address, tokenUri);
    await nftTxn.wait();
    console.log(
        `NFT Minted! Check it out at: https://sepolia.etherscan.io/tx/${nftTxn.hash}`
    );
};

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
