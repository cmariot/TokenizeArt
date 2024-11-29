// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFT42 is ERC721URIStorage, Ownable {

    uint256 private _tokenIds;

    constructor(address initialOwner) ERC721("NFT42", "NFT42") Ownable(initialOwner) {}

    event Mint(uint256 indexed tokenId);

    function mintNFT(address recipient, string memory tokenURI)
        public
        onlyOwner
        returns (uint256)
    {
        _tokenIds++;

        uint256 newItemId = _tokenIds;
        _mint(recipient, newItemId);
        _setTokenURI(newItemId, tokenURI);

        emit Mint(newItemId);

        return newItemId;
    }

}