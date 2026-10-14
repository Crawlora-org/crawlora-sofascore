"""Typed SofaScore client for the Crawlora hosted API."""

from .platform import SofascoreClient, AsyncSofascoreClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = SofascoreClient
AsyncClient = AsyncSofascoreClient
__version__ = '0.4.0'
DISPLAY_NAME = 'SofaScore'
PLATFORM = 'sofascore'
CONTRACT_REVISION = 'sha256:44b9998fd17df2fdc0c63369c092da2aa7b9a992b5647e0af2a1c31017a7ac92'

__all__ = [
    "SofascoreClient", "AsyncSofascoreClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
