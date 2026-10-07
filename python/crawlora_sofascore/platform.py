"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class SofascoreClient(CrawloraClient):
    """Synchronous SofaScore API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-sofascore-python/0.1.0')
        super().__init__(*args, **kwargs)

    def event(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_h2h(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-h2h', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_incidents(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-incidents', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_lineups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-lineups', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_odds(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-odds', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    def live_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-live-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player', params, response_type=response_type, timeout=timeout, headers=headers)

    def round_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-round-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncSofascoreClient(AsyncCrawloraClient):
    """Asynchronous SofaScore API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-sofascore-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def event(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_h2h(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-h2h', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_incidents(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-incidents', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_lineups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-lineups', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_odds(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-odds', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-live-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player', params, response_type=response_type, timeout=timeout, headers=headers)

    async def round_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-round-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-seasons', params, response_type=response_type, timeout=timeout, headers=headers)
