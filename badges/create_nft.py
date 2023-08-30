import requests
from db import SessionLocal2
from schemas import UnclaimedBadge, Wallet

positions = ["First", "Second", "Third", "Top 5", "Top 10"]
category = ["Contribution", "Commits"]


pos_to_badge = {
    "First": "Gold Medal",
    "Second": "Silver Medal",
    "Third": "Bronze Medal",
    "Top 5": "Top 5",
    "Top 10": "Top 10",
}


def createNFT(dev, position, category, week, language):
    ses = SessionLocal2()
    wallet = ses.query(Wallet).filter(Wallet.userid == dev["id"]).first()
    print("Wallet: ", wallet)
    
    if position not in positions:
        return "Positions must be in: " + " ".join(positions)
    
    url = "https://dev.underdogprotocol.com/v2/projects/1/nfts"

    payload = {
        "attributes": {
            "Github Name": dev["github_name"],
            "Position": position,
            "Category": f"Top Developer By {category}",
            "Language": language,
            "Week": week,
        },
        "name": pos_to_badge[position] + " Badge",
        "symbol": "LBADGE",
        "description": f"{position} place developer by commits for the week: {week}" if category == "Commits" else f"{position} place {language.upper()} developer in the week: {week}",
        "image": "https://bafkreietxwwsmhmlw2x5dxgknrq6yhbtakwcbzddrxeqkkp2b73xevpw2m.ipfs.nftstorage.link/",
        "externalUrl": "https://lancer.so"
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer 2d274b3da5f894.a96a116120c447dc9f72cc1e856b33e9"
    }

    if (wallet):
        payload.update({"receiverAddress": wallet.publicKey})
        response = requests.post(url, json=payload, headers=headers)
        return response
    else:
        
        new_unclaimed_badge = UnclaimedBadge(user_id=dev["id"], details=payload)
        ses.add(new_unclaimed_badge)
        ses.commit()
        return "Saved unclaimed data to db"