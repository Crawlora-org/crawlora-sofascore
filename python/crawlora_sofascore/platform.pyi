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

ModelSofascoreTournamentTopTeamsResponseDoc = TypedDict('ModelSofascoreTournamentTopTeamsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentTopTeamsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentTopTeamsResponse = TypedDict('ModelSofascoreTournamentTopTeamsResponse', {
    'categories': NotRequired[list[ModelSofascoreTopTeamCategory]],
    'category_count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
    'tournament_id': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreTopTeamCategory = TypedDict('ModelSofascoreTopTeamCategory', {
    'count': NotRequired[int],
    'key': NotRequired[str],
    'teams': NotRequired[list[ModelSofascoreTopTeamEntry]],
}, total=False)

ModelSofascoreTopTeamEntry = TypedDict('ModelSofascoreTopTeamEntry', {
    'details': NotRequired[dict[str, float]],
    'matches': NotRequired[int],
    'rank': NotRequired[int],
    'team': NotRequired[ModelSofascoreTeamRef],
    'value': NotRequired[float],
}, total=False)

ModelSofascoreTeamRef = TypedDict('ModelSofascoreTeamRef', {
    'country': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'national': NotRequired[bool],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelSofascoreTournamentTopPlayersResponseDoc = TypedDict('ModelSofascoreTournamentTopPlayersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentTopPlayersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentTopPlayersResponse = TypedDict('ModelSofascoreTournamentTopPlayersResponse', {
    'categories': NotRequired[list[ModelSofascoreTopPlayerCategory]],
    'category_count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
    'tournament_id': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreTopPlayerCategory = TypedDict('ModelSofascoreTopPlayerCategory', {
    'count': NotRequired[int],
    'key': NotRequired[str],
    'players': NotRequired[list[ModelSofascoreTopPlayerEntry]],
}, total=False)

ModelSofascoreTopPlayerEntry = TypedDict('ModelSofascoreTopPlayerEntry', {
    'appearances': NotRequired[int],
    'details': NotRequired[dict[str, float]],
    'played_enough': NotRequired[bool],
    'player': NotRequired[ModelSofascorePlayerRef],
    'rank': NotRequired[int],
    'team': NotRequired[ModelSofascoreTeamRef],
    'value': NotRequired[float],
}, total=False)

ModelSofascorePlayerRef = TypedDict('ModelSofascorePlayerRef', {
    'country': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'position': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
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

ModelSofascoreTournamentRoundsResponseDoc = TypedDict('ModelSofascoreTournamentRoundsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentRoundsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentRoundsResponse = TypedDict('ModelSofascoreTournamentRoundsResponse', {
    'count': NotRequired[int],
    'current_round': NotRequired[ModelSofascoreRoundRef],
    'fetched_at': NotRequired[str],
    'rounds': NotRequired[list[ModelSofascoreRoundRef]],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[int],
}, total=False)

ModelSofascoreRoundRef = TypedDict('ModelSofascoreRoundRef', {
    'name': NotRequired[str],
    'prefix': NotRequired[str],
    'round': NotRequired[int],
    'slug': NotRequired[str],
}, total=False)

ModelSofascoreTournamentPlayerStatisticsResponseDoc = TypedDict('ModelSofascoreTournamentPlayerStatisticsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentPlayerStatisticsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentPlayerStatisticsResponse = TypedDict('ModelSofascoreTournamentPlayerStatisticsResponse', {
    'accumulation': NotRequired[str],
    'count': NotRequired[int],
    'direction': NotRequired[str],
    'fetched_at': NotRequired[str],
    'group': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
    'order': NotRequired[str],
    'page': NotRequired[int],
    'players': NotRequired[list[ModelSofascorePlayerStatisticsRow]],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'total_pages': NotRequired[int],
    'tournament_id': NotRequired[int],
}, total=False)

ModelSofascorePlayerStatisticsRow = TypedDict('ModelSofascorePlayerStatisticsRow', {
    'player': NotRequired[ModelSofascorePlayerRef],
    'rank': NotRequired[int],
    'statistics': NotRequired[dict[str, float]],
    'team': NotRequired[ModelSofascoreTeamRef],
}, total=False)

ModelSofascoreTournamentInfoResponseDoc = TypedDict('ModelSofascoreTournamentInfoResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentInfoResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentInfoResponse = TypedDict('ModelSofascoreTournamentInfoResponse', {
    'fetched_at': NotRequired[str],
    'season': NotRequired[ModelSofascoreSeasonInfo],
    'season_id': NotRequired[int],
    'season_source_url': NotRequired[str],
    'source_url': NotRequired[str],
    'tournament': NotRequired[ModelSofascoreTournamentDetail],
    'tournament_id': NotRequired[int],
}, total=False)

ModelSofascoreTournamentDetail = TypedDict('ModelSofascoreTournamentDetail', {
    'category': NotRequired[str],
    'current_season_end': NotRequired[str],
    'current_season_start': NotRequired[str],
    'gender': NotRequired[str],
    'has_groups': NotRequired[bool],
    'has_playoff_series': NotRequired[bool],
    'has_rounds': NotRequired[bool],
    'id': NotRequired[int],
    'linked_tournaments': NotRequired[list[ModelSofascoreCompetitionRef]],
    'lower_divisions': NotRequired[list[ModelSofascoreCompetitionRef]],
    'most_titles': NotRequired[int],
    'most_titles_teams': NotRequired[list[ModelSofascoreTeamRef]],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'tier': NotRequired[int],
    'title_holder': NotRequired[ModelSofascoreTeamRef],
    'title_holder_titles': NotRequired[int],
    'upper_divisions': NotRequired[list[ModelSofascoreCompetitionRef]],
}, total=False)

ModelSofascoreCompetitionRef = TypedDict('ModelSofascoreCompetitionRef', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelSofascoreSeasonInfo = TypedDict('ModelSofascoreSeasonInfo', {
    'away_team_wins': NotRequired[int],
    'draws': NotRequired[int],
    'goals': NotRequired[int],
    'home_team_wins': NotRequired[int],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'newcomers_lower_division': NotRequired[list[ModelSofascoreTeamRef]],
    'newcomers_other': NotRequired[list[ModelSofascoreTeamRef]],
    'newcomers_upper_division': NotRequired[list[ModelSofascoreTeamRef]],
    'number_of_competitors': NotRequired[int],
    'red_cards': NotRequired[int],
    'year': NotRequired[str],
    'yellow_cards': NotRequired[int],
}, total=False)

ModelSofascoreTeamTransfersResponseDoc = TypedDict('ModelSofascoreTeamTransfersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamTransfersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamTransfersResponse = TypedDict('ModelSofascoreTeamTransfersResponse', {
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
    'transfers_in': NotRequired[list[ModelSofascoreTransfer]],
    'transfers_out': NotRequired[list[ModelSofascoreTransfer]],
}, total=False)

ModelSofascoreTransfer = TypedDict('ModelSofascoreTransfer', {
    'fee': NotRequired[int],
    'fee_currency': NotRequired[str],
    'fee_description': NotRequired[str],
    'from_team': NotRequired[ModelSofascoreTeamRef],
    'from_team_name': NotRequired[str],
    'id': NotRequired[int],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'to_team': NotRequired[ModelSofascoreTeamRef],
    'to_team_name': NotRequired[str],
    'transfer_date': NotRequired[str],
    'transfer_timestamp': NotRequired[int],
    'type_code': NotRequired[int],
}, total=False)

ModelSofascorePlayerBrief = TypedDict('ModelSofascorePlayerBrief', {
    'id': NotRequired[int],
    'jersey_number': NotRequired[str],
    'name': NotRequired[str],
    'position': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelSofascoreTeamStatisticsSeasonsResponseDoc = TypedDict('ModelSofascoreTeamStatisticsSeasonsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamStatisticsSeasonsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamStatisticsSeasonsResponse = TypedDict('ModelSofascoreTeamStatisticsSeasonsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
    'tournaments': NotRequired[list[ModelSofascoreStatisticsTournament]],
}, total=False)

ModelSofascoreStatisticsTournament = TypedDict('ModelSofascoreStatisticsTournament', {
    'category': NotRequired[str],
    'name': NotRequired[str],
    'seasons': NotRequired[list[ModelSofascoreStatisticsSeason]],
    'slug': NotRequired[str],
    'unique_tournament_id': NotRequired[int],
}, total=False)

ModelSofascoreStatisticsSeason = TypedDict('ModelSofascoreStatisticsSeason', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'types': NotRequired[list[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']]],
    'year': NotRequired[str],
}, total=False)

ModelSofascoreTeamSeasonStatisticsResponseDoc = TypedDict('ModelSofascoreTeamSeasonStatisticsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamSeasonStatisticsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamSeasonStatisticsResponse = TypedDict('ModelSofascoreTeamSeasonStatisticsResponse', {
    'fetched_at': NotRequired[str],
    'season': NotRequired[int],
    'source_url': NotRequired[str],
    'statistics': NotRequired[dict[str, float]],
    'team_id': NotRequired[int],
    'tournament_id': NotRequired[int],
    'type': NotRequired[str],
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

ModelSofascoreTeamOfTheWeekPeriodsResponseDoc = TypedDict('ModelSofascoreTeamOfTheWeekPeriodsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamOfTheWeekPeriodsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamOfTheWeekPeriodsResponse = TypedDict('ModelSofascoreTeamOfTheWeekPeriodsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'periods': NotRequired[list[ModelSofascoreTeamOfTheWeekPeriod]],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[int],
}, total=False)

ModelSofascoreTeamOfTheWeekPeriod = TypedDict('ModelSofascoreTeamOfTheWeekPeriod', {
    'created_at': NotRequired[str],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'round': NotRequired[int],
    'round_name': NotRequired[str],
    'sequence': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreTeamOfTheWeekResponseDoc = TypedDict('ModelSofascoreTeamOfTheWeekResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamOfTheWeekResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamOfTheWeekResponse = TypedDict('ModelSofascoreTeamOfTheWeekResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'formation': NotRequired[str],
    'period': NotRequired[ModelSofascoreTeamOfTheWeekPeriod],
    'players': NotRequired[list[ModelSofascoreTeamOfTheWeekPlayer]],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[int],
}, total=False)

ModelSofascoreTeamOfTheWeekPlayer = TypedDict('ModelSofascoreTeamOfTheWeekPlayer', {
    'event': NotRequired[ModelSofascoreEventSummary],
    'jersey_number': NotRequired[str],
    'order': NotRequired[int],
    'player': NotRequired[ModelSofascorePlayerRef],
    'rating': NotRequired[float],
    'team': NotRequired[ModelSofascoreTeamRef],
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

ModelSofascoreScoreLine = TypedDict('ModelSofascoreScoreLine', {
    'current': NotRequired[int],
    'period1': NotRequired[int],
    'period2': NotRequired[int],
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

ModelSofascoreSportsResponseDoc = TypedDict('ModelSofascoreSportsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreSportsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreSportsResponse = TypedDict('ModelSofascoreSportsResponse', {
    'count': NotRequired[int],
    'counts_available': NotRequired[bool],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'sports': NotRequired[list[ModelSofascoreSportEntry]],
}, total=False)

ModelSofascoreSportEntry = TypedDict('ModelSofascoreSportEntry', {
    'key': NotRequired[str],
    'live_events': NotRequired[int],
    'name': NotRequired[str],
    'total_events': NotRequired[int],
}, total=False)

ModelSofascoreSeasonEventsResponseDoc = TypedDict('ModelSofascoreSeasonEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreSeasonEventsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreSeasonEventsResponse = TypedDict('ModelSofascoreSeasonEventsResponse', {
    'count': NotRequired[int],
    'direction': NotRequired[str],
    'events': NotRequired[list[ModelSofascoreSeasonEvent]],
    'fetched_at': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'page': NotRequired[int],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[int],
}, total=False)

ModelSofascoreSeasonEvent = TypedDict('ModelSofascoreSeasonEvent', {
    'away_score': NotRequired[ModelSofascoreScoreLine],
    'away_team': NotRequired[ModelSofascoreTeamRef],
    'home_score': NotRequired[ModelSofascoreScoreLine],
    'home_team': NotRequired[ModelSofascoreTeamRef],
    'id': NotRequired[int],
    'round': NotRequired[int],
    'round_name': NotRequired[str],
    'slug': NotRequired[str],
    'start_time': NotRequired[str],
    'start_timestamp': NotRequired[int],
    'status': NotRequired[ModelSofascoreEventStatus],
    'tournament': NotRequired[ModelSofascoreTournamentRef],
    'winner_code': NotRequired[int],
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

ModelSofascoreScheduledTournamentsResponseDoc = TypedDict('ModelSofascoreScheduledTournamentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreScheduledTournamentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreScheduledTournamentsResponse = TypedDict('ModelSofascoreScheduledTournamentsResponse', {
    'count': NotRequired[int],
    'date': NotRequired[str],
    'fetched_at': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
    'tournaments': NotRequired[list[ModelSofascoreScheduledTournament]],
}, total=False)

ModelSofascoreScheduledTournament = TypedDict('ModelSofascoreScheduledTournament', {
    'category_id': NotRequired[int],
    'category_name': NotRequired[str],
    'event_count': NotRequired[int],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'unique_tournament_id': NotRequired[int],
    'unique_tournament_name': NotRequired[str],
}, total=False)

ModelSofascoreScheduledEventsResponseDoc = TypedDict('ModelSofascoreScheduledEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreScheduledEventsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreScheduledEventsResponse = TypedDict('ModelSofascoreScheduledEventsResponse', {
    'category_id': NotRequired[int],
    'count': NotRequired[int],
    'date': NotRequired[str],
    'events': NotRequired[list[ModelSofascoreEventSummary]],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
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
    'prefix': NotRequired[str],
    'round': NotRequired[int],
    'season_id': NotRequired[int],
    'slug': NotRequired[str],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[int],
}, total=False)

ModelSofascoreRankingsResponseDoc = TypedDict('ModelSofascoreRankingsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreRankingsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreRankingsResponse = TypedDict('ModelSofascoreRankingsResponse', {
    'count': NotRequired[int],
    'entity_type': NotRequired[str],
    'fetched_at': NotRequired[str],
    'name': NotRequired[str],
    'rankings': NotRequired[list[ModelSofascoreRankingRow]],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
    'total_rows': NotRequired[int],
    'type': NotRequired[int],
    'updated_at': NotRequired[str],
    'updated_timestamp': NotRequired[int],
}, total=False)

ModelSofascoreRankingRow = TypedDict('ModelSofascoreRankingRow', {
    'best_rank': NotRequired[int],
    'entity': NotRequired[ModelSofascoreRankingEntity],
    'label': NotRequired[str],
    'max_points': NotRequired[float],
    'next_win_points': NotRequired[float],
    'playing_teams': NotRequired[int],
    'points': NotRequired[float],
    'previous_points': NotRequired[float],
    'previous_rank': NotRequired[int],
    'rank': NotRequired[int],
    'total_teams': NotRequired[int],
    'tournaments_played': NotRequired[int],
    'year': NotRequired[str],
}, total=False)

ModelSofascoreRankingEntity = TypedDict('ModelSofascoreRankingEntity', {
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'gender': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'national': NotRequired[bool],
    'record': NotRequired[ModelSofascoreWdlrecord],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreWdlrecord = TypedDict('ModelSofascoreWdlrecord', {
    'draws': NotRequired[int],
    'losses': NotRequired[int],
    'wins': NotRequired[int],
}, total=False)

ModelSofascoreRankingTypesResponseDoc = TypedDict('ModelSofascoreRankingTypesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreRankingTypesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreRankingTypesResponse = TypedDict('ModelSofascoreRankingTypesResponse', {
    'count': NotRequired[int],
    'types': NotRequired[list[ModelSofascoreRankingType]],
}, total=False)

ModelSofascoreRankingType = TypedDict('ModelSofascoreRankingType', {
    'description': NotRequired[str],
    'entity_type': NotRequired[str],
    'gender': NotRequired[str],
    'name': NotRequired[str],
    'sport': NotRequired[str],
    'type': NotRequired[int],
}, total=False)

ModelSofascorePlayerTransfersResponseDoc = TypedDict('ModelSofascorePlayerTransfersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascorePlayerTransfersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascorePlayerTransfersResponse = TypedDict('ModelSofascorePlayerTransfersResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'player_id': NotRequired[int],
    'source_url': NotRequired[str],
    'transfers': NotRequired[list[ModelSofascoreTransfer]],
}, total=False)

ModelSofascorePlayerStatisticsSeasonsResponseDoc = TypedDict('ModelSofascorePlayerStatisticsSeasonsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascorePlayerStatisticsSeasonsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascorePlayerStatisticsSeasonsResponse = TypedDict('ModelSofascorePlayerStatisticsSeasonsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'player_id': NotRequired[int],
    'source_url': NotRequired[str],
    'tournaments': NotRequired[list[ModelSofascoreStatisticsTournament]],
}, total=False)

ModelSofascorePlayerSeasonStatisticsResponseDoc = TypedDict('ModelSofascorePlayerSeasonStatisticsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascorePlayerSeasonStatisticsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascorePlayerSeasonStatisticsResponse = TypedDict('ModelSofascorePlayerSeasonStatisticsResponse', {
    'fetched_at': NotRequired[str],
    'player_id': NotRequired[int],
    'rating_breakdown': NotRequired[dict[str, float]],
    'season': NotRequired[int],
    'source_url': NotRequired[str],
    'statistics': NotRequired[dict[str, float]],
    'team': NotRequired[ModelSofascoreTeamRef],
    'tournament_id': NotRequired[int],
    'type': NotRequired[str],
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

ModelSofascoreManagerEventsResponseDoc = TypedDict('ModelSofascoreManagerEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreManagerEventsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreManagerEventsResponse = TypedDict('ModelSofascoreManagerEventsResponse', {
    'count': NotRequired[int],
    'events': NotRequired[list[ModelSofascoreEventSummary]],
    'fetched_at': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'manager_id': NotRequired[int],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreManagerResponseDoc = TypedDict('ModelSofascoreManagerResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreManagerResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreManagerResponse = TypedDict('ModelSofascoreManagerResponse', {
    'fetched_at': NotRequired[str],
    'manager': NotRequired[ModelSofascoreManagerDetail],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreManagerDetail = TypedDict('ModelSofascoreManagerDetail', {
    'country': NotRequired[str],
    'date_of_birth': NotRequired[str],
    'deceased': NotRequired[bool],
    'former_player_id': NotRequired[int],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'nationality_code': NotRequired[str],
    'nationality_iso2': NotRequired[str],
    'performance': NotRequired[ModelSofascoreManagerPerformance],
    'preferred_formation': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
    'team': NotRequired[ModelSofascoreTeamRef],
    'teams': NotRequired[list[ModelSofascoreTeamRef]],
}, total=False)

ModelSofascoreManagerPerformance = TypedDict('ModelSofascoreManagerPerformance', {
    'draws': NotRequired[int],
    'goals_conceded': NotRequired[int],
    'goals_scored': NotRequired[int],
    'losses': NotRequired[int],
    'total': NotRequired[int],
    'total_points': NotRequired[int],
    'wins': NotRequired[int],
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

ModelSofascoreEventShotmapResponseDoc = TypedDict('ModelSofascoreEventShotmapResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventShotmapResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventShotmapResponse = TypedDict('ModelSofascoreEventShotmapResponse', {
    'count': NotRequired[int],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'shots': NotRequired[list[ModelSofascoreShot]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreShot = TypedDict('ModelSofascoreShot', {
    'added_time': NotRequired[int],
    'block_coordinates': NotRequired[ModelSofascoreCoordinates],
    'body_part': NotRequired[str],
    'goal_mouth_coordinates': NotRequired[ModelSofascoreCoordinates],
    'goal_mouth_location': NotRequired[str],
    'goal_type': NotRequired[str],
    'goalkeeper': NotRequired[ModelSofascorePlayerBrief],
    'id': NotRequired[int],
    'is_home': NotRequired[bool],
    'minute': NotRequired[int],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'player_coordinates': NotRequired[ModelSofascoreCoordinates],
    'shot_type': NotRequired[str],
    'situation': NotRequired[str],
    'time_seconds': NotRequired[int],
    'xg': NotRequired[float],
    'xgot': NotRequired[float],
}, total=False)

ModelSofascoreCoordinates = TypedDict('ModelSofascoreCoordinates', {
    'x': NotRequired[float],
    'y': NotRequired[float],
    'z': NotRequired[float],
}, total=False)

ModelSofascoreEventPlayerStatisticsResponseDoc = TypedDict('ModelSofascoreEventPlayerStatisticsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventPlayerStatisticsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventPlayerStatisticsResponse = TypedDict('ModelSofascoreEventPlayerStatisticsResponse', {
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'player_id': NotRequired[int],
    'position': NotRequired[str],
    'source_url': NotRequired[str],
    'statistics': NotRequired[dict[str, float]],
    'team': NotRequired[ModelSofascoreTeamRef],
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

ModelSofascoreEventGraphResponseDoc = TypedDict('ModelSofascoreEventGraphResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventGraphResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventGraphResponse = TypedDict('ModelSofascoreEventGraphResponse', {
    'count': NotRequired[int],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'overtime_count': NotRequired[int],
    'overtime_length': NotRequired[int],
    'period_count': NotRequired[int],
    'period_time': NotRequired[int],
    'points': NotRequired[list[ModelSofascoreGraphPoint]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreGraphPoint = TypedDict('ModelSofascoreGraphPoint', {
    'minute': NotRequired[float],
    'value': NotRequired[float],
}, total=False)

ModelSofascoreEventCommentsResponseDoc = TypedDict('ModelSofascoreEventCommentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventCommentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventCommentsResponse = TypedDict('ModelSofascoreEventCommentsResponse', {
    'comments': NotRequired[list[ModelSofascoreEventComment]],
    'count': NotRequired[int],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreEventComment = TypedDict('ModelSofascoreEventComment', {
    'assist': NotRequired[ModelSofascorePlayerBrief],
    'away_score': NotRequired[int],
    'goal_type': NotRequired[str],
    'home_score': NotRequired[int],
    'id': NotRequired[int],
    'is_home': NotRequired[bool],
    'minute': NotRequired[int],
    'penalty_drawn_by': NotRequired[ModelSofascorePlayerBrief],
    'period': NotRequired[str],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'player_in': NotRequired[ModelSofascorePlayerBrief],
    'player_out': NotRequired[ModelSofascorePlayerBrief],
    'text': NotRequired[str],
    'time_seconds': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreEventBestPlayersResponseDoc = TypedDict('ModelSofascoreEventBestPlayersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventBestPlayersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventBestPlayersResponse = TypedDict('ModelSofascoreEventBestPlayersResponse', {
    'away_players': NotRequired[list[ModelSofascoreBestPlayer]],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'home_players': NotRequired[list[ModelSofascoreBestPlayer]],
    'player_of_the_match': NotRequired[ModelSofascoreBestPlayer],
    'source_url': NotRequired[str],
    'top_players': NotRequired[list[ModelSofascoreBestPlayer]],
}, total=False)

ModelSofascoreBestPlayer = TypedDict('ModelSofascoreBestPlayer', {
    'label': NotRequired[str],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'team': NotRequired[ModelSofascoreTeamRef],
    'value': NotRequired[float],
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

ModelSofascoreCategoryTournamentsResponseDoc = TypedDict('ModelSofascoreCategoryTournamentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreCategoryTournamentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreCategoryTournamentsResponse = TypedDict('ModelSofascoreCategoryTournamentsResponse', {
    'category_id': NotRequired[int],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'tournaments': NotRequired[list[ModelSofascoreCategoryTournament]],
}, total=False)

ModelSofascoreCategoryTournament = TypedDict('ModelSofascoreCategoryTournament', {
    'category_id': NotRequired[int],
    'category_name': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'user_count': NotRequired[int],
}, total=False)

ModelSofascoreCategoriesResponseDoc = TypedDict('ModelSofascoreCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreCategoriesResponse = TypedDict('ModelSofascoreCategoriesResponse', {
    'categories': NotRequired[list[ModelSofascoreCategory]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelSofascoreCategory = TypedDict('ModelSofascoreCategory', {
    'alpha2': NotRequired[str],
    'flag': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'priority': NotRequired[int],
    'slug': NotRequired[str],
}, total=False)

SofascoreCategoriesResponse = ModelSofascoreCategoriesResponseDoc
SofascoreCategoriesParams = TypedDict('SofascoreCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreCategoryTournamentsResponse = ModelSofascoreCategoryTournamentsResponseDoc
SofascoreCategoryTournamentsParams = TypedDict('SofascoreCategoryTournamentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventResponse = ModelSofascoreEventResponseDoc
SofascoreEventParams = TypedDict('SofascoreEventParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventBestPlayersResponse = ModelSofascoreEventBestPlayersResponseDoc
SofascoreEventBestPlayersParams = TypedDict('SofascoreEventBestPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventCommentsResponse = ModelSofascoreEventCommentsResponseDoc
SofascoreEventCommentsParams = TypedDict('SofascoreEventCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventGraphResponse = ModelSofascoreEventGraphResponseDoc
SofascoreEventGraphParams = TypedDict('SofascoreEventGraphParams', {
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

SofascoreEventPlayerStatisticsResponse = ModelSofascoreEventPlayerStatisticsResponseDoc
SofascoreEventPlayerStatisticsParams = TypedDict('SofascoreEventPlayerStatisticsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'player_id': Required[str],
}, total=False)

SofascoreEventShotmapResponse = ModelSofascoreEventShotmapResponseDoc
SofascoreEventShotmapParams = TypedDict('SofascoreEventShotmapParams', {
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
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreManagerResponse = ModelSofascoreManagerResponseDoc
SofascoreManagerParams = TypedDict('SofascoreManagerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreManagerEventsResponse = ModelSofascoreManagerEventsResponseDoc
SofascoreManagerEventsParams = TypedDict('SofascoreManagerEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascorePlayerResponse = ModelSofascorePlayerResponseDoc
SofascorePlayerParams = TypedDict('SofascorePlayerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascorePlayerSeasonStatisticsResponse = ModelSofascorePlayerSeasonStatisticsResponseDoc
SofascorePlayerSeasonStatisticsParams = TypedDict('SofascorePlayerSeasonStatisticsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascorePlayerStatisticsSeasonsResponse = ModelSofascorePlayerStatisticsSeasonsResponseDoc
SofascorePlayerStatisticsSeasonsParams = TypedDict('SofascorePlayerStatisticsSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascorePlayerTransfersResponse = ModelSofascorePlayerTransfersResponseDoc
SofascorePlayerTransfersParams = TypedDict('SofascorePlayerTransfersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreRankingTypesResponse = ModelSofascoreRankingTypesResponseDoc
SofascoreRankingTypesParams = TypedDict('SofascoreRankingTypesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

SofascoreRankingsResponse = ModelSofascoreRankingsResponseDoc
SofascoreRankingsParams = TypedDict('SofascoreRankingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'type': Required[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '34', '35', '36', '37', '40', '41', '42', '43', '44', '45', '46']],
    'limit': NotRequired[int],
}, total=False)

SofascoreRoundEventsResponse = ModelSofascoreRoundEventsResponseDoc
SofascoreRoundEventsParams = TypedDict('SofascoreRoundEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
    'round': Required[int],
    'slug': NotRequired[str],
    'prefix': NotRequired[str],
}, total=False)

SofascoreScheduledEventsResponse = ModelSofascoreScheduledEventsResponseDoc
SofascoreScheduledEventsParams = TypedDict('SofascoreScheduledEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category_id': Required[str],
    'date': Required[str],
}, total=False)

SofascoreScheduledTournamentsResponse = ModelSofascoreScheduledTournamentsResponseDoc
SofascoreScheduledTournamentsParams = TypedDict('SofascoreScheduledTournamentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
    'date': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreSearchResponse = ModelSofascoreSearchResponseDoc
SofascoreSearchParams = TypedDict('SofascoreSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

SofascoreSeasonEventsResponse = ModelSofascoreSeasonEventsResponseDoc
SofascoreSeasonEventsParams = TypedDict('SofascoreSeasonEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
    'direction': Required[Literal['next', 'last']],
    'page': NotRequired[int],
}, total=False)

SofascoreSportsResponse = ModelSofascoreSportsResponseDoc
SofascoreSportsParams = TypedDict('SofascoreSportsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
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

SofascoreTeamOfTheWeekResponse = ModelSofascoreTeamOfTheWeekResponseDoc
SofascoreTeamOfTheWeekParams = TypedDict('SofascoreTeamOfTheWeekParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
    'period': Required[str],
}, total=False)

SofascoreTeamOfTheWeekPeriodsResponse = ModelSofascoreTeamOfTheWeekPeriodsResponseDoc
SofascoreTeamOfTheWeekPeriodsParams = TypedDict('SofascoreTeamOfTheWeekPeriodsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTeamPlayersResponse = ModelSofascoreTeamPlayersResponseDoc
SofascoreTeamPlayersParams = TypedDict('SofascoreTeamPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTeamSeasonStatisticsResponse = ModelSofascoreTeamSeasonStatisticsResponseDoc
SofascoreTeamSeasonStatisticsParams = TypedDict('SofascoreTeamSeasonStatisticsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascoreTeamStatisticsSeasonsResponse = ModelSofascoreTeamStatisticsSeasonsResponseDoc
SofascoreTeamStatisticsSeasonsParams = TypedDict('SofascoreTeamStatisticsSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTeamTransfersResponse = ModelSofascoreTeamTransfersResponseDoc
SofascoreTeamTransfersParams = TypedDict('SofascoreTeamTransfersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTournamentInfoResponse = ModelSofascoreTournamentInfoResponseDoc
SofascoreTournamentInfoParams = TypedDict('SofascoreTournamentInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': NotRequired[str],
}, total=False)

SofascoreTournamentPlayerStatisticsResponse = ModelSofascoreTournamentPlayerStatisticsResponseDoc
SofascoreTournamentPlayerStatisticsParams = TypedDict('SofascoreTournamentPlayerStatisticsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
    'order': NotRequired[Literal['rating', 'goals', 'expectedGoals', 'assists', 'successfulDribbles', 'tackles', 'accuratePassesPercentage', 'bigChancesMissed', 'totalShots', 'goalConversionPercentage', 'interceptions', 'clearances', 'errorLeadToGoal', 'outfielderBlocks', 'bigChancesCreated', 'accuratePasses', 'keyPasses', 'saves', 'cleanSheet', 'penaltySave', 'savedShotsFromInsideTheBox', 'runsOut']],
    'direction': NotRequired[Literal['desc', 'asc']],
    'accumulation': NotRequired[Literal['total', 'perGame', 'per90']],
    'group': NotRequired[Literal['summary', 'attack', 'defence', 'passing', 'goalkeeper']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SofascoreTournamentRoundsResponse = ModelSofascoreTournamentRoundsResponseDoc
SofascoreTournamentRoundsParams = TypedDict('SofascoreTournamentRoundsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentSeasonsResponse = ModelSofascoreTournamentSeasonsResponseDoc
SofascoreTournamentSeasonsParams = TypedDict('SofascoreTournamentSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTournamentTopPlayersResponse = ModelSofascoreTournamentTopPlayersResponseDoc
SofascoreTournamentTopPlayersParams = TypedDict('SofascoreTournamentTopPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'regular_season', 'playoffs']],
    'limit': NotRequired[int],
}, total=False)

SofascoreTournamentTopTeamsResponse = ModelSofascoreTournamentTopTeamsResponseDoc
SofascoreTournamentTopTeamsParams = TypedDict('SofascoreTournamentTopTeamsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'regular_season', 'playoffs']],
    'limit': NotRequired[int],
}, total=False)

class SofascoreGroup:
    @overload
    def categories(self, **params: Unpack[SofascoreCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[SofascoreCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[SofascoreCategoriesDefaultParams]) -> SofascoreCategoriesResponse: ...
    @overload
    def category_tournaments(self, **params: Unpack[SofascoreCategoryTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def category_tournaments(self, **params: Unpack[SofascoreCategoryTournamentsTextResponseParams]) -> str: ...
    @overload
    def category_tournaments(self, **params: Unpack[SofascoreCategoryTournamentsDefaultParams]) -> SofascoreCategoryTournamentsResponse: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventStreamParams]) -> BinaryIO: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventTextResponseParams]) -> str: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventDefaultParams]) -> SofascoreEventResponse: ...
    @overload
    def event_best_players(self, **params: Unpack[SofascoreEventBestPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def event_best_players(self, **params: Unpack[SofascoreEventBestPlayersTextResponseParams]) -> str: ...
    @overload
    def event_best_players(self, **params: Unpack[SofascoreEventBestPlayersDefaultParams]) -> SofascoreEventBestPlayersResponse: ...
    @overload
    def event_comments(self, **params: Unpack[SofascoreEventCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def event_comments(self, **params: Unpack[SofascoreEventCommentsTextResponseParams]) -> str: ...
    @overload
    def event_comments(self, **params: Unpack[SofascoreEventCommentsDefaultParams]) -> SofascoreEventCommentsResponse: ...
    @overload
    def event_graph(self, **params: Unpack[SofascoreEventGraphStreamParams]) -> BinaryIO: ...
    @overload
    def event_graph(self, **params: Unpack[SofascoreEventGraphTextResponseParams]) -> str: ...
    @overload
    def event_graph(self, **params: Unpack[SofascoreEventGraphDefaultParams]) -> SofascoreEventGraphResponse: ...
    @overload
    def event_h2h(self, **params: Unpack[SofascoreEventH2hStreamParams]) -> BinaryIO: ...
    @overload
    def event_h2h(self, **params: Unpack[SofascoreEventH2hTextResponseParams]) -> str: ...
    @overload
    def event_h2h(self, **params: Unpack[SofascoreEventH2hDefaultParams]) -> SofascoreEventH2hResponse: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsStreamParams]) -> BinaryIO: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsTextResponseParams]) -> str: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsDefaultParams]) -> SofascoreEventIncidentsResponse: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsStreamParams]) -> BinaryIO: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsTextResponseParams]) -> str: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsDefaultParams]) -> SofascoreEventLineupsResponse: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsStreamParams]) -> BinaryIO: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsTextResponseParams]) -> str: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsDefaultParams]) -> SofascoreEventOddsResponse: ...
    @overload
    def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsDefaultParams]) -> SofascoreEventPlayerStatisticsResponse: ...
    @overload
    def event_shotmap(self, **params: Unpack[SofascoreEventShotmapStreamParams]) -> BinaryIO: ...
    @overload
    def event_shotmap(self, **params: Unpack[SofascoreEventShotmapTextResponseParams]) -> str: ...
    @overload
    def event_shotmap(self, **params: Unpack[SofascoreEventShotmapDefaultParams]) -> SofascoreEventShotmapResponse: ...
    @overload
    def event_statistics(self, **params: Unpack[SofascoreEventStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def event_statistics(self, **params: Unpack[SofascoreEventStatisticsTextResponseParams]) -> str: ...
    @overload
    def event_statistics(self, **params: Unpack[SofascoreEventStatisticsDefaultParams]) -> SofascoreEventStatisticsResponse: ...
    @overload
    def live_events(self, **params: Unpack[SofascoreLiveEventsStreamParams]) -> BinaryIO: ...
    @overload
    def live_events(self, **params: Unpack[SofascoreLiveEventsTextResponseParams]) -> str: ...
    @overload
    def live_events(self, **params: Unpack[SofascoreLiveEventsDefaultParams]) -> SofascoreLiveEventsResponse: ...
    @overload
    def manager(self, **params: Unpack[SofascoreManagerStreamParams]) -> BinaryIO: ...
    @overload
    def manager(self, **params: Unpack[SofascoreManagerTextResponseParams]) -> str: ...
    @overload
    def manager(self, **params: Unpack[SofascoreManagerDefaultParams]) -> SofascoreManagerResponse: ...
    @overload
    def manager_events(self, **params: Unpack[SofascoreManagerEventsStreamParams]) -> BinaryIO: ...
    @overload
    def manager_events(self, **params: Unpack[SofascoreManagerEventsTextResponseParams]) -> str: ...
    @overload
    def manager_events(self, **params: Unpack[SofascoreManagerEventsDefaultParams]) -> SofascoreManagerEventsResponse: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerDefaultParams]) -> SofascorePlayerResponse: ...
    @overload
    def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsTextResponseParams]) -> str: ...
    @overload
    def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsDefaultParams]) -> SofascorePlayerSeasonStatisticsResponse: ...
    @overload
    def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsDefaultParams]) -> SofascorePlayerStatisticsSeasonsResponse: ...
    @overload
    def player_transfers(self, **params: Unpack[SofascorePlayerTransfersStreamParams]) -> BinaryIO: ...
    @overload
    def player_transfers(self, **params: Unpack[SofascorePlayerTransfersTextResponseParams]) -> str: ...
    @overload
    def player_transfers(self, **params: Unpack[SofascorePlayerTransfersDefaultParams]) -> SofascorePlayerTransfersResponse: ...
    @overload
    def ranking_types(self, **params: Unpack[SofascoreRankingTypesStreamParams]) -> BinaryIO: ...
    @overload
    def ranking_types(self, **params: Unpack[SofascoreRankingTypesTextResponseParams]) -> str: ...
    @overload
    def ranking_types(self, **params: Unpack[SofascoreRankingTypesDefaultParams]) -> SofascoreRankingTypesResponse: ...
    @overload
    def rankings(self, **params: Unpack[SofascoreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def rankings(self, **params: Unpack[SofascoreRankingsTextResponseParams]) -> str: ...
    @overload
    def rankings(self, **params: Unpack[SofascoreRankingsDefaultParams]) -> SofascoreRankingsResponse: ...
    @overload
    def round_events(self, **params: Unpack[SofascoreRoundEventsStreamParams]) -> BinaryIO: ...
    @overload
    def round_events(self, **params: Unpack[SofascoreRoundEventsTextResponseParams]) -> str: ...
    @overload
    def round_events(self, **params: Unpack[SofascoreRoundEventsDefaultParams]) -> SofascoreRoundEventsResponse: ...
    @overload
    def scheduled_events(self, **params: Unpack[SofascoreScheduledEventsStreamParams]) -> BinaryIO: ...
    @overload
    def scheduled_events(self, **params: Unpack[SofascoreScheduledEventsTextResponseParams]) -> str: ...
    @overload
    def scheduled_events(self, **params: Unpack[SofascoreScheduledEventsDefaultParams]) -> SofascoreScheduledEventsResponse: ...
    @overload
    def scheduled_tournaments(self, **params: Unpack[SofascoreScheduledTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def scheduled_tournaments(self, **params: Unpack[SofascoreScheduledTournamentsTextResponseParams]) -> str: ...
    @overload
    def scheduled_tournaments(self, **params: Unpack[SofascoreScheduledTournamentsDefaultParams]) -> SofascoreScheduledTournamentsResponse: ...
    @overload
    def search(self, **params: Unpack[SofascoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[SofascoreSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[SofascoreSearchDefaultParams]) -> SofascoreSearchResponse: ...
    @overload
    def season_events(self, **params: Unpack[SofascoreSeasonEventsStreamParams]) -> BinaryIO: ...
    @overload
    def season_events(self, **params: Unpack[SofascoreSeasonEventsTextResponseParams]) -> str: ...
    @overload
    def season_events(self, **params: Unpack[SofascoreSeasonEventsDefaultParams]) -> SofascoreSeasonEventsResponse: ...
    @overload
    def sports(self, **params: Unpack[SofascoreSportsStreamParams]) -> BinaryIO: ...
    @overload
    def sports(self, **params: Unpack[SofascoreSportsTextResponseParams]) -> str: ...
    @overload
    def sports(self, **params: Unpack[SofascoreSportsDefaultParams]) -> SofascoreSportsResponse: ...
    @overload
    def standings(self, **params: Unpack[SofascoreStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def standings(self, **params: Unpack[SofascoreStandingsTextResponseParams]) -> str: ...
    @overload
    def standings(self, **params: Unpack[SofascoreStandingsDefaultParams]) -> SofascoreStandingsResponse: ...
    @overload
    def team(self, **params: Unpack[SofascoreTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[SofascoreTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[SofascoreTeamDefaultParams]) -> SofascoreTeamResponse: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsStreamParams]) -> BinaryIO: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsTextResponseParams]) -> str: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsDefaultParams]) -> SofascoreTeamEventsResponse: ...
    @overload
    def team_of_the_week(self, **params: Unpack[SofascoreTeamOfTheWeekStreamParams]) -> BinaryIO: ...
    @overload
    def team_of_the_week(self, **params: Unpack[SofascoreTeamOfTheWeekTextResponseParams]) -> str: ...
    @overload
    def team_of_the_week(self, **params: Unpack[SofascoreTeamOfTheWeekDefaultParams]) -> SofascoreTeamOfTheWeekResponse: ...
    @overload
    def team_of_the_week_periods(self, **params: Unpack[SofascoreTeamOfTheWeekPeriodsStreamParams]) -> BinaryIO: ...
    @overload
    def team_of_the_week_periods(self, **params: Unpack[SofascoreTeamOfTheWeekPeriodsTextResponseParams]) -> str: ...
    @overload
    def team_of_the_week_periods(self, **params: Unpack[SofascoreTeamOfTheWeekPeriodsDefaultParams]) -> SofascoreTeamOfTheWeekPeriodsResponse: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersTextResponseParams]) -> str: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersDefaultParams]) -> SofascoreTeamPlayersResponse: ...
    @overload
    def team_season_statistics(self, **params: Unpack[SofascoreTeamSeasonStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def team_season_statistics(self, **params: Unpack[SofascoreTeamSeasonStatisticsTextResponseParams]) -> str: ...
    @overload
    def team_season_statistics(self, **params: Unpack[SofascoreTeamSeasonStatisticsDefaultParams]) -> SofascoreTeamSeasonStatisticsResponse: ...
    @overload
    def team_statistics_seasons(self, **params: Unpack[SofascoreTeamStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def team_statistics_seasons(self, **params: Unpack[SofascoreTeamStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    def team_statistics_seasons(self, **params: Unpack[SofascoreTeamStatisticsSeasonsDefaultParams]) -> SofascoreTeamStatisticsSeasonsResponse: ...
    @overload
    def team_transfers(self, **params: Unpack[SofascoreTeamTransfersStreamParams]) -> BinaryIO: ...
    @overload
    def team_transfers(self, **params: Unpack[SofascoreTeamTransfersTextResponseParams]) -> str: ...
    @overload
    def team_transfers(self, **params: Unpack[SofascoreTeamTransfersDefaultParams]) -> SofascoreTeamTransfersResponse: ...
    @overload
    def tournament_info(self, **params: Unpack[SofascoreTournamentInfoStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_info(self, **params: Unpack[SofascoreTournamentInfoTextResponseParams]) -> str: ...
    @overload
    def tournament_info(self, **params: Unpack[SofascoreTournamentInfoDefaultParams]) -> SofascoreTournamentInfoResponse: ...
    @overload
    def tournament_player_statistics(self, **params: Unpack[SofascoreTournamentPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_player_statistics(self, **params: Unpack[SofascoreTournamentPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    def tournament_player_statistics(self, **params: Unpack[SofascoreTournamentPlayerStatisticsDefaultParams]) -> SofascoreTournamentPlayerStatisticsResponse: ...
    @overload
    def tournament_rounds(self, **params: Unpack[SofascoreTournamentRoundsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_rounds(self, **params: Unpack[SofascoreTournamentRoundsTextResponseParams]) -> str: ...
    @overload
    def tournament_rounds(self, **params: Unpack[SofascoreTournamentRoundsDefaultParams]) -> SofascoreTournamentRoundsResponse: ...
    @overload
    def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsDefaultParams]) -> SofascoreTournamentSeasonsResponse: ...
    @overload
    def tournament_top_players(self, **params: Unpack[SofascoreTournamentTopPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_top_players(self, **params: Unpack[SofascoreTournamentTopPlayersTextResponseParams]) -> str: ...
    @overload
    def tournament_top_players(self, **params: Unpack[SofascoreTournamentTopPlayersDefaultParams]) -> SofascoreTournamentTopPlayersResponse: ...
    @overload
    def tournament_top_teams(self, **params: Unpack[SofascoreTournamentTopTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_top_teams(self, **params: Unpack[SofascoreTournamentTopTeamsTextResponseParams]) -> str: ...
    @overload
    def tournament_top_teams(self, **params: Unpack[SofascoreTournamentTopTeamsDefaultParams]) -> SofascoreTournamentTopTeamsResponse: ...

OperationId = Literal[
    'sofascore-categories',
    'sofascore-category-tournaments',
    'sofascore-event',
    'sofascore-event-best-players',
    'sofascore-event-comments',
    'sofascore-event-graph',
    'sofascore-event-h2h',
    'sofascore-event-incidents',
    'sofascore-event-lineups',
    'sofascore-event-odds',
    'sofascore-event-player-statistics',
    'sofascore-event-shotmap',
    'sofascore-event-statistics',
    'sofascore-live-events',
    'sofascore-manager',
    'sofascore-manager-events',
    'sofascore-player',
    'sofascore-player-season-statistics',
    'sofascore-player-statistics-seasons',
    'sofascore-player-transfers',
    'sofascore-ranking-types',
    'sofascore-rankings',
    'sofascore-round-events',
    'sofascore-scheduled-events',
    'sofascore-scheduled-tournaments',
    'sofascore-search',
    'sofascore-season-events',
    'sofascore-sports',
    'sofascore-standings',
    'sofascore-team',
    'sofascore-team-events',
    'sofascore-team-of-the-week',
    'sofascore-team-of-the-week-periods',
    'sofascore-team-players',
    'sofascore-team-season-statistics',
    'sofascore-team-statistics-seasons',
    'sofascore-team-transfers',
    'sofascore-tournament-info',
    'sofascore-tournament-player-statistics',
    'sofascore-tournament-rounds',
    'sofascore-tournament-seasons',
    'sofascore-tournament-top-players',
    'sofascore-tournament-top-teams',
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
        operation_id: Literal['sofascore-categories'],
        params: SofascoreCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-category-tournaments'],
        params: SofascoreCategoryTournamentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreCategoryTournamentsResponse: ...
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
        operation_id: Literal['sofascore-event-best-players'],
        params: SofascoreEventBestPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventBestPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-comments'],
        params: SofascoreEventCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventCommentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-graph'],
        params: SofascoreEventGraphParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventGraphResponse: ...
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
        operation_id: Literal['sofascore-event-player-statistics'],
        params: SofascoreEventPlayerStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventPlayerStatisticsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-shotmap'],
        params: SofascoreEventShotmapParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventShotmapResponse: ...
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
        operation_id: Literal['sofascore-manager'],
        params: SofascoreManagerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreManagerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-manager-events'],
        params: SofascoreManagerEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreManagerEventsResponse: ...
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
        operation_id: Literal['sofascore-player-season-statistics'],
        params: SofascorePlayerSeasonStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerSeasonStatisticsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-player-statistics-seasons'],
        params: SofascorePlayerStatisticsSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerStatisticsSeasonsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-player-transfers'],
        params: SofascorePlayerTransfersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerTransfersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-ranking-types'],
        params: SofascoreRankingTypesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreRankingTypesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-rankings'],
        params: SofascoreRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreRankingsResponse: ...
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
        operation_id: Literal['sofascore-scheduled-events'],
        params: SofascoreScheduledEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreScheduledEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-scheduled-tournaments'],
        params: SofascoreScheduledTournamentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreScheduledTournamentsResponse: ...
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
        operation_id: Literal['sofascore-season-events'],
        params: SofascoreSeasonEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreSeasonEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-sports'],
        params: SofascoreSportsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreSportsResponse: ...
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
        operation_id: Literal['sofascore-team-of-the-week'],
        params: SofascoreTeamOfTheWeekParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamOfTheWeekResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-team-of-the-week-periods'],
        params: SofascoreTeamOfTheWeekPeriodsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamOfTheWeekPeriodsResponse: ...
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
        operation_id: Literal['sofascore-team-season-statistics'],
        params: SofascoreTeamSeasonStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamSeasonStatisticsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-team-statistics-seasons'],
        params: SofascoreTeamStatisticsSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamStatisticsSeasonsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-team-transfers'],
        params: SofascoreTeamTransfersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamTransfersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-tournament-info'],
        params: SofascoreTournamentInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-tournament-player-statistics'],
        params: SofascoreTournamentPlayerStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentPlayerStatisticsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-tournament-rounds'],
        params: SofascoreTournamentRoundsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentRoundsResponse: ...
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
        operation_id: Literal['sofascore-tournament-top-players'],
        params: SofascoreTournamentTopPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentTopPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-tournament-top-teams'],
        params: SofascoreTournamentTopTeamsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentTopTeamsResponse: ...
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
        operation_id: Literal['sofascore-categories'],
        params: SofascoreCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-category-tournaments'],
        params: SofascoreCategoryTournamentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreCategoryTournamentsResponse: ...
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
        operation_id: Literal['sofascore-event-best-players'],
        params: SofascoreEventBestPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventBestPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-comments'],
        params: SofascoreEventCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventCommentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-graph'],
        params: SofascoreEventGraphParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventGraphResponse: ...
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
        operation_id: Literal['sofascore-event-player-statistics'],
        params: SofascoreEventPlayerStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventPlayerStatisticsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-shotmap'],
        params: SofascoreEventShotmapParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventShotmapResponse: ...
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
        operation_id: Literal['sofascore-manager'],
        params: SofascoreManagerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreManagerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-manager-events'],
        params: SofascoreManagerEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreManagerEventsResponse: ...
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
        operation_id: Literal['sofascore-player-season-statistics'],
        params: SofascorePlayerSeasonStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerSeasonStatisticsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-player-statistics-seasons'],
        params: SofascorePlayerStatisticsSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerStatisticsSeasonsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-player-transfers'],
        params: SofascorePlayerTransfersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerTransfersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-ranking-types'],
        params: SofascoreRankingTypesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreRankingTypesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-rankings'],
        params: SofascoreRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreRankingsResponse: ...
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
        operation_id: Literal['sofascore-scheduled-events'],
        params: SofascoreScheduledEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreScheduledEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-scheduled-tournaments'],
        params: SofascoreScheduledTournamentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreScheduledTournamentsResponse: ...
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
        operation_id: Literal['sofascore-season-events'],
        params: SofascoreSeasonEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreSeasonEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-sports'],
        params: SofascoreSportsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreSportsResponse: ...
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
        operation_id: Literal['sofascore-team-of-the-week'],
        params: SofascoreTeamOfTheWeekParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamOfTheWeekResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-team-of-the-week-periods'],
        params: SofascoreTeamOfTheWeekPeriodsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamOfTheWeekPeriodsResponse: ...
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
        operation_id: Literal['sofascore-team-season-statistics'],
        params: SofascoreTeamSeasonStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamSeasonStatisticsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-team-statistics-seasons'],
        params: SofascoreTeamStatisticsSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamStatisticsSeasonsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-team-transfers'],
        params: SofascoreTeamTransfersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamTransfersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-tournament-info'],
        params: SofascoreTournamentInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-tournament-player-statistics'],
        params: SofascoreTournamentPlayerStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentPlayerStatisticsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-tournament-rounds'],
        params: SofascoreTournamentRoundsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentRoundsResponse: ...
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
        operation_id: Literal['sofascore-tournament-top-players'],
        params: SofascoreTournamentTopPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentTopPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-tournament-top-teams'],
        params: SofascoreTournamentTopTeamsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentTopTeamsResponse: ...
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
    @overload
    def categories(self, **params: Unpack[SofascoreCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[SofascoreCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[SofascoreCategoriesDefaultParams]) -> SofascoreCategoriesResponse: ...
    @overload
    def category_tournaments(self, **params: Unpack[SofascoreCategoryTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def category_tournaments(self, **params: Unpack[SofascoreCategoryTournamentsTextResponseParams]) -> str: ...
    @overload
    def category_tournaments(self, **params: Unpack[SofascoreCategoryTournamentsDefaultParams]) -> SofascoreCategoryTournamentsResponse: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventStreamParams]) -> BinaryIO: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventTextResponseParams]) -> str: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventDefaultParams]) -> SofascoreEventResponse: ...
    @overload
    def event_best_players(self, **params: Unpack[SofascoreEventBestPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def event_best_players(self, **params: Unpack[SofascoreEventBestPlayersTextResponseParams]) -> str: ...
    @overload
    def event_best_players(self, **params: Unpack[SofascoreEventBestPlayersDefaultParams]) -> SofascoreEventBestPlayersResponse: ...
    @overload
    def event_comments(self, **params: Unpack[SofascoreEventCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def event_comments(self, **params: Unpack[SofascoreEventCommentsTextResponseParams]) -> str: ...
    @overload
    def event_comments(self, **params: Unpack[SofascoreEventCommentsDefaultParams]) -> SofascoreEventCommentsResponse: ...
    @overload
    def event_graph(self, **params: Unpack[SofascoreEventGraphStreamParams]) -> BinaryIO: ...
    @overload
    def event_graph(self, **params: Unpack[SofascoreEventGraphTextResponseParams]) -> str: ...
    @overload
    def event_graph(self, **params: Unpack[SofascoreEventGraphDefaultParams]) -> SofascoreEventGraphResponse: ...
    @overload
    def event_h2h(self, **params: Unpack[SofascoreEventH2hStreamParams]) -> BinaryIO: ...
    @overload
    def event_h2h(self, **params: Unpack[SofascoreEventH2hTextResponseParams]) -> str: ...
    @overload
    def event_h2h(self, **params: Unpack[SofascoreEventH2hDefaultParams]) -> SofascoreEventH2hResponse: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsStreamParams]) -> BinaryIO: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsTextResponseParams]) -> str: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsDefaultParams]) -> SofascoreEventIncidentsResponse: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsStreamParams]) -> BinaryIO: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsTextResponseParams]) -> str: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsDefaultParams]) -> SofascoreEventLineupsResponse: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsStreamParams]) -> BinaryIO: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsTextResponseParams]) -> str: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsDefaultParams]) -> SofascoreEventOddsResponse: ...
    @overload
    def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsDefaultParams]) -> SofascoreEventPlayerStatisticsResponse: ...
    @overload
    def event_shotmap(self, **params: Unpack[SofascoreEventShotmapStreamParams]) -> BinaryIO: ...
    @overload
    def event_shotmap(self, **params: Unpack[SofascoreEventShotmapTextResponseParams]) -> str: ...
    @overload
    def event_shotmap(self, **params: Unpack[SofascoreEventShotmapDefaultParams]) -> SofascoreEventShotmapResponse: ...
    @overload
    def event_statistics(self, **params: Unpack[SofascoreEventStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def event_statistics(self, **params: Unpack[SofascoreEventStatisticsTextResponseParams]) -> str: ...
    @overload
    def event_statistics(self, **params: Unpack[SofascoreEventStatisticsDefaultParams]) -> SofascoreEventStatisticsResponse: ...
    @overload
    def live_events(self, **params: Unpack[SofascoreLiveEventsStreamParams]) -> BinaryIO: ...
    @overload
    def live_events(self, **params: Unpack[SofascoreLiveEventsTextResponseParams]) -> str: ...
    @overload
    def live_events(self, **params: Unpack[SofascoreLiveEventsDefaultParams]) -> SofascoreLiveEventsResponse: ...
    @overload
    def manager(self, **params: Unpack[SofascoreManagerStreamParams]) -> BinaryIO: ...
    @overload
    def manager(self, **params: Unpack[SofascoreManagerTextResponseParams]) -> str: ...
    @overload
    def manager(self, **params: Unpack[SofascoreManagerDefaultParams]) -> SofascoreManagerResponse: ...
    @overload
    def manager_events(self, **params: Unpack[SofascoreManagerEventsStreamParams]) -> BinaryIO: ...
    @overload
    def manager_events(self, **params: Unpack[SofascoreManagerEventsTextResponseParams]) -> str: ...
    @overload
    def manager_events(self, **params: Unpack[SofascoreManagerEventsDefaultParams]) -> SofascoreManagerEventsResponse: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerDefaultParams]) -> SofascorePlayerResponse: ...
    @overload
    def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsTextResponseParams]) -> str: ...
    @overload
    def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsDefaultParams]) -> SofascorePlayerSeasonStatisticsResponse: ...
    @overload
    def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsDefaultParams]) -> SofascorePlayerStatisticsSeasonsResponse: ...
    @overload
    def player_transfers(self, **params: Unpack[SofascorePlayerTransfersStreamParams]) -> BinaryIO: ...
    @overload
    def player_transfers(self, **params: Unpack[SofascorePlayerTransfersTextResponseParams]) -> str: ...
    @overload
    def player_transfers(self, **params: Unpack[SofascorePlayerTransfersDefaultParams]) -> SofascorePlayerTransfersResponse: ...
    @overload
    def ranking_types(self, **params: Unpack[SofascoreRankingTypesStreamParams]) -> BinaryIO: ...
    @overload
    def ranking_types(self, **params: Unpack[SofascoreRankingTypesTextResponseParams]) -> str: ...
    @overload
    def ranking_types(self, **params: Unpack[SofascoreRankingTypesDefaultParams]) -> SofascoreRankingTypesResponse: ...
    @overload
    def rankings(self, **params: Unpack[SofascoreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def rankings(self, **params: Unpack[SofascoreRankingsTextResponseParams]) -> str: ...
    @overload
    def rankings(self, **params: Unpack[SofascoreRankingsDefaultParams]) -> SofascoreRankingsResponse: ...
    @overload
    def round_events(self, **params: Unpack[SofascoreRoundEventsStreamParams]) -> BinaryIO: ...
    @overload
    def round_events(self, **params: Unpack[SofascoreRoundEventsTextResponseParams]) -> str: ...
    @overload
    def round_events(self, **params: Unpack[SofascoreRoundEventsDefaultParams]) -> SofascoreRoundEventsResponse: ...
    @overload
    def scheduled_events(self, **params: Unpack[SofascoreScheduledEventsStreamParams]) -> BinaryIO: ...
    @overload
    def scheduled_events(self, **params: Unpack[SofascoreScheduledEventsTextResponseParams]) -> str: ...
    @overload
    def scheduled_events(self, **params: Unpack[SofascoreScheduledEventsDefaultParams]) -> SofascoreScheduledEventsResponse: ...
    @overload
    def scheduled_tournaments(self, **params: Unpack[SofascoreScheduledTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def scheduled_tournaments(self, **params: Unpack[SofascoreScheduledTournamentsTextResponseParams]) -> str: ...
    @overload
    def scheduled_tournaments(self, **params: Unpack[SofascoreScheduledTournamentsDefaultParams]) -> SofascoreScheduledTournamentsResponse: ...
    @overload
    def search(self, **params: Unpack[SofascoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[SofascoreSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[SofascoreSearchDefaultParams]) -> SofascoreSearchResponse: ...
    @overload
    def season_events(self, **params: Unpack[SofascoreSeasonEventsStreamParams]) -> BinaryIO: ...
    @overload
    def season_events(self, **params: Unpack[SofascoreSeasonEventsTextResponseParams]) -> str: ...
    @overload
    def season_events(self, **params: Unpack[SofascoreSeasonEventsDefaultParams]) -> SofascoreSeasonEventsResponse: ...
    @overload
    def sports(self, **params: Unpack[SofascoreSportsStreamParams]) -> BinaryIO: ...
    @overload
    def sports(self, **params: Unpack[SofascoreSportsTextResponseParams]) -> str: ...
    @overload
    def sports(self, **params: Unpack[SofascoreSportsDefaultParams]) -> SofascoreSportsResponse: ...
    @overload
    def standings(self, **params: Unpack[SofascoreStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def standings(self, **params: Unpack[SofascoreStandingsTextResponseParams]) -> str: ...
    @overload
    def standings(self, **params: Unpack[SofascoreStandingsDefaultParams]) -> SofascoreStandingsResponse: ...
    @overload
    def team(self, **params: Unpack[SofascoreTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[SofascoreTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[SofascoreTeamDefaultParams]) -> SofascoreTeamResponse: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsStreamParams]) -> BinaryIO: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsTextResponseParams]) -> str: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsDefaultParams]) -> SofascoreTeamEventsResponse: ...
    @overload
    def team_of_the_week(self, **params: Unpack[SofascoreTeamOfTheWeekStreamParams]) -> BinaryIO: ...
    @overload
    def team_of_the_week(self, **params: Unpack[SofascoreTeamOfTheWeekTextResponseParams]) -> str: ...
    @overload
    def team_of_the_week(self, **params: Unpack[SofascoreTeamOfTheWeekDefaultParams]) -> SofascoreTeamOfTheWeekResponse: ...
    @overload
    def team_of_the_week_periods(self, **params: Unpack[SofascoreTeamOfTheWeekPeriodsStreamParams]) -> BinaryIO: ...
    @overload
    def team_of_the_week_periods(self, **params: Unpack[SofascoreTeamOfTheWeekPeriodsTextResponseParams]) -> str: ...
    @overload
    def team_of_the_week_periods(self, **params: Unpack[SofascoreTeamOfTheWeekPeriodsDefaultParams]) -> SofascoreTeamOfTheWeekPeriodsResponse: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersTextResponseParams]) -> str: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersDefaultParams]) -> SofascoreTeamPlayersResponse: ...
    @overload
    def team_season_statistics(self, **params: Unpack[SofascoreTeamSeasonStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def team_season_statistics(self, **params: Unpack[SofascoreTeamSeasonStatisticsTextResponseParams]) -> str: ...
    @overload
    def team_season_statistics(self, **params: Unpack[SofascoreTeamSeasonStatisticsDefaultParams]) -> SofascoreTeamSeasonStatisticsResponse: ...
    @overload
    def team_statistics_seasons(self, **params: Unpack[SofascoreTeamStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def team_statistics_seasons(self, **params: Unpack[SofascoreTeamStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    def team_statistics_seasons(self, **params: Unpack[SofascoreTeamStatisticsSeasonsDefaultParams]) -> SofascoreTeamStatisticsSeasonsResponse: ...
    @overload
    def team_transfers(self, **params: Unpack[SofascoreTeamTransfersStreamParams]) -> BinaryIO: ...
    @overload
    def team_transfers(self, **params: Unpack[SofascoreTeamTransfersTextResponseParams]) -> str: ...
    @overload
    def team_transfers(self, **params: Unpack[SofascoreTeamTransfersDefaultParams]) -> SofascoreTeamTransfersResponse: ...
    @overload
    def tournament_info(self, **params: Unpack[SofascoreTournamentInfoStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_info(self, **params: Unpack[SofascoreTournamentInfoTextResponseParams]) -> str: ...
    @overload
    def tournament_info(self, **params: Unpack[SofascoreTournamentInfoDefaultParams]) -> SofascoreTournamentInfoResponse: ...
    @overload
    def tournament_player_statistics(self, **params: Unpack[SofascoreTournamentPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_player_statistics(self, **params: Unpack[SofascoreTournamentPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    def tournament_player_statistics(self, **params: Unpack[SofascoreTournamentPlayerStatisticsDefaultParams]) -> SofascoreTournamentPlayerStatisticsResponse: ...
    @overload
    def tournament_rounds(self, **params: Unpack[SofascoreTournamentRoundsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_rounds(self, **params: Unpack[SofascoreTournamentRoundsTextResponseParams]) -> str: ...
    @overload
    def tournament_rounds(self, **params: Unpack[SofascoreTournamentRoundsDefaultParams]) -> SofascoreTournamentRoundsResponse: ...
    @overload
    def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsDefaultParams]) -> SofascoreTournamentSeasonsResponse: ...
    @overload
    def tournament_top_players(self, **params: Unpack[SofascoreTournamentTopPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_top_players(self, **params: Unpack[SofascoreTournamentTopPlayersTextResponseParams]) -> str: ...
    @overload
    def tournament_top_players(self, **params: Unpack[SofascoreTournamentTopPlayersDefaultParams]) -> SofascoreTournamentTopPlayersResponse: ...
    @overload
    def tournament_top_teams(self, **params: Unpack[SofascoreTournamentTopTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_top_teams(self, **params: Unpack[SofascoreTournamentTopTeamsTextResponseParams]) -> str: ...
    @overload
    def tournament_top_teams(self, **params: Unpack[SofascoreTournamentTopTeamsDefaultParams]) -> SofascoreTournamentTopTeamsResponse: ...

class AsyncSofascoreClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncSofascoreClient: ...
    sofascore: _AsyncSofascoreGroup
    @overload
    async def categories(self, **params: Unpack[SofascoreCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[SofascoreCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[SofascoreCategoriesDefaultParams]) -> SofascoreCategoriesResponse: ...
    @overload
    async def category_tournaments(self, **params: Unpack[SofascoreCategoryTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def category_tournaments(self, **params: Unpack[SofascoreCategoryTournamentsTextResponseParams]) -> str: ...
    @overload
    async def category_tournaments(self, **params: Unpack[SofascoreCategoryTournamentsDefaultParams]) -> SofascoreCategoryTournamentsResponse: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventStreamParams]) -> BinaryIO: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventTextResponseParams]) -> str: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventDefaultParams]) -> SofascoreEventResponse: ...
    @overload
    async def event_best_players(self, **params: Unpack[SofascoreEventBestPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def event_best_players(self, **params: Unpack[SofascoreEventBestPlayersTextResponseParams]) -> str: ...
    @overload
    async def event_best_players(self, **params: Unpack[SofascoreEventBestPlayersDefaultParams]) -> SofascoreEventBestPlayersResponse: ...
    @overload
    async def event_comments(self, **params: Unpack[SofascoreEventCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_comments(self, **params: Unpack[SofascoreEventCommentsTextResponseParams]) -> str: ...
    @overload
    async def event_comments(self, **params: Unpack[SofascoreEventCommentsDefaultParams]) -> SofascoreEventCommentsResponse: ...
    @overload
    async def event_graph(self, **params: Unpack[SofascoreEventGraphStreamParams]) -> BinaryIO: ...
    @overload
    async def event_graph(self, **params: Unpack[SofascoreEventGraphTextResponseParams]) -> str: ...
    @overload
    async def event_graph(self, **params: Unpack[SofascoreEventGraphDefaultParams]) -> SofascoreEventGraphResponse: ...
    @overload
    async def event_h2h(self, **params: Unpack[SofascoreEventH2hStreamParams]) -> BinaryIO: ...
    @overload
    async def event_h2h(self, **params: Unpack[SofascoreEventH2hTextResponseParams]) -> str: ...
    @overload
    async def event_h2h(self, **params: Unpack[SofascoreEventH2hDefaultParams]) -> SofascoreEventH2hResponse: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsTextResponseParams]) -> str: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsDefaultParams]) -> SofascoreEventIncidentsResponse: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsTextResponseParams]) -> str: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsDefaultParams]) -> SofascoreEventLineupsResponse: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsTextResponseParams]) -> str: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsDefaultParams]) -> SofascoreEventOddsResponse: ...
    @overload
    async def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    async def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsDefaultParams]) -> SofascoreEventPlayerStatisticsResponse: ...
    @overload
    async def event_shotmap(self, **params: Unpack[SofascoreEventShotmapStreamParams]) -> BinaryIO: ...
    @overload
    async def event_shotmap(self, **params: Unpack[SofascoreEventShotmapTextResponseParams]) -> str: ...
    @overload
    async def event_shotmap(self, **params: Unpack[SofascoreEventShotmapDefaultParams]) -> SofascoreEventShotmapResponse: ...
    @overload
    async def event_statistics(self, **params: Unpack[SofascoreEventStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_statistics(self, **params: Unpack[SofascoreEventStatisticsTextResponseParams]) -> str: ...
    @overload
    async def event_statistics(self, **params: Unpack[SofascoreEventStatisticsDefaultParams]) -> SofascoreEventStatisticsResponse: ...
    @overload
    async def live_events(self, **params: Unpack[SofascoreLiveEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_events(self, **params: Unpack[SofascoreLiveEventsTextResponseParams]) -> str: ...
    @overload
    async def live_events(self, **params: Unpack[SofascoreLiveEventsDefaultParams]) -> SofascoreLiveEventsResponse: ...
    @overload
    async def manager(self, **params: Unpack[SofascoreManagerStreamParams]) -> BinaryIO: ...
    @overload
    async def manager(self, **params: Unpack[SofascoreManagerTextResponseParams]) -> str: ...
    @overload
    async def manager(self, **params: Unpack[SofascoreManagerDefaultParams]) -> SofascoreManagerResponse: ...
    @overload
    async def manager_events(self, **params: Unpack[SofascoreManagerEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def manager_events(self, **params: Unpack[SofascoreManagerEventsTextResponseParams]) -> str: ...
    @overload
    async def manager_events(self, **params: Unpack[SofascoreManagerEventsDefaultParams]) -> SofascoreManagerEventsResponse: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerDefaultParams]) -> SofascorePlayerResponse: ...
    @overload
    async def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsTextResponseParams]) -> str: ...
    @overload
    async def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsDefaultParams]) -> SofascorePlayerSeasonStatisticsResponse: ...
    @overload
    async def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    async def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsDefaultParams]) -> SofascorePlayerStatisticsSeasonsResponse: ...
    @overload
    async def player_transfers(self, **params: Unpack[SofascorePlayerTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def player_transfers(self, **params: Unpack[SofascorePlayerTransfersTextResponseParams]) -> str: ...
    @overload
    async def player_transfers(self, **params: Unpack[SofascorePlayerTransfersDefaultParams]) -> SofascorePlayerTransfersResponse: ...
    @overload
    async def ranking_types(self, **params: Unpack[SofascoreRankingTypesStreamParams]) -> BinaryIO: ...
    @overload
    async def ranking_types(self, **params: Unpack[SofascoreRankingTypesTextResponseParams]) -> str: ...
    @overload
    async def ranking_types(self, **params: Unpack[SofascoreRankingTypesDefaultParams]) -> SofascoreRankingTypesResponse: ...
    @overload
    async def rankings(self, **params: Unpack[SofascoreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def rankings(self, **params: Unpack[SofascoreRankingsTextResponseParams]) -> str: ...
    @overload
    async def rankings(self, **params: Unpack[SofascoreRankingsDefaultParams]) -> SofascoreRankingsResponse: ...
    @overload
    async def round_events(self, **params: Unpack[SofascoreRoundEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def round_events(self, **params: Unpack[SofascoreRoundEventsTextResponseParams]) -> str: ...
    @overload
    async def round_events(self, **params: Unpack[SofascoreRoundEventsDefaultParams]) -> SofascoreRoundEventsResponse: ...
    @overload
    async def scheduled_events(self, **params: Unpack[SofascoreScheduledEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def scheduled_events(self, **params: Unpack[SofascoreScheduledEventsTextResponseParams]) -> str: ...
    @overload
    async def scheduled_events(self, **params: Unpack[SofascoreScheduledEventsDefaultParams]) -> SofascoreScheduledEventsResponse: ...
    @overload
    async def scheduled_tournaments(self, **params: Unpack[SofascoreScheduledTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def scheduled_tournaments(self, **params: Unpack[SofascoreScheduledTournamentsTextResponseParams]) -> str: ...
    @overload
    async def scheduled_tournaments(self, **params: Unpack[SofascoreScheduledTournamentsDefaultParams]) -> SofascoreScheduledTournamentsResponse: ...
    @overload
    async def search(self, **params: Unpack[SofascoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[SofascoreSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[SofascoreSearchDefaultParams]) -> SofascoreSearchResponse: ...
    @overload
    async def season_events(self, **params: Unpack[SofascoreSeasonEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def season_events(self, **params: Unpack[SofascoreSeasonEventsTextResponseParams]) -> str: ...
    @overload
    async def season_events(self, **params: Unpack[SofascoreSeasonEventsDefaultParams]) -> SofascoreSeasonEventsResponse: ...
    @overload
    async def sports(self, **params: Unpack[SofascoreSportsStreamParams]) -> BinaryIO: ...
    @overload
    async def sports(self, **params: Unpack[SofascoreSportsTextResponseParams]) -> str: ...
    @overload
    async def sports(self, **params: Unpack[SofascoreSportsDefaultParams]) -> SofascoreSportsResponse: ...
    @overload
    async def standings(self, **params: Unpack[SofascoreStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def standings(self, **params: Unpack[SofascoreStandingsTextResponseParams]) -> str: ...
    @overload
    async def standings(self, **params: Unpack[SofascoreStandingsDefaultParams]) -> SofascoreStandingsResponse: ...
    @overload
    async def team(self, **params: Unpack[SofascoreTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[SofascoreTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[SofascoreTeamDefaultParams]) -> SofascoreTeamResponse: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsTextResponseParams]) -> str: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsDefaultParams]) -> SofascoreTeamEventsResponse: ...
    @overload
    async def team_of_the_week(self, **params: Unpack[SofascoreTeamOfTheWeekStreamParams]) -> BinaryIO: ...
    @overload
    async def team_of_the_week(self, **params: Unpack[SofascoreTeamOfTheWeekTextResponseParams]) -> str: ...
    @overload
    async def team_of_the_week(self, **params: Unpack[SofascoreTeamOfTheWeekDefaultParams]) -> SofascoreTeamOfTheWeekResponse: ...
    @overload
    async def team_of_the_week_periods(self, **params: Unpack[SofascoreTeamOfTheWeekPeriodsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_of_the_week_periods(self, **params: Unpack[SofascoreTeamOfTheWeekPeriodsTextResponseParams]) -> str: ...
    @overload
    async def team_of_the_week_periods(self, **params: Unpack[SofascoreTeamOfTheWeekPeriodsDefaultParams]) -> SofascoreTeamOfTheWeekPeriodsResponse: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersTextResponseParams]) -> str: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersDefaultParams]) -> SofascoreTeamPlayersResponse: ...
    @overload
    async def team_season_statistics(self, **params: Unpack[SofascoreTeamSeasonStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_season_statistics(self, **params: Unpack[SofascoreTeamSeasonStatisticsTextResponseParams]) -> str: ...
    @overload
    async def team_season_statistics(self, **params: Unpack[SofascoreTeamSeasonStatisticsDefaultParams]) -> SofascoreTeamSeasonStatisticsResponse: ...
    @overload
    async def team_statistics_seasons(self, **params: Unpack[SofascoreTeamStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_statistics_seasons(self, **params: Unpack[SofascoreTeamStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    async def team_statistics_seasons(self, **params: Unpack[SofascoreTeamStatisticsSeasonsDefaultParams]) -> SofascoreTeamStatisticsSeasonsResponse: ...
    @overload
    async def team_transfers(self, **params: Unpack[SofascoreTeamTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_transfers(self, **params: Unpack[SofascoreTeamTransfersTextResponseParams]) -> str: ...
    @overload
    async def team_transfers(self, **params: Unpack[SofascoreTeamTransfersDefaultParams]) -> SofascoreTeamTransfersResponse: ...
    @overload
    async def tournament_info(self, **params: Unpack[SofascoreTournamentInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_info(self, **params: Unpack[SofascoreTournamentInfoTextResponseParams]) -> str: ...
    @overload
    async def tournament_info(self, **params: Unpack[SofascoreTournamentInfoDefaultParams]) -> SofascoreTournamentInfoResponse: ...
    @overload
    async def tournament_player_statistics(self, **params: Unpack[SofascoreTournamentPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_player_statistics(self, **params: Unpack[SofascoreTournamentPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    async def tournament_player_statistics(self, **params: Unpack[SofascoreTournamentPlayerStatisticsDefaultParams]) -> SofascoreTournamentPlayerStatisticsResponse: ...
    @overload
    async def tournament_rounds(self, **params: Unpack[SofascoreTournamentRoundsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_rounds(self, **params: Unpack[SofascoreTournamentRoundsTextResponseParams]) -> str: ...
    @overload
    async def tournament_rounds(self, **params: Unpack[SofascoreTournamentRoundsDefaultParams]) -> SofascoreTournamentRoundsResponse: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsDefaultParams]) -> SofascoreTournamentSeasonsResponse: ...
    @overload
    async def tournament_top_players(self, **params: Unpack[SofascoreTournamentTopPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_top_players(self, **params: Unpack[SofascoreTournamentTopPlayersTextResponseParams]) -> str: ...
    @overload
    async def tournament_top_players(self, **params: Unpack[SofascoreTournamentTopPlayersDefaultParams]) -> SofascoreTournamentTopPlayersResponse: ...
    @overload
    async def tournament_top_teams(self, **params: Unpack[SofascoreTournamentTopTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_top_teams(self, **params: Unpack[SofascoreTournamentTopTeamsTextResponseParams]) -> str: ...
    @overload
    async def tournament_top_teams(self, **params: Unpack[SofascoreTournamentTopTeamsDefaultParams]) -> SofascoreTournamentTopTeamsResponse: ...

class _AsyncSofascoreGroup:
    @overload
    async def categories(self, **params: Unpack[SofascoreCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[SofascoreCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[SofascoreCategoriesDefaultParams]) -> SofascoreCategoriesResponse: ...
    @overload
    async def category_tournaments(self, **params: Unpack[SofascoreCategoryTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def category_tournaments(self, **params: Unpack[SofascoreCategoryTournamentsTextResponseParams]) -> str: ...
    @overload
    async def category_tournaments(self, **params: Unpack[SofascoreCategoryTournamentsDefaultParams]) -> SofascoreCategoryTournamentsResponse: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventStreamParams]) -> BinaryIO: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventTextResponseParams]) -> str: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventDefaultParams]) -> SofascoreEventResponse: ...
    @overload
    async def event_best_players(self, **params: Unpack[SofascoreEventBestPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def event_best_players(self, **params: Unpack[SofascoreEventBestPlayersTextResponseParams]) -> str: ...
    @overload
    async def event_best_players(self, **params: Unpack[SofascoreEventBestPlayersDefaultParams]) -> SofascoreEventBestPlayersResponse: ...
    @overload
    async def event_comments(self, **params: Unpack[SofascoreEventCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_comments(self, **params: Unpack[SofascoreEventCommentsTextResponseParams]) -> str: ...
    @overload
    async def event_comments(self, **params: Unpack[SofascoreEventCommentsDefaultParams]) -> SofascoreEventCommentsResponse: ...
    @overload
    async def event_graph(self, **params: Unpack[SofascoreEventGraphStreamParams]) -> BinaryIO: ...
    @overload
    async def event_graph(self, **params: Unpack[SofascoreEventGraphTextResponseParams]) -> str: ...
    @overload
    async def event_graph(self, **params: Unpack[SofascoreEventGraphDefaultParams]) -> SofascoreEventGraphResponse: ...
    @overload
    async def event_h2h(self, **params: Unpack[SofascoreEventH2hStreamParams]) -> BinaryIO: ...
    @overload
    async def event_h2h(self, **params: Unpack[SofascoreEventH2hTextResponseParams]) -> str: ...
    @overload
    async def event_h2h(self, **params: Unpack[SofascoreEventH2hDefaultParams]) -> SofascoreEventH2hResponse: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsTextResponseParams]) -> str: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsDefaultParams]) -> SofascoreEventIncidentsResponse: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsTextResponseParams]) -> str: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsDefaultParams]) -> SofascoreEventLineupsResponse: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsTextResponseParams]) -> str: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsDefaultParams]) -> SofascoreEventOddsResponse: ...
    @overload
    async def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    async def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsDefaultParams]) -> SofascoreEventPlayerStatisticsResponse: ...
    @overload
    async def event_shotmap(self, **params: Unpack[SofascoreEventShotmapStreamParams]) -> BinaryIO: ...
    @overload
    async def event_shotmap(self, **params: Unpack[SofascoreEventShotmapTextResponseParams]) -> str: ...
    @overload
    async def event_shotmap(self, **params: Unpack[SofascoreEventShotmapDefaultParams]) -> SofascoreEventShotmapResponse: ...
    @overload
    async def event_statistics(self, **params: Unpack[SofascoreEventStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_statistics(self, **params: Unpack[SofascoreEventStatisticsTextResponseParams]) -> str: ...
    @overload
    async def event_statistics(self, **params: Unpack[SofascoreEventStatisticsDefaultParams]) -> SofascoreEventStatisticsResponse: ...
    @overload
    async def live_events(self, **params: Unpack[SofascoreLiveEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def live_events(self, **params: Unpack[SofascoreLiveEventsTextResponseParams]) -> str: ...
    @overload
    async def live_events(self, **params: Unpack[SofascoreLiveEventsDefaultParams]) -> SofascoreLiveEventsResponse: ...
    @overload
    async def manager(self, **params: Unpack[SofascoreManagerStreamParams]) -> BinaryIO: ...
    @overload
    async def manager(self, **params: Unpack[SofascoreManagerTextResponseParams]) -> str: ...
    @overload
    async def manager(self, **params: Unpack[SofascoreManagerDefaultParams]) -> SofascoreManagerResponse: ...
    @overload
    async def manager_events(self, **params: Unpack[SofascoreManagerEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def manager_events(self, **params: Unpack[SofascoreManagerEventsTextResponseParams]) -> str: ...
    @overload
    async def manager_events(self, **params: Unpack[SofascoreManagerEventsDefaultParams]) -> SofascoreManagerEventsResponse: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerDefaultParams]) -> SofascorePlayerResponse: ...
    @overload
    async def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsTextResponseParams]) -> str: ...
    @overload
    async def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsDefaultParams]) -> SofascorePlayerSeasonStatisticsResponse: ...
    @overload
    async def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    async def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsDefaultParams]) -> SofascorePlayerStatisticsSeasonsResponse: ...
    @overload
    async def player_transfers(self, **params: Unpack[SofascorePlayerTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def player_transfers(self, **params: Unpack[SofascorePlayerTransfersTextResponseParams]) -> str: ...
    @overload
    async def player_transfers(self, **params: Unpack[SofascorePlayerTransfersDefaultParams]) -> SofascorePlayerTransfersResponse: ...
    @overload
    async def ranking_types(self, **params: Unpack[SofascoreRankingTypesStreamParams]) -> BinaryIO: ...
    @overload
    async def ranking_types(self, **params: Unpack[SofascoreRankingTypesTextResponseParams]) -> str: ...
    @overload
    async def ranking_types(self, **params: Unpack[SofascoreRankingTypesDefaultParams]) -> SofascoreRankingTypesResponse: ...
    @overload
    async def rankings(self, **params: Unpack[SofascoreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def rankings(self, **params: Unpack[SofascoreRankingsTextResponseParams]) -> str: ...
    @overload
    async def rankings(self, **params: Unpack[SofascoreRankingsDefaultParams]) -> SofascoreRankingsResponse: ...
    @overload
    async def round_events(self, **params: Unpack[SofascoreRoundEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def round_events(self, **params: Unpack[SofascoreRoundEventsTextResponseParams]) -> str: ...
    @overload
    async def round_events(self, **params: Unpack[SofascoreRoundEventsDefaultParams]) -> SofascoreRoundEventsResponse: ...
    @overload
    async def scheduled_events(self, **params: Unpack[SofascoreScheduledEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def scheduled_events(self, **params: Unpack[SofascoreScheduledEventsTextResponseParams]) -> str: ...
    @overload
    async def scheduled_events(self, **params: Unpack[SofascoreScheduledEventsDefaultParams]) -> SofascoreScheduledEventsResponse: ...
    @overload
    async def scheduled_tournaments(self, **params: Unpack[SofascoreScheduledTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def scheduled_tournaments(self, **params: Unpack[SofascoreScheduledTournamentsTextResponseParams]) -> str: ...
    @overload
    async def scheduled_tournaments(self, **params: Unpack[SofascoreScheduledTournamentsDefaultParams]) -> SofascoreScheduledTournamentsResponse: ...
    @overload
    async def search(self, **params: Unpack[SofascoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[SofascoreSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[SofascoreSearchDefaultParams]) -> SofascoreSearchResponse: ...
    @overload
    async def season_events(self, **params: Unpack[SofascoreSeasonEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def season_events(self, **params: Unpack[SofascoreSeasonEventsTextResponseParams]) -> str: ...
    @overload
    async def season_events(self, **params: Unpack[SofascoreSeasonEventsDefaultParams]) -> SofascoreSeasonEventsResponse: ...
    @overload
    async def sports(self, **params: Unpack[SofascoreSportsStreamParams]) -> BinaryIO: ...
    @overload
    async def sports(self, **params: Unpack[SofascoreSportsTextResponseParams]) -> str: ...
    @overload
    async def sports(self, **params: Unpack[SofascoreSportsDefaultParams]) -> SofascoreSportsResponse: ...
    @overload
    async def standings(self, **params: Unpack[SofascoreStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def standings(self, **params: Unpack[SofascoreStandingsTextResponseParams]) -> str: ...
    @overload
    async def standings(self, **params: Unpack[SofascoreStandingsDefaultParams]) -> SofascoreStandingsResponse: ...
    @overload
    async def team(self, **params: Unpack[SofascoreTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[SofascoreTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[SofascoreTeamDefaultParams]) -> SofascoreTeamResponse: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsTextResponseParams]) -> str: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsDefaultParams]) -> SofascoreTeamEventsResponse: ...
    @overload
    async def team_of_the_week(self, **params: Unpack[SofascoreTeamOfTheWeekStreamParams]) -> BinaryIO: ...
    @overload
    async def team_of_the_week(self, **params: Unpack[SofascoreTeamOfTheWeekTextResponseParams]) -> str: ...
    @overload
    async def team_of_the_week(self, **params: Unpack[SofascoreTeamOfTheWeekDefaultParams]) -> SofascoreTeamOfTheWeekResponse: ...
    @overload
    async def team_of_the_week_periods(self, **params: Unpack[SofascoreTeamOfTheWeekPeriodsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_of_the_week_periods(self, **params: Unpack[SofascoreTeamOfTheWeekPeriodsTextResponseParams]) -> str: ...
    @overload
    async def team_of_the_week_periods(self, **params: Unpack[SofascoreTeamOfTheWeekPeriodsDefaultParams]) -> SofascoreTeamOfTheWeekPeriodsResponse: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersTextResponseParams]) -> str: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersDefaultParams]) -> SofascoreTeamPlayersResponse: ...
    @overload
    async def team_season_statistics(self, **params: Unpack[SofascoreTeamSeasonStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_season_statistics(self, **params: Unpack[SofascoreTeamSeasonStatisticsTextResponseParams]) -> str: ...
    @overload
    async def team_season_statistics(self, **params: Unpack[SofascoreTeamSeasonStatisticsDefaultParams]) -> SofascoreTeamSeasonStatisticsResponse: ...
    @overload
    async def team_statistics_seasons(self, **params: Unpack[SofascoreTeamStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_statistics_seasons(self, **params: Unpack[SofascoreTeamStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    async def team_statistics_seasons(self, **params: Unpack[SofascoreTeamStatisticsSeasonsDefaultParams]) -> SofascoreTeamStatisticsSeasonsResponse: ...
    @overload
    async def team_transfers(self, **params: Unpack[SofascoreTeamTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_transfers(self, **params: Unpack[SofascoreTeamTransfersTextResponseParams]) -> str: ...
    @overload
    async def team_transfers(self, **params: Unpack[SofascoreTeamTransfersDefaultParams]) -> SofascoreTeamTransfersResponse: ...
    @overload
    async def tournament_info(self, **params: Unpack[SofascoreTournamentInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_info(self, **params: Unpack[SofascoreTournamentInfoTextResponseParams]) -> str: ...
    @overload
    async def tournament_info(self, **params: Unpack[SofascoreTournamentInfoDefaultParams]) -> SofascoreTournamentInfoResponse: ...
    @overload
    async def tournament_player_statistics(self, **params: Unpack[SofascoreTournamentPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_player_statistics(self, **params: Unpack[SofascoreTournamentPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    async def tournament_player_statistics(self, **params: Unpack[SofascoreTournamentPlayerStatisticsDefaultParams]) -> SofascoreTournamentPlayerStatisticsResponse: ...
    @overload
    async def tournament_rounds(self, **params: Unpack[SofascoreTournamentRoundsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_rounds(self, **params: Unpack[SofascoreTournamentRoundsTextResponseParams]) -> str: ...
    @overload
    async def tournament_rounds(self, **params: Unpack[SofascoreTournamentRoundsDefaultParams]) -> SofascoreTournamentRoundsResponse: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[SofascoreTournamentSeasonsDefaultParams]) -> SofascoreTournamentSeasonsResponse: ...
    @overload
    async def tournament_top_players(self, **params: Unpack[SofascoreTournamentTopPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_top_players(self, **params: Unpack[SofascoreTournamentTopPlayersTextResponseParams]) -> str: ...
    @overload
    async def tournament_top_players(self, **params: Unpack[SofascoreTournamentTopPlayersDefaultParams]) -> SofascoreTournamentTopPlayersResponse: ...
    @overload
    async def tournament_top_teams(self, **params: Unpack[SofascoreTournamentTopTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_top_teams(self, **params: Unpack[SofascoreTournamentTopTeamsTextResponseParams]) -> str: ...
    @overload
    async def tournament_top_teams(self, **params: Unpack[SofascoreTournamentTopTeamsDefaultParams]) -> SofascoreTournamentTopTeamsResponse: ...

SofascoreCategoriesDefaultParams = TypedDict('SofascoreCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreCategoriesTextResponseParams = TypedDict('SofascoreCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreCategoriesStreamParams = TypedDict('SofascoreCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreCategoryTournamentsDefaultParams = TypedDict('SofascoreCategoryTournamentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreCategoryTournamentsTextResponseParams = TypedDict('SofascoreCategoryTournamentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreCategoryTournamentsStreamParams = TypedDict('SofascoreCategoryTournamentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventDefaultParams = TypedDict('SofascoreEventDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventTextResponseParams = TypedDict('SofascoreEventTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventStreamParams = TypedDict('SofascoreEventStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventBestPlayersDefaultParams = TypedDict('SofascoreEventBestPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventBestPlayersTextResponseParams = TypedDict('SofascoreEventBestPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventBestPlayersStreamParams = TypedDict('SofascoreEventBestPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventCommentsDefaultParams = TypedDict('SofascoreEventCommentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventCommentsTextResponseParams = TypedDict('SofascoreEventCommentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventCommentsStreamParams = TypedDict('SofascoreEventCommentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventGraphDefaultParams = TypedDict('SofascoreEventGraphDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventGraphTextResponseParams = TypedDict('SofascoreEventGraphTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventGraphStreamParams = TypedDict('SofascoreEventGraphStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventH2hDefaultParams = TypedDict('SofascoreEventH2hDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventH2hTextResponseParams = TypedDict('SofascoreEventH2hTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventH2hStreamParams = TypedDict('SofascoreEventH2hStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventIncidentsDefaultParams = TypedDict('SofascoreEventIncidentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventIncidentsTextResponseParams = TypedDict('SofascoreEventIncidentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventIncidentsStreamParams = TypedDict('SofascoreEventIncidentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventLineupsDefaultParams = TypedDict('SofascoreEventLineupsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventLineupsTextResponseParams = TypedDict('SofascoreEventLineupsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventLineupsStreamParams = TypedDict('SofascoreEventLineupsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventOddsDefaultParams = TypedDict('SofascoreEventOddsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventOddsTextResponseParams = TypedDict('SofascoreEventOddsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventOddsStreamParams = TypedDict('SofascoreEventOddsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventPlayerStatisticsDefaultParams = TypedDict('SofascoreEventPlayerStatisticsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'player_id': Required[str],
}, total=False)

SofascoreEventPlayerStatisticsTextResponseParams = TypedDict('SofascoreEventPlayerStatisticsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'player_id': Required[str],
}, total=False)

SofascoreEventPlayerStatisticsStreamParams = TypedDict('SofascoreEventPlayerStatisticsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'player_id': Required[str],
}, total=False)

SofascoreEventShotmapDefaultParams = TypedDict('SofascoreEventShotmapDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventShotmapTextResponseParams = TypedDict('SofascoreEventShotmapTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventShotmapStreamParams = TypedDict('SofascoreEventShotmapStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventStatisticsDefaultParams = TypedDict('SofascoreEventStatisticsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventStatisticsTextResponseParams = TypedDict('SofascoreEventStatisticsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventStatisticsStreamParams = TypedDict('SofascoreEventStatisticsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreLiveEventsDefaultParams = TypedDict('SofascoreLiveEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreLiveEventsTextResponseParams = TypedDict('SofascoreLiveEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreLiveEventsStreamParams = TypedDict('SofascoreLiveEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreManagerDefaultParams = TypedDict('SofascoreManagerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreManagerTextResponseParams = TypedDict('SofascoreManagerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreManagerStreamParams = TypedDict('SofascoreManagerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreManagerEventsDefaultParams = TypedDict('SofascoreManagerEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreManagerEventsTextResponseParams = TypedDict('SofascoreManagerEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreManagerEventsStreamParams = TypedDict('SofascoreManagerEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascorePlayerDefaultParams = TypedDict('SofascorePlayerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascorePlayerTextResponseParams = TypedDict('SofascorePlayerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascorePlayerStreamParams = TypedDict('SofascorePlayerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascorePlayerSeasonStatisticsDefaultParams = TypedDict('SofascorePlayerSeasonStatisticsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascorePlayerSeasonStatisticsTextResponseParams = TypedDict('SofascorePlayerSeasonStatisticsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascorePlayerSeasonStatisticsStreamParams = TypedDict('SofascorePlayerSeasonStatisticsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascorePlayerStatisticsSeasonsDefaultParams = TypedDict('SofascorePlayerStatisticsSeasonsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascorePlayerStatisticsSeasonsTextResponseParams = TypedDict('SofascorePlayerStatisticsSeasonsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascorePlayerStatisticsSeasonsStreamParams = TypedDict('SofascorePlayerStatisticsSeasonsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascorePlayerTransfersDefaultParams = TypedDict('SofascorePlayerTransfersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascorePlayerTransfersTextResponseParams = TypedDict('SofascorePlayerTransfersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascorePlayerTransfersStreamParams = TypedDict('SofascorePlayerTransfersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreRankingTypesDefaultParams = TypedDict('SofascoreRankingTypesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

SofascoreRankingTypesTextResponseParams = TypedDict('SofascoreRankingTypesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

SofascoreRankingTypesStreamParams = TypedDict('SofascoreRankingTypesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

SofascoreRankingsDefaultParams = TypedDict('SofascoreRankingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'type': Required[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '34', '35', '36', '37', '40', '41', '42', '43', '44', '45', '46']],
    'limit': NotRequired[int],
}, total=False)

SofascoreRankingsTextResponseParams = TypedDict('SofascoreRankingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'type': Required[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '34', '35', '36', '37', '40', '41', '42', '43', '44', '45', '46']],
    'limit': NotRequired[int],
}, total=False)

SofascoreRankingsStreamParams = TypedDict('SofascoreRankingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'type': Required[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '34', '35', '36', '37', '40', '41', '42', '43', '44', '45', '46']],
    'limit': NotRequired[int],
}, total=False)

SofascoreRoundEventsDefaultParams = TypedDict('SofascoreRoundEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
    'round': Required[int],
    'slug': NotRequired[str],
    'prefix': NotRequired[str],
}, total=False)

SofascoreRoundEventsTextResponseParams = TypedDict('SofascoreRoundEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
    'round': Required[int],
    'slug': NotRequired[str],
    'prefix': NotRequired[str],
}, total=False)

SofascoreRoundEventsStreamParams = TypedDict('SofascoreRoundEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
    'round': Required[int],
    'slug': NotRequired[str],
    'prefix': NotRequired[str],
}, total=False)

SofascoreScheduledEventsDefaultParams = TypedDict('SofascoreScheduledEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'category_id': Required[str],
    'date': Required[str],
}, total=False)

SofascoreScheduledEventsTextResponseParams = TypedDict('SofascoreScheduledEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'category_id': Required[str],
    'date': Required[str],
}, total=False)

SofascoreScheduledEventsStreamParams = TypedDict('SofascoreScheduledEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'category_id': Required[str],
    'date': Required[str],
}, total=False)

SofascoreScheduledTournamentsDefaultParams = TypedDict('SofascoreScheduledTournamentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
    'date': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreScheduledTournamentsTextResponseParams = TypedDict('SofascoreScheduledTournamentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
    'date': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreScheduledTournamentsStreamParams = TypedDict('SofascoreScheduledTournamentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
    'date': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreSearchDefaultParams = TypedDict('SofascoreSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
}, total=False)

SofascoreSearchTextResponseParams = TypedDict('SofascoreSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
}, total=False)

SofascoreSearchStreamParams = TypedDict('SofascoreSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
}, total=False)

SofascoreSeasonEventsDefaultParams = TypedDict('SofascoreSeasonEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
    'direction': Required[Literal['next', 'last']],
    'page': NotRequired[int],
}, total=False)

SofascoreSeasonEventsTextResponseParams = TypedDict('SofascoreSeasonEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
    'direction': Required[Literal['next', 'last']],
    'page': NotRequired[int],
}, total=False)

SofascoreSeasonEventsStreamParams = TypedDict('SofascoreSeasonEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
    'direction': Required[Literal['next', 'last']],
    'page': NotRequired[int],
}, total=False)

SofascoreSportsDefaultParams = TypedDict('SofascoreSportsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

SofascoreSportsTextResponseParams = TypedDict('SofascoreSportsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

SofascoreSportsStreamParams = TypedDict('SofascoreSportsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

SofascoreStandingsDefaultParams = TypedDict('SofascoreStandingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
    'type': Required[Literal['total', 'home', 'away']],
}, total=False)

SofascoreStandingsTextResponseParams = TypedDict('SofascoreStandingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
    'type': Required[Literal['total', 'home', 'away']],
}, total=False)

SofascoreStandingsStreamParams = TypedDict('SofascoreStandingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
    'type': Required[Literal['total', 'home', 'away']],
}, total=False)

SofascoreTeamDefaultParams = TypedDict('SofascoreTeamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreTeamTextResponseParams = TypedDict('SofascoreTeamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreTeamStreamParams = TypedDict('SofascoreTeamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreTeamEventsDefaultParams = TypedDict('SofascoreTeamEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'direction': Required[Literal['next', 'last']],
    'page': NotRequired[int],
}, total=False)

SofascoreTeamEventsTextResponseParams = TypedDict('SofascoreTeamEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'direction': Required[Literal['next', 'last']],
    'page': NotRequired[int],
}, total=False)

SofascoreTeamEventsStreamParams = TypedDict('SofascoreTeamEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'direction': Required[Literal['next', 'last']],
    'page': NotRequired[int],
}, total=False)

SofascoreTeamOfTheWeekDefaultParams = TypedDict('SofascoreTeamOfTheWeekDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
    'period': Required[str],
}, total=False)

SofascoreTeamOfTheWeekTextResponseParams = TypedDict('SofascoreTeamOfTheWeekTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
    'period': Required[str],
}, total=False)

SofascoreTeamOfTheWeekStreamParams = TypedDict('SofascoreTeamOfTheWeekStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
    'period': Required[str],
}, total=False)

SofascoreTeamOfTheWeekPeriodsDefaultParams = TypedDict('SofascoreTeamOfTheWeekPeriodsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTeamOfTheWeekPeriodsTextResponseParams = TypedDict('SofascoreTeamOfTheWeekPeriodsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTeamOfTheWeekPeriodsStreamParams = TypedDict('SofascoreTeamOfTheWeekPeriodsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTeamPlayersDefaultParams = TypedDict('SofascoreTeamPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreTeamPlayersTextResponseParams = TypedDict('SofascoreTeamPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreTeamPlayersStreamParams = TypedDict('SofascoreTeamPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreTeamSeasonStatisticsDefaultParams = TypedDict('SofascoreTeamSeasonStatisticsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascoreTeamSeasonStatisticsTextResponseParams = TypedDict('SofascoreTeamSeasonStatisticsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascoreTeamSeasonStatisticsStreamParams = TypedDict('SofascoreTeamSeasonStatisticsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascoreTeamStatisticsSeasonsDefaultParams = TypedDict('SofascoreTeamStatisticsSeasonsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreTeamStatisticsSeasonsTextResponseParams = TypedDict('SofascoreTeamStatisticsSeasonsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreTeamStatisticsSeasonsStreamParams = TypedDict('SofascoreTeamStatisticsSeasonsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreTeamTransfersDefaultParams = TypedDict('SofascoreTeamTransfersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreTeamTransfersTextResponseParams = TypedDict('SofascoreTeamTransfersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreTeamTransfersStreamParams = TypedDict('SofascoreTeamTransfersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreTournamentInfoDefaultParams = TypedDict('SofascoreTournamentInfoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': NotRequired[str],
}, total=False)

SofascoreTournamentInfoTextResponseParams = TypedDict('SofascoreTournamentInfoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': NotRequired[str],
}, total=False)

SofascoreTournamentInfoStreamParams = TypedDict('SofascoreTournamentInfoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': NotRequired[str],
}, total=False)

SofascoreTournamentPlayerStatisticsDefaultParams = TypedDict('SofascoreTournamentPlayerStatisticsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
    'order': NotRequired[Literal['rating', 'goals', 'expectedGoals', 'assists', 'successfulDribbles', 'tackles', 'accuratePassesPercentage', 'bigChancesMissed', 'totalShots', 'goalConversionPercentage', 'interceptions', 'clearances', 'errorLeadToGoal', 'outfielderBlocks', 'bigChancesCreated', 'accuratePasses', 'keyPasses', 'saves', 'cleanSheet', 'penaltySave', 'savedShotsFromInsideTheBox', 'runsOut']],
    'direction': NotRequired[Literal['desc', 'asc']],
    'accumulation': NotRequired[Literal['total', 'perGame', 'per90']],
    'group': NotRequired[Literal['summary', 'attack', 'defence', 'passing', 'goalkeeper']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SofascoreTournamentPlayerStatisticsTextResponseParams = TypedDict('SofascoreTournamentPlayerStatisticsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
    'order': NotRequired[Literal['rating', 'goals', 'expectedGoals', 'assists', 'successfulDribbles', 'tackles', 'accuratePassesPercentage', 'bigChancesMissed', 'totalShots', 'goalConversionPercentage', 'interceptions', 'clearances', 'errorLeadToGoal', 'outfielderBlocks', 'bigChancesCreated', 'accuratePasses', 'keyPasses', 'saves', 'cleanSheet', 'penaltySave', 'savedShotsFromInsideTheBox', 'runsOut']],
    'direction': NotRequired[Literal['desc', 'asc']],
    'accumulation': NotRequired[Literal['total', 'perGame', 'per90']],
    'group': NotRequired[Literal['summary', 'attack', 'defence', 'passing', 'goalkeeper']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SofascoreTournamentPlayerStatisticsStreamParams = TypedDict('SofascoreTournamentPlayerStatisticsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
    'order': NotRequired[Literal['rating', 'goals', 'expectedGoals', 'assists', 'successfulDribbles', 'tackles', 'accuratePassesPercentage', 'bigChancesMissed', 'totalShots', 'goalConversionPercentage', 'interceptions', 'clearances', 'errorLeadToGoal', 'outfielderBlocks', 'bigChancesCreated', 'accuratePasses', 'keyPasses', 'saves', 'cleanSheet', 'penaltySave', 'savedShotsFromInsideTheBox', 'runsOut']],
    'direction': NotRequired[Literal['desc', 'asc']],
    'accumulation': NotRequired[Literal['total', 'perGame', 'per90']],
    'group': NotRequired[Literal['summary', 'attack', 'defence', 'passing', 'goalkeeper']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

SofascoreTournamentRoundsDefaultParams = TypedDict('SofascoreTournamentRoundsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentRoundsTextResponseParams = TypedDict('SofascoreTournamentRoundsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentRoundsStreamParams = TypedDict('SofascoreTournamentRoundsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentSeasonsDefaultParams = TypedDict('SofascoreTournamentSeasonsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreTournamentSeasonsTextResponseParams = TypedDict('SofascoreTournamentSeasonsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreTournamentSeasonsStreamParams = TypedDict('SofascoreTournamentSeasonsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreTournamentTopPlayersDefaultParams = TypedDict('SofascoreTournamentTopPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'regular_season', 'playoffs']],
    'limit': NotRequired[int],
}, total=False)

SofascoreTournamentTopPlayersTextResponseParams = TypedDict('SofascoreTournamentTopPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'regular_season', 'playoffs']],
    'limit': NotRequired[int],
}, total=False)

SofascoreTournamentTopPlayersStreamParams = TypedDict('SofascoreTournamentTopPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'regular_season', 'playoffs']],
    'limit': NotRequired[int],
}, total=False)

SofascoreTournamentTopTeamsDefaultParams = TypedDict('SofascoreTournamentTopTeamsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'regular_season', 'playoffs']],
    'limit': NotRequired[int],
}, total=False)

SofascoreTournamentTopTeamsTextResponseParams = TypedDict('SofascoreTournamentTopTeamsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'regular_season', 'playoffs']],
    'limit': NotRequired[int],
}, total=False)

SofascoreTournamentTopTeamsStreamParams = TypedDict('SofascoreTournamentTopTeamsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'regular_season', 'playoffs']],
    'limit': NotRequired[int],
}, total=False)
