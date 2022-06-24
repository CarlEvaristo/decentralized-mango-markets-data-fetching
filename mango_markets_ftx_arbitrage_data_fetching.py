import mango
import websocket_code
import sys
import time

# CONNECT TO FTX WS
ws_ftx = websocket_code.FtxWebsocketClient()
try:
    ws_ftx.connect()
except Exception as e:
    print(f"Websocket Error Message: {e}")
    sys.exit()

spot = (ws_ftx.get_ticker(market="BTC/USD"))
while spot == {}:
    spot = (ws_ftx.get_ticker(market="BTC/USD"))
    time.sleep(0.01)

# CONNECT TO MANGO MARKETS
with mango.ContextBuilder.build(cluster_name="devnet") as context:
    market = mango.market(context, "BTC-PERP")
    data = market.fetch_orderbook(context)
    perp_bid = float(data.top_bid.price)
    perp_ask = float(data.top_ask.price)
    print("MANGO ", perp_ask, perp_bid)

# FTX
spot_ask = spot['ask']
spot_bid = spot['bid']
print("FTX ", spot_ask, spot_bid)

spread = ((perp_ask - spot_ask)/spot_ask)*100
print(spread)