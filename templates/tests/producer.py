#%%
import asyncio
from binance import AsyncClient, BinanceSocketManager
from confluent_kafka import Producer
import configparser
import socket
import json


async def main(producer):
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    # start any sockets here, i.e a trade socket
    # ts = bm.trade_socket('DOGEEUR')
    ts = bm.multiplex_socket(['dogeeur@trade', 'btceur@trade', 'etheur@trade'])
    
    # then start receiving messages
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            print(res)
            user_encode_data = json.dumps(res, indent=2).encode('utf-8')
            producer.produce('doge', value=user_encode_data)
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
