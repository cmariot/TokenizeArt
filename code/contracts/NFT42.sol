// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "hardhat/console.sol";

contract NFT42 is ERC721URIStorage {

    uint256 public tokenId;

    constructor() ERC721("NFT42", "NFT42") {
        tokenId = 0;
        console.log("NFT42 deployed !");
    }

    function mint(address to, string memory tokenURI) public {

        uint256 newTokenId = tokenId + 1;
        tokenId = newTokenId;

        _mint(to, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
    }

}
