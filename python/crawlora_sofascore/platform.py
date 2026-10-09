"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class SofascoreClient(CrawloraClient):
    """Synchronous SofaScore API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-sofascore-python/0.3.3')
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

    def draft(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-draft', params, response_type=response_type, timeout=timeout, headers=headers)

    def draft_picks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-draft-picks', params, response_type=response_type, timeout=timeout, headers=headers)

    def esports_game(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-esports-game', params, response_type=response_type, timeout=timeout, headers=headers)

    def event(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_at_bat_pitches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-at-bat-pitches', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_at_bats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-at-bats', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_average_positions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-average-positions', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_baseball_top_performers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-baseball-top-performers', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def event_esports_games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-esports-games', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def event_highlights(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-highlights', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_incidents(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-incidents', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_innings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-innings', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_lineups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-lineups', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_managers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-managers', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_odds(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-odds', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_player_heatmap(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-player-heatmap', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_player_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-player-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_point_by_point(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-point-by-point', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_pregame_form(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-pregame-form', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def event_team_heatmap(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-team-heatmap', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_team_streaks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-team-streaks', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_tennis_power(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-tennis-power', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_tv_channels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-tv-channels', params, response_type=response_type, timeout=timeout, headers=headers)

    def event_votes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-event-votes', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def mma_card(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-mma-card', params, response_type=response_type, timeout=timeout, headers=headers)

    def mma_schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-mma-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    def odds_dropping(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-odds-dropping', params, response_type=response_type, timeout=timeout, headers=headers)

    def odds_winning(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-odds-winning', params, response_type=response_type, timeout=timeout, headers=headers)

    def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_attributes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-attributes', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_last_year_summary(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-last-year-summary', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_national_team_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-national-team-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_penalty_history(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-penalty-history', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_ratings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-ratings', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_season_heatmap(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-season-heatmap', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_season_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-season-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_statistical_rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-statistical-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_statistics_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-statistics-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    def player_tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-player-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def referee(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-referee', params, response_type=response_type, timeout=timeout, headers=headers)

    def referee_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-referee-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def referee_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-referee-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def search_typed(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-search-typed', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def stage(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-stage', params, response_type=response_type, timeout=timeout, headers=headers)

    def stage_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-stage-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def stage_driver_performance(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-stage-driver-performance', params, response_type=response_type, timeout=timeout, headers=headers)

    def stage_featured(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-stage-featured', params, response_type=response_type, timeout=timeout, headers=headers)

    def stage_schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-stage-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    def stage_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-stage-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    def stage_standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-stage-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    def stage_substages(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-stage-substages', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def team_achievements(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-achievements', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_goal_distributions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-goal-distributions', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_near_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-near-events', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def team_performance(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-performance', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_player_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-player-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_player_statistics_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-player-statistics-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def team_top_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-top-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

    def team_transfers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-team-transfers', params, response_type=response_type, timeout=timeout, headers=headers)

    def tennis_player_grand_slam_results(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tennis-player-grand-slam-results', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_cuptree(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-cuptree', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-info', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_player_of_the_season(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-player-of-the-season', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def tournament_statistics_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-statistics-info', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_team_of_the_season(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-team-of-the-season', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-teams', params, response_type=response_type, timeout=timeout, headers=headers)

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

    def tournament_venues(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-venues', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_winners(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournament-winners', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournaments_with_feature(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-tournaments-with-feature', params, response_type=response_type, timeout=timeout, headers=headers)

    def trending_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-trending-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def trending_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-trending-players', params, response_type=response_type, timeout=timeout, headers=headers)

    def venue(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-venue', params, response_type=response_type, timeout=timeout, headers=headers)

    def venue_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('sofascore-venue-events', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncSofascoreClient(AsyncCrawloraClient):
    """Asynchronous SofaScore API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-sofascore-python/0.3.3')
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

    async def draft(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-draft', params, response_type=response_type, timeout=timeout, headers=headers)

    async def draft_picks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-draft-picks', params, response_type=response_type, timeout=timeout, headers=headers)

    async def esports_game(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-esports-game', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_at_bat_pitches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-at-bat-pitches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_at_bats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-at-bats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_average_positions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-average-positions', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_baseball_top_performers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-baseball-top-performers', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def event_esports_games(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-esports-games', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def event_highlights(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-highlights', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_incidents(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-incidents', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_innings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-innings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_lineups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-lineups', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_managers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-managers', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_odds(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-odds', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_player_heatmap(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-player-heatmap', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_player_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-player-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_point_by_point(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-point-by-point', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_pregame_form(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-pregame-form', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def event_team_heatmap(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-team-heatmap', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_team_streaks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-team-streaks', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_tennis_power(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-tennis-power', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_tv_channels(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-tv-channels', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event_votes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-event-votes', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def mma_card(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-mma-card', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mma_schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-mma-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    async def odds_dropping(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-odds-dropping', params, response_type=response_type, timeout=timeout, headers=headers)

    async def odds_winning(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-odds-winning', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_attributes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-attributes', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_last_year_summary(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-last-year-summary', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_national_team_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-national-team-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_penalty_history(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-penalty-history', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_ratings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-ratings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_season_heatmap(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-season-heatmap', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_season_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-season-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_statistical_rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-statistical-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_statistics_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-statistics-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    async def player_tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-player-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def referee(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-referee', params, response_type=response_type, timeout=timeout, headers=headers)

    async def referee_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-referee-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def referee_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-referee-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def search_typed(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-search-typed', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def stage(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-stage', params, response_type=response_type, timeout=timeout, headers=headers)

    async def stage_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-stage-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def stage_driver_performance(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-stage-driver-performance', params, response_type=response_type, timeout=timeout, headers=headers)

    async def stage_featured(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-stage-featured', params, response_type=response_type, timeout=timeout, headers=headers)

    async def stage_schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-stage-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    async def stage_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-stage-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    async def stage_standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-stage-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def stage_substages(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-stage-substages', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def team_achievements(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-achievements', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_goal_distributions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-goal-distributions', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_near_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-near-events', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def team_performance(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-performance', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_player_statistics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-player-statistics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_player_statistics_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-player-statistics-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def team_top_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-top-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def team_transfers(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-team-transfers', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tennis_player_grand_slam_results(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tennis-player-grand-slam-results', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_cuptree(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-cuptree', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-info', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_player_of_the_season(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-player-of-the-season', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def tournament_statistics_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-statistics-info', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_team_of_the_season(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-team-of-the-season', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-teams', params, response_type=response_type, timeout=timeout, headers=headers)

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

    async def tournament_venues(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-venues', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_winners(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournament-winners', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournaments_with_feature(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-tournaments-with-feature', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trending_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-trending-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trending_players(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-trending-players', params, response_type=response_type, timeout=timeout, headers=headers)

    async def venue(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-venue', params, response_type=response_type, timeout=timeout, headers=headers)

    async def venue_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('sofascore-venue-events', params, response_type=response_type, timeout=timeout, headers=headers)
