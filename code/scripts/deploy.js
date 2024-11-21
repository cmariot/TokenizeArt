function saveContractAddress(contractName, contractAddress) {
    // Save the contract address to the file system
    const fs = require("fs");
    const data = { contractName, contractAddress };
    const jsonString = JSON.stringify(data);
    fs.writeFileSync("./contract-address.json", jsonString);
}


async function main() {
    const [deployer] = await ethers.getSigners();
    const GER42 = await ethers.getContractFactory("Gertrude42");
    const Ger42 = await GER42.deploy(deployer.address);
    await Ger42.deployed();
    saveContractAddress("Gertrude42", Ger42.address);
    console.log("Contract deployed to address:", Ger42.address);
}


main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
