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
    min_rate = -0.002
    for i in data:
        if float(i["r"]) > max_rate or float(i["r"]) < min_rate:
            list_better_rate.append(
                {
                    "symbol": i["s"],
                    "rate": float(i["r"]) * 100,
                    "date_time": datetime.utcfromtimestamp(int(i["T"]) / 1000).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                }
            )

    return list_better_rate
