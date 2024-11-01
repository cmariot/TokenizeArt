async function main() {
  const [deployer] = await ethers.getSigners();

  // Grab the contract factory
  const GER42 = await ethers.getContractFactory("Gertrude42");

  // Start deployment, returning a promise that resolves to a contract object
  const Ger42 = await GER42.deploy(deployer.address); // Pass the deployer's address as the initial owner

  await Ger42.deployed();

  console.log("Contract deployed to address:", Ger42.address);

  // Save the contract address in a file
  const fs = require("fs");
  const contractAddress = Ger42.address;
  const contractName = "Gertrude42";
  const data = { contractName, contractAddress };
  const jsonString = JSON.stringify(data, null, 2);
  fs.writeFileSync("./contract-address.json", jsonString);
  console.log("Contract address written to contract-address.json");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
