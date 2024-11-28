const xrpl = require("xrpl");
(async () => {
    const client = new xrpl.Client("wss://s.altnet.rippletest.net:51233");
    await client.connect();
    const wallet = await client.fundWallet();
    console.log("Address:", wallet.wallet.address);
    console.log("Seed:", wallet.wallet.seed);
    client.disconnect();
})();
