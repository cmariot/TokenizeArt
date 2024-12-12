const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("NFT42 Contract", function () {
    let NFT42, nft42, owner, addr1, addr2;

    beforeEach(async function () {
        // Déployer le contrat avant chaque test
        NFT42 = await ethers.getContractFactory("NFT42");
        [owner, addr1, addr2] = await ethers.getSigners();
        nft42 = await NFT42.deploy();
    });

    it("Doit permettre de minter un NFT", async function () {
        const tokenURI = "https://example.com/metadata/1.json";
        await nft42.mint(addr1.address, tokenURI);

        // Vérifie la propriété du token
        expect(await nft42.ownerOf(1)).to.equal(addr1.address);

        // Vérifie que le tokenURI est bien défini
        expect(await nft42.tokenURI(1)).to.equal(tokenURI);
    });

    it("Doit permettre de minter plusieurs NFTs", async function () {
        const tokenURI1 = "https://example.com/metadata/1.json";
        const tokenURI2 = "https://example.com/metadata/2.json";

        await nft42.mint(addr1.address, tokenURI1);
        await nft42.mint(addr2.address, tokenURI2);

        // Vérifie les propriétaires des tokens
        expect(await nft42.ownerOf(1)).to.equal(addr1.address);
        expect(await nft42.ownerOf(2)).to.equal(addr2.address);

        // Vérifie les tokenURIs
        expect(await nft42.tokenURI(1)).to.equal(tokenURI1);
        expect(await nft42.tokenURI(2)).to.equal(tokenURI2);
    });

    it("Doit empêcher l'accès au tokenURI pour un token inexistant", async function () {
        await expect(nft42.tokenURI(99)).to.be.reverted;
    });

    it("Doit correctement initialiser l'ID des tokens à 0", async function () {
        const tokenId = await nft42.tokenId();
        expect(tokenId).to.equal(0);
    });

    it("Doit incrémenter l'ID après chaque mint", async function () {
        const tokenURI = "https://example.com/metadata/1.json";

        // Mint un premier NFT
        await nft42.mint(addr1.address, tokenURI);
        let tokenId = await nft42.tokenId();
        expect(tokenId).to.equal(1);

        // Mint un second NFT
        await nft42.mint(addr2.address, tokenURI);
        tokenId = await nft42.tokenId();
        expect(tokenId).to.equal(2);
    });
});
