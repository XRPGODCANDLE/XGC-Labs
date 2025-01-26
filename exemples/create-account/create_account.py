import xrpl
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.models.requests import FaucetFundRequest
from xrpl.models.exceptions import XRPLRequestFailureException

# Function to create an XRPL account
def create_account():
    try:
        # Connect to the XRPL Testnet
        print("🔗 Connecting to the XRPL Testnet...")
        client = JsonRpcClient("https://s.altnet.rippletest.net:51234")

        # Generate a new wallet
        print("🧰 Generating a new wallet...")
        wallet = Wallet.generate()

        # Display the generated wallet details
        print("\n🎉 New XRPL Account Created:")
        print(f"Account Address: {wallet.classic_address}")
        print(f"Secret Key: {wallet.seed}")

        # Request funds from the XRPL Testnet faucet
        print("\n🚰 Requesting Testnet funds...")
        fund_request = FaucetFundRequest(account=wallet.classic_address)
        fund_response = client.request(fund_request)

        # Check if the funding was successful
        if fund_response.is_successful():
            print("✅ Funding successful!")
        else:
            raise XRPLRequestFailureException(f"Faucet funding failed: {fund_response.result}")

        # Fetch and display the account balance
        print("\n🔍 Fetching account details...")
        balance_request = xrpl.models.requests.AccountInfo(
            account=wallet.classic_address,
            ledger_index="validated",
            strict=True
        )
        balance_response = client.request(balance_request)
        balance = balance_response.result.get("account_data", {}).get("Balance", "0")

        print(f"💰 Account Balance: {int(balance) / 1_000_000} XRP")

        # Return the wallet details
        return {
            "account": wallet.classic_address,
            "secret": wallet.seed,
            "balance": int(balance) / 1_000_000
        }
    except Exception as e:
        print(f"❌ Error creating account: {e}")
        return None


# Execute the script if run directly
if __name__ == "__main__":
    account_details = create_account()
    if account_details:
        print("\n🎉 Account Details:")
        print(account_details)
