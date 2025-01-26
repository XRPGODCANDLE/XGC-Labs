// Import the required XRPL library
const xrpl = require('xrpl');

// Function to create an XRPL account
async function createAccount() {
    try {
        // Connect to the XRPL Testnet
        console.log("Connecting to the XRPL Testnet...");
        const client = new xrpl.Client("wss://s.altnet.rippletest.net:51233");
        await client.connect();

        // Generate a new wallet
        console.log("Generating a new XRPL wallet...");
        const wallet = xrpl.Wallet.generate();

        // Display the generated account details
        console.log("\n🎉 New XRPL Account Created:");
        console.log("Account Address: ", wallet.classicAddress);
        console.log("Secret Key: ", wallet.seed);

        // Optionally, fund the account using the XRPL Testnet faucet
        console.log("\nRequesting Testnet funds...");
        const faucetResult = await client.fundWallet(wallet);
        console.log("Funding transaction result: ", faucetResult);

        // Disconnect from the XRPL Testnet
        await client.disconnect();
        console.log("\n✅ Account creation complete!");

        // Return the account details
        return {
            account: wallet.classicAddress,
            secret: wallet.seed,
            balance: faucetResult.balance
        };
    } catch (error) {
        console.error("❌ Error during account creation:", error.message);
        throw error;
    }
}

// Execute the function when the script is run directly
if (require.main === module) {
    createAccount()
        .then((accountDetails) => {
            console.log("\n🎉 Account Details:", accountDetails);
        })
        .catch((error) => {
            console.error("❌ An error occurred:", error);
        });
}

// Export the function for reuse in other scripts
module.exports = createAccount;
