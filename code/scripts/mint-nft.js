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

    // Check if the number of arguments is correct (metadata_uri and wallet_address)
    if (process.argv.length !== 4) {
        throw new Error("Usage: node mint-nft.js <METADATA_URI> <WALLET_ADDRESS>");
    }

    const metadata_uri = process.argv[2];
    const wallet_address = process.argv[3];

    let nftTxn = await Gertrude42Contract.mintNFT(signer.address, metadata_uri);
    let transaction_receipt = await nftTxn.wait();
    console.log("TRANSACTION RESPONSE: ", nftTxn);
    console.log("TRANSACTION RECEIPT: ", transaction_receipt);
    // const [transferEvent] = transaction_receipt.events;
    // console.log("TRANSFER EVENT: ", transferEvent);
    // const { tokenId } = transferEvent.args;
    // console.log("TOKEN ID: ", tokenId);

    // If the wallet address is not the same as the signer address, transfer the NFT to the wallet address
    if (wallet_address !== signer.address) {
        // TOKEN ID is NOT 0 !!!!!!!!!!
        // Need to get the tokenId from the event



        let transferTxn = await Gertrude42Contract.safeTransferFrom(signer.address, wallet_address, 0);
        await transferTxn.wait();
    }

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
