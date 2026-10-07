import os

from crawlora_sofascore import SofascoreClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with SofascoreClient(api_key=api_key) as client:
    search = client.search(q='Liverpool')
    print('search', search)
    live_events = client.live_events(sport='football')
    print('live_events', live_events)
