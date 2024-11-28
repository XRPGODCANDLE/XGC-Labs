# Trustline Setup

This directory contains scripts to set up a Trustline on the XRP Ledger (XRPL). Trustlines are required to hold or receive issued tokens like XGC on the XRPL.

## Scripts Included
- **setup_trustline.py**: A Python script to configure a Trustline for the XGC token.
- **setup_trustline.js**: A JavaScript (Node.js) script to achieve the same functionality.

## Prerequisites
1. Ensure you have an active XRPL account with sufficient XRP balance.
2. Install the necessary dependencies:
   - Python: Install `xrpl-py` using `pip install xrpl-py`.
   - Node.js: Install `xrpl` using `npm install xrpl`.

## How to Use
1. Update the script with your XRPL account credentials (seed/secret and address).
2. Run the script in your preferred environment.
3. Verify the Trustline on the XRPL Testnet or Mainnet using a block explorer like [xrpl.org](https://xrpl.org).

Refer to the comments in each script for more details.
