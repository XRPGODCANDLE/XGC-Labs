from xrpl.clients import JsonRpcClient
from xrpl.models.transactions import Payment
from xrpl.transaction import submit_and_wait
from xrpl.wallet import Wallet

client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")
wallet = Wallet(seed="s████████", sequence=0)
tx = Payment(account=wallet.classic_address, amount="1000000", destination="r████████")
response = submit_and_wait(tx, client, wallet)
print(response)
