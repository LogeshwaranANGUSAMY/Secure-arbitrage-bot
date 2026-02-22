import json
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

RPC_URL = os.getenv("SEPOLIA_RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")

# Connect to Sepolia
w3 = Web3(Web3.HTTPProvider(RPC_URL))

if not w3.is_connected():
    print("❌ Failed to connect to Sepolia")
    exit()

print("✅ Connected to Sepolia")

# Load ABI
with open("abi.json", "r") as file:
    abi = json.load(file)

# Setup contract instance
contract = w3.eth.contract(
    address=Web3.to_checksum_address(CONTRACT_ADDRESS),
    abi=abi
)

account = w3.eth.account.from_key(PRIVATE_KEY)
print(f"✅ Wallet loaded: {account.address}")

# Example: Read owner() function
try:
    owner = contract.functions.owner().call()
    print("👤 Contract Owner:", owner)
except Exception as e:
    print("⚠ Could not read owner:", e)