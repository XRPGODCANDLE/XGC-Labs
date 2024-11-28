const xrpl = require("xrpl");

async function main() {
    // Connect to the XRPL Testnet
    const client = new xrpl.Client("wss://s.altnet.rippletest.net:51233");
    await client.connect();

    // Replace with your wallet's secret and issuer details
    const WALLET_SECRET = "s████████████████████████████";
    const TOKEN_ISSUER = "r████████████████████████████";
    const TOKEN_CURRENCY = "XGC";

    // Initialize wallet
    const wallet = xrpl.Wallet.fromSeed(WALLET_SECRET);

    // Prepare TrustSet transaction
    const trustSetTx = {
        TransactionType: "TrustSet",
        Account: wallet.address,
        LimitAmount: {
            currency: TOKEN_CURRENCY,
            issuer: TOKEN_ISSUER,
            value: "1000000" // Adjust the limit as needed
        }
    };

    // Submit the transaction
    const response = await client.submitAndWait(trustSetTx, { wallet });
    console.log("Transaction result:", response.result.meta.TransactionResult);

    client.disconnect();
}

main();
