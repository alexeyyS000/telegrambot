import json
from datetime import datetime
from websockets.sync.client import connect
from .config import max_rate, min_rate

def parse_better_funding_rate():


    with connect("wss://fstream.binance.com/ws/!markPrice@arr") as websocket:
        data = websocket.recv()

    data = json.loads(data)

    list_better_rate = []

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
