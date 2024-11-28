from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet

client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")
wallet = generate_faucet_wallet(client, debug=True)
print(f"Address: {wallet.classic_address}, Seed: {wallet.seed}")
