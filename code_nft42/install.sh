#!/bin/sh
#
# Remove all the files in this directory except for this script
BLUE='\033[0;34m'
NC='\033[0m'

blue_echo () {
	echo "${BLUE}$1${NC}"
}

# Remove all the files in this directory except for this script
FILES=`ls -1 | grep -v install.sh`
for FILE in $FILES
do
	rm -rf $FILE
done

# Init the npm project
blue_echo "Initializing the npm project\n"
npm init -y
blue_echo "Npm project initialized\n"

# Install hardhat, an euthereum development environment
echo "Installing Hardhat\n"
npm install --save-dev hardhat
npm install --save-dev @nomicfoundation/hardhat-toolbox

# Create the hardhat project
npx hardhat init

# Install the required packages
npm install --save dotenv
npm install @openzeppelin/contracts
npm uninstall --legacy-peer-deps ethers
npm install --legacy-peer-deps ethers@5 @nomiclabs/hardhat-ethers 
 
# Clean the default directories
rm -rf contracts/* test ignition README.md

# Copy the contracts and the scripts
cp -r ../code/contracts/* ./contracts/
cp -r ../code/scripts .

# Copy the hardhat config
cp ../code/hardhat.config.js ./hardhat.config.js

npx hardhat run scripts/deploy.js --network sepolia
