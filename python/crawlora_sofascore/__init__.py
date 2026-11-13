"""Typed SofaScore client for the Crawlora hosted API."""

from .platform import SofascoreClient, AsyncSofascoreClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = SofascoreClient
AsyncClient = AsyncSofascoreClient
__version__ = '0.5.0'
DISPLAY_NAME = 'SofaScore'
PLATFORM = 'sofascore'
CONTRACT_REVISION = 'sha256:da5eb33b004378f90899a9cefef992842f7a32b122e006a31dda22e23a68c5f7'

__all__ = [
    "SofascoreClient", "AsyncSofascoreClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
