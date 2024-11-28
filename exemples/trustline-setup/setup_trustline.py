from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.models.transactions import TrustSet
from xrpl.transaction import send_reliable_submission

# Connect to the XRPL Testnet
client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")

# Replace with your wallet's secret and issuer details
WALLET_SECRET = "s████████████████████████████"
TOKEN_ISSUER = "r████████████████████████████"
TOKEN_CURRENCY = "XGC"

# Initialize wallet
wallet = Wallet(seed=WALLET_SECRET, sequence=0)

# Create a TrustSet transaction
trust_set = TrustSet(
    account=wallet.classic_address,
    limit_amount={
        "currency": TOKEN_CURRENCY,
        "issuer": TOKEN_ISSUER,
        "value": "1000000"  # Adjust the limit as needed
    }
)

# Submit the transaction
response = send_reliable_submission(trust_set, client, wallet)

# Print the result
print("Transaction result:", response.result["meta"]["TransactionResult"])
