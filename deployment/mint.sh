#!/bin/sh

# Mint NFT
echo "Minting NFT..."

# Check if the script receives the correct number of arguments
if [ "$#" -ne 2 ]; then
  echo "Usage: ./mint.sh <TOKEN_METADATAS> <RECIPIENT_ADDRESS>"
  exit 1
fi

cd ../code/scripts

# Mint NFT
node mint-nft.js $1 $2
pwd