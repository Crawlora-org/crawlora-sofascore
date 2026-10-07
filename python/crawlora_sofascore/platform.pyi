from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelSofascoreTournamentSeasonsResponseDoc = TypedDict('ModelSofascoreTournamentSeasonsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentSeasonsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentSeasonsResponse = TypedDict('ModelSofascoreTournamentSeasonsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'seasons': NotRequired[list[ModelSofascoreSeason]],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[int],
}, total=False)

ModelSofascoreSeason = TypedDict('ModelSofascoreSeason', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelSofascoreTeamPlayersResponseDoc = TypedDict('ModelSofascoreTeamPlayersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamPlayersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamPlayersResponse = TypedDict('ModelSofascoreTeamPlayersResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'players': NotRequired[list[ModelSofascoreSquadPlayer]],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
}, total=False)

ModelSofascoreSquadPlayer = TypedDict('ModelSofascoreSquadPlayer', {
    'country': NotRequired[str],
    'date_of_birth': NotRequired[str],
    'height': NotRequired[int],
    'id': NotRequired[int],
    'jersey_number': NotRequired[str],
    'market_value': NotRequired[int],
    'market_value_currency': NotRequired[str],
    'name': NotRequired[str],
    'position': NotRequired[str],
    'preferred_foot': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelSofascoreTeamEventsResponseDoc = TypedDict('ModelSofascoreTeamEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamEventsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamEventsResponse = TypedDict('ModelSofascoreTeamEventsResponse', {
    'count': NotRequired[int],
    'direction': NotRequired[str],
    'events': NotRequired[list[ModelSofascoreEventSummary]],
    'fetched_at': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
}, total=False)

ModelSofascoreEventSummary = TypedDict('ModelSofascoreEventSummary', {
    'away_score': NotRequired[ModelSofascoreScoreLine],
    'away_team': NotRequired[ModelSofascoreTeamRef],
    'home_score': NotRequired[ModelSofascoreScoreLine],
    'home_team': NotRequired[ModelSofascoreTeamRef],
    'id': NotRequired[int],
    'slug': NotRequired[str],
    'start_time': NotRequired[str],
    'start_timestamp': NotRequired[int],
    'status': NotRequired[ModelSofascoreEventStatus],
    'tournament': NotRequired[ModelSofascoreTournamentRef],
    'winner_code': NotRequired[int],
}, total=False)

ModelSofascoreTournamentRef = TypedDict('ModelSofascoreTournamentRef', {
    'category': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'unique_tournament_id': NotRequired[int],
    'unique_tournament_name': NotRequired[str],
}, total=False)

ModelSofascoreEventStatus = TypedDict('ModelSofascoreEventStatus', {
    'code': NotRequired[int],
    'description': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreTeamRef = TypedDict('ModelSofascoreTeamRef', {
    'country': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'national': NotRequired[bool],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelSofascoreScoreLine = TypedDict('ModelSofascoreScoreLine', {
    'current': NotRequired[int],
    'period1': NotRequired[int],
    'period2': NotRequired[int],
}, total=False)

ModelSofascoreTeamResponseDoc = TypedDict('ModelSofascoreTeamResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamResponse = TypedDict('ModelSofascoreTeamResponse', {
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'team': NotRequired[ModelSofascoreTeamDetail],
}, total=False)

ModelSofascoreTeamDetail = TypedDict('ModelSofascoreTeamDetail', {
    'country': NotRequired[str],
    'id': NotRequired[int],
    'manager': NotRequired[str],
    'name': NotRequired[str],
    'national': NotRequired[bool],
    'primary_color': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'tournament_id': NotRequired[int],
    'tournament_name': NotRequired[str],
    'venue': NotRequired[str],
    'venue_capacity': NotRequired[int],
    'venue_city': NotRequired[str],
}, total=False)

ModelSofascoreStandingsResponseDoc = TypedDict('ModelSofascoreStandingsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreStandingsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreStandingsResponse = TypedDict('ModelSofascoreStandingsResponse', {
    'fetched_at': NotRequired[str],
    'groups': NotRequired[list[ModelSofascoreStandingsGroup]],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreStandingsGroup = TypedDict('ModelSofascoreStandingsGroup', {
    'name': NotRequired[str],
    'rows': NotRequired[list[ModelSofascoreStandingsRow]],
}, total=False)

ModelSofascoreStandingsRow = TypedDict('ModelSofascoreStandingsRow', {
    'draws': NotRequired[int],
    'losses': NotRequired[int],
    'matches': NotRequired[int],
    'points': NotRequired[int],
    'position': NotRequired[int],
    'promotion': NotRequired[str],
    'scores_against': NotRequired[int],
    'scores_for': NotRequired[int],
    'team': NotRequired[ModelSofascoreTeamRef],
    'wins': NotRequired[int],
}, total=False)

ModelSofascoreSearchResponseDoc = TypedDict('ModelSofascoreSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreSearchResponse = TypedDict('ModelSofascoreSearchResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelSofascoreSearchResult]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreSearchResult = TypedDict('ModelSofascoreSearchResult', {
    'country': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'team_id': NotRequired[int],
    'team_name': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreRoundEventsResponseDoc = TypedDict('ModelSofascoreRoundEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreRoundEventsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreRoundEventsResponse = TypedDict('ModelSofascoreRoundEventsResponse', {
    'count': NotRequired[int],
    'events': NotRequired[list[ModelSofascoreEventSummary]],
    'fetched_at': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'round': NotRequired[int],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[int],
}, total=False)

ModelSofascorePlayerResponseDoc = TypedDict('ModelSofascorePlayerResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascorePlayerResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascorePlayerResponse = TypedDict('ModelSofascorePlayerResponse', {
    'fetched_at': NotRequired[str],
    'player': NotRequired[ModelSofascorePlayerDetail],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascorePlayerDetail = TypedDict('ModelSofascorePlayerDetail', {
    'country': NotRequired[str],
    'date_of_birth': NotRequired[str],
    'deceased': NotRequired[bool],
    'height': NotRequired[int],
    'id': NotRequired[int],
    'jersey_number': NotRequired[str],
    'market_value': NotRequired[int],
    'market_value_currency': NotRequired[str],
    'name': NotRequired[str],
    'position': NotRequired[str],
    'preferred_foot': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
    'team': NotRequired[ModelSofascoreTeamRef],
}, total=False)

ModelSofascoreLiveEventsResponseDoc = TypedDict('ModelSofascoreLiveEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreLiveEventsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreLiveEventsResponse = TypedDict('ModelSofascoreLiveEventsResponse', {
    'count': NotRequired[int],
    'events': NotRequired[list[ModelSofascoreEventSummary]],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelSofascoreEventStatisticsResponseDoc = TypedDict('ModelSofascoreEventStatisticsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventStatisticsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventStatisticsResponse = TypedDict('ModelSofascoreEventStatisticsResponse', {
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'periods': NotRequired[list[ModelSofascoreStatPeriod]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreStatPeriod = TypedDict('ModelSofascoreStatPeriod', {
    'groups': NotRequired[list[ModelSofascoreStatGroup]],
    'period': NotRequired[str],
}, total=False)

ModelSofascoreStatGroup = TypedDict('ModelSofascoreStatGroup', {
    'items': NotRequired[list[ModelSofascoreStatItem]],
    'name': NotRequired[str],
}, total=False)

ModelSofascoreStatItem = TypedDict('ModelSofascoreStatItem', {
    'away': NotRequired[str],
    'home': NotRequired[str],
    'key': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelSofascoreEventOddsResponseDoc = TypedDict('ModelSofascoreEventOddsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventOddsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventOddsResponse = TypedDict('ModelSofascoreEventOddsResponse', {
    'count': NotRequired[int],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'markets': NotRequired[list[ModelSofascoreOddsMarket]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreOddsMarket = TypedDict('ModelSofascoreOddsMarket', {
    'choices': NotRequired[list[ModelSofascoreOddsChoice]],
    'group': NotRequired[str],
    'name': NotRequired[str],
    'period': NotRequired[str],
    'suspended': NotRequired[bool],
}, total=False)

ModelSofascoreOddsChoice = TypedDict('ModelSofascoreOddsChoice', {
    'name': NotRequired[str],
    'value': NotRequired[str],
    'winning': NotRequired[bool],
}, total=False)

ModelSofascoreEventLineupsResponseDoc = TypedDict('ModelSofascoreEventLineupsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventLineupsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventLineupsResponse = TypedDict('ModelSofascoreEventLineupsResponse', {
    'away': NotRequired[ModelSofascoreTeamLineup],
    'confirmed': NotRequired[bool],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'home': NotRequired[ModelSofascoreTeamLineup],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreTeamLineup = TypedDict('ModelSofascoreTeamLineup', {
    'formation': NotRequired[str],
    'players': NotRequired[list[ModelSofascoreLineupPlayer]],
}, total=False)

ModelSofascoreLineupPlayer = TypedDict('ModelSofascoreLineupPlayer', {
    'jersey_number': NotRequired[str],
    'player': NotRequired[ModelSofascorePlayerRef],
    'position': NotRequired[str],
    'substitute': NotRequired[bool],
}, total=False)

ModelSofascorePlayerRef = TypedDict('ModelSofascorePlayerRef', {
    'country': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'position': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelSofascoreEventIncidentsResponseDoc = TypedDict('ModelSofascoreEventIncidentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventIncidentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventIncidentsResponse = TypedDict('ModelSofascoreEventIncidentsResponse', {
    'count': NotRequired[int],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'incidents': NotRequired[list[ModelSofascoreIncident]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreIncident = TypedDict('ModelSofascoreIncident', {
    'added_time': NotRequired[int],
    'away_score': NotRequired[int],
    'card_color': NotRequired[str],
    'home_score': NotRequired[int],
    'is_home': NotRequired[bool],
    'player': NotRequired[str],
    'player_in': NotRequired[str],
    'player_out': NotRequired[str],
    'reason': NotRequired[str],
    'text': NotRequired[str],
    'time': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreEventH2HresponseDoc = TypedDict('ModelSofascoreEventH2HresponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventH2Hresponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventH2Hresponse = TypedDict('ModelSofascoreEventH2Hresponse', {
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'manager_duel': NotRequired[ModelSofascoreTeamDuel],
    'source_url': NotRequired[str],
    'team_duel': NotRequired[ModelSofascoreTeamDuel],
}, total=False)

ModelSofascoreTeamDuel = TypedDict('ModelSofascoreTeamDuel', {
    'away_wins': NotRequired[int],
    'draws': NotRequired[int],
    'home_wins': NotRequired[int],
}, total=False)

ModelSofascoreEventResponseDoc = TypedDict('ModelSofascoreEventResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventResponse = TypedDict('ModelSofascoreEventResponse', {
    'event': NotRequired[ModelSofascoreEventDetail],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreEventDetail = TypedDict('ModelSofascoreEventDetail', {
    'attendance': NotRequired[int],
    'away_score': NotRequired[ModelSofascoreScoreLine],
    'away_team': NotRequired[ModelSofascoreTeamRef],
    'home_score': NotRequired[ModelSofascoreScoreLine],
    'home_team': NotRequired[ModelSofascoreTeamRef],
    'id': NotRequired[int],
    'referee': NotRequired[ModelSofascoreReferee],
    'slug': NotRequired[str],
    'start_time': NotRequired[str],
    'start_timestamp': NotRequired[int],
    'status': NotRequired[ModelSofascoreEventStatus],
    'tournament': NotRequired[ModelSofascoreTournamentRef],
    'venue': NotRequired[ModelSofascoreVenue],
    'winner_code': NotRequired[int],
}, total=False)

ModelSofascoreVenue = TypedDict('ModelSofascoreVenue', {
    'capacity': NotRequired[int],
    'city': NotRequired[str],
    'country': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelSofascoreReferee = TypedDict('ModelSofascoreReferee', {
    'country': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

SofascoreEventResponse = ModelSofascoreEventResponseDoc
SofascoreEventParams = TypedDict('SofascoreEventParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventH2hResponse = ModelSofascoreEventH2HresponseDoc
SofascoreEventH2hParams = TypedDict('SofascoreEventH2hParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventIncidentsResponse = ModelSofascoreEventIncidentsResponseDoc
SofascoreEventIncidentsParams = TypedDict('SofascoreEventIncidentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventLineupsResponse = ModelSofascoreEventLineupsResponseDoc
SofascoreEventLineupsParams = TypedDict('SofascoreEventLineupsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventOddsResponse = ModelSofascoreEventOddsResponseDoc
SofascoreEventOddsParams = TypedDict('SofascoreEventOddsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventStatisticsResponse = ModelSofascoreEventStatisticsResponseDoc
SofascoreEventStatisticsParams = TypedDict('SofascoreEventStatisticsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreLiveEventsResponse = ModelSofascoreLiveEventsResponseDoc
SofascoreLiveEventsParams = TypedDict('SofascoreLiveEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['football', 'basketball', 'tennis']],
}, total=False)

SofascorePlayerResponse = ModelSofascorePlayerResponseDoc
SofascorePlayerParams = TypedDict('SofascorePlayerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreRoundEventsResponse = ModelSofascoreRoundEventsResponseDoc
SofascoreRoundEventsParams = TypedDict('SofascoreRoundEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
    'round': Required[int],
}, total=False)

SofascoreSearchResponse = ModelSofascoreSearchResponseDoc
SofascoreSearchParams = TypedDict('SofascoreSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

SofascoreStandingsResponse = ModelSofascoreStandingsResponseDoc
SofascoreStandingsParams = TypedDict('SofascoreStandingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
    'type': Required[Literal['total', 'home', 'away']],
}, total=False)

SofascoreTeamResponse = ModelSofascoreTeamResponseDoc
SofascoreTeamParams = TypedDict('SofascoreTeamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTeamEventsResponse = ModelSofascoreTeamEventsResponseDoc
SofascoreTeamEventsParams = TypedDict('SofascoreTeamEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'direction': Required[Literal['next', 'last']],
    'page': NotRequired[int],
}, total=False)

SofascoreTeamPlayersResponse = ModelSofascoreTeamPlayersResponseDoc
SofascoreTeamPlayersParams = TypedDict('SofascoreTeamPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTournamentSeasonsResponse = ModelSofascoreTournamentSeasonsResponseDoc
SofascoreTournamentSeasonsParams = TypedDict('SofascoreTournamentSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

class SofascoreGroup:
    def event(self, **params: Unpack[SofascoreEventParams]) -> SofascoreEventResponse: ...
    def event_h2h(self, **params: Unpack[SofascoreEventH2hParams]) -> SofascoreEventH2hResponse: ...
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsParams]) -> SofascoreEventIncidentsResponse: ...
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsParams]) -> SofascoreEventLineupsResponse: ...
    def event_odds(self, **params: Unpack[SofascoreEventOddsParams]) -> SofascoreEventOddsResponse: ...
    def event_statistics(self, **params: Unpack[SofascoreEventStatisticsParams]) -> SofascoreEventStatisticsResponse: ...
    def live_events(self, **params: Unpack[SofascoreLiveEventsParams]) -> SofascoreLiveEventsResponse: ...
    def player(self, **params: Unpack[SofascorePlayerParams]) -> SofascorePlayerResponse: ...
    def round_events(self, **params: Unpack[SofascoreRoundEventsParams]) -> SofascoreRoundEventsResponse: ...
    def search(self, **params: Unpack[SofascoreSearchParams]) -> SofascoreSearchResponse: ...
    def standings(self, **params: Unpack[SofascoreStandingsParams]) -> SofascoreStandingsResponse: ...
    def team(self, **params: Unpack[SofascoreTeamParams]) -> SofascoreTeamResponse: ...
    def team_events(self, **params: Unpack[SofascoreTeamEventsParams]) -> SofascoreTeamEventsResponse: ...
    def team_players(self, **params: Unpack[SofascoreTeamPlayersParams]) -> SofascoreTeamPlayersResponse: ...
    def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsParams]) -> SofascoreTournamentSeasonsResponse: ...

OperationId = Literal[
    'sofascore-event',
    'sofascore-event-h2h',
    'sofascore-event-incidents',
    'sofascore-event-lineups',
    'sofascore-event-odds',
    'sofascore-event-statistics',
    'sofascore-live-events',
    'sofascore-player',
    'sofascore-round-events',
    'sofascore-search',
    'sofascore-standings',
    'sofascore-team',
    'sofascore-team-events',
    'sofascore-team-players',
    'sofascore-tournament-seasons',
]

class CrawloraClient:
    sofascore: SofascoreGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event'],
        params: SofascoreEventParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-h2h'],
        params: SofascoreEventH2hParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventH2hResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-incidents'],
        params: SofascoreEventIncidentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventIncidentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-lineups'],
        params: SofascoreEventLineupsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventLineupsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-odds'],
        params: SofascoreEventOddsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventOddsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-statistics'],
        params: SofascoreEventStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventStatisticsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-live-events'],
        params: SofascoreLiveEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreLiveEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-player'],
        params: SofascorePlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-round-events'],
        params: SofascoreRoundEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreRoundEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-search'],
        params: SofascoreSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-standings'],
        params: SofascoreStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStandingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-team'],
        params: SofascoreTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-team-events'],
        params: SofascoreTeamEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-team-players'],
        params: SofascoreTeamPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-tournament-seasons'],
        params: SofascoreTournamentSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentSeasonsResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event'],
        params: SofascoreEventParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-h2h'],
        params: SofascoreEventH2hParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventH2hResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-incidents'],
        params: SofascoreEventIncidentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventIncidentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-lineups'],
        params: SofascoreEventLineupsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventLineupsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-odds'],
        params: SofascoreEventOddsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventOddsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-statistics'],
        params: SofascoreEventStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventStatisticsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-live-events'],
        params: SofascoreLiveEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreLiveEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-player'],
        params: SofascorePlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-round-events'],
        params: SofascoreRoundEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreRoundEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-search'],
        params: SofascoreSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-standings'],
        params: SofascoreStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStandingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-team'],
        params: SofascoreTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-team-events'],
        params: SofascoreTeamEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-team-players'],
        params: SofascoreTeamPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-tournament-seasons'],
        params: SofascoreTournamentSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentSeasonsResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class SofascoreClient(CrawloraClient):
    def __enter__(self) -> SofascoreClient: ...
    sofascore: SofascoreGroup
    @overload
    def event(self, **params: Unpack[SofascoreEventStreamParams]) -> BinaryIO: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventTextResponseParams]) -> str: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventParams]) -> SofascoreEventResponse: ...
    @overload
    def event_h2h(self, **params: Unpack[SofascoreEventH2hStreamParams]) -> BinaryIO: ...
    @overload
    def event_h2h(self, **params: Unpack[SofascoreEventH2hTextResponseParams]) -> str: ...
    @overload
    def event_h2h(self, **params: Unpack[SofascoreEventH2hParams]) -> SofascoreEventH2hResponse: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsStreamParams]) -> BinaryIO: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsTextResponseParams]) -> str: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsParams]) -> SofascoreEventIncidentsResponse: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsStreamParams]) -> BinaryIO: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsTextResponseParams]) -> str: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsParams]) -> SofascoreEventLineupsResponse: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsStreamParams]) -> BinaryIO: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsTextResponseParams]) -> str: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsParams]) -> SofascoreEventOddsResponse: ...
    @overload
    def event_statistics(self, **params: Unpack[SofascoreEventStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def event_statistics(self, **params: Unpack[SofascoreEventStatisticsTextResponseParams]) -> str: ...
    @overload
    def event_statistics(self, **params: Unpack[SofascoreEventStatisticsParams]) -> SofascoreEventStatisticsResponse: ...
    @overload
    def live_events(self, **params: Unpack[SofascoreLiveEventsStreamParams]) -> BinaryIO: ...
    @overload
    def live_events(self, **params: Unpack[SofascoreLiveEventsTextResponseParams]) -> str: ...
    @overload
    def live_events(self, **params: Unpack[SofascoreLiveEventsParams]) -> SofascoreLiveEventsResponse: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerParams]) -> SofascorePlayerResponse: ...
    @overload
    def round_events(self, **params: Unpack[SofascoreRoundEventsStreamParams]) -> BinaryIO: ...
    @overload
    def round_events(self, **params: Unpack[SofascoreRoundEventsTextResponseParams]) -> str: ...
    @overload
    def round_events(self, **params: Unpack[SofascoreRoundEventsParams]) -> SofascoreRoundEventsResponse: ...
    @overload
    def search(self, **params: Unpack[SofascoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[SofascoreSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[SofascoreSearchParams]) -> SofascoreSearchResponse: ...
    @overload
    def standings(self, **params: Unpack[SofascoreStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def standings(self, **params: Unpack[SofascoreStandingsTextResponseParams]) -> str: ...
    @overload
    def standings(self, **params: Unpack[SofascoreStandingsParams]) -> SofascoreStandingsResponse: ...
    @overload
    def team(self, **params: Unpack[SofascoreTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[SofascoreTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[SofascoreTeamParams]) -> SofascoreTeamResponse: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsStreamParams]) -> BinaryIO: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsTextResponseParams]) -> str: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsParams]) -> SofascoreTeamEventsResponse: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersTextResponseParams]) -> str: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersParams]) -> SofascoreTeamPlayersResponse: ...
    @overload
    def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsParams]) -> SofascoreTournamentSeasonsResponse: ...

class AsyncSofascoreClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncSofascoreClient: ...
    sofascore: _AsyncSofascoreGroup
    @overload
    async def event(self, **params: Unpack[SofascoreEventStreamParams]) -> BinaryIO: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventTextResponseParams]) -> str: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventParams]) -> SofascoreEventResponse: ...
    @overload
    async def event_h2h(self, **params: Unpack[SofascoreEventH2hStreamParams]) -> BinaryIO: ...
    @overload
    async def event_h2h(self, **params: Unpack[SofascoreEventH2hTextResponseParams]) -> str: ...
    @overload
    async def event_h2h(self, **params: Unpack[SofascoreEventH2hParams]) -> SofascoreEventH2hResponse: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsTextResponseParams]) -> str: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsParams]) -> SofascoreEventIncidentsResponse: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsTextResponseParams]) -> str: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsParams]) -> SofascoreEventLineupsResponse: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsTextResponseParams]) -> str: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsParams]) -> SofascoreEventOddsResponse: ...
    @overload
    async def event_statistics(self, **params: Unpack[SofascoreEventStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_statistics(self, **params: Unpack[SofascoreEventStatisticsTextResponseParams]) -> str: ...
    @overload
    async def event_statistics(self, **params: Unpack[SofascoreEventStatisticsParams]) -> SofascoreEventStatisticsResponse: ...
    @overload
    async def live_events(self, **params: Unpack[SofascoreLiveEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_events(self, **params: Unpack[SofascoreLiveEventsTextResponseParams]) -> str: ...
    @overload
    async def live_events(self, **params: Unpack[SofascoreLiveEventsParams]) -> SofascoreLiveEventsResponse: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerParams]) -> SofascorePlayerResponse: ...
    @overload
    async def round_events(self, **params: Unpack[SofascoreRoundEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def round_events(self, **params: Unpack[SofascoreRoundEventsTextResponseParams]) -> str: ...
    @overload
    async def round_events(self, **params: Unpack[SofascoreRoundEventsParams]) -> SofascoreRoundEventsResponse: ...
    @overload
    async def search(self, **params: Unpack[SofascoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[SofascoreSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[SofascoreSearchParams]) -> SofascoreSearchResponse: ...
    @overload
    async def standings(self, **params: Unpack[SofascoreStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def standings(self, **params: Unpack[SofascoreStandingsTextResponseParams]) -> str: ...
    @overload
    async def standings(self, **params: Unpack[SofascoreStandingsParams]) -> SofascoreStandingsResponse: ...
    @overload
    async def team(self, **params: Unpack[SofascoreTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[SofascoreTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[SofascoreTeamParams]) -> SofascoreTeamResponse: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsTextResponseParams]) -> str: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsParams]) -> SofascoreTeamEventsResponse: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersTextResponseParams]) -> str: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersParams]) -> SofascoreTeamPlayersResponse: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsParams]) -> SofascoreTournamentSeasonsResponse: ...

class _AsyncSofascoreGroup:
    @overload
    async def event(self, **params: Unpack[SofascoreEventStreamParams]) -> BinaryIO: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventTextResponseParams]) -> str: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventParams]) -> SofascoreEventResponse: ...
    @overload
    async def event_h2h(self, **params: Unpack[SofascoreEventH2hStreamParams]) -> BinaryIO: ...
    @overload
    async def event_h2h(self, **params: Unpack[SofascoreEventH2hTextResponseParams]) -> str: ...
    @overload
    async def event_h2h(self, **params: Unpack[SofascoreEventH2hParams]) -> SofascoreEventH2hResponse: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsTextResponseParams]) -> str: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsParams]) -> SofascoreEventIncidentsResponse: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsTextResponseParams]) -> str: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsParams]) -> SofascoreEventLineupsResponse: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsTextResponseParams]) -> str: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsParams]) -> SofascoreEventOddsResponse: ...
    @overload
    async def event_statistics(self, **params: Unpack[SofascoreEventStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_statistics(self, **params: Unpack[SofascoreEventStatisticsTextResponseParams]) -> str: ...
    @overload
    async def event_statistics(self, **params: Unpack[SofascoreEventStatisticsParams]) -> SofascoreEventStatisticsResponse: ...
    @overload
    async def live_events(self, **params: Unpack[SofascoreLiveEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_events(self, **params: Unpack[SofascoreLiveEventsTextResponseParams]) -> str: ...
    @overload
    async def live_events(self, **params: Unpack[SofascoreLiveEventsParams]) -> SofascoreLiveEventsResponse: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerParams]) -> SofascorePlayerResponse: ...
    @overload
    async def round_events(self, **params: Unpack[SofascoreRoundEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def round_events(self, **params: Unpack[SofascoreRoundEventsTextResponseParams]) -> str: ...
    @overload
    async def round_events(self, **params: Unpack[SofascoreRoundEventsParams]) -> SofascoreRoundEventsResponse: ...
    @overload
    async def search(self, **params: Unpack[SofascoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[SofascoreSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[SofascoreSearchParams]) -> SofascoreSearchResponse: ...
    @overload
    async def standings(self, **params: Unpack[SofascoreStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def standings(self, **params: Unpack[SofascoreStandingsTextResponseParams]) -> str: ...
    @overload
    async def standings(self, **params: Unpack[SofascoreStandingsParams]) -> SofascoreStandingsResponse: ...
    @overload
    async def team(self, **params: Unpack[SofascoreTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[SofascoreTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[SofascoreTeamParams]) -> SofascoreTeamResponse: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsTextResponseParams]) -> str: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsParams]) -> SofascoreTeamEventsResponse: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersTextResponseParams]) -> str: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersParams]) -> SofascoreTeamPlayersResponse: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsParams]) -> SofascoreTournamentSeasonsResponse: ...

SofascoreEventTextResponseParams = TypedDict('SofascoreEventTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventStreamParams = TypedDict('SofascoreEventStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventH2hTextResponseParams = TypedDict('SofascoreEventH2hTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventH2hStreamParams = TypedDict('SofascoreEventH2hStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventIncidentsTextResponseParams = TypedDict('SofascoreEventIncidentsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventIncidentsStreamParams = TypedDict('SofascoreEventIncidentsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventLineupsTextResponseParams = TypedDict('SofascoreEventLineupsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventLineupsStreamParams = TypedDict('SofascoreEventLineupsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventOddsTextResponseParams = TypedDict('SofascoreEventOddsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventOddsStreamParams = TypedDict('SofascoreEventOddsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventStatisticsTextResponseParams = TypedDict('SofascoreEventStatisticsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventStatisticsStreamParams = TypedDict('SofascoreEventStatisticsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreLiveEventsTextResponseParams = TypedDict('SofascoreLiveEventsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['football', 'basketball', 'tennis']],
}, total=False)

SofascoreLiveEventsStreamParams = TypedDict('SofascoreLiveEventsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['football', 'basketball', 'tennis']],
}, total=False)

SofascorePlayerTextResponseParams = TypedDict('SofascorePlayerTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascorePlayerStreamParams = TypedDict('SofascorePlayerStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreRoundEventsTextResponseParams = TypedDict('SofascoreRoundEventsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
    'round': Required[int],
}, total=False)

SofascoreRoundEventsStreamParams = TypedDict('SofascoreRoundEventsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
    'round': Required[int],
}, total=False)

SofascoreSearchTextResponseParams = TypedDict('SofascoreSearchTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

SofascoreSearchStreamParams = TypedDict('SofascoreSearchStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

SofascoreStandingsTextResponseParams = TypedDict('SofascoreStandingsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
    'type': Required[Literal['total', 'home', 'away']],
}, total=False)

SofascoreStandingsStreamParams = TypedDict('SofascoreStandingsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
    'type': Required[Literal['total', 'home', 'away']],
}, total=False)

SofascoreTeamTextResponseParams = TypedDict('SofascoreTeamTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTeamStreamParams = TypedDict('SofascoreTeamStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTeamEventsTextResponseParams = TypedDict('SofascoreTeamEventsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'direction': Required[Literal['next', 'last']],
    'page': NotRequired[int],
}, total=False)

SofascoreTeamEventsStreamParams = TypedDict('SofascoreTeamEventsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'direction': Required[Literal['next', 'last']],
    'page': NotRequired[int],
}, total=False)

SofascoreTeamPlayersTextResponseParams = TypedDict('SofascoreTeamPlayersTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTeamPlayersStreamParams = TypedDict('SofascoreTeamPlayersStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTournamentSeasonsTextResponseParams = TypedDict('SofascoreTournamentSeasonsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTournamentSeasonsStreamParams = TypedDict('SofascoreTournamentSeasonsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)
