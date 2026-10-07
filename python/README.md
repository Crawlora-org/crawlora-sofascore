# crawlora-sofascore

Python client for Crawlora's hosted SofaScore API. It calls Crawlora's
service; it does not run a browser or scrape SofaScore locally. A Crawlora
account and `CRAWLORA_API_KEY` are required, and API use is billed under your
Crawlora account. Crawlora is independent from and not endorsed by
SofaScore or its owners.

## Install

```sh
python -m pip install crawlora-sofascore
```

## Use

```python
import os

from crawlora_sofascore import SofascoreClient

with SofascoreClient(api_key=os.environ["CRAWLORA_API_KEY"]) as client:
    result = client.search(q='Liverpool')
    print(result)
```

The package also exports `Client` as an alias for `SofascoreClient`. Operation
methods are available directly in snake_case and through the `sofascore`
group. The async package client is `AsyncSofascoreClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-sofascore/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-sofascore/blob/main/examples/python.py).

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API, and response data and availability follow its current contract.
