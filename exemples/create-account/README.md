
# Create Account Example

This example demonstrates how to programmatically create an XRPL account using both Python and JavaScript. It also includes unit tests for the Python implementation.

## 🔍 Overview
Creating an XRPL account involves generating a wallet (including a public address and private key) and optionally funding it using the XRPL Testnet faucet. This example provides ready-to-use scripts to achieve this.

## 📂 Files
- **`create_account.js`**: JavaScript implementation to create an XRPL account.
- **`create_account.py`**: Python implementation to create an XRPL account.
- **`create_account_test.py`**: Unit tests for the Python implementation.

---

## 🛠 Prerequisites
Before running the scripts, ensure the following dependencies are installed:

### For Python:
1. **Python 3.7+** installed on your system.
2. Install the XRPL library:
   ```bash
   pip install xrpl
   ```

### For JavaScript:
1. **Node.js** installed on your system.
2. Install the XRPL library:
   ```bash
   npm install xrpl
   ```

---

## 🚀 Usage

### Python:
Run the Python script:
```bash
python create_account.py
```

The script will:
- Connect to the XRPL Testnet.
- Generate a new wallet.
- Request Testnet funds from the faucet.
- Display the account address, secret key, and balance.

Example output:
```yaml
🔗 Connecting to the XRPL Testnet...
🧰 Generating a new wallet...
🎉 New XRPL Account Created:
Account Address: rEXAMPLE12345Address
Secret Key: snEXAMPLE12345SecretKey
🚰 Requesting Testnet funds...
✅ Funding successful!
💰 Account Balance: 1000 XRP
```

---

### JavaScript:
Run the JavaScript script:
```bash
node create_account.js
```

The script performs similar steps:
- Connects to the XRPL Testnet.
- Generates a wallet.
- Funds the wallet using the Testnet faucet.
- Displays the account details.

Example output:
```yaml
Connecting to the XRPL Testnet...
Generating a new wallet...
🎉 New XRPL Account Created:
Account Address: rEXAMPLE12345Address
Secret Key: snEXAMPLE12345SecretKey
Requesting Testnet funds...
Funding successful!
✅ Account Balance: 1000 XRP
```

---

## 🧪 Running Tests
To ensure the Python implementation works correctly, use the included unit test script:

Run the tests:
```bash
python create_account_test.py
```

Example output:
```yaml
...
Ran 1 test in 0.123s

OK
```

---

## 📝 Additional Notes
- **Do not share your secret keys**: The secret key (seed) is sensitive information and should not be shared publicly or stored insecurely.
- **XRPL Testnet funds**: The funds provided by the Testnet faucet have no real-world value and are meant for testing purposes only.
- **Using Mainnet**: These scripts currently connect to the XRPL Testnet. To connect to the XRPL Mainnet, modify the WebSocket/JSON-RPC endpoint accordingly:
  - Mainnet URL: `wss://xrplcluster.com`

---

## 🌐 Resources
- [XRPL Testnet Faucet](https://xrpl.org/xrp-testnet-faucet.html): Use this to manually fund accounts.
- [XRPL Documentation](https://xrpl.org/): Official XRPL documentation.
- [xrpl-py GitHub](https://github.com/XRPLF/xrpl-py): Python library for XRPL development.
- [xrpl.js GitHub](https://github.com/XRPLF/xrpl.js): JavaScript library for XRPL development.

---

## 🤝 Contribution
If you'd like to contribute to this project:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m "Add your message here"`.
4. Push to your branch: `git push origin feature/your-feature-name`.
5. Submit a pull request.

---

## 📧 Support
If you encounter any issues or have questions, feel free to:
- Open an issue on GitHub.
- Contact us via [your preferred communication channel].
