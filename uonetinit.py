import asyncio, os
from vulcan import Keystore, Account
from dotenv import load_dotenv

load_dotenv()
   
async def main():
    keystore = await Keystore.create()
    keystore = await Keystore.create(device_model=os.getenv("BOT_NAME"))
    account = await Account.register(keystore, os.getenv("V_TOKEN"), os.getenv("V_SYMBOL"), os.getenv("V_PIN"))
    with open("account.json", "w") as f:
        f.write(account.as_json)
    with open("keystore.json", "w") as f:
        f.write(keystore.as_json)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())