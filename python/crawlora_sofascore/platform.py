"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class SofascoreClient(CrawloraClient):
    """Synchronous SofaScore API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-sofascore-python/0.2.0')
        super().__init__(*args, **kwargs)

    def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def category_tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-category-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

    def event(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_best_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-best-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_graph(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-graph', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def event_player_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-player-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_shotmap(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-shotmap', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def manager(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-manager', params, response_type=response_type, timeout=timeout, headers=headers)

    def manager_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-manager-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_season_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-season-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_statistics_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-statistics-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_transfers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-transfers', params, response_type=response_type, timeout=timeout, headers=headers)

    def ranking_types(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-ranking-types', params, response_type=response_type, timeout=timeout, headers=headers)

    def rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    def round_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-round-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def scheduled_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-scheduled-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def scheduled_tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-scheduled-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def season_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-season-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def sports(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-sports', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def team_of_the_week(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-of-the-week', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_of_the_week_periods(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-of-the-week-periods', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_season_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-season-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_statistics_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-statistics-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_transfers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-transfers', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-info', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_player_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-player-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_rounds(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-rounds', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_top_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-top-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_top_teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-top-teams', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncSofascoreClient(AsyncCrawloraClient):
    """Asynchronous SofaScore API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-sofascore-python/0.2.0')
        super().__init__(*args, **kwargs)

    async def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def category_tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-category-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_best_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-best-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_graph(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-graph', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def event_player_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-player-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_shotmap(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-shotmap', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def manager(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-manager', params, response_type=response_type, timeout=timeout, headers=headers)

    async def manager_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-manager-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_season_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-season-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_statistics_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-statistics-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_transfers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-transfers', params, response_type=response_type, timeout=timeout, headers=headers)

    async def ranking_types(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-ranking-types', params, response_type=response_type, timeout=timeout, headers=headers)

    async def rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def round_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-round-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def scheduled_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-scheduled-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def scheduled_tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-scheduled-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def season_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-season-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sports(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-sports', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def team_of_the_week(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-of-the-week', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_of_the_week_periods(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-of-the-week-periods', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_season_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-season-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_statistics_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-statistics-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_transfers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-transfers', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-info', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_player_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-player-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_rounds(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-rounds', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_top_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-top-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_top_teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-top-teams', params, response_type=response_type, timeout=timeout, headers=headers)
