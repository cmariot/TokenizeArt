# Deploy the smart contract
deploy:
	@echo "Deploying the smart contract..."
	@cd deployment && ./deploy.sh
	@echo "Smart contract deployed successfully!"


# Mint a default NFT
mint:
	@echo "Minting a default NFT..."
	@cd mint && ./mint.sh
	@echo "Default NFT minted successfully!"


# Launch the test of the smart contract
test:
	@echo "Testing the smart contract..."
	@cd code && yarn && yarn test
	@echo "Smart contract tested successfully!"


fclean:
	@echo "Cleaning up the project..."
	@rm -rf code/artifacts code/cache code/node_modules code/yarn.lock
	@rm -rf website/.venv
	@rm -rf deployment/build
	@rm -rf mint/build
	@echo "Project cleaned up successfully!"


.PHONY: deploy mint test django fclean
