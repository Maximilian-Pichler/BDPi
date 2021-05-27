#!/home/ubuntu/archiconda3/envs/streaming/bin/python3.7
#%%
import asyncio
from binance import AsyncClient, BinanceSocketManager
from confluent_kafka import Producer
import configparser
import socket
import ast


async def main(producer):
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    # start any sockets here, i.e a trade socket
    ts = bm.multiplex_socket(['dogeeur@trade', 'btceur@trade', 'etheur@trade', 'maticeur@trade', 'linkeur@trade', 'doteur@trade', 'bnbeur@trade', 'adaeur@trade', 'icpeur@trade', 'xtzeur@trade'])
    
    # then start receiving messages
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            dictionary = ast.literal_eval(str(res))
            #print(dictionary)
            csv_record = "%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s" % (
                        dictionary["stream"],
                        dictionary["data"]["E"],
                        dictionary["data"]["s"],
                        dictionary["data"]["t"],
                        dictionary["data"]["p"],
                        dictionary["data"]["q"],
                        dictionary["data"]["b"],
                        dictionary["data"]["a"],
                        dictionary["data"]["T"],
                        dictionary["data"]["m"],
                        dictionary["data"]["M"])
            producer.produce('crypto', value=csv_record)
            producer.flush()

    await client.close_connection()


#%%
if __name__ == "__main__":
    conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}
    producer = Producer(conf)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(producer))


# %%
