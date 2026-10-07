from .platform import SofascoreClient as SofascoreClient
from .platform import AsyncSofascoreClient as AsyncSofascoreClient
Client = SofascoreClient
AsyncClient = AsyncSofascoreClient
from .client import CrawloraClientError as CrawloraClientError, CrawloraError as CrawloraError, CrawloraNetworkError as CrawloraNetworkError, CrawloraServerError as CrawloraServerError
from .operations import OPERATION_COUNT as OPERATION_COUNT, OPERATION_IDS as OPERATION_IDS, PLATFORM as PLATFORM
__version__: str
DISPLAY_NAME: str
CONTRACT_REVISION: str
__all__ = ['SofascoreClient', 'AsyncSofascoreClient', 'Client', 'AsyncClient', 'CrawloraError', 'CrawloraClientError', 'CrawloraServerError', 'CrawloraNetworkError', 'DISPLAY_NAME', 'PLATFORM', 'CONTRACT_REVISION', 'OPERATION_COUNT', 'OPERATION_IDS', '__version__']
