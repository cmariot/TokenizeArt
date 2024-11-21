require("dotenv").config();
require("@nomiclabs/hardhat-ethers");

const { ALCHEMY_URL, METAMASK_PRIVATE_KEY } = process.env;

module.exports = {
  solidity: {
    compilers: [
      {
        version: "0.8.27",
        settings: {
          optimizer: {
            enabled: true,
            runs: 200,
          },
        },
      },
    ],
  },
  defaultNetwork: "sepolia",
  networks: {
    hardhat: {},
    sepolia: {
      url: ALCHEMY_URL,
      accounts: [`0x${METAMASK_PRIVATE_KEY}`],
    },
  },
};
