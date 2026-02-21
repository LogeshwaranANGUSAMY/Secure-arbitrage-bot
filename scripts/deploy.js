const { ethers } = require("hardhat");

async function main() {
  const Arbitrage = await ethers.getContractFactory("Arbitrage");
  const arbitrage = await Arbitrage.deploy();

  // ✅ ethers v5
  await arbitrage.deployed();

  console.log("✅ Contract deployed at:", arbitrage.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
