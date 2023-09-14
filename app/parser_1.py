import websockets
import asyncio
import json
from datetime import datetime


def parse_better_funding_rate():
    async def parse_fanding_data():
        url = "wss://fstream.binance.com/ws/!markPrice@arr"
        async with websockets.connect(url) as client:
            data = await client.recv()
            return data

    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(parse_fanding_data())
    data = json.loads(data)

    list_better_rate = []

    max_rate = 0.005
    min_rate = -0.003
    for i in data:
        rate = float(i["r"])
        if rate > max_rate or rate < min_rate:
            list_better_rate.append(
                {
                    "symbol": i["s"],
                    "rate": rate * 100,
                    "date_time": datetime.utcfromtimestamp(int(i["T"]) / 1000).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                }
            )

    return list_better_rate
