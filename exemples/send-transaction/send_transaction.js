const xrpl = require("xrpl");
(async () => {
    const client = new xrpl.Client("wss://s.altnet.rippletest.net:51233");
    await client.connect();
    const wallet = xrpl.Wallet.fromSeed("s████████");
    const tx = {
        TransactionType: "Payment",
        Account: wallet.address,
        Destination: "r████████",
        Amount: xrpl.xrpToDrops("10")
    };
    const response = await client.submitAndWait(tx, { wallet });
    console.log("Result:", response.result.meta.TransactionResult);
    client.disconnect();
})();
