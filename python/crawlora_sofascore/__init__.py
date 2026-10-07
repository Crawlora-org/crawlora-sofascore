"""Typed SofaScore client for the Crawlora hosted API."""

from .platform import SofascoreClient, AsyncSofascoreClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = SofascoreClient
AsyncClient = AsyncSofascoreClient
__version__ = '0.1.2'
DISPLAY_NAME = 'SofaScore'
PLATFORM = 'sofascore'
CONTRACT_REVISION = 'sha256:8dc2e500465b7b7f98054def2f9794e0e433d8bbbcba6cfb688e0b6ed0ecbfcd'

__all__ = [
    "SofascoreClient", "AsyncSofascoreClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
