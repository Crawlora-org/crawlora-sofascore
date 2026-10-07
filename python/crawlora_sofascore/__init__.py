"""Typed SofaScore client for the Crawlora hosted API."""

from .platform import SofascoreClient, AsyncSofascoreClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = SofascoreClient
AsyncClient = AsyncSofascoreClient
__version__ = '0.2.0'
DISPLAY_NAME = 'SofaScore'
PLATFORM = 'sofascore'
CONTRACT_REVISION = 'sha256:91686922e3c5ab6569dbe0abd882fbbbc86c4395a86f151582a2291fb11de036'

__all__ = [
    "SofascoreClient", "AsyncSofascoreClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
