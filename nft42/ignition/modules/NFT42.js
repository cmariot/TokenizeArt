const { buildModule } = require("@nomicfoundation/hardhat-ignition/modules");

const NFT42Module = buildModule("NFT42Module", (m) => {
  const token = m.contract("NFT42");
  return { token };
});

module.exports = NFT42Module;