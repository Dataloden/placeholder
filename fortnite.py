#basic lobby bot made by Datalodon and Kai

import fortnitepy
import json
import os
import asyncio
import BenBotAsync as bb


filename = 'device_auths.json'


def get_device_auth_details():
    if os.path.isfile(filename):
        with open(filename, 'r') as fp:
            return json.load(fp)
    return {}


def store_device_auth_details(email, details):
    existing = get_device_auth_details()
    existing[email] = details

    with open(filename, 'w') as fp:
        json.dump(existing, fp)


device_auth_details = get_device_auth_details().get(email, {})
client = fortnitepy.Client(
    auth=fortnitepy.AdvancedAuth(
        email=email,   #put email where it says email the second in quotations (eg. "memes@memes.memes")
        password=password,       #put password where it says password the second time in quotations (eg. "password")
        prompt_exchange_code=True,
        delete_existing_device_auths=True,
        **device_auth_details
    )
)


@client.event
async def event_device_auth_generate(details, email):
    store_device_auth_details(email, details)


@client.event
async def event_ready():
    global ready
    print('Client ready as {0.user.display_name}'.format(client))




@client.event
async def event_friend_request(request):
    await request.accept()
    #accept friend request



@client.event
async def event_friend_message(message):
    #what lobby bot does when you type a command

    
@client.event
async def event_party_invite(invitation):
    #what lobby bot does on invitation



client.run()
