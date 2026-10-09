"""Typed SofaScore client for the Crawlora hosted API."""

from .platform import SofascoreClient, AsyncSofascoreClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = SofascoreClient
AsyncClient = AsyncSofascoreClient
__version__ = '0.3.1'
DISPLAY_NAME = 'SofaScore'
PLATFORM = 'sofascore'
CONTRACT_REVISION = 'sha256:645115670262bb86bf9c49f16ddbfdd94bbec67befb2aa8497f10f86ee2d5e46'

__all__ = [
    "SofascoreClient", "AsyncSofascoreClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
