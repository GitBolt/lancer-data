
def lang_to_ext(extension):
  programming_languages = {
      "ts": "Typescript",
      "js": "JavaScript",
      "css": "CSS",
      "html": "HTML",
      "py": "Python",
      "rb": "Ruby",
      "go": "Go",
      "java": "Java",
      "rs": "Rust",
      "sol": "Solidity",
      "cs": "C#",
      "c": "C",
      "cpp": "C++",
      "h": "C++",
      "json": "JSON",
  }

  return programming_languages.get(extension, None)

def get_language_breakdown(commit_data):
  languages_used = {}
  for file in commit_data["files"]:
      filename, extension = file["filename"].rsplit(".", 1)

      language = lang_to_ext(extension)
      if language is None:
        continue
      
      if languages_used.get(language):
        additions = file["additions"] + languages_used[language]["additions"]
        deletions = file["deletions"] + languages_used[language]["deletions"]
      else:
        additions = file["additions"]
        deletions= file["deletions"]

      languages_used[language] = {"additions": additions, "deletions": deletions}

  return languages_used


import json

x = json.loads(r"""
{
  "sha": "f7574246a361abec4c52fa5d6e91449e2b42a036",
  "node_id": "C_kwDOJyGHONoAKGY3NTc0MjQ2YTM2MWFiZWM0YzUyZmE1ZDZlOTE0NDllMmI0MmEwMzY",
  "commit": {
    "author": {
      "name": "Sai Kranthi",
      "email": "iamsaikranthi@gmail.com",
      "date": "2023-07-10T10:39:38Z"
    },
    "committer": {
      "name": "Sai Kranthi",
      "email": "iamsaikranthi@gmail.com",
      "date": "2023-07-10T10:39:38Z"
    },
    "message": "feat(sdk): improve instantbuy",
    "tree": {
      "sha": "0aaa91c708ba4870b4fc88fc388e6e2065064d79",
      "url": "https://api.github.com/repos/sadoprotocol/ordit-sdk/git/trees/0aaa91c708ba4870b4fc88fc388e6e2065064d79"
    },
    "url": "https://api.github.com/repos/sadoprotocol/ordit-sdk/git/commits/f7574246a361abec4c52fa5d6e91449e2b42a036",
    "comment_count": 0,
    "verification": {
      "verified": false,
      "reason": "unsigned",
      "signature": null,
      "payload": null
    }
  },
  "url": "https://api.github.com/repos/sadoprotocol/ordit-sdk/commits/f7574246a361abec4c52fa5d6e91449e2b42a036",
  "html_url": "https://github.com/sadoprotocol/ordit-sdk/commit/f7574246a361abec4c52fa5d6e91449e2b42a036",
  "comments_url": "https://api.github.com/repos/sadoprotocol/ordit-sdk/commits/f7574246a361abec4c52fa5d6e91449e2b42a036/comments",
  "author": {
    "login": "kranthicodes",
    "id": 57343520,
    "node_id": "MDQ6VXNlcjU3MzQzNTIw",
    "avatar_url": "https://avatars.githubusercontent.com/u/57343520?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/kranthicodes",
    "html_url": "https://github.com/kranthicodes",
    "followers_url": "https://api.github.com/users/kranthicodes/followers",
    "following_url": "https://api.github.com/users/kranthicodes/following{/other_user}",
    "gists_url": "https://api.github.com/users/kranthicodes/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/kranthicodes/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/kranthicodes/subscriptions",
    "organizations_url": "https://api.github.com/users/kranthicodes/orgs",
    "repos_url": "https://api.github.com/users/kranthicodes/repos",
    "events_url": "https://api.github.com/users/kranthicodes/events{/privacy}",
    "received_events_url": "https://api.github.com/users/kranthicodes/received_events",
    "type": "User",
    "site_admin": false
  },
  "committer": {
    "login": "kranthicodes",
    "id": 57343520,
    "node_id": "MDQ6VXNlcjU3MzQzNTIw",
    "avatar_url": "https://avatars.githubusercontent.com/u/57343520?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/kranthicodes",
    "html_url": "https://github.com/kranthicodes",
    "followers_url": "https://api.github.com/users/kranthicodes/followers",
    "following_url": "https://api.github.com/users/kranthicodes/following{/other_user}",
    "gists_url": "https://api.github.com/users/kranthicodes/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/kranthicodes/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/kranthicodes/subscriptions",
    "organizations_url": "https://api.github.com/users/kranthicodes/orgs",
    "repos_url": "https://api.github.com/users/kranthicodes/repos",
    "events_url": "https://api.github.com/users/kranthicodes/events{/privacy}",
    "received_events_url": "https://api.github.com/users/kranthicodes/received_events",
    "type": "User",
    "site_admin": false
  },
  "parents": [
    {
      "sha": "6a519581fd18611285bc05d520db88fd0bcac3a2",
      "url": "https://api.github.com/repos/sadoprotocol/ordit-sdk/commits/6a519581fd18611285bc05d520db88fd0bcac3a2",
      "html_url": "https://github.com/sadoprotocol/ordit-sdk/commit/6a519581fd18611285bc05d520db88fd0bcac3a2"
    }
  ],
  "stats": {
    "total": 311,
    "additions": 215,
    "deletions": 96
  },
  "files": [
    {
      "sha": "aa6454d59bf89fa8fd31d1d7079acef4b88e3b46",
      "filename": "packages/sdk/src/addresses/index.ts",
      "status": "modified",
      "additions": 65,
      "deletions": 4,
      "changes": 69,
      "blob_url": "https://github.com/sadoprotocol/ordit-sdk/blob/f7574246a361abec4c52fa5d6e91449e2b42a036/packages%2Fsdk%2Fsrc%2Faddresses%2Findex.ts",
      "raw_url": "https://github.com/sadoprotocol/ordit-sdk/raw/f7574246a361abec4c52fa5d6e91449e2b42a036/packages%2Fsdk%2Fsrc%2Faddresses%2Findex.ts",
      "contents_url": "https://api.github.com/repos/sadoprotocol/ordit-sdk/contents/packages%2Fsdk%2Fsrc%2Faddresses%2Findex.ts?ref=f7574246a361abec4c52fa5d6e91449e2b42a036",
      "patch": "@@ -1,10 +1,10 @@\n import * as ecc from \"@bitcoinerlab/secp256k1\";\n-import BIP32Factory from \"bip32\";\n+import BIP32Factory, { BIP32Interface } from \"bip32\";\n \n import { Network } from \"../config/types\";\n import { getWalletKeys } from \"../keys\";\n-import { createTransaction, getNetwork } from \"../utils\";\n-import { addressFormats, AddressTypes, addressTypeToName } from \"./formats\";\n+import { createTransaction, getNetwork, hdNodeToChild, toXOnly } from \"../utils\";\n+import { AddressFormats, addressFormats, addressNameToType, AddressTypes, addressTypeToName } from \"./formats\";\n \n export function getAddressFormat(address: string, network: Network) {\n   let format = {\n@@ -111,13 +111,66 @@ export async function getAddresses({\n   return getAddressesFromPublicKey(pubKey!, network, format);\n }\n \n-type Address = {\n+export function getAccountDataFromHdNode({\n+  hdNode,\n+  format = \"legacy\",\n+  network = \"testnet\"\n+}: GetAccountDataFromHdNodeOptions) {\n+  if (!hdNode) {\n+    throw new Error(\"Invalid options provided.\");\n+  }\n+\n+  const addressType = addressNameToType[format];\n+  //\n+  const child = hdNodeToChild(hdNode, format, 0);\n+  const pubKey = format === \"taproot\" ? toXOnly(child.publicKey) : child.publicKey;\n+  const paymentObj = createTransaction(pubKey, addressType, network);\n+\n+  const address = paymentObj.address!;\n+  const account: Account = {\n+    address,\n+    pub: child.publicKey.toString(\"hex\"),\n+    priv: child.privateKey!.toString(\"hex\"),\n+    format,\n+    type: addressType\n+  };\n+\n+  if (format === \"taproot\") {\n+    account.xkey = toXOnly(child.publicKey).toString(\"hex\");\n+  }\n+\n+  return account;\n+}\n+\n+export function getAllAccountsFromHdNode({ hdNode, network = \"testnet\" }: GetAllAccountsFromHDNodeOptions) {\n+  const accounts: Account[] = [];\n+  const addressTypesList = Object.values(addressTypeToName) as AddressFormats[];\n+\n+  addressTypesList.forEach((addrType) => {\n+    const account = getAccountDataFromHdNode({\n+      hdNode,\n+      format: addrType,\n+      network\n+    });\n+\n+    accounts.push(account);\n+  });\n+\n+  return accounts;\n+}\n+\n+export type Address = {\n   address: string | undefined;\n   xkey?: string;\n   format: string;\n   pub: string;\n };\n \n+export type Account = Address & {\n+  priv: string;\n+  type: AddressTypes;\n+};\n+\n type GetAddressesOptions = {\n   pubKey?: string;\n   seed?: string;\n@@ -127,4 +180,12 @@ type GetAddressesOptions = {\n   path: string;\n };\n \n+type GetAccountDataFromHdNodeOptions = {\n+  hdNode: BIP32Interface;\n+  format?: AddressFormats;\n+  network?: Network;\n+};\n+\n+type GetAllAccountsFromHDNodeOptions = Omit<GetAccountDataFromHdNodeOptions, \"format\">;\n+\n export * from \"./formats\";"
    },
    {
      "sha": "8b2fbb1b138e006d51da92a0ed4d128a5368e898",
      "filename": "packages/sdk/src/inscription/instant-buy.ts",
      "status": "modified",
      "additions": 49,
      "deletions": 10,
      "changes": 59,
      "blob_url": "https://github.com/sadoprotocol/ordit-sdk/blob/f7574246a361abec4c52fa5d6e91449e2b42a036/packages%2Fsdk%2Fsrc%2Finscription%2Finstant-buy.ts",
      "raw_url": "https://github.com/sadoprotocol/ordit-sdk/raw/f7574246a361abec4c52fa5d6e91449e2b42a036/packages%2Fsdk%2Fsrc%2Finscription%2Finstant-buy.ts",
      "contents_url": "https://api.github.com/repos/sadoprotocol/ordit-sdk/contents/packages%2Fsdk%2Fsrc%2Finscription%2Finstant-buy.ts?ref=f7574246a361abec4c52fa5d6e91449e2b42a036",
      "patch": "@@ -8,7 +8,8 @@ import {\n   createTransaction,\n   getAddressesFromPublicKey,\n   getNetwork,\n-  OrditApi\n+  OrditApi,\n+  toXOnly\n } from \"..\";\n import { Network } from \"../config/types\";\n \n@@ -132,9 +133,7 @@ export async function generateBuyerInstantBuyPsbt({\n     const input: any = {\n       hash: dummyUtxo.txid,\n       index: dummyUtxo.n,\n-      nonWitnessUtxo: rawTx.toBuffer(),\n-      witnessUtxo: format === \"p2tr\" ? rawTx.outs[0] : undefined,\n-      tapInternalKey: format === \"p2tr\" ? Buffer.from(address.xkey!, \"hex\") : undefined\n+      nonWitnessUtxo: rawTx.toBuffer()\n     };\n \n     const p2shInputRedeemScript: any = {};\n@@ -149,6 +148,17 @@ export async function generateBuyerInstantBuyPsbt({\n       p2shInputRedeemScript.redeemScript = p2sh.redeem?.output;\n     }\n \n+    if (format === \"p2tr\") {\n+      const xKey = toXOnly(Buffer.from(publicKey, \"hex\"));\n+      const p2tr = createTransaction(xKey, \"p2tr\", network);\n+\n+      input.tapInternalKey = toXOnly(Buffer.from(publicKey, \"hex\"));\n+      input.witnessUtxo = {\n+        script: p2tr.output!,\n+        value: dummyUtxo.sats\n+      };\n+    }\n+\n     psbt.addInput({\n       ...input,\n       ...p2shInputWitnessUTXO,\n@@ -201,13 +211,24 @@ export async function generateBuyerInstantBuyPsbt({\n         } catch {}\n       }\n     }\n+\n     const input: any = {\n       hash: utxo.txid,\n       index: utxo.n,\n-      nonWitnessUtxo: rawTx.toBuffer(),\n-      witnessUtxo: rawTx.outs[2]\n+      nonWitnessUtxo: rawTx.toBuffer()\n     };\n \n+    if (pubKeyType === \"taproot\") {\n+      const xKey = toXOnly(Buffer.from(publicKey, \"hex\"));\n+      const p2tr = createTransaction(xKey, \"p2tr\", network);\n+\n+      input.tapInternalKey = toXOnly(Buffer.from(publicKey, \"hex\"));\n+      input.witnessUtxo = {\n+        script: p2tr.output!,\n+        value: utxo.sats\n+      };\n+    }\n+\n     psbt.addInput({\n       ...input\n     });\n@@ -305,7 +326,19 @@ export async function generateDummyUtxos({\n       nonWitnessUtxo: rawTx.toBuffer()\n     };\n \n+    if (pubKeyType === \"taproot\") {\n+      const xKey = toXOnly(Buffer.from(publicKey, \"hex\"));\n+      const p2tr = createTransaction(xKey, \"p2tr\", network);\n+\n+      input.tapInternalKey = toXOnly(Buffer.from(publicKey, \"hex\"));\n+      input.witnessUtxo = {\n+        script: p2tr.output!,\n+        value: utxo.sats\n+      };\n+    }\n+\n     psbt.addInput(input);\n+\n     totalValue += utxo.sats;\n     paymentUtxoCount += 1;\n \n@@ -452,19 +485,25 @@ export async function getSellerInputsOutputs({\n \n       const options: any = {};\n \n-      const data = {\n+      const data: any = {\n         hash: ordUtxo.txid,\n         index: parseInt(ordUtxo.n),\n-        nonWitnessUtxo: rawTx.toBuffer(),\n-        witnessUtxo: rawTx.outs[0]\n+        nonWitnessUtxo: rawTx.toBuffer()\n       };\n \n       if (side === \"seller\") {\n         options.sighashType = bitcoin.Transaction.SIGHASH_SINGLE | bitcoin.Transaction.SIGHASH_ANYONECANPAY;\n       }\n \n       if (format === \"p2tr\") {\n-        options.tapInternalKey = Buffer.from(address.xkey!, \"hex\");\n+        const xKey = toXOnly(Buffer.from(publicKey, \"hex\"));\n+        const p2tr = createTransaction(xKey, \"p2tr\", network);\n+\n+        data.tapInternalKey = toXOnly(Buffer.from(publicKey, \"hex\"));\n+        data.witnessUtxo = {\n+          script: p2tr.output!,\n+          value: ordUtxo.sats\n+        };\n       }\n \n       inputs.push({"
    },
    {
      "sha": "6d63c93ec682f08cd4d5dd372f44de36865f60f3",
      "filename": "packages/sdk/src/utils/index.ts",
      "status": "modified",
      "additions": 32,
      "deletions": 0,
      "changes": 32,
      "blob_url": "https://github.com/sadoprotocol/ordit-sdk/blob/f7574246a361abec4c52fa5d6e91449e2b42a036/packages%2Fsdk%2Fsrc%2Futils%2Findex.ts",
      "raw_url": "https://github.com/sadoprotocol/ordit-sdk/raw/f7574246a361abec4c52fa5d6e91449e2b42a036/packages%2Fsdk%2Fsrc%2Futils%2Findex.ts",
      "contents_url": "https://api.github.com/repos/sadoprotocol/ordit-sdk/contents/packages%2Fsdk%2Fsrc%2Futils%2Findex.ts?ref=f7574246a361abec4c52fa5d6e91449e2b42a036",
      "patch": "@@ -1,6 +1,7 @@\n import * as ecc from \"@bitcoinerlab/secp256k1\";\n import { BIP32Interface } from \"bip32\";\n import * as bitcoin from \"bitcoinjs-lib\";\n+import ECPairFactory from \"ecpair\";\n \n import { AddressFormats, AddressTypes } from \"../addresses/formats\";\n import { Network } from \"../config/types\";\n@@ -57,3 +58,34 @@ export function calculateTxFeeWithRate(\n   const fee = txSize * feeRate;\n   return fee;\n }\n+\n+export function toXOnly(pubkey: Buffer): Buffer {\n+  return pubkey.subarray(1, 33);\n+}\n+\n+export function tweakSigner(signer: bitcoin.Signer, opts: any = {}): bitcoin.Signer {\n+  const ECPair = ECPairFactory(ecc);\n+\n+  // eslint-disable-next-line @typescript-eslint/ban-ts-comment\n+  // @ts-ignore\n+  let privateKey: Uint8Array | undefined = signer.privateKey!;\n+  if (!privateKey) {\n+    throw new Error(\"Private key is required for tweaking signer!\");\n+  }\n+  if (signer.publicKey[0] === 3) {\n+    privateKey = ecc.privateNegate(privateKey);\n+  }\n+\n+  const tweakedPrivateKey = ecc.privateAdd(privateKey, tapTweakHash(toXOnly(signer.publicKey), opts.tweakHash));\n+  if (!tweakedPrivateKey) {\n+    throw new Error(\"Invalid tweaked private key!\");\n+  }\n+\n+  return ECPair.fromPrivateKey(Buffer.from(tweakedPrivateKey), {\n+    network: opts.network\n+  });\n+}\n+\n+export function tapTweakHash(pubKey: Buffer, h: Buffer | undefined): Buffer {\n+  return bitcoin.crypto.taggedHash(\"TapTweak\", Buffer.concat(h ? [pubKey, h] : [pubKey]));\n+}"
    },
    {
      "sha": "881eb66f0c433efa95d8a592791432c4c1a26a53",
      "filename": "packages/sdk/src/wallet/Ordit.ts",
      "status": "modified",
      "additions": 69,
      "deletions": 82,
      "changes": 151,
      "blob_url": "https://github.com/sadoprotocol/ordit-sdk/blob/f7574246a361abec4c52fa5d6e91449e2b42a036/packages%2Fsdk%2Fsrc%2Fwallet%2FOrdit.ts",
      "raw_url": "https://github.com/sadoprotocol/ordit-sdk/raw/f7574246a361abec4c52fa5d6e91449e2b42a036/packages%2Fsdk%2Fsrc%2Fwallet%2FOrdit.ts",
      "contents_url": "https://api.github.com/repos/sadoprotocol/ordit-sdk/contents/packages%2Fsdk%2Fsrc%2Fwallet%2FOrdit.ts?ref=f7574246a361abec4c52fa5d6e91449e2b42a036",
      "patch": "@@ -5,7 +5,15 @@ import * as bitcoin from \"bitcoinjs-lib\";\n import { isTaprootInput } from \"bitcoinjs-lib/src/psbt/bip371\";\n import ECPairFactory, { ECPairInterface } from \"ecpair\";\n \n-import { AddressFormats, getAddressesFromPublicKey, getNetwork, hdNodeToChild } from \"..\";\n+import {\n+  Account,\n+  AddressFormats,\n+  addressNameToType,\n+  getAddressesFromPublicKey,\n+  getAllAccountsFromHdNode,\n+  getNetwork,\n+  tweakSigner\n+} from \"..\";\n import { OrditApi } from \"../api\";\n import { Network } from \"../config/types\";\n import { OrdTransaction, OrdTransactionOptions } from \"../transactions\";\n@@ -20,48 +28,59 @@ export class Ordit {\n   #initialized = false;\n   #keyPair: ECPairInterface;\n   publicKey: string;\n-  taprootPublicKey: string | null = null;\n-  allAddresses: ReturnType<typeof getAddressesFromPublicKey> = [];\n+  allAddresses: ReturnType<typeof getAddressesFromPublicKey> | ReturnType<typeof getAllAccountsFromHdNode> = [];\n   selectedAddressType: AddressFormats | undefined;\n   selectedAddress: string | undefined;\n-  #taprootKeypair: ECPairInterface | null = null;\n \n-  constructor({ wif, seed, privateKey, bip39, network = \"testnet\" }: WalletOptions) {\n+  constructor({ wif, seed, privateKey, bip39, network = \"testnet\", type = \"legacy\" }: WalletOptions) {\n     this.#network = network;\n     const networkObj = getNetwork(network);\n+    const format = addressNameToType[type];\n \n     if (wif) {\n       const keyPair = ECPair.fromWIF(wif, networkObj);\n       this.#keyPair = keyPair;\n+\n+      this.publicKey = keyPair.publicKey.toString(\"hex\");\n+\n+      const accounts = getAddressesFromPublicKey(keyPair.publicKey, network, format);\n+      this.#initialize(accounts);\n     } else if (privateKey) {\n       const pkBuffer = Buffer.from(privateKey, \"hex\");\n       const keyPair = ECPair.fromPrivateKey(pkBuffer, { network: networkObj });\n       this.#keyPair = keyPair;\n+\n+      this.publicKey = keyPair.publicKey.toString(\"hex\");\n+\n+      const accounts = getAddressesFromPublicKey(keyPair.publicKey, network, format);\n+      this.#initialize(accounts);\n     } else if (seed) {\n       const seedBuffer = Buffer.from(seed, \"hex\");\n       const hdNode = bip32.fromSeed(seedBuffer, networkObj);\n-      const child = hdNodeToChild(hdNode, \"legacy\", 0);\n-      const taprootChild = hdNodeToChild(hdNode, \"taproot\", 0);\n \n-      this.#keyPair = ECPair.fromPrivateKey(child.privateKey!, { network: networkObj });\n-      this.#taprootKeypair = ECPair.fromPrivateKey(taprootChild.privateKey!, { network: networkObj });\n-      this.taprootPublicKey = this.#taprootKeypair.publicKey.toString(\"hex\");\n+      const accounts = getAllAccountsFromHdNode({ hdNode, network });\n+\n+      const pkBuf = Buffer.from(accounts[0].priv, \"hex\");\n+      this.#keyPair = ECPair.fromPrivateKey(pkBuf, { network: networkObj });\n+\n+      this.publicKey = this.#keyPair.publicKey.toString(\"hex\");\n+\n+      this.#initialize(accounts);\n     } else if (bip39) {\n       const seedBuffer = mnemonicToSeedSync(bip39);\n       const hdNode = bip32.fromSeed(seedBuffer, networkObj);\n-      const child = hdNodeToChild(hdNode, \"legacy\", 0);\n-      const taprootChild = hdNodeToChild(hdNode, \"taproot\", 0);\n \n-      this.#keyPair = ECPair.fromPrivateKey(child.privateKey!, { network: networkObj });\n-      this.#taprootKeypair = ECPair.fromPrivateKey(taprootChild.privateKey!, { network: networkObj });\n-      this.taprootPublicKey = this.#taprootKeypair.publicKey.toString(\"hex\");\n+      const accounts = getAllAccountsFromHdNode({ hdNode, network });\n+\n+      const pkBuf = Buffer.from(accounts[0].priv, \"hex\");\n+      this.#keyPair = ECPair.fromPrivateKey(pkBuf, { network: networkObj });\n+\n+      this.publicKey = this.#keyPair.publicKey.toString(\"hex\");\n+\n+      this.#initialize(accounts);\n     } else {\n       throw new Error(\"Invalid options provided.\");\n     }\n-\n-    this.publicKey = this.#keyPair.publicKey.toString(\"hex\");\n-\n-    this.#initialize();\n   }\n \n   get network() {\n@@ -90,36 +109,38 @@ export class Ordit {\n       throw new Error(\"Keypair not found\");\n     }\n \n-    return getAddressesFromPublicKey(this.publicKey, this.#network, \"all\");\n+    return this.allAddresses;\n   }\n \n   setDefaultAddress(type: AddressFormats) {\n     if (this.selectedAddressType === type) return;\n \n-    const result = this.getAddressByType(type);\n+    const result = this.getAddressByType(type) as Account;\n+    const networkObj = getNetwork(this.#network);\n \n     this.selectedAddress = result.address;\n-    this.publicKey = result.pub\n+    this.publicKey = result.pub;\n     this.selectedAddressType = type;\n+\n+    if (result.priv) {\n+      this.#keyPair = ECPair.fromPrivateKey(Buffer.from(result.priv, \"hex\"), {\n+        network: networkObj\n+      });\n+    }\n   }\n \n-  signPsbt(hex?: string, base64?: string) {\n+  signPsbt(value: string, { finalized = true }: { finalized?: boolean }) {\n     const networkObj = getNetwork(this.#network);\n     let psbt: bitcoin.Psbt | null = null;\n \n     if (!this.#keyPair || !this.#initialized) {\n       throw new Error(\"Wallet not fully initialized.\");\n     }\n-    if (!(hex || base64) || (hex && base64)) {\n-      throw new Error(\"Invalid options provided.\");\n-    }\n \n-    if (hex) {\n-      psbt = bitcoin.Psbt.fromHex(hex);\n-    }\n-\n-    if (base64) {\n-      psbt = bitcoin.Psbt.fromBase64(base64);\n+    try {\n+      psbt = bitcoin.Psbt.fromHex(value);\n+    } catch (error) {\n+      psbt = bitcoin.Psbt.fromBase64(value);\n     }\n \n     if (!psbt || !psbt.inputCount) {\n@@ -152,16 +173,17 @@ export class Ordit {\n       }\n     });\n \n+    let psbtHasBeenSigned = false;\n+\n     for (let i = 0; i < inputsToSign.length; i++) {\n       try {\n         const input = psbt.data.inputs[i];\n+        psbtHasBeenSigned = input.finalScriptSig || input.finalScriptWitness ? true : false;\n \n-        if (isTaprootInput(input)) {\n-          if (!this.#taprootKeypair) {\n-            throw new Error(\"Taproot signer not found.\");\n-          }\n+        if (psbtHasBeenSigned) continue;\n \n-          const tweakedSigner = tweakSigner(this.#taprootKeypair, {\n+        if (isTaprootInput(input)) {\n+          const tweakedSigner = tweakSigner(this.#keyPair, {\n             network: networkObj\n           });\n \n@@ -175,27 +197,21 @@ export class Ordit {\n     }\n \n     const psbtHex = psbt.toHex();\n-    const psbtBase64 = psbt.toBase64();\n \n-    const psbtHasBeenSigned = psbtHex !== hex || psbtBase64 !== base64;\n+    //TODO: check if psbt has been signed\n \n-    if (psbtHasBeenSigned) {\n-      try {\n+    try {\n+      if (finalized) {\n         psbt.finalizeAllInputs();\n \n         const signedHex = psbt.extractTransaction().toHex();\n \n-        return {\n-          hex: signedHex\n-        };\n-      } catch (error) {\n-        return {\n-          hex: psbtHex,\n-          base64: psbtBase64\n-        };\n+        return signedHex;\n       }\n-    } else {\n-      throw new Error(\"Signed PSBT is same as input PSBT.\");\n+\n+      return psbtHex;\n+    } catch (error) {\n+      throw new Error(\"Cannot finalize the inputs.\", error);\n     }\n   }\n \n@@ -243,8 +259,7 @@ export class Ordit {\n     }\n   };\n \n-  #initialize() {\n-    const addresses = this.getAllAddresses();\n+  #initialize(addresses: Address[]) {\n     this.allAddresses = addresses;\n \n     const addressFormat = addresses[0].format as AddressFormats;\n@@ -261,39 +276,11 @@ export type WalletOptions = {\n   privateKey?: string;\n   bip39?: string;\n   network?: Network;\n+  type?: AddressFormats;\n };\n \n export type Address = ReturnType<typeof getAddressesFromPublicKey>[0];\n \n-function tweakSigner(signer: bitcoin.Signer, opts: any = {}): bitcoin.Signer {\n-  // eslint-disable-next-line @typescript-eslint/ban-ts-comment\n-  // @ts-ignore\n-  let privateKey: Uint8Array | undefined = signer.privateKey!;\n-  if (!privateKey) {\n-    throw new Error(\"Private key is required for tweaking signer!\");\n-  }\n-  if (signer.publicKey[0] === 3) {\n-    privateKey = ecc.privateNegate(privateKey);\n-  }\n-\n-  const tweakedPrivateKey = ecc.privateAdd(privateKey, tapTweakHash(toXOnly(signer.publicKey), opts.tweakHash));\n-  if (!tweakedPrivateKey) {\n-    throw new Error(\"Invalid tweaked private key!\");\n-  }\n-\n-  return ECPair.fromPrivateKey(Buffer.from(tweakedPrivateKey), {\n-    network: opts.network\n-  });\n-}\n-\n-function tapTweakHash(pubKey: Buffer, h: Buffer | undefined): Buffer {\n-  return bitcoin.crypto.taggedHash(\"TapTweak\", Buffer.concat(h ? [pubKey, h] : [pubKey]));\n-}\n-\n-function toXOnly(pubkey: Buffer): Buffer {\n-  return pubkey.subarray(1, 33);\n-}\n-\n export interface Input {\n   index: number;\n   publicKey: string;"
    }
  ]
}
"""
)


print(get_language_breakdown(x))