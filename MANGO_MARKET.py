import mango

# EERST PERP OPENEN OP MANGO OM REBATE TE KRIJGEN (0.04%)
# DAN SPOT MARKET OPENEN OP FTX?

# Create a 'devnet' Context
context = mango.ContextBuilder.build(cluster_name="devnet")

# Load the market
stub = context.market_lookup.find_by_symbol("BTC/USDC")
market = mango.ensure_market_loaded(context, stub)

pyth = mango.create_oracle_provider(context, "pyth")
pyth_btc = pyth.oracle_for_market(context, market)
# Note that Pyth provides a +/- confidence interval
print("BTC price on Pyth is:\n\t", pyth_btc.fetch_price(context))

ftx = mango.create_oracle_provider(context, "ftx")
ftx_btc = ftx.oracle_for_market(context, market)
print("BTC price on FTX is:\n\t", ftx_btc.fetch_price(context))

# The 'market' oracle accesses the market's bids and asks, and our
# market-type for "BTC/USDC" is spot.
spot = mango.create_oracle_provider(context, "market")
spot_btc = spot.oracle_for_market(context, market)
print("BTC price on Serum is:\n\t", spot_btc.fetch_price(context))

# Load the market
stub = context.market_lookup.find_by_symbol("SOL-PERP")
market = mango.ensure_market_loaded(context, stub)

print("Example complete.")