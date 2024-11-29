function saveContractAddress(contractName, contractAddress) {
    // Save the contract address to the file system
    const fs = require("fs");
    const data = { contractName, contractAddress };
    const jsonString = JSON.stringify(data);
    fs.writeFileSync("./contract-address.json", jsonString);
}


async function main() {
    const [deployer] = await ethers.getSigners();
    const NFT42 = await ethers.getContractFactory("NFT42");
    const Nft42 = await NFT42.deploy(deployer.address);
    await Nft42.deployed();
    saveContractAddress("NFT42", Nft42.address);
    console.log("Contract deployed to address:", Nft42.address);
}


main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
