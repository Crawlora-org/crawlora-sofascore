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

ModelSofascoreVenueEventsResponseDoc = TypedDict('ModelSofascoreVenueEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreVenueEventsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreVenueEventsResponse = TypedDict('ModelSofascoreVenueEventsResponse', {
    'count': NotRequired[int],
    'direction': NotRequired[str],
    'events': NotRequired[list[ModelSofascoreEventSummary]],
    'fetched_at': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'page': NotRequired[int],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
    'tournament_id': NotRequired[int],
    'venue_id': NotRequired[int],
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

ModelSofascoreVenueResponseDoc = TypedDict('ModelSofascoreVenueResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreVenueResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreVenueResponse = TypedDict('ModelSofascoreVenueResponse', {
    'fetched_at': NotRequired[str],
    'main_teams': NotRequired[list[ModelSofascoreTeamRef]],
    'source_url': NotRequired[str],
    'sports': NotRequired[list[ModelSofascoreVenueSportStatistics]],
    'totals': NotRequired[ModelSofascoreVenueTotals],
    'venue': NotRequired[ModelSofascoreVenueRecord],
}, total=False)

ModelSofascoreVenueRecord = TypedDict('ModelSofascoreVenueRecord', {
    'capacity': NotRequired[int],
    'city': NotRequired[str],
    'country': NotRequired[str],
    'hidden': NotRequired[bool],
    'id': NotRequired[int],
    'latitude': NotRequired[float],
    'longitude': NotRequired[float],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'state': NotRequired[str],
}, total=False)

ModelSofascoreVenueTotals = TypedDict('ModelSofascoreVenueTotals', {
    'avg_corner_kicks_per_game': NotRequired[float],
    'avg_red_cards_per_game': NotRequired[float],
    'away_team_goals_scored': NotRequired[float],
    'away_team_wins_percentage': NotRequired[float],
    'draws_percentage': NotRequired[float],
    'home_team_goals_scored': NotRequired[float],
    'home_team_wins_percentage': NotRequired[float],
    'total_matches': NotRequired[int],
}, total=False)

ModelSofascoreVenueSportStatistics = TypedDict('ModelSofascoreVenueSportStatistics', {
    'draw_percentage': NotRequired[float],
    'goals_scored': NotRequired[float],
    'home_win_percentage': NotRequired[float],
    'sport': NotRequired[str],
    'total_matches': NotRequired[int],
}, total=False)

ModelSofascoreTrendingPlayersResponseDoc = TypedDict('ModelSofascoreTrendingPlayersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTrendingPlayersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTrendingPlayersResponse = TypedDict('ModelSofascoreTrendingPlayersResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'players': NotRequired[list[ModelSofascoreTrendingPlayer]],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelSofascoreTrendingPlayer = TypedDict('ModelSofascoreTrendingPlayer', {
    'event': NotRequired[ModelSofascoreEventSummary],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'statistics': NotRequired[dict[str, float]],
    'team': NotRequired[ModelSofascoreTeamRef],
}, total=False)

ModelSofascorePlayerBrief = TypedDict('ModelSofascorePlayerBrief', {
    'id': NotRequired[int],
    'jersey_number': NotRequired[str],
    'name': NotRequired[str],
    'position': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelSofascoreTrendingEventsResponseDoc = TypedDict('ModelSofascoreTrendingEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTrendingEventsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTrendingEventsResponse = TypedDict('ModelSofascoreTrendingEventsResponse', {
    'count': NotRequired[int],
    'country': NotRequired[str],
    'events': NotRequired[list[ModelSofascoreTrendingEvent]],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreTrendingEvent = TypedDict('ModelSofascoreTrendingEvent', {
    'away_score': NotRequired[ModelSofascoreScoreLine],
    'away_team': NotRequired[ModelSofascoreTeamRef],
    'home_score': NotRequired[ModelSofascoreScoreLine],
    'home_team': NotRequired[ModelSofascoreTeamRef],
    'id': NotRequired[int],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'start_time': NotRequired[str],
    'start_timestamp': NotRequired[int],
    'status': NotRequired[ModelSofascoreEventStatus],
    'tournament': NotRequired[ModelSofascoreTournamentRef],
    'winner_code': NotRequired[int],
}, total=False)

ModelSofascoreTournamentsWithFeatureResponseDoc = TypedDict('ModelSofascoreTournamentsWithFeatureResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentsWithFeatureResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentsWithFeatureResponse = TypedDict('ModelSofascoreTournamentsWithFeatureResponse', {
    'count': NotRequired[int],
    'feature': NotRequired[str],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
    'tournaments': NotRequired[list[ModelSofascoreFeatureTournament]],
}, total=False)

ModelSofascoreFeatureTournament = TypedDict('ModelSofascoreFeatureTournament', {
    'category_id': NotRequired[int],
    'category_name': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'user_count': NotRequired[int],
}, total=False)

ModelSofascoreTournamentWinnersResponseDoc = TypedDict('ModelSofascoreTournamentWinnersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentWinnersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentWinnersResponse = TypedDict('ModelSofascoreTournamentWinnersResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[int],
    'winners': NotRequired[list[ModelSofascoreTournamentWinner]],
}, total=False)

ModelSofascoreTournamentWinner = TypedDict('ModelSofascoreTournamentWinner', {
    'season_id': NotRequired[int],
    'winner': NotRequired[ModelSofascoreTeamRef],
    'year': NotRequired[int],
}, total=False)

ModelSofascoreTournamentVenuesResponseDoc = TypedDict('ModelSofascoreTournamentVenuesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentVenuesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentVenuesResponse = TypedDict('ModelSofascoreTournamentVenuesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[int],
    'venues': NotRequired[list[ModelSofascoreVenueRecord]],
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

ModelSofascoreTournamentTeamsResponseDoc = TypedDict('ModelSofascoreTournamentTeamsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentTeamsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentTeamsResponse = TypedDict('ModelSofascoreTournamentTeamsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelSofascoreSeasonTeam]],
    'tournament_id': NotRequired[int],
}, total=False)

ModelSofascoreSeasonTeam = TypedDict('ModelSofascoreSeasonTeam', {
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'gender': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'name_code': NotRequired[str],
    'national': NotRequired[bool],
    'ranking': NotRequired[int],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'type': NotRequired[int],
    'user_count': NotRequired[int],
}, total=False)

ModelSofascoreTournamentTeamOfTheSeasonResponseDoc = TypedDict('ModelSofascoreTournamentTeamOfTheSeasonResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentTeamOfTheSeasonResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentTeamOfTheSeasonResponse = TypedDict('ModelSofascoreTournamentTeamOfTheSeasonResponse', {
    'count': NotRequired[int],
    'created_at': NotRequired[str],
    'fetched_at': NotRequired[str],
    'formation': NotRequired[str],
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

ModelSofascoreTournamentStatisticsInfoResponseDoc = TypedDict('ModelSofascoreTournamentStatisticsInfoResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentStatisticsInfoResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentStatisticsInfoResponse = TypedDict('ModelSofascoreTournamentStatisticsInfoResponse', {
    'detailed_groups': NotRequired[dict[str, list[str]]],
    'fetched_at': NotRequired[str],
    'groups': NotRequired[dict[str, list[str]]],
    'nationalities': NotRequired[list[ModelSofascoreNamedCode]],
    'positions': NotRequired[list[ModelSofascoreNamedCode]],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelSofascoreTeamRef]],
    'tournament_id': NotRequired[int],
}, total=False)

ModelSofascoreNamedCode = TypedDict('ModelSofascoreNamedCode', {
    'code': NotRequired[str],
    'name': NotRequired[str],
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
    'filters': NotRequired[ModelSofascorePlayerStatisticsFilters],
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

ModelSofascorePlayerStatisticsFilters = TypedDict('ModelSofascorePlayerStatisticsFilters', {
    'min_appearances': NotRequired[int],
    'min_minutes': NotRequired[int],
    'nationalities': NotRequired[list[str]],
    'positions': NotRequired[list[str]],
    'team_ids': NotRequired[list[int]],
}, total=False)

ModelSofascoreTournamentPlayerOfTheSeasonResponseDoc = TypedDict('ModelSofascoreTournamentPlayerOfTheSeasonResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentPlayerOfTheSeasonResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentPlayerOfTheSeasonResponse = TypedDict('ModelSofascoreTournamentPlayerOfTheSeasonResponse', {
    'appearances': NotRequired[int],
    'fetched_at': NotRequired[str],
    'jersey_number': NotRequired[str],
    'player': NotRequired[ModelSofascorePlayerRef],
    'rating': NotRequired[float],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'statistics_type': NotRequired[str],
    'team': NotRequired[ModelSofascoreTeamRef],
    'tournament_id': NotRequired[int],
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

ModelSofascoreTournamentCupTreeResponseDoc = TypedDict('ModelSofascoreTournamentCupTreeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTournamentCupTreeResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTournamentCupTreeResponse = TypedDict('ModelSofascoreTournamentCupTreeResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[int],
    'trees': NotRequired[list[ModelSofascoreCupTree]],
}, total=False)

ModelSofascoreCupTree = TypedDict('ModelSofascoreCupTree', {
    'current_round': NotRequired[int],
    'final_match': NotRequired[ModelSofascoreCupTreeBlock],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'rounds': NotRequired[list[ModelSofascoreCupTreeRound]],
    'third_place_match': NotRequired[ModelSofascoreCupTreeBlock],
    'tournament_name': NotRequired[str],
}, total=False)

ModelSofascoreCupTreeBlock = TypedDict('ModelSofascoreCupTreeBlock', {
    'away_score': NotRequired[str],
    'block_id': NotRequired[int],
    'event_ids': NotRequired[list[int]],
    'finished': NotRequired[bool],
    'home_score': NotRequired[str],
    'id': NotRequired[int],
    'in_progress': NotRequired[bool],
    'matches': NotRequired[int],
    'order': NotRequired[int],
    'participants': NotRequired[list[ModelSofascoreCupTreeParticipant]],
    'result': NotRequired[str],
    'series_start_time': NotRequired[str],
    'series_start_timestamp': NotRequired[int],
    'venue': NotRequired[ModelSofascoreVenue],
}, total=False)

ModelSofascoreVenue = TypedDict('ModelSofascoreVenue', {
    'capacity': NotRequired[int],
    'city': NotRequired[str],
    'country': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelSofascoreCupTreeParticipant = TypedDict('ModelSofascoreCupTreeParticipant', {
    'order': NotRequired[int],
    'seed': NotRequired[str],
    'source_block_id': NotRequired[int],
    'team': NotRequired[ModelSofascoreTeamRef],
    'winner': NotRequired[bool],
}, total=False)

ModelSofascoreCupTreeRound = TypedDict('ModelSofascoreCupTreeRound', {
    'blocks': NotRequired[list[ModelSofascoreCupTreeBlock]],
    'description': NotRequired[str],
    'id': NotRequired[int],
    'order': NotRequired[int],
    'round_type': NotRequired[int],
}, total=False)

ModelSofascoreTennisGrandSlamResultsResponseDoc = TypedDict('ModelSofascoreTennisGrandSlamResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTennisGrandSlamResultsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTennisGrandSlamResultsResponse = TypedDict('ModelSofascoreTennisGrandSlamResultsResponse', {
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
    'tournaments': NotRequired[list[ModelSofascoreGrandSlamTournament]],
}, total=False)

ModelSofascoreGrandSlamTournament = TypedDict('ModelSofascoreGrandSlamTournament', {
    'name': NotRequired[str],
    'tournament_id': NotRequired[int],
    'years': NotRequired[list[ModelSofascoreGrandSlamYear]],
}, total=False)

ModelSofascoreGrandSlamYear = TypedDict('ModelSofascoreGrandSlamYear', {
    'is_live': NotRequired[bool],
    'is_upcoming': NotRequired[bool],
    'round': NotRequired[str],
    'season_id': NotRequired[int],
    'winner': NotRequired[bool],
    'year': NotRequired[int],
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

ModelSofascoreTeamTournamentsResponseDoc = TypedDict('ModelSofascoreTeamTournamentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamTournamentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamTournamentsResponse = TypedDict('ModelSofascoreTeamTournamentsResponse', {
    'all': NotRequired[bool],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
    'tournaments': NotRequired[list[ModelSofascoreUniqueTournamentBrief]],
}, total=False)

ModelSofascoreUniqueTournamentBrief = TypedDict('ModelSofascoreUniqueTournamentBrief', {
    'category': NotRequired[str],
    'gender': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelSofascoreTeamTopPlayersResponseDoc = TypedDict('ModelSofascoreTeamTopPlayersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamTopPlayersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamTopPlayersResponse = TypedDict('ModelSofascoreTeamTopPlayersResponse', {
    'categories': NotRequired[list[ModelSofascoreTopPlayerCategory]],
    'category_count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
    'team_id': NotRequired[int],
    'tournament_id': NotRequired[int],
    'type': NotRequired[str],
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

ModelSofascoreTeamRankingsResponseDoc = TypedDict('ModelSofascoreTeamRankingsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamRankingsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamRankingsResponse = TypedDict('ModelSofascoreTeamRankingsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'rankings': NotRequired[list[ModelSofascoreTeamRanking]],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
}, total=False)

ModelSofascoreTeamRanking = TypedDict('ModelSofascoreTeamRanking', {
    'category': NotRequired[str],
    'gender': NotRequired[str],
    'last_updated': NotRequired[str],
    'last_updated_timestamp': NotRequired[int],
    'name': NotRequired[str],
    'rows': NotRequired[list[ModelSofascoreTeamRankingRow]],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'type_id': NotRequired[int],
}, total=False)

ModelSofascoreTeamRankingRow = TypedDict('ModelSofascoreTeamRankingRow', {
    'best_position': NotRequired[int],
    'max_points': NotRequired[float],
    'next_win_points': NotRequired[float],
    'points': NotRequired[float],
    'position': NotRequired[int],
    'previous_points': NotRequired[float],
    'previous_position': NotRequired[int],
    'team': NotRequired[ModelSofascoreTeamRef],
    'tournaments_played': NotRequired[int],
    'updated_at': NotRequired[str],
    'updated_timestamp': NotRequired[int],
    'year': NotRequired[int],
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

ModelSofascoreTeamPlayerStatisticsSeasonsResponseDoc = TypedDict('ModelSofascoreTeamPlayerStatisticsSeasonsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamPlayerStatisticsSeasonsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamPlayerStatisticsSeasonsResponse = TypedDict('ModelSofascoreTeamPlayerStatisticsSeasonsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
    'tournaments': NotRequired[list[ModelSofascoreStatisticsTournament]],
}, total=False)

ModelSofascoreTeamPlayerStatisticsResponseDoc = TypedDict('ModelSofascoreTeamPlayerStatisticsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamPlayerStatisticsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamPlayerStatisticsResponse = TypedDict('ModelSofascoreTeamPlayerStatisticsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'players': NotRequired[list[ModelSofascoreTeamPlayerStatistics]],
    'season': NotRequired[int],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
    'tournament_id': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreTeamPlayerStatistics = TypedDict('ModelSofascoreTeamPlayerStatistics', {
    'played_enough': NotRequired[bool],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'statistics': NotRequired[dict[str, float]],
}, total=False)

ModelSofascoreTeamPerformanceResponseDoc = TypedDict('ModelSofascoreTeamPerformanceResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamPerformanceResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamPerformanceResponse = TypedDict('ModelSofascoreTeamPerformanceResponse', {
    'count': NotRequired[int],
    'events': NotRequired[list[ModelSofascoreTeamPerformanceEvent]],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
}, total=False)

ModelSofascoreTeamPerformanceEvent = TypedDict('ModelSofascoreTeamPerformanceEvent', {
    'event': NotRequired[ModelSofascoreEventSummary],
    'points': NotRequired[float],
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

ModelSofascoreTeamNearEventsResponseDoc = TypedDict('ModelSofascoreTeamNearEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamNearEventsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamNearEventsResponse = TypedDict('ModelSofascoreTeamNearEventsResponse', {
    'fetched_at': NotRequired[str],
    'next_event': NotRequired[ModelSofascoreEventSummary],
    'previous_event': NotRequired[ModelSofascoreEventSummary],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
}, total=False)

ModelSofascoreTeamGoalDistributionsResponseDoc = TypedDict('ModelSofascoreTeamGoalDistributionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamGoalDistributionsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamGoalDistributionsResponse = TypedDict('ModelSofascoreTeamGoalDistributionsResponse', {
    'distributions': NotRequired[list[ModelSofascoreGoalDistribution]],
    'fetched_at': NotRequired[str],
    'season_id': NotRequired[int],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
    'tournament_id': NotRequired[int],
}, total=False)

ModelSofascoreGoalDistribution = TypedDict('ModelSofascoreGoalDistribution', {
    'conceded_goals': NotRequired[int],
    'matches': NotRequired[int],
    'periods': NotRequired[list[ModelSofascoreGoalPeriod]],
    'scored_goals': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreGoalPeriod = TypedDict('ModelSofascoreGoalPeriod', {
    'conceded_goals': NotRequired[int],
    'end_minute': NotRequired[int],
    'scored_goals': NotRequired[int],
    'start_minute': NotRequired[int],
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

ModelSofascoreTeamAchievementsResponseDoc = TypedDict('ModelSofascoreTeamAchievementsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreTeamAchievementsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreTeamAchievementsResponse = TypedDict('ModelSofascoreTeamAchievementsResponse', {
    'achievements': NotRequired[list[ModelSofascoreTeamAchievement]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
    'total_trophies': NotRequired[int],
}, total=False)

ModelSofascoreTeamAchievement = TypedDict('ModelSofascoreTeamAchievement', {
    'competition': NotRequired[ModelSofascoreUniqueTournamentBrief],
    'seasons': NotRequired[list[ModelSofascoreAchievementSeason]],
    'trophies_won': NotRequired[int],
}, total=False)

ModelSofascoreAchievementSeason = TypedDict('ModelSofascoreAchievementSeason', {
    'season_id': NotRequired[int],
    'year': NotRequired[str],
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

ModelSofascoreStageSubstagesResponseDoc = TypedDict('ModelSofascoreStageSubstagesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreStageSubstagesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreStageSubstagesResponse = TypedDict('ModelSofascoreStageSubstagesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'stage_id': NotRequired[int],
    'stages': NotRequired[list[ModelSofascoreStage]],
}, total=False)

ModelSofascoreStage = TypedDict('ModelSofascoreStage', {
    'competition': NotRequired[ModelSofascoreStageCompetition],
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'end_timestamp': NotRequired[int],
    'id': NotRequired[int],
    'info': NotRequired[ModelSofascoreStageInfo],
    'name': NotRequired[str],
    'on_date': NotRequired[bool],
    'parent': NotRequired[ModelSofascoreStageRef],
    'parts': NotRequired[list[ModelSofascoreStageSession]],
    'season_name': NotRequired[str],
    'sequence': NotRequired[int],
    'session': NotRequired[ModelSofascoreStageSession],
    'session_start_timestamps': NotRequired[list[int]],
    'slug': NotRequired[str],
    'start_time': NotRequired[str],
    'start_timestamp': NotRequired[int],
    'status': NotRequired[ModelSofascoreStageStatus],
    'type': NotRequired[ModelSofascoreStageType],
    'winner': NotRequired[ModelSofascoreStageEntity],
    'year': NotRequired[str],
}, total=False)

ModelSofascoreStageEntity = TypedDict('ModelSofascoreStageEntity', {
    'code': NotRequired[str],
    'country': NotRequired[str],
    'country_code': NotRequired[str],
    'id': NotRequired[int],
    'kind': NotRequired[str],
    'name': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
    'team': NotRequired[ModelSofascoreStageTeamRef],
}, total=False)

ModelSofascoreStageTeamRef = TypedDict('ModelSofascoreStageTeamRef', {
    'chassis': NotRequired[str],
    'code': NotRequired[str],
    'country': NotRequired[str],
    'engine': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'short_name': NotRequired[str],
}, total=False)

ModelSofascoreStageType = TypedDict('ModelSofascoreStageType', {
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelSofascoreStageStatus = TypedDict('ModelSofascoreStageStatus', {
    'description': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreStageSession = TypedDict('ModelSofascoreStageSession', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'sequence': NotRequired[int],
    'slug': NotRequired[str],
    'start_timestamp': NotRequired[int],
    'status': NotRequired[ModelSofascoreStageStatus],
    'type': NotRequired[ModelSofascoreStageType],
}, total=False)

ModelSofascoreStageRef = TypedDict('ModelSofascoreStageRef', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'start_timestamp': NotRequired[int],
}, total=False)

ModelSofascoreStageInfo = TypedDict('ModelSofascoreStageInfo', {
    'actual_distance': NotRequired[float],
    'air_temperature': NotRequired[float],
    'arrival_city': NotRequired[str],
    'average_speed': NotRequired[float],
    'caution_laps': NotRequired[int],
    'cautions': NotRequired[int],
    'circuit': NotRequired[str],
    'circuit_city': NotRequired[str],
    'circuit_country': NotRequired[str],
    'circuit_length_m': NotRequired[float],
    'departure_city': NotRequired[str],
    'discipline': NotRequired[str],
    'distance': NotRequired[float],
    'elapsed_time': NotRequired[str],
    'humidity': NotRequired[float],
    'lap_record': NotRequired[str],
    'laps': NotRequired[int],
    'laps_completed': NotRequired[int],
    'lead_changes': NotRequired[int],
    'race_distance_m': NotRequired[float],
    'race_segments': NotRequired[int],
    'race_type': NotRequired[str],
    'round': NotRequired[int],
    'safety_car': NotRequired[bool],
    'special_stages': NotRequired[int],
    'stage_day': NotRequired[str],
    'summary': NotRequired[str],
    'track_condition': NotRequired[str],
    'track_temperature': NotRequired[float],
    'weather': NotRequired[str],
}, total=False)

ModelSofascoreStageCompetition = TypedDict('ModelSofascoreStageCompetition', {
    'category_id': NotRequired[int],
    'category_name': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelSofascoreStageStandingsResponseDoc = TypedDict('ModelSofascoreStageStandingsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreStageStandingsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreStageStandingsResponse = TypedDict('ModelSofascoreStageStandingsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'stage_id': NotRequired[int],
    'standings': NotRequired[list[ModelSofascoreStageStanding]],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreStageStanding = TypedDict('ModelSofascoreStageStanding', {
    'bonus_points': NotRequired[float],
    'comment': NotRequired[str],
    'competitor': NotRequired[ModelSofascoreStageEntity],
    'did_not_finish': NotRequired[int],
    'distance': NotRequired[float],
    'fastest_lap_time': NotRequired[str],
    'fastest_laps': NotRequired[int],
    'gap': NotRequired[str],
    'grid_position': NotRequired[int],
    'interval': NotRequired[str],
    'jersey': NotRequired[str],
    'laps': NotRequired[int],
    'laps_behind': NotRequired[int],
    'laps_led': NotRequired[int],
    'personal_fastest_lap': NotRequired[int],
    'personal_fastest_lap_time': NotRequired[str],
    'pit_stops': NotRequired[int],
    'podiums': NotRequired[int],
    'points': NotRequired[float],
    'pole_positions': NotRequired[int],
    'position': NotRequired[int],
    'races_started': NotRequired[int],
    'races_with_points': NotRequired[int],
    'rank': NotRequired[int],
    'start_number': NotRequired[int],
    'status': NotRequired[str],
    'sub_status': NotRequired[str],
    'time': NotRequired[str],
    'top10': NotRequired[int],
    'top5': NotRequired[int],
    'total_time': NotRequired[str],
    'tyre_state': NotRequired[str],
    'tyre_stints': NotRequired[list[ModelSofascoreStageTyreStint]],
    'tyre_type': NotRequired[str],
    'updated_timestamp': NotRequired[int],
    'victories': NotRequired[int],
}, total=False)

ModelSofascoreStageTyreStint = TypedDict('ModelSofascoreStageTyreStint', {
    'laps': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreStageSeasonsResponseDoc = TypedDict('ModelSofascoreStageSeasonsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreStageSeasonsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreStageSeasonsResponse = TypedDict('ModelSofascoreStageSeasonsResponse', {
    'competition': NotRequired[ModelSofascoreStageCompetition],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'seasons': NotRequired[list[ModelSofascoreStageSeason]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreStageSeason = TypedDict('ModelSofascoreStageSeason', {
    'end_timestamp': NotRequired[int],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'start_timestamp': NotRequired[int],
    'year': NotRequired[str],
}, total=False)

ModelSofascoreStageScheduleResponseDoc = TypedDict('ModelSofascoreStageScheduleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreStageScheduleResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreStageScheduleResponse = TypedDict('ModelSofascoreStageScheduleResponse', {
    'count': NotRequired[int],
    'date': NotRequired[str],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
    'stages': NotRequired[list[ModelSofascoreStage]],
}, total=False)

ModelSofascoreStageFeaturedResponseDoc = TypedDict('ModelSofascoreStageFeaturedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreStageFeaturedResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreStageFeaturedResponse = TypedDict('ModelSofascoreStageFeaturedResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
    'stages': NotRequired[list[ModelSofascoreStage]],
}, total=False)

ModelSofascoreStageDriverPerformanceResponseDoc = TypedDict('ModelSofascoreStageDriverPerformanceResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreStageDriverPerformanceResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreStageDriverPerformanceResponse = TypedDict('ModelSofascoreStageDriverPerformanceResponse', {
    'competitors': NotRequired[list[ModelSofascoreStagePerformance]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'stage': NotRequired[ModelSofascoreStage],
    'stage_id': NotRequired[int],
}, total=False)

ModelSofascoreStagePerformance = TypedDict('ModelSofascoreStagePerformance', {
    'competitor': NotRequired[ModelSofascoreStageEntity],
    'laps': NotRequired[list[ModelSofascoreStageLap]],
    'stage_positions': NotRequired[list[ModelSofascoreStageSpecialStagePosition]],
    'start_number': NotRequired[int],
}, total=False)

ModelSofascoreStageSpecialStagePosition = TypedDict('ModelSofascoreStageSpecialStagePosition', {
    'position': NotRequired[int],
    'stage': NotRequired[int],
}, total=False)

ModelSofascoreStageLap = TypedDict('ModelSofascoreStageLap', {
    'lap': NotRequired[int],
    'pit_stop': NotRequired[bool],
    'position': NotRequired[int],
    'retired': NotRequired[bool],
    'tyre_type': NotRequired[str],
}, total=False)

ModelSofascoreStageCategoriesResponseDoc = TypedDict('ModelSofascoreStageCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreStageCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreStageCategoriesResponse = TypedDict('ModelSofascoreStageCategoriesResponse', {
    'categories': NotRequired[list[ModelSofascoreStageCategory]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelSofascoreStageCategory = TypedDict('ModelSofascoreStageCategory', {
    'competitions': NotRequired[list[ModelSofascoreStageCompetition]],
    'flag': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'priority': NotRequired[int],
    'slug': NotRequired[str],
}, total=False)

ModelSofascoreStageDetailResponseDoc = TypedDict('ModelSofascoreStageDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreStageDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreStageDetailResponse = TypedDict('ModelSofascoreStageDetailResponse', {
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'stage': NotRequired[ModelSofascoreStage],
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

ModelSofascoreSearchTypedResponseDoc = TypedDict('ModelSofascoreSearchTypedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreSearchTypedResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreSearchTypedResponse = TypedDict('ModelSofascoreSearchTypedResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'page': NotRequired[int],
    'query': NotRequired[str],
    'results': NotRequired[list[ModelSofascoreTypedSearchResult]],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelSofascoreTypedSearchResult = TypedDict('ModelSofascoreTypedSearchResult', {
    'capacity': NotRequired[int],
    'category_id': NotRequired[int],
    'category_name': NotRequired[str],
    'city': NotRequired[str],
    'country': NotRequired[str],
    'deceased': NotRequired[bool],
    'event': NotRequired[ModelSofascoreEventSummary],
    'gender': NotRequired[str],
    'id': NotRequired[int],
    'jersey_number': NotRequired[str],
    'name': NotRequired[str],
    'name_code': NotRequired[str],
    'national': NotRequired[bool],
    'position': NotRequired[str],
    'retired': NotRequired[bool],
    'score': NotRequired[float],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'team': NotRequired[ModelSofascoreTeamRef],
    'type': NotRequired[str],
    'user_count': NotRequired[int],
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

ModelSofascoreRefereeStatisticsResponseDoc = TypedDict('ModelSofascoreRefereeStatisticsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreRefereeStatisticsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreRefereeStatisticsResponse = TypedDict('ModelSofascoreRefereeStatisticsResponse', {
    'competitions': NotRequired[list[ModelSofascoreRefereeCompetitionStatistics]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'referee_id': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreRefereeCompetitionStatistics = TypedDict('ModelSofascoreRefereeCompetitionStatistics', {
    'appearances': NotRequired[int],
    'competition': NotRequired[ModelSofascoreUniqueTournamentBrief],
    'penalties': NotRequired[int],
    'red_cards': NotRequired[int],
    'yellow_cards': NotRequired[int],
    'yellow_red_cards': NotRequired[int],
}, total=False)

ModelSofascoreRefereeEventsResponseDoc = TypedDict('ModelSofascoreRefereeEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreRefereeEventsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreRefereeEventsResponse = TypedDict('ModelSofascoreRefereeEventsResponse', {
    'count': NotRequired[int],
    'events': NotRequired[list[ModelSofascoreEventSummary]],
    'fetched_at': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'page': NotRequired[int],
    'referee_id': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreRefereeResponseDoc = TypedDict('ModelSofascoreRefereeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreRefereeResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreRefereeResponse = TypedDict('ModelSofascoreRefereeResponse', {
    'fetched_at': NotRequired[str],
    'referee': NotRequired[ModelSofascoreRefereeDetail],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreRefereeDetail = TypedDict('ModelSofascoreRefereeDetail', {
    'country': NotRequired[str],
    'date_of_birth': NotRequired[str],
    'first_league_debut': NotRequired[str],
    'games': NotRequired[int],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'red_cards': NotRequired[int],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'yellow_cards': NotRequired[int],
    'yellow_red_cards': NotRequired[int],
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

ModelSofascorePlayerTournamentsResponseDoc = TypedDict('ModelSofascorePlayerTournamentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascorePlayerTournamentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascorePlayerTournamentsResponse = TypedDict('ModelSofascorePlayerTournamentsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'player_id': NotRequired[int],
    'source_url': NotRequired[str],
    'tournaments': NotRequired[list[ModelSofascoreUniqueTournamentBrief]],
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

ModelSofascorePlayerStatisticalRankingsResponseDoc = TypedDict('ModelSofascorePlayerStatisticalRankingsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascorePlayerStatisticalRankingsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascorePlayerStatisticalRankingsResponse = TypedDict('ModelSofascorePlayerStatisticalRankingsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'player_id': NotRequired[int],
    'rankings': NotRequired[list[ModelSofascorePlayerStatisticRank]],
    'season': NotRequired[ModelSofascoreSeason],
    'source_url': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelSofascorePlayerStatisticRank = TypedDict('ModelSofascorePlayerStatisticRank', {
    'count': NotRequired[int],
    'order': NotRequired[int],
    'rank': NotRequired[int],
    'statistic': NotRequired[str],
    'value': NotRequired[float],
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

ModelSofascorePlayerSeasonHeatmapResponseDoc = TypedDict('ModelSofascorePlayerSeasonHeatmapResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascorePlayerSeasonHeatmapResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascorePlayerSeasonHeatmapResponse = TypedDict('ModelSofascorePlayerSeasonHeatmapResponse', {
    'count': NotRequired[int],
    'events': NotRequired[list[ModelSofascoreEventSummary]],
    'fetched_at': NotRequired[str],
    'matches': NotRequired[int],
    'player_id': NotRequired[int],
    'points': NotRequired[list[ModelSofascoreSeasonHeatmapPoint]],
    'season': NotRequired[int],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[int],
}, total=False)

ModelSofascoreSeasonHeatmapPoint = TypedDict('ModelSofascoreSeasonHeatmapPoint', {
    'count': NotRequired[int],
    'x': NotRequired[float],
    'y': NotRequired[float],
}, total=False)

ModelSofascorePlayerRatingsResponseDoc = TypedDict('ModelSofascorePlayerRatingsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascorePlayerRatingsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascorePlayerRatingsResponse = TypedDict('ModelSofascorePlayerRatingsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'player_id': NotRequired[int],
    'ratings': NotRequired[list[ModelSofascorePlayerMatchRating]],
    'season': NotRequired[int],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelSofascorePlayerMatchRating = TypedDict('ModelSofascorePlayerMatchRating', {
    'event': NotRequired[ModelSofascoreEventSummary],
    'event_id': NotRequired[int],
    'is_home': NotRequired[bool],
    'opponent': NotRequired[ModelSofascoreTeamRef],
    'rating': NotRequired[float],
    'start_time': NotRequired[str],
    'start_timestamp': NotRequired[int],
}, total=False)

ModelSofascorePlayerPenaltyHistoryResponseDoc = TypedDict('ModelSofascorePlayerPenaltyHistoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascorePlayerPenaltyHistoryResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascorePlayerPenaltyHistoryResponse = TypedDict('ModelSofascorePlayerPenaltyHistoryResponse', {
    'attempts': NotRequired[int],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'penalties': NotRequired[list[ModelSofascorePlayerPenalty]],
    'player_id': NotRequired[int],
    'scored': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascorePlayerPenalty = TypedDict('ModelSofascorePlayerPenalty', {
    'event': NotRequired[ModelSofascoreEventSummary],
    'id': NotRequired[int],
    'outcome': NotRequired[str],
    'x': NotRequired[float],
    'xg': NotRequired[float],
    'y': NotRequired[float],
    'zone': NotRequired[str],
}, total=False)

ModelSofascorePlayerNationalTeamStatisticsResponseDoc = TypedDict('ModelSofascorePlayerNationalTeamStatisticsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascorePlayerNationalTeamStatisticsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascorePlayerNationalTeamStatisticsResponse = TypedDict('ModelSofascorePlayerNationalTeamStatisticsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'player_id': NotRequired[int],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelSofascorePlayerNationalTeamRecord]],
}, total=False)

ModelSofascorePlayerNationalTeamRecord = TypedDict('ModelSofascorePlayerNationalTeamRecord', {
    'appearances': NotRequired[int],
    'debut_date': NotRequired[str],
    'debut_timestamp': NotRequired[int],
    'goals': NotRequired[int],
    'team': NotRequired[ModelSofascoreTeamRef],
}, total=False)

ModelSofascorePlayerLastYearSummaryResponseDoc = TypedDict('ModelSofascorePlayerLastYearSummaryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascorePlayerLastYearSummaryResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascorePlayerLastYearSummaryResponse = TypedDict('ModelSofascorePlayerLastYearSummaryResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'player_id': NotRequired[int],
    'source_url': NotRequired[str],
    'summary': NotRequired[list[ModelSofascorePlayerFormEntry]],
    'tournaments': NotRequired[list[ModelSofascoreUniqueTournamentBrief]],
}, total=False)

ModelSofascorePlayerFormEntry = TypedDict('ModelSofascorePlayerFormEntry', {
    'date': NotRequired[str],
    'rating': NotRequired[float],
    'timestamp': NotRequired[int],
    'tournament_id': NotRequired[int],
    'type': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelSofascorePlayerEventsResponseDoc = TypedDict('ModelSofascorePlayerEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascorePlayerEventsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascorePlayerEventsResponse = TypedDict('ModelSofascorePlayerEventsResponse', {
    'count': NotRequired[int],
    'events': NotRequired[list[ModelSofascorePlayerEventRow]],
    'fetched_at': NotRequired[str],
    'has_next_page': NotRequired[bool],
    'page': NotRequired[int],
    'player_id': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascorePlayerEventRow = TypedDict('ModelSofascorePlayerEventRow', {
    'event': NotRequired[ModelSofascoreEventSummary],
    'incident_counts': NotRequired[dict[str, float]],
    'on_bench': NotRequired[bool],
    'played_for_team_id': NotRequired[int],
    'statistics': NotRequired[dict[str, float]],
}, total=False)

ModelSofascorePlayerAttributesResponseDoc = TypedDict('ModelSofascorePlayerAttributesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascorePlayerAttributesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascorePlayerAttributesResponse = TypedDict('ModelSofascorePlayerAttributesResponse', {
    'characteristics': NotRequired[ModelSofascorePlayerCharacteristics],
    'characteristics_url': NotRequired[str],
    'fetched_at': NotRequired[str],
    'overviews': NotRequired[list[ModelSofascorePlayerAttributeOverview]],
    'player_id': NotRequired[int],
    'position_averages': NotRequired[list[ModelSofascorePlayerAttributeOverview]],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelSofascorePlayerAttributeOverview = TypedDict('ModelSofascorePlayerAttributeOverview', {
    'attributes': NotRequired[dict[str, float]],
    'position': NotRequired[str],
    'year_shift': NotRequired[int],
}, total=False)

ModelSofascorePlayerCharacteristics = TypedDict('ModelSofascorePlayerCharacteristics', {
    'positions': NotRequired[list[str]],
    'strengths': NotRequired[list[ModelSofascorePlayerCharacteristic]],
    'weaknesses': NotRequired[list[ModelSofascorePlayerCharacteristic]],
}, total=False)

ModelSofascorePlayerCharacteristic = TypedDict('ModelSofascorePlayerCharacteristic', {
    'code': NotRequired[int],
    'key': NotRequired[str],
    'name': NotRequired[str],
    'rank': NotRequired[int],
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

ModelSofascoreOddsWinningResponseDoc = TypedDict('ModelSofascoreOddsWinningResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreOddsWinningResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreOddsWinningResponse = TypedDict('ModelSofascoreOddsWinningResponse', {
    'count': NotRequired[int],
    'events': NotRequired[list[ModelSofascoreOddsWinningEvent]],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelSofascoreOddsWinningEvent = TypedDict('ModelSofascoreOddsWinningEvent', {
    'actual': NotRequired[float],
    'away_score': NotRequired[ModelSofascoreScoreLine],
    'away_team': NotRequired[ModelSofascoreTeamRef],
    'expected': NotRequired[float],
    'home_score': NotRequired[ModelSofascoreScoreLine],
    'home_team': NotRequired[ModelSofascoreTeamRef],
    'id': NotRequired[int],
    'market': NotRequired[ModelSofascoreMoverOddsMarket],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'start_time': NotRequired[str],
    'start_timestamp': NotRequired[int],
    'status': NotRequired[ModelSofascoreEventStatus],
    'tournament': NotRequired[ModelSofascoreTournamentRef],
    'winner_code': NotRequired[int],
    'winning_odds': NotRequired[str],
}, total=False)

ModelSofascoreMoverOddsMarket = TypedDict('ModelSofascoreMoverOddsMarket', {
    'choices': NotRequired[list[ModelSofascoreMoverOddsChoice]],
    'group': NotRequired[str],
    'is_live': NotRequired[bool],
    'name': NotRequired[str],
    'period': NotRequired[str],
    'suspended': NotRequired[bool],
}, total=False)

ModelSofascoreMoverOddsChoice = TypedDict('ModelSofascoreMoverOddsChoice', {
    'change': NotRequired[int],
    'initial_value': NotRequired[str],
    'name': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelSofascoreOddsDroppingResponseDoc = TypedDict('ModelSofascoreOddsDroppingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreOddsDroppingResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreOddsDroppingResponse = TypedDict('ModelSofascoreOddsDroppingResponse', {
    'count': NotRequired[int],
    'events': NotRequired[list[ModelSofascoreOddsDroppingEvent]],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelSofascoreOddsDroppingEvent = TypedDict('ModelSofascoreOddsDroppingEvent', {
    'away_score': NotRequired[ModelSofascoreScoreLine],
    'away_team': NotRequired[ModelSofascoreTeamRef],
    'choice_name': NotRequired[str],
    'home_score': NotRequired[ModelSofascoreScoreLine],
    'home_team': NotRequired[ModelSofascoreTeamRef],
    'id': NotRequired[int],
    'market': NotRequired[ModelSofascoreMoverOddsMarket],
    'percentage': NotRequired[float],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'start_time': NotRequired[str],
    'start_timestamp': NotRequired[int],
    'status': NotRequired[ModelSofascoreEventStatus],
    'tournament': NotRequired[ModelSofascoreTournamentRef],
    'winner_code': NotRequired[int],
}, total=False)

ModelSofascoreMmaScheduleResponseDoc = TypedDict('ModelSofascoreMmaScheduleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreMmascheduleResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreMmascheduleResponse = TypedDict('ModelSofascoreMmascheduleResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'main_events': NotRequired[list[ModelSofascoreMmafight]],
    'month': NotRequired[str],
    'org_id': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreMmafight = TypedDict('ModelSofascoreMmafight', {
    'away_fighter': NotRequired[ModelSofascoreMmafighter],
    'card_id': NotRequired[int],
    'card_name': NotRequired[str],
    'fight_type': NotRequired[str],
    'final_round': NotRequired[int],
    'gender': NotRequired[str],
    'home_fighter': NotRequired[ModelSofascoreMmafighter],
    'id': NotRequired[int],
    'order': NotRequired[int],
    'scheduled_rounds': NotRequired[int],
    'slug': NotRequired[str],
    'start_time': NotRequired[str],
    'start_timestamp': NotRequired[int],
    'status': NotRequired[ModelSofascoreEventStatus],
    'time_played_seconds': NotRequired[int],
    'weight_class': NotRequired[str],
    'win_type': NotRequired[str],
    'winner_code': NotRequired[int],
}, total=False)

ModelSofascoreMmafighter = TypedDict('ModelSofascoreMmafighter', {
    'country': NotRequired[str],
    'draws': NotRequired[int],
    'id': NotRequired[int],
    'losses': NotRequired[int],
    'name': NotRequired[str],
    'nickname': NotRequired[str],
    'ranking': NotRequired[int],
    'slug': NotRequired[str],
    'wins': NotRequired[int],
}, total=False)

ModelSofascoreMmaCardResponseDoc = TypedDict('ModelSofascoreMmaCardResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreMmacardResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreMmacardResponse = TypedDict('ModelSofascoreMmacardResponse', {
    'card_id': NotRequired[int],
    'card_name': NotRequired[str],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'fights': NotRequired[list[ModelSofascoreMmafight]],
    'org_id': NotRequired[int],
    'part': NotRequired[str],
    'source_url': NotRequired[str],
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

ModelSofascoreEventVotesResponseDoc = TypedDict('ModelSofascoreEventVotesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventVotesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventVotesResponse = TypedDict('ModelSofascoreEventVotesResponse', {
    'both_teams_to_score': NotRequired[ModelSofascoreVoteBothTeamsToScore],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'first_to_score': NotRequired[ModelSofascoreVoteFirstToScore],
    'match_result': NotRequired[ModelSofascoreVoteMatchResult],
    'source_url': NotRequired[str],
    'who_should_have_won': NotRequired[ModelSofascoreVoteWhoShouldHaveWon],
}, total=False)

ModelSofascoreVoteWhoShouldHaveWon = TypedDict('ModelSofascoreVoteWhoShouldHaveWon', {
    'away': NotRequired[int],
    'home': NotRequired[int],
}, total=False)

ModelSofascoreVoteMatchResult = TypedDict('ModelSofascoreVoteMatchResult', {
    'away': NotRequired[int],
    'draw': NotRequired[int],
    'home': NotRequired[int],
    'total': NotRequired[int],
}, total=False)

ModelSofascoreVoteFirstToScore = TypedDict('ModelSofascoreVoteFirstToScore', {
    'away': NotRequired[int],
    'home': NotRequired[int],
    'no_goal': NotRequired[int],
}, total=False)

ModelSofascoreVoteBothTeamsToScore = TypedDict('ModelSofascoreVoteBothTeamsToScore', {
    'no': NotRequired[int],
    'yes': NotRequired[int],
}, total=False)

ModelSofascoreEventTvchannelsResponseDoc = TypedDict('ModelSofascoreEventTvchannelsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventTvchannelsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventTvchannelsResponse = TypedDict('ModelSofascoreEventTvchannelsResponse', {
    'available_countries': NotRequired[list[ModelSofascoreTvcountryChannels]],
    'channels': NotRequired[list[ModelSofascoreTvchannel]],
    'country': NotRequired[str],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreTvchannel = TypedDict('ModelSofascoreTvchannel', {
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelSofascoreTvcountryChannels = TypedDict('ModelSofascoreTvcountryChannels', {
    'channel_ids': NotRequired[list[int]],
    'country': NotRequired[str],
}, total=False)

ModelSofascoreEventTennisPowerResponseDoc = TypedDict('ModelSofascoreEventTennisPowerResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventTennisPowerResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventTennisPowerResponse = TypedDict('ModelSofascoreEventTennisPowerResponse', {
    'count': NotRequired[int],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'games': NotRequired[list[ModelSofascoreTennisPowerGame]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreTennisPowerGame = TypedDict('ModelSofascoreTennisPowerGame', {
    'break_occurred': NotRequired[bool],
    'game': NotRequired[int],
    'set': NotRequired[int],
    'value': NotRequired[float],
}, total=False)

ModelSofascoreEventTeamStreaksResponseDoc = TypedDict('ModelSofascoreEventTeamStreaksResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventTeamStreaksResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventTeamStreaksResponse = TypedDict('ModelSofascoreEventTeamStreaksResponse', {
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'general': NotRequired[list[ModelSofascoreTeamStreak]],
    'head2head': NotRequired[list[ModelSofascoreTeamStreak]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreTeamStreak = TypedDict('ModelSofascoreTeamStreak', {
    'continued': NotRequired[bool],
    'name': NotRequired[str],
    'team': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelSofascoreEventTeamHeatmapResponseDoc = TypedDict('ModelSofascoreEventTeamHeatmapResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventTeamHeatmapResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventTeamHeatmapResponse = TypedDict('ModelSofascoreEventTeamHeatmapResponse', {
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'goalkeeper_points': NotRequired[list[ModelSofascoreHeatmapPoint]],
    'player_points': NotRequired[list[ModelSofascoreHeatmapPoint]],
    'source_url': NotRequired[str],
    'team_id': NotRequired[int],
}, total=False)

ModelSofascoreHeatmapPoint = TypedDict('ModelSofascoreHeatmapPoint', {
    'x': NotRequired[float],
    'y': NotRequired[float],
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
    'coordinates': NotRequired[ModelSofascoreCoordinates],
    'goal_mouth_coordinates': NotRequired[ModelSofascoreCoordinates],
    'goal_mouth_location': NotRequired[str],
    'goal_type': NotRequired[str],
    'goalkeeper': NotRequired[ModelSofascorePlayerBrief],
    'id': NotRequired[int],
    'is_home': NotRequired[bool],
    'minute': NotRequired[int],
    'outcome': NotRequired[str],
    'period': NotRequired[str],
    'period_time_seconds': NotRequired[int],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'player_coordinates': NotRequired[ModelSofascoreCoordinates],
    'reversed_period_time_seconds': NotRequired[int],
    'shot_type': NotRequired[str],
    'situation': NotRequired[str],
    'strength': NotRequired[str],
    'team': NotRequired[ModelSofascoreTeamRef],
    'time_seconds': NotRequired[int],
    'xg': NotRequired[float],
    'xgot': NotRequired[float],
}, total=False)

ModelSofascoreCoordinates = TypedDict('ModelSofascoreCoordinates', {
    'x': NotRequired[float],
    'y': NotRequired[float],
    'z': NotRequired[float],
}, total=False)

ModelSofascoreEventPregameFormResponseDoc = TypedDict('ModelSofascoreEventPregameFormResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventPregameFormResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventPregameFormResponse = TypedDict('ModelSofascoreEventPregameFormResponse', {
    'away': NotRequired[ModelSofascorePregameFormSide],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'home': NotRequired[ModelSofascorePregameFormSide],
    'label': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascorePregameFormSide = TypedDict('ModelSofascorePregameFormSide', {
    'avg_rating': NotRequired[float],
    'form': NotRequired[list[str]],
    'position': NotRequired[int],
    'value': NotRequired[str],
}, total=False)

ModelSofascoreEventPointByPointResponseDoc = TypedDict('ModelSofascoreEventPointByPointResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventPointByPointResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventPointByPointResponse = TypedDict('ModelSofascoreEventPointByPointResponse', {
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'set_count': NotRequired[int],
    'sets': NotRequired[list[ModelSofascorePointByPointSet]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascorePointByPointSet = TypedDict('ModelSofascorePointByPointSet', {
    'games': NotRequired[list[ModelSofascorePointByPointGame]],
    'points': NotRequired[list[ModelSofascorePointByPointPoint]],
    'score': NotRequired[ModelSofascorePointByPointScore],
    'set': NotRequired[int],
}, total=False)

ModelSofascorePointByPointScore = TypedDict('ModelSofascorePointByPointScore', {
    'away_score': NotRequired[int],
    'home_score': NotRequired[int],
    'server': NotRequired[str],
    'winner': NotRequired[str],
}, total=False)

ModelSofascorePointByPointPoint = TypedDict('ModelSofascorePointByPointPoint', {
    'away_marker': NotRequired[str],
    'away_point': NotRequired[str],
    'away_point_type': NotRequired[int],
    'description': NotRequired[str],
    'description_code': NotRequired[int],
    'home_marker': NotRequired[str],
    'home_point': NotRequired[str],
    'home_point_type': NotRequired[int],
}, total=False)

ModelSofascorePointByPointGame = TypedDict('ModelSofascorePointByPointGame', {
    'game': NotRequired[int],
    'points': NotRequired[list[ModelSofascorePointByPointPoint]],
    'score': NotRequired[ModelSofascorePointByPointScore],
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

ModelSofascoreEventPlayerHeatmapResponseDoc = TypedDict('ModelSofascoreEventPlayerHeatmapResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventPlayerHeatmapResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventPlayerHeatmapResponse = TypedDict('ModelSofascoreEventPlayerHeatmapResponse', {
    'count': NotRequired[int],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'player_id': NotRequired[int],
    'points': NotRequired[list[ModelSofascoreHeatmapPoint]],
    'source_url': NotRequired[str],
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

ModelSofascoreEventManagersResponseDoc = TypedDict('ModelSofascoreEventManagersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventManagersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventManagersResponse = TypedDict('ModelSofascoreEventManagersResponse', {
    'away': NotRequired[ModelSofascoreManagerBrief],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'home': NotRequired[ModelSofascoreManagerBrief],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreManagerBrief = TypedDict('ModelSofascoreManagerBrief', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
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

ModelSofascoreEventInningsResponseDoc = TypedDict('ModelSofascoreEventInningsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventInningsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventInningsResponse = TypedDict('ModelSofascoreEventInningsResponse', {
    'count': NotRequired[int],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'innings': NotRequired[list[ModelSofascoreCricketInnings]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreCricketInnings = TypedDict('ModelSofascoreCricketInnings', {
    'batting': NotRequired[list[ModelSofascoreCricketBattingLine]],
    'batting_team': NotRequired[ModelSofascoreTeamRef],
    'bowling': NotRequired[list[ModelSofascoreCricketBowlingLine]],
    'bowling_team': NotRequired[ModelSofascoreTeamRef],
    'extras': NotRequired[ModelSofascoreCricketExtras],
    'fall_of_wickets': NotRequired[list[ModelSofascoreCricketFallOfWicket]],
    'id': NotRequired[int],
    'number': NotRequired[int],
    'overs': NotRequired[float],
    'partnerships': NotRequired[list[ModelSofascoreCricketPartnership]],
    'runs': NotRequired[int],
    'wickets': NotRequired[int],
}, total=False)

ModelSofascoreCricketPartnership = TypedDict('ModelSofascoreCricketPartnership', {
    'balls': NotRequired[int],
    'number': NotRequired[int],
    'player1': NotRequired[ModelSofascorePlayerBrief],
    'player2': NotRequired[ModelSofascorePlayerBrief],
    'runs': NotRequired[int],
}, total=False)

ModelSofascoreCricketFallOfWicket = TypedDict('ModelSofascoreCricketFallOfWicket', {
    'over': NotRequired[float],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'score': NotRequired[int],
    'wicket': NotRequired[int],
}, total=False)

ModelSofascoreCricketExtras = TypedDict('ModelSofascoreCricketExtras', {
    'byes': NotRequired[int],
    'leg_byes': NotRequired[int],
    'no_balls': NotRequired[int],
    'penalty': NotRequired[int],
    'total': NotRequired[int],
    'wides': NotRequired[int],
}, total=False)

ModelSofascoreCricketBowlingLine = TypedDict('ModelSofascoreCricketBowlingLine', {
    'maidens': NotRequired[int],
    'no_balls': NotRequired[int],
    'overs': NotRequired[float],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'runs': NotRequired[int],
    'scorecard_name': NotRequired[str],
    'wickets': NotRequired[int],
    'wides': NotRequired[int],
}, total=False)

ModelSofascoreCricketBattingLine = TypedDict('ModelSofascoreCricketBattingLine', {
    'balls': NotRequired[int],
    'bowler': NotRequired[ModelSofascorePlayerBrief],
    'dismissal': NotRequired[str],
    'dismissal_code': NotRequired[int],
    'fall_of_wicket_over': NotRequired[float],
    'fall_of_wicket_score': NotRequired[int],
    'fielder': NotRequired[ModelSofascorePlayerBrief],
    'fours': NotRequired[int],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'runs': NotRequired[int],
    'scorecard_name': NotRequired[str],
    'sixes': NotRequired[int],
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

ModelSofascoreEventHighlightsResponseDoc = TypedDict('ModelSofascoreEventHighlightsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventHighlightsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventHighlightsResponse = TypedDict('ModelSofascoreEventHighlightsResponse', {
    'count': NotRequired[int],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'highlights': NotRequired[list[ModelSofascoreEventHighlight]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreEventHighlight = TypedDict('ModelSofascoreEventHighlight', {
    'created_at': NotRequired[str],
    'created_timestamp': NotRequired[int],
    'for_countries': NotRequired[list[str]],
    'id': NotRequired[int],
    'key_highlight': NotRequired[bool],
    'livestream': NotRequired[bool],
    'media_type_code': NotRequired[int],
    'subtitle': NotRequired[str],
    'thumbnail_url': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
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

ModelSofascoreEventEsportsGamesResponseDoc = TypedDict('ModelSofascoreEventEsportsGamesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventEsportsGamesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventEsportsGamesResponse = TypedDict('ModelSofascoreEventEsportsGamesResponse', {
    'count': NotRequired[int],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'games': NotRequired[list[ModelSofascoreEsportsGame]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreEsportsGame = TypedDict('ModelSofascoreEsportsGame', {
    'away_score': NotRequired[ModelSofascoreEsportsGameScore],
    'has_complete_statistics': NotRequired[bool],
    'home_score': NotRequired[ModelSofascoreEsportsGameScore],
    'home_team_starting_side_code': NotRequired[int],
    'id': NotRequired[int],
    'length_seconds': NotRequired[int],
    'map': NotRequired[ModelSofascoreEsportsGameMap],
    'start_time': NotRequired[str],
    'start_timestamp': NotRequired[int],
    'status': NotRequired[ModelSofascoreEventStatus],
    'winner_code': NotRequired[int],
}, total=False)

ModelSofascoreEsportsGameMap = TypedDict('ModelSofascoreEsportsGameMap', {
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelSofascoreEsportsGameScore = TypedDict('ModelSofascoreEsportsGameScore', {
    'display': NotRequired[int],
    'overtime': NotRequired[int],
    'period1': NotRequired[int],
    'period2': NotRequired[int],
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
    'value_text': NotRequired[str],
}, total=False)

ModelSofascoreEventBaseballTopPerformersResponseDoc = TypedDict('ModelSofascoreEventBaseballTopPerformersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventBaseballTopPerformersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventBaseballTopPerformersResponse = TypedDict('ModelSofascoreEventBaseballTopPerformersResponse', {
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'performers': NotRequired[list[ModelSofascoreBaseballPerformer]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreBaseballPerformer = TypedDict('ModelSofascoreBaseballPerformer', {
    'player': NotRequired[ModelSofascorePlayerBrief],
    'rating': NotRequired[float],
    'role': NotRequired[str],
    'statistics': NotRequired[dict[str, float]],
    'team': NotRequired[ModelSofascoreTeamRef],
}, total=False)

ModelSofascoreEventAveragePositionsResponseDoc = TypedDict('ModelSofascoreEventAveragePositionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventAveragePositionsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventAveragePositionsResponse = TypedDict('ModelSofascoreEventAveragePositionsResponse', {
    'away': NotRequired[list[ModelSofascoreAveragePosition]],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'home': NotRequired[list[ModelSofascoreAveragePosition]],
    'source_url': NotRequired[str],
    'substitutions': NotRequired[list[ModelSofascoreAveragePositionSubstitution]],
}, total=False)

ModelSofascoreAveragePositionSubstitution = TypedDict('ModelSofascoreAveragePositionSubstitution', {
    'is_home': NotRequired[bool],
    'minute': NotRequired[int],
    'player_in': NotRequired[ModelSofascorePlayerBrief],
    'player_out': NotRequired[ModelSofascorePlayerBrief],
}, total=False)

ModelSofascoreAveragePosition = TypedDict('ModelSofascoreAveragePosition', {
    'average_x': NotRequired[float],
    'average_y': NotRequired[float],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'points_count': NotRequired[int],
}, total=False)

ModelSofascoreEventAtBatsResponseDoc = TypedDict('ModelSofascoreEventAtBatsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventAtBatsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventAtBatsResponse = TypedDict('ModelSofascoreEventAtBatsResponse', {
    'at_bats': NotRequired[list[ModelSofascoreBaseballAtBat]],
    'count': NotRequired[int],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreBaseballAtBat = TypedDict('ModelSofascoreBaseballAtBat', {
    'away_win_probability': NotRequired[float],
    'away_win_probability_start': NotRequired[float],
    'end_time': NotRequired[str],
    'end_timestamp': NotRequired[int],
    'hitter': NotRequired[ModelSofascorePlayerBrief],
    'hitter_team': NotRequired[ModelSofascoreTeamRef],
    'home_win_probability': NotRequired[float],
    'home_win_probability_start': NotRequired[float],
    'id': NotRequired[int],
    'inning': NotRequired[int],
    'inning_half': NotRequired[str],
    'pitcher': NotRequired[ModelSofascorePlayerBrief],
    'pitcher_team': NotRequired[ModelSofascoreTeamRef],
}, total=False)

ModelSofascoreEventAtBatPitchesResponseDoc = TypedDict('ModelSofascoreEventAtBatPitchesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEventAtBatPitchesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEventAtBatPitchesResponse = TypedDict('ModelSofascoreEventAtBatPitchesResponse', {
    'at_bat_id': NotRequired[int],
    'count': NotRequired[int],
    'event_id': NotRequired[int],
    'fetched_at': NotRequired[str],
    'hitter': NotRequired[ModelSofascorePlayerBrief],
    'pitcher': NotRequired[ModelSofascorePlayerBrief],
    'pitches': NotRequired[list[ModelSofascoreBaseballPitch]],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreBaseballPitch = TypedDict('ModelSofascoreBaseballPitch', {
    'at_bat_over': NotRequired[bool],
    'away_team_runs': NotRequired[int],
    'balls': NotRequired[int],
    'bunt': NotRequired[bool],
    'double_play': NotRequired[bool],
    'end_time': NotRequired[str],
    'fielders': NotRequired[list[ModelSofascoreBaseballFielder]],
    'hit': NotRequired[bool],
    'hit_hardness': NotRequired[str],
    'hit_location': NotRequired[str],
    'hit_trajectory': NotRequired[str],
    'hit_type': NotRequired[str],
    'hit_x': NotRequired[float],
    'hit_y': NotRequired[float],
    'hitter_hand': NotRequired[str],
    'home_team_runs': NotRequired[int],
    'id': NotRequired[int],
    'inning': NotRequired[int],
    'inning_half': NotRequired[str],
    'mlb_x': NotRequired[float],
    'mlb_y': NotRequired[float],
    'mlb_zone': NotRequired[int],
    'outcome': NotRequired[str],
    'outs': NotRequired[int],
    'passed_ball': NotRequired[bool],
    'pitch_code': NotRequired[str],
    'pitch_count': NotRequired[int],
    'pitch_description': NotRequired[str],
    'pitch_speed': NotRequired[float],
    'pitch_type': NotRequired[str],
    'pitch_x': NotRequired[int],
    'pitch_y': NotRequired[int],
    'pitch_zone': NotRequired[int],
    'pitcher_hand': NotRequired[str],
    'runners': NotRequired[list[ModelSofascoreBaseballRunner]],
    'sequence': NotRequired[int],
    'start_time': NotRequired[str],
    'status': NotRequired[str],
    'strike_zone_bottom': NotRequired[float],
    'strike_zone_top': NotRequired[float],
    'strikes': NotRequired[int],
    'triple_play': NotRequired[bool],
    'type': NotRequired[str],
    'wild_pitch': NotRequired[bool],
}, total=False)

ModelSofascoreBaseballRunner = TypedDict('ModelSofascoreBaseballRunner', {
    'description': NotRequired[str],
    'ending_base': NotRequired[int],
    'jersey_number': NotRequired[str],
    'out': NotRequired[bool],
    'outcome_code': NotRequired[str],
    'player_id': NotRequired[int],
    'player_name': NotRequired[str],
    'starting_base': NotRequired[int],
}, total=False)

ModelSofascoreBaseballFielder = TypedDict('ModelSofascoreBaseballFielder', {
    'first_name': NotRequired[str],
    'jersey_number': NotRequired[str],
    'last_name': NotRequired[str],
    'player_id': NotRequired[int],
    'sequence': NotRequired[int],
    'type': NotRequired[str],
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

ModelSofascoreReferee = TypedDict('ModelSofascoreReferee', {
    'country': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelSofascoreEsportsGameResponseDoc = TypedDict('ModelSofascoreEsportsGameResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreEsportsGameResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreEsportsGameResponse = TypedDict('ModelSofascoreEsportsGameResponse', {
    'bans': NotRequired[ModelSofascoreEsportsGameBans],
    'fetched_at': NotRequired[str],
    'game_id': NotRequired[int],
    'lineups': NotRequired[ModelSofascoreEsportsGameLineups],
    'part': NotRequired[str],
    'rounds': NotRequired[ModelSofascoreEsportsGameRounds],
    'source_url': NotRequired[str],
    'statistics': NotRequired[ModelSofascoreEsportsGameStatistics],
}, total=False)

ModelSofascoreEsportsGameStatistics = TypedDict('ModelSofascoreEsportsGameStatistics', {
    'away': NotRequired[ModelSofascoreEsportsTeamStatistics],
    'home': NotRequired[ModelSofascoreEsportsTeamStatistics],
}, total=False)

ModelSofascoreEsportsTeamStatistics = TypedDict('ModelSofascoreEsportsTeamStatistics', {
    'flags': NotRequired[dict[str, bool]],
    'statistics': NotRequired[dict[str, float]],
}, total=False)

ModelSofascoreEsportsGameRounds = TypedDict('ModelSofascoreEsportsGameRounds', {
    'normaltime': NotRequired[list[ModelSofascoreEsportsRound]],
    'overtime': NotRequired[list[ModelSofascoreEsportsRound]],
    'overtime_chunk_size': NotRequired[int],
    'rounds_in_a_half': NotRequired[int],
}, total=False)

ModelSofascoreEsportsRound = TypedDict('ModelSofascoreEsportsRound', {
    'home_team_side': NotRequired[str],
    'home_team_side_code': NotRequired[int],
    'outcome': NotRequired[str],
    'outcome_code': NotRequired[int],
    'winner_code': NotRequired[int],
}, total=False)

ModelSofascoreEsportsGameLineups = TypedDict('ModelSofascoreEsportsGameLineups', {
    'away_players': NotRequired[list[ModelSofascoreEsportsPlayerLine]],
    'home_players': NotRequired[list[ModelSofascoreEsportsPlayerLine]],
}, total=False)

ModelSofascoreEsportsPlayerLine = TypedDict('ModelSofascoreEsportsPlayerLine', {
    'character': NotRequired[ModelSofascoreEsportsCharacter],
    'flags': NotRequired[dict[str, bool]],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'role': NotRequired[str],
    'statistics': NotRequired[dict[str, float]],
}, total=False)

ModelSofascoreEsportsCharacter = TypedDict('ModelSofascoreEsportsCharacter', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelSofascoreEsportsGameBans = TypedDict('ModelSofascoreEsportsGameBans', {
    'away': NotRequired[list[ModelSofascoreEsportsCharacter]],
    'home': NotRequired[list[ModelSofascoreEsportsCharacter]],
}, total=False)

ModelSofascoreDraftPicksResponseDoc = TypedDict('ModelSofascoreDraftPicksResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreDraftPicksResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreDraftPicksResponse = TypedDict('ModelSofascoreDraftPicksResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'league': NotRequired[str],
    'picks': NotRequired[list[ModelSofascoreDraftPick]],
    'round': NotRequired[int],
    'source_url': NotRequired[str],
    'teams_without_round_pick': NotRequired[list[ModelSofascoreTeamRef]],
    'year': NotRequired[int],
}, total=False)

ModelSofascoreDraftPick = TypedDict('ModelSofascoreDraftPick', {
    'overall_pick': NotRequired[int],
    'pick_in_round': NotRequired[int],
    'prospect': NotRequired[ModelSofascoreDraftProspect],
    'round': NotRequired[int],
    'team': NotRequired[ModelSofascoreTeamRef],
}, total=False)

ModelSofascoreDraftProspect = TypedDict('ModelSofascoreDraftProspect', {
    'first_name': NotRequired[str],
    'is_top_prospect': NotRequired[bool],
    'last_name': NotRequired[str],
    'name': NotRequired[str],
    'player': NotRequired[ModelSofascorePlayerBrief],
    'position': NotRequired[str],
    'school': NotRequired[ModelSofascoreTeamRef],
    'school_name': NotRequired[str],
}, total=False)

ModelSofascoreDraftResponseDoc = TypedDict('ModelSofascoreDraftResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelSofascoreDraftResponse],
    'msg': NotRequired[str],
}, total=False)

ModelSofascoreDraftResponse = TypedDict('ModelSofascoreDraftResponse', {
    'draft': NotRequired[ModelSofascoreDraftInfo],
    'fetched_at': NotRequired[str],
    'has_lottery_draw': NotRequired[bool],
    'league': NotRequired[str],
    'lottery_year': NotRequired[int],
    'previous_draft': NotRequired[ModelSofascoreDraftInfo],
    'prospects_year': NotRequired[int],
    'season': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelSofascoreDraftInfo = TypedDict('ModelSofascoreDraftInfo', {
    'end_time': NotRequired[str],
    'end_timestamp': NotRequired[int],
    'is_lottery_complete': NotRequired[bool],
    'rounds': NotRequired[list[int]],
    'start_time': NotRequired[str],
    'start_timestamp': NotRequired[int],
    'status': NotRequired[str],
    'year': NotRequired[int],
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

SofascoreDraftResponse = ModelSofascoreDraftResponseDoc
SofascoreDraftParams = TypedDict('SofascoreDraftParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nba', 'nfl']],
    'season': Required[str],
}, total=False)

SofascoreDraftPicksResponse = ModelSofascoreDraftPicksResponseDoc
SofascoreDraftPicksParams = TypedDict('SofascoreDraftPicksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'league': Required[Literal['nba', 'nfl']],
    'year': Required[str],
    'round': Required[int],
}, total=False)

SofascoreEsportsGameResponse = ModelSofascoreEsportsGameResponseDoc
SofascoreEsportsGameParams = TypedDict('SofascoreEsportsGameParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'part': Required[Literal['statistics', 'lineups', 'bans', 'rounds']],
}, total=False)

SofascoreEventResponse = ModelSofascoreEventResponseDoc
SofascoreEventParams = TypedDict('SofascoreEventParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventAtBatPitchesResponse = ModelSofascoreEventAtBatPitchesResponseDoc
SofascoreEventAtBatPitchesParams = TypedDict('SofascoreEventAtBatPitchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'at_bat_id': Required[str],
}, total=False)

SofascoreEventAtBatsResponse = ModelSofascoreEventAtBatsResponseDoc
SofascoreEventAtBatsParams = TypedDict('SofascoreEventAtBatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventAveragePositionsResponse = ModelSofascoreEventAveragePositionsResponseDoc
SofascoreEventAveragePositionsParams = TypedDict('SofascoreEventAveragePositionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventBaseballTopPerformersResponse = ModelSofascoreEventBaseballTopPerformersResponseDoc
SofascoreEventBaseballTopPerformersParams = TypedDict('SofascoreEventBaseballTopPerformersParams', {
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

SofascoreEventEsportsGamesResponse = ModelSofascoreEventEsportsGamesResponseDoc
SofascoreEventEsportsGamesParams = TypedDict('SofascoreEventEsportsGamesParams', {
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

SofascoreEventHighlightsResponse = ModelSofascoreEventHighlightsResponseDoc
SofascoreEventHighlightsParams = TypedDict('SofascoreEventHighlightsParams', {
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

SofascoreEventInningsResponse = ModelSofascoreEventInningsResponseDoc
SofascoreEventInningsParams = TypedDict('SofascoreEventInningsParams', {
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

SofascoreEventManagersResponse = ModelSofascoreEventManagersResponseDoc
SofascoreEventManagersParams = TypedDict('SofascoreEventManagersParams', {
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

SofascoreEventPlayerHeatmapResponse = ModelSofascoreEventPlayerHeatmapResponseDoc
SofascoreEventPlayerHeatmapParams = TypedDict('SofascoreEventPlayerHeatmapParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'player_id': Required[str],
}, total=False)

SofascoreEventPlayerStatisticsResponse = ModelSofascoreEventPlayerStatisticsResponseDoc
SofascoreEventPlayerStatisticsParams = TypedDict('SofascoreEventPlayerStatisticsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'player_id': Required[str],
}, total=False)

SofascoreEventPointByPointResponse = ModelSofascoreEventPointByPointResponseDoc
SofascoreEventPointByPointParams = TypedDict('SofascoreEventPointByPointParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventPregameFormResponse = ModelSofascoreEventPregameFormResponseDoc
SofascoreEventPregameFormParams = TypedDict('SofascoreEventPregameFormParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
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

SofascoreEventTeamHeatmapResponse = ModelSofascoreEventTeamHeatmapResponseDoc
SofascoreEventTeamHeatmapParams = TypedDict('SofascoreEventTeamHeatmapParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'team_id': Required[str],
}, total=False)

SofascoreEventTeamStreaksResponse = ModelSofascoreEventTeamStreaksResponseDoc
SofascoreEventTeamStreaksParams = TypedDict('SofascoreEventTeamStreaksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventTennisPowerResponse = ModelSofascoreEventTennisPowerResponseDoc
SofascoreEventTennisPowerParams = TypedDict('SofascoreEventTennisPowerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreEventTvChannelsResponse = ModelSofascoreEventTvchannelsResponseDoc
SofascoreEventTvChannelsParams = TypedDict('SofascoreEventTvChannelsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'country': NotRequired[str],
}, total=False)

SofascoreEventVotesResponse = ModelSofascoreEventVotesResponseDoc
SofascoreEventVotesParams = TypedDict('SofascoreEventVotesParams', {
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

SofascoreMmaCardResponse = ModelSofascoreMmaCardResponseDoc
SofascoreMmaCardParams = TypedDict('SofascoreMmaCardParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'org_id': Required[str],
    'card_id': Required[str],
    'part': Required[Literal['all', 'maincard', 'prelims', 'earlyprelims']],
}, total=False)

SofascoreMmaScheduleResponse = ModelSofascoreMmaScheduleResponseDoc
SofascoreMmaScheduleParams = TypedDict('SofascoreMmaScheduleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'org_id': Required[str],
    'month': Required[str],
}, total=False)

SofascoreOddsDroppingResponse = ModelSofascoreOddsDroppingResponseDoc
SofascoreOddsDroppingParams = TypedDict('SofascoreOddsDroppingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': NotRequired[Literal['all', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreOddsWinningResponse = ModelSofascoreOddsWinningResponseDoc
SofascoreOddsWinningParams = TypedDict('SofascoreOddsWinningParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': NotRequired[Literal['all', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascorePlayerResponse = ModelSofascorePlayerResponseDoc
SofascorePlayerParams = TypedDict('SofascorePlayerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascorePlayerAttributesResponse = ModelSofascorePlayerAttributesResponseDoc
SofascorePlayerAttributesParams = TypedDict('SofascorePlayerAttributesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascorePlayerEventsResponse = ModelSofascorePlayerEventsResponseDoc
SofascorePlayerEventsParams = TypedDict('SofascorePlayerEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascorePlayerLastYearSummaryResponse = ModelSofascorePlayerLastYearSummaryResponseDoc
SofascorePlayerLastYearSummaryParams = TypedDict('SofascorePlayerLastYearSummaryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascorePlayerNationalTeamStatisticsResponse = ModelSofascorePlayerNationalTeamStatisticsResponseDoc
SofascorePlayerNationalTeamStatisticsParams = TypedDict('SofascorePlayerNationalTeamStatisticsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascorePlayerPenaltyHistoryResponse = ModelSofascorePlayerPenaltyHistoryResponseDoc
SofascorePlayerPenaltyHistoryParams = TypedDict('SofascorePlayerPenaltyHistoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascorePlayerRatingsResponse = ModelSofascorePlayerRatingsResponseDoc
SofascorePlayerRatingsParams = TypedDict('SofascorePlayerRatingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascorePlayerSeasonHeatmapResponse = ModelSofascorePlayerSeasonHeatmapResponseDoc
SofascorePlayerSeasonHeatmapParams = TypedDict('SofascorePlayerSeasonHeatmapParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
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

SofascorePlayerStatisticalRankingsResponse = ModelSofascorePlayerStatisticalRankingsResponseDoc
SofascorePlayerStatisticalRankingsParams = TypedDict('SofascorePlayerStatisticalRankingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall']],
}, total=False)

SofascorePlayerStatisticsSeasonsResponse = ModelSofascorePlayerStatisticsSeasonsResponseDoc
SofascorePlayerStatisticsSeasonsParams = TypedDict('SofascorePlayerStatisticsSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascorePlayerTournamentsResponse = ModelSofascorePlayerTournamentsResponseDoc
SofascorePlayerTournamentsParams = TypedDict('SofascorePlayerTournamentsParams', {
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

SofascoreRefereeResponse = ModelSofascoreRefereeResponseDoc
SofascoreRefereeParams = TypedDict('SofascoreRefereeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreRefereeEventsResponse = ModelSofascoreRefereeEventsResponseDoc
SofascoreRefereeEventsParams = TypedDict('SofascoreRefereeEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreRefereeStatisticsResponse = ModelSofascoreRefereeStatisticsResponseDoc
SofascoreRefereeStatisticsParams = TypedDict('SofascoreRefereeStatisticsParams', {
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

SofascoreSearchTypedResponse = ModelSofascoreSearchTypedResponseDoc
SofascoreSearchTypedParams = TypedDict('SofascoreSearchTypedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'type': Required[Literal['events', 'teams', 'players', 'managers', 'referees', 'venues', 'unique_tournaments']],
    'q': Required[str],
    'page': NotRequired[int],
    'sport': NotRequired[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
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

SofascoreStageResponse = ModelSofascoreStageDetailResponseDoc
SofascoreStageParams = TypedDict('SofascoreStageParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreStageCategoriesResponse = ModelSofascoreStageCategoriesResponseDoc
SofascoreStageCategoriesParams = TypedDict('SofascoreStageCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['motorsport', 'cycling']],
}, total=False)

SofascoreStageDriverPerformanceResponse = ModelSofascoreStageDriverPerformanceResponseDoc
SofascoreStageDriverPerformanceParams = TypedDict('SofascoreStageDriverPerformanceParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreStageFeaturedResponse = ModelSofascoreStageFeaturedResponseDoc
SofascoreStageFeaturedParams = TypedDict('SofascoreStageFeaturedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['motorsport', 'cycling']],
}, total=False)

SofascoreStageScheduleResponse = ModelSofascoreStageScheduleResponseDoc
SofascoreStageScheduleParams = TypedDict('SofascoreStageScheduleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['motorsport', 'cycling']],
    'date': Required[str],
}, total=False)

SofascoreStageSeasonsResponse = ModelSofascoreStageSeasonsResponseDoc
SofascoreStageSeasonsParams = TypedDict('SofascoreStageSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreStageStandingsResponse = ModelSofascoreStageStandingsResponseDoc
SofascoreStageStandingsParams = TypedDict('SofascoreStageStandingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'type': Required[Literal['competitor', 'team']],
}, total=False)

SofascoreStageSubstagesResponse = ModelSofascoreStageSubstagesResponseDoc
SofascoreStageSubstagesParams = TypedDict('SofascoreStageSubstagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
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

SofascoreTeamAchievementsResponse = ModelSofascoreTeamAchievementsResponseDoc
SofascoreTeamAchievementsParams = TypedDict('SofascoreTeamAchievementsParams', {
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

SofascoreTeamGoalDistributionsResponse = ModelSofascoreTeamGoalDistributionsResponseDoc
SofascoreTeamGoalDistributionsParams = TypedDict('SofascoreTeamGoalDistributionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTeamNearEventsResponse = ModelSofascoreTeamNearEventsResponseDoc
SofascoreTeamNearEventsParams = TypedDict('SofascoreTeamNearEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
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

SofascoreTeamPerformanceResponse = ModelSofascoreTeamPerformanceResponseDoc
SofascoreTeamPerformanceParams = TypedDict('SofascoreTeamPerformanceParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTeamPlayerStatisticsResponse = ModelSofascoreTeamPlayerStatisticsResponseDoc
SofascoreTeamPlayerStatisticsParams = TypedDict('SofascoreTeamPlayerStatisticsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascoreTeamPlayerStatisticsSeasonsResponse = ModelSofascoreTeamPlayerStatisticsSeasonsResponseDoc
SofascoreTeamPlayerStatisticsSeasonsParams = TypedDict('SofascoreTeamPlayerStatisticsSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTeamPlayersResponse = ModelSofascoreTeamPlayersResponseDoc
SofascoreTeamPlayersParams = TypedDict('SofascoreTeamPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTeamRankingsResponse = ModelSofascoreTeamRankingsResponseDoc
SofascoreTeamRankingsParams = TypedDict('SofascoreTeamRankingsParams', {
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

SofascoreTeamTopPlayersResponse = ModelSofascoreTeamTopPlayersResponseDoc
SofascoreTeamTopPlayersParams = TypedDict('SofascoreTeamTopPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'regular_season', 'playoffs']],
    'limit': NotRequired[int],
}, total=False)

SofascoreTeamTournamentsResponse = ModelSofascoreTeamTournamentsResponseDoc
SofascoreTeamTournamentsParams = TypedDict('SofascoreTeamTournamentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'all': NotRequired[bool],
}, total=False)

SofascoreTeamTransfersResponse = ModelSofascoreTeamTransfersResponseDoc
SofascoreTeamTransfersParams = TypedDict('SofascoreTeamTransfersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTennisPlayerGrandSlamResultsResponse = ModelSofascoreTennisGrandSlamResultsResponseDoc
SofascoreTennisPlayerGrandSlamResultsParams = TypedDict('SofascoreTennisPlayerGrandSlamResultsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreTournamentCuptreeResponse = ModelSofascoreTournamentCupTreeResponseDoc
SofascoreTournamentCuptreeParams = TypedDict('SofascoreTournamentCuptreeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentInfoResponse = ModelSofascoreTournamentInfoResponseDoc
SofascoreTournamentInfoParams = TypedDict('SofascoreTournamentInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': NotRequired[str],
}, total=False)

SofascoreTournamentPlayerOfTheSeasonResponse = ModelSofascoreTournamentPlayerOfTheSeasonResponseDoc
SofascoreTournamentPlayerOfTheSeasonParams = TypedDict('SofascoreTournamentPlayerOfTheSeasonParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
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
    'team': NotRequired[list[str]],
    'nationality': NotRequired[list[str]],
    'position': NotRequired[list[Literal['G', 'D', 'M', 'F']]],
    'min_appearances': NotRequired[int],
    'min_minutes': NotRequired[int],
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

SofascoreTournamentStatisticsInfoResponse = ModelSofascoreTournamentStatisticsInfoResponseDoc
SofascoreTournamentStatisticsInfoParams = TypedDict('SofascoreTournamentStatisticsInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentTeamOfTheSeasonResponse = ModelSofascoreTournamentTeamOfTheSeasonResponseDoc
SofascoreTournamentTeamOfTheSeasonParams = TypedDict('SofascoreTournamentTeamOfTheSeasonParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentTeamsResponse = ModelSofascoreTournamentTeamsResponseDoc
SofascoreTournamentTeamsParams = TypedDict('SofascoreTournamentTeamsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
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

SofascoreTournamentVenuesResponse = ModelSofascoreTournamentVenuesResponseDoc
SofascoreTournamentVenuesParams = TypedDict('SofascoreTournamentVenuesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentWinnersResponse = ModelSofascoreTournamentWinnersResponseDoc
SofascoreTournamentWinnersParams = TypedDict('SofascoreTournamentWinnersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreTournamentsWithFeatureResponse = ModelSofascoreTournamentsWithFeatureResponseDoc
SofascoreTournamentsWithFeatureParams = TypedDict('SofascoreTournamentsWithFeatureParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'feature': Required[Literal['cuptree', 'standings', 'totw', 'power_rankings']],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'minifootball', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreTrendingEventsResponse = ModelSofascoreTrendingEventsResponseDoc
SofascoreTrendingEventsParams = TypedDict('SofascoreTrendingEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country': Required[str],
}, total=False)

SofascoreTrendingPlayersResponse = ModelSofascoreTrendingPlayersResponseDoc
SofascoreTrendingPlayersParams = TypedDict('SofascoreTrendingPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['football', 'basketball']],
}, total=False)

SofascoreVenueResponse = ModelSofascoreVenueResponseDoc
SofascoreVenueParams = TypedDict('SofascoreVenueParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

SofascoreVenueEventsResponse = ModelSofascoreVenueEventsResponseDoc
SofascoreVenueEventsParams = TypedDict('SofascoreVenueEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'direction': Required[Literal['next', 'last']],
    'sport': NotRequired[Literal['all', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
    'page': NotRequired[int],
    'tournament': NotRequired[str],
    'season': NotRequired[str],
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
    def draft(self, **params: Unpack[SofascoreDraftStreamParams]) -> BinaryIO: ...
    @overload
    def draft(self, **params: Unpack[SofascoreDraftTextResponseParams]) -> str: ...
    @overload
    def draft(self, **params: Unpack[SofascoreDraftDefaultParams]) -> SofascoreDraftResponse: ...
    @overload
    def draft_picks(self, **params: Unpack[SofascoreDraftPicksStreamParams]) -> BinaryIO: ...
    @overload
    def draft_picks(self, **params: Unpack[SofascoreDraftPicksTextResponseParams]) -> str: ...
    @overload
    def draft_picks(self, **params: Unpack[SofascoreDraftPicksDefaultParams]) -> SofascoreDraftPicksResponse: ...
    @overload
    def esports_game(self, **params: Unpack[SofascoreEsportsGameStreamParams]) -> BinaryIO: ...
    @overload
    def esports_game(self, **params: Unpack[SofascoreEsportsGameTextResponseParams]) -> str: ...
    @overload
    def esports_game(self, **params: Unpack[SofascoreEsportsGameDefaultParams]) -> SofascoreEsportsGameResponse: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventStreamParams]) -> BinaryIO: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventTextResponseParams]) -> str: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventDefaultParams]) -> SofascoreEventResponse: ...
    @overload
    def event_at_bat_pitches(self, **params: Unpack[SofascoreEventAtBatPitchesStreamParams]) -> BinaryIO: ...
    @overload
    def event_at_bat_pitches(self, **params: Unpack[SofascoreEventAtBatPitchesTextResponseParams]) -> str: ...
    @overload
    def event_at_bat_pitches(self, **params: Unpack[SofascoreEventAtBatPitchesDefaultParams]) -> SofascoreEventAtBatPitchesResponse: ...
    @overload
    def event_at_bats(self, **params: Unpack[SofascoreEventAtBatsStreamParams]) -> BinaryIO: ...
    @overload
    def event_at_bats(self, **params: Unpack[SofascoreEventAtBatsTextResponseParams]) -> str: ...
    @overload
    def event_at_bats(self, **params: Unpack[SofascoreEventAtBatsDefaultParams]) -> SofascoreEventAtBatsResponse: ...
    @overload
    def event_average_positions(self, **params: Unpack[SofascoreEventAveragePositionsStreamParams]) -> BinaryIO: ...
    @overload
    def event_average_positions(self, **params: Unpack[SofascoreEventAveragePositionsTextResponseParams]) -> str: ...
    @overload
    def event_average_positions(self, **params: Unpack[SofascoreEventAveragePositionsDefaultParams]) -> SofascoreEventAveragePositionsResponse: ...
    @overload
    def event_baseball_top_performers(self, **params: Unpack[SofascoreEventBaseballTopPerformersStreamParams]) -> BinaryIO: ...
    @overload
    def event_baseball_top_performers(self, **params: Unpack[SofascoreEventBaseballTopPerformersTextResponseParams]) -> str: ...
    @overload
    def event_baseball_top_performers(self, **params: Unpack[SofascoreEventBaseballTopPerformersDefaultParams]) -> SofascoreEventBaseballTopPerformersResponse: ...
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
    def event_esports_games(self, **params: Unpack[SofascoreEventEsportsGamesStreamParams]) -> BinaryIO: ...
    @overload
    def event_esports_games(self, **params: Unpack[SofascoreEventEsportsGamesTextResponseParams]) -> str: ...
    @overload
    def event_esports_games(self, **params: Unpack[SofascoreEventEsportsGamesDefaultParams]) -> SofascoreEventEsportsGamesResponse: ...
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
    def event_highlights(self, **params: Unpack[SofascoreEventHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    def event_highlights(self, **params: Unpack[SofascoreEventHighlightsTextResponseParams]) -> str: ...
    @overload
    def event_highlights(self, **params: Unpack[SofascoreEventHighlightsDefaultParams]) -> SofascoreEventHighlightsResponse: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsStreamParams]) -> BinaryIO: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsTextResponseParams]) -> str: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsDefaultParams]) -> SofascoreEventIncidentsResponse: ...
    @overload
    def event_innings(self, **params: Unpack[SofascoreEventInningsStreamParams]) -> BinaryIO: ...
    @overload
    def event_innings(self, **params: Unpack[SofascoreEventInningsTextResponseParams]) -> str: ...
    @overload
    def event_innings(self, **params: Unpack[SofascoreEventInningsDefaultParams]) -> SofascoreEventInningsResponse: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsStreamParams]) -> BinaryIO: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsTextResponseParams]) -> str: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsDefaultParams]) -> SofascoreEventLineupsResponse: ...
    @overload
    def event_managers(self, **params: Unpack[SofascoreEventManagersStreamParams]) -> BinaryIO: ...
    @overload
    def event_managers(self, **params: Unpack[SofascoreEventManagersTextResponseParams]) -> str: ...
    @overload
    def event_managers(self, **params: Unpack[SofascoreEventManagersDefaultParams]) -> SofascoreEventManagersResponse: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsStreamParams]) -> BinaryIO: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsTextResponseParams]) -> str: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsDefaultParams]) -> SofascoreEventOddsResponse: ...
    @overload
    def event_player_heatmap(self, **params: Unpack[SofascoreEventPlayerHeatmapStreamParams]) -> BinaryIO: ...
    @overload
    def event_player_heatmap(self, **params: Unpack[SofascoreEventPlayerHeatmapTextResponseParams]) -> str: ...
    @overload
    def event_player_heatmap(self, **params: Unpack[SofascoreEventPlayerHeatmapDefaultParams]) -> SofascoreEventPlayerHeatmapResponse: ...
    @overload
    def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsDefaultParams]) -> SofascoreEventPlayerStatisticsResponse: ...
    @overload
    def event_point_by_point(self, **params: Unpack[SofascoreEventPointByPointStreamParams]) -> BinaryIO: ...
    @overload
    def event_point_by_point(self, **params: Unpack[SofascoreEventPointByPointTextResponseParams]) -> str: ...
    @overload
    def event_point_by_point(self, **params: Unpack[SofascoreEventPointByPointDefaultParams]) -> SofascoreEventPointByPointResponse: ...
    @overload
    def event_pregame_form(self, **params: Unpack[SofascoreEventPregameFormStreamParams]) -> BinaryIO: ...
    @overload
    def event_pregame_form(self, **params: Unpack[SofascoreEventPregameFormTextResponseParams]) -> str: ...
    @overload
    def event_pregame_form(self, **params: Unpack[SofascoreEventPregameFormDefaultParams]) -> SofascoreEventPregameFormResponse: ...
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
    def event_team_heatmap(self, **params: Unpack[SofascoreEventTeamHeatmapStreamParams]) -> BinaryIO: ...
    @overload
    def event_team_heatmap(self, **params: Unpack[SofascoreEventTeamHeatmapTextResponseParams]) -> str: ...
    @overload
    def event_team_heatmap(self, **params: Unpack[SofascoreEventTeamHeatmapDefaultParams]) -> SofascoreEventTeamHeatmapResponse: ...
    @overload
    def event_team_streaks(self, **params: Unpack[SofascoreEventTeamStreaksStreamParams]) -> BinaryIO: ...
    @overload
    def event_team_streaks(self, **params: Unpack[SofascoreEventTeamStreaksTextResponseParams]) -> str: ...
    @overload
    def event_team_streaks(self, **params: Unpack[SofascoreEventTeamStreaksDefaultParams]) -> SofascoreEventTeamStreaksResponse: ...
    @overload
    def event_tennis_power(self, **params: Unpack[SofascoreEventTennisPowerStreamParams]) -> BinaryIO: ...
    @overload
    def event_tennis_power(self, **params: Unpack[SofascoreEventTennisPowerTextResponseParams]) -> str: ...
    @overload
    def event_tennis_power(self, **params: Unpack[SofascoreEventTennisPowerDefaultParams]) -> SofascoreEventTennisPowerResponse: ...
    @overload
    def event_tv_channels(self, **params: Unpack[SofascoreEventTvChannelsStreamParams]) -> BinaryIO: ...
    @overload
    def event_tv_channels(self, **params: Unpack[SofascoreEventTvChannelsTextResponseParams]) -> str: ...
    @overload
    def event_tv_channels(self, **params: Unpack[SofascoreEventTvChannelsDefaultParams]) -> SofascoreEventTvChannelsResponse: ...
    @overload
    def event_votes(self, **params: Unpack[SofascoreEventVotesStreamParams]) -> BinaryIO: ...
    @overload
    def event_votes(self, **params: Unpack[SofascoreEventVotesTextResponseParams]) -> str: ...
    @overload
    def event_votes(self, **params: Unpack[SofascoreEventVotesDefaultParams]) -> SofascoreEventVotesResponse: ...
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
    def mma_card(self, **params: Unpack[SofascoreMmaCardStreamParams]) -> BinaryIO: ...
    @overload
    def mma_card(self, **params: Unpack[SofascoreMmaCardTextResponseParams]) -> str: ...
    @overload
    def mma_card(self, **params: Unpack[SofascoreMmaCardDefaultParams]) -> SofascoreMmaCardResponse: ...
    @overload
    def mma_schedule(self, **params: Unpack[SofascoreMmaScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def mma_schedule(self, **params: Unpack[SofascoreMmaScheduleTextResponseParams]) -> str: ...
    @overload
    def mma_schedule(self, **params: Unpack[SofascoreMmaScheduleDefaultParams]) -> SofascoreMmaScheduleResponse: ...
    @overload
    def odds_dropping(self, **params: Unpack[SofascoreOddsDroppingStreamParams]) -> BinaryIO: ...
    @overload
    def odds_dropping(self, **params: Unpack[SofascoreOddsDroppingTextResponseParams]) -> str: ...
    @overload
    def odds_dropping(self, **params: Unpack[SofascoreOddsDroppingDefaultParams]) -> SofascoreOddsDroppingResponse: ...
    @overload
    def odds_winning(self, **params: Unpack[SofascoreOddsWinningStreamParams]) -> BinaryIO: ...
    @overload
    def odds_winning(self, **params: Unpack[SofascoreOddsWinningTextResponseParams]) -> str: ...
    @overload
    def odds_winning(self, **params: Unpack[SofascoreOddsWinningDefaultParams]) -> SofascoreOddsWinningResponse: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerDefaultParams]) -> SofascorePlayerResponse: ...
    @overload
    def player_attributes(self, **params: Unpack[SofascorePlayerAttributesStreamParams]) -> BinaryIO: ...
    @overload
    def player_attributes(self, **params: Unpack[SofascorePlayerAttributesTextResponseParams]) -> str: ...
    @overload
    def player_attributes(self, **params: Unpack[SofascorePlayerAttributesDefaultParams]) -> SofascorePlayerAttributesResponse: ...
    @overload
    def player_events(self, **params: Unpack[SofascorePlayerEventsStreamParams]) -> BinaryIO: ...
    @overload
    def player_events(self, **params: Unpack[SofascorePlayerEventsTextResponseParams]) -> str: ...
    @overload
    def player_events(self, **params: Unpack[SofascorePlayerEventsDefaultParams]) -> SofascorePlayerEventsResponse: ...
    @overload
    def player_last_year_summary(self, **params: Unpack[SofascorePlayerLastYearSummaryStreamParams]) -> BinaryIO: ...
    @overload
    def player_last_year_summary(self, **params: Unpack[SofascorePlayerLastYearSummaryTextResponseParams]) -> str: ...
    @overload
    def player_last_year_summary(self, **params: Unpack[SofascorePlayerLastYearSummaryDefaultParams]) -> SofascorePlayerLastYearSummaryResponse: ...
    @overload
    def player_national_team_statistics(self, **params: Unpack[SofascorePlayerNationalTeamStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def player_national_team_statistics(self, **params: Unpack[SofascorePlayerNationalTeamStatisticsTextResponseParams]) -> str: ...
    @overload
    def player_national_team_statistics(self, **params: Unpack[SofascorePlayerNationalTeamStatisticsDefaultParams]) -> SofascorePlayerNationalTeamStatisticsResponse: ...
    @overload
    def player_penalty_history(self, **params: Unpack[SofascorePlayerPenaltyHistoryStreamParams]) -> BinaryIO: ...
    @overload
    def player_penalty_history(self, **params: Unpack[SofascorePlayerPenaltyHistoryTextResponseParams]) -> str: ...
    @overload
    def player_penalty_history(self, **params: Unpack[SofascorePlayerPenaltyHistoryDefaultParams]) -> SofascorePlayerPenaltyHistoryResponse: ...
    @overload
    def player_ratings(self, **params: Unpack[SofascorePlayerRatingsStreamParams]) -> BinaryIO: ...
    @overload
    def player_ratings(self, **params: Unpack[SofascorePlayerRatingsTextResponseParams]) -> str: ...
    @overload
    def player_ratings(self, **params: Unpack[SofascorePlayerRatingsDefaultParams]) -> SofascorePlayerRatingsResponse: ...
    @overload
    def player_season_heatmap(self, **params: Unpack[SofascorePlayerSeasonHeatmapStreamParams]) -> BinaryIO: ...
    @overload
    def player_season_heatmap(self, **params: Unpack[SofascorePlayerSeasonHeatmapTextResponseParams]) -> str: ...
    @overload
    def player_season_heatmap(self, **params: Unpack[SofascorePlayerSeasonHeatmapDefaultParams]) -> SofascorePlayerSeasonHeatmapResponse: ...
    @overload
    def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsTextResponseParams]) -> str: ...
    @overload
    def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsDefaultParams]) -> SofascorePlayerSeasonStatisticsResponse: ...
    @overload
    def player_statistical_rankings(self, **params: Unpack[SofascorePlayerStatisticalRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def player_statistical_rankings(self, **params: Unpack[SofascorePlayerStatisticalRankingsTextResponseParams]) -> str: ...
    @overload
    def player_statistical_rankings(self, **params: Unpack[SofascorePlayerStatisticalRankingsDefaultParams]) -> SofascorePlayerStatisticalRankingsResponse: ...
    @overload
    def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsDefaultParams]) -> SofascorePlayerStatisticsSeasonsResponse: ...
    @overload
    def player_tournaments(self, **params: Unpack[SofascorePlayerTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def player_tournaments(self, **params: Unpack[SofascorePlayerTournamentsTextResponseParams]) -> str: ...
    @overload
    def player_tournaments(self, **params: Unpack[SofascorePlayerTournamentsDefaultParams]) -> SofascorePlayerTournamentsResponse: ...
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
    def referee(self, **params: Unpack[SofascoreRefereeStreamParams]) -> BinaryIO: ...
    @overload
    def referee(self, **params: Unpack[SofascoreRefereeTextResponseParams]) -> str: ...
    @overload
    def referee(self, **params: Unpack[SofascoreRefereeDefaultParams]) -> SofascoreRefereeResponse: ...
    @overload
    def referee_events(self, **params: Unpack[SofascoreRefereeEventsStreamParams]) -> BinaryIO: ...
    @overload
    def referee_events(self, **params: Unpack[SofascoreRefereeEventsTextResponseParams]) -> str: ...
    @overload
    def referee_events(self, **params: Unpack[SofascoreRefereeEventsDefaultParams]) -> SofascoreRefereeEventsResponse: ...
    @overload
    def referee_statistics(self, **params: Unpack[SofascoreRefereeStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def referee_statistics(self, **params: Unpack[SofascoreRefereeStatisticsTextResponseParams]) -> str: ...
    @overload
    def referee_statistics(self, **params: Unpack[SofascoreRefereeStatisticsDefaultParams]) -> SofascoreRefereeStatisticsResponse: ...
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
    def search_typed(self, **params: Unpack[SofascoreSearchTypedStreamParams]) -> BinaryIO: ...
    @overload
    def search_typed(self, **params: Unpack[SofascoreSearchTypedTextResponseParams]) -> str: ...
    @overload
    def search_typed(self, **params: Unpack[SofascoreSearchTypedDefaultParams]) -> SofascoreSearchTypedResponse: ...
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
    def stage(self, **params: Unpack[SofascoreStageStreamParams]) -> BinaryIO: ...
    @overload
    def stage(self, **params: Unpack[SofascoreStageTextResponseParams]) -> str: ...
    @overload
    def stage(self, **params: Unpack[SofascoreStageDefaultParams]) -> SofascoreStageResponse: ...
    @overload
    def stage_categories(self, **params: Unpack[SofascoreStageCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def stage_categories(self, **params: Unpack[SofascoreStageCategoriesTextResponseParams]) -> str: ...
    @overload
    def stage_categories(self, **params: Unpack[SofascoreStageCategoriesDefaultParams]) -> SofascoreStageCategoriesResponse: ...
    @overload
    def stage_driver_performance(self, **params: Unpack[SofascoreStageDriverPerformanceStreamParams]) -> BinaryIO: ...
    @overload
    def stage_driver_performance(self, **params: Unpack[SofascoreStageDriverPerformanceTextResponseParams]) -> str: ...
    @overload
    def stage_driver_performance(self, **params: Unpack[SofascoreStageDriverPerformanceDefaultParams]) -> SofascoreStageDriverPerformanceResponse: ...
    @overload
    def stage_featured(self, **params: Unpack[SofascoreStageFeaturedStreamParams]) -> BinaryIO: ...
    @overload
    def stage_featured(self, **params: Unpack[SofascoreStageFeaturedTextResponseParams]) -> str: ...
    @overload
    def stage_featured(self, **params: Unpack[SofascoreStageFeaturedDefaultParams]) -> SofascoreStageFeaturedResponse: ...
    @overload
    def stage_schedule(self, **params: Unpack[SofascoreStageScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def stage_schedule(self, **params: Unpack[SofascoreStageScheduleTextResponseParams]) -> str: ...
    @overload
    def stage_schedule(self, **params: Unpack[SofascoreStageScheduleDefaultParams]) -> SofascoreStageScheduleResponse: ...
    @overload
    def stage_seasons(self, **params: Unpack[SofascoreStageSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def stage_seasons(self, **params: Unpack[SofascoreStageSeasonsTextResponseParams]) -> str: ...
    @overload
    def stage_seasons(self, **params: Unpack[SofascoreStageSeasonsDefaultParams]) -> SofascoreStageSeasonsResponse: ...
    @overload
    def stage_standings(self, **params: Unpack[SofascoreStageStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def stage_standings(self, **params: Unpack[SofascoreStageStandingsTextResponseParams]) -> str: ...
    @overload
    def stage_standings(self, **params: Unpack[SofascoreStageStandingsDefaultParams]) -> SofascoreStageStandingsResponse: ...
    @overload
    def stage_substages(self, **params: Unpack[SofascoreStageSubstagesStreamParams]) -> BinaryIO: ...
    @overload
    def stage_substages(self, **params: Unpack[SofascoreStageSubstagesTextResponseParams]) -> str: ...
    @overload
    def stage_substages(self, **params: Unpack[SofascoreStageSubstagesDefaultParams]) -> SofascoreStageSubstagesResponse: ...
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
    def team_achievements(self, **params: Unpack[SofascoreTeamAchievementsStreamParams]) -> BinaryIO: ...
    @overload
    def team_achievements(self, **params: Unpack[SofascoreTeamAchievementsTextResponseParams]) -> str: ...
    @overload
    def team_achievements(self, **params: Unpack[SofascoreTeamAchievementsDefaultParams]) -> SofascoreTeamAchievementsResponse: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsStreamParams]) -> BinaryIO: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsTextResponseParams]) -> str: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsDefaultParams]) -> SofascoreTeamEventsResponse: ...
    @overload
    def team_goal_distributions(self, **params: Unpack[SofascoreTeamGoalDistributionsStreamParams]) -> BinaryIO: ...
    @overload
    def team_goal_distributions(self, **params: Unpack[SofascoreTeamGoalDistributionsTextResponseParams]) -> str: ...
    @overload
    def team_goal_distributions(self, **params: Unpack[SofascoreTeamGoalDistributionsDefaultParams]) -> SofascoreTeamGoalDistributionsResponse: ...
    @overload
    def team_near_events(self, **params: Unpack[SofascoreTeamNearEventsStreamParams]) -> BinaryIO: ...
    @overload
    def team_near_events(self, **params: Unpack[SofascoreTeamNearEventsTextResponseParams]) -> str: ...
    @overload
    def team_near_events(self, **params: Unpack[SofascoreTeamNearEventsDefaultParams]) -> SofascoreTeamNearEventsResponse: ...
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
    def team_performance(self, **params: Unpack[SofascoreTeamPerformanceStreamParams]) -> BinaryIO: ...
    @overload
    def team_performance(self, **params: Unpack[SofascoreTeamPerformanceTextResponseParams]) -> str: ...
    @overload
    def team_performance(self, **params: Unpack[SofascoreTeamPerformanceDefaultParams]) -> SofascoreTeamPerformanceResponse: ...
    @overload
    def team_player_statistics(self, **params: Unpack[SofascoreTeamPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def team_player_statistics(self, **params: Unpack[SofascoreTeamPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    def team_player_statistics(self, **params: Unpack[SofascoreTeamPlayerStatisticsDefaultParams]) -> SofascoreTeamPlayerStatisticsResponse: ...
    @overload
    def team_player_statistics_seasons(self, **params: Unpack[SofascoreTeamPlayerStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def team_player_statistics_seasons(self, **params: Unpack[SofascoreTeamPlayerStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    def team_player_statistics_seasons(self, **params: Unpack[SofascoreTeamPlayerStatisticsSeasonsDefaultParams]) -> SofascoreTeamPlayerStatisticsSeasonsResponse: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersTextResponseParams]) -> str: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersDefaultParams]) -> SofascoreTeamPlayersResponse: ...
    @overload
    def team_rankings(self, **params: Unpack[SofascoreTeamRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def team_rankings(self, **params: Unpack[SofascoreTeamRankingsTextResponseParams]) -> str: ...
    @overload
    def team_rankings(self, **params: Unpack[SofascoreTeamRankingsDefaultParams]) -> SofascoreTeamRankingsResponse: ...
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
    def team_top_players(self, **params: Unpack[SofascoreTeamTopPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def team_top_players(self, **params: Unpack[SofascoreTeamTopPlayersTextResponseParams]) -> str: ...
    @overload
    def team_top_players(self, **params: Unpack[SofascoreTeamTopPlayersDefaultParams]) -> SofascoreTeamTopPlayersResponse: ...
    @overload
    def team_tournaments(self, **params: Unpack[SofascoreTeamTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def team_tournaments(self, **params: Unpack[SofascoreTeamTournamentsTextResponseParams]) -> str: ...
    @overload
    def team_tournaments(self, **params: Unpack[SofascoreTeamTournamentsDefaultParams]) -> SofascoreTeamTournamentsResponse: ...
    @overload
    def team_transfers(self, **params: Unpack[SofascoreTeamTransfersStreamParams]) -> BinaryIO: ...
    @overload
    def team_transfers(self, **params: Unpack[SofascoreTeamTransfersTextResponseParams]) -> str: ...
    @overload
    def team_transfers(self, **params: Unpack[SofascoreTeamTransfersDefaultParams]) -> SofascoreTeamTransfersResponse: ...
    @overload
    def tennis_player_grand_slam_results(self, **params: Unpack[SofascoreTennisPlayerGrandSlamResultsStreamParams]) -> BinaryIO: ...
    @overload
    def tennis_player_grand_slam_results(self, **params: Unpack[SofascoreTennisPlayerGrandSlamResultsTextResponseParams]) -> str: ...
    @overload
    def tennis_player_grand_slam_results(self, **params: Unpack[SofascoreTennisPlayerGrandSlamResultsDefaultParams]) -> SofascoreTennisPlayerGrandSlamResultsResponse: ...
    @overload
    def tournament_cuptree(self, **params: Unpack[SofascoreTournamentCuptreeStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_cuptree(self, **params: Unpack[SofascoreTournamentCuptreeTextResponseParams]) -> str: ...
    @overload
    def tournament_cuptree(self, **params: Unpack[SofascoreTournamentCuptreeDefaultParams]) -> SofascoreTournamentCuptreeResponse: ...
    @overload
    def tournament_info(self, **params: Unpack[SofascoreTournamentInfoStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_info(self, **params: Unpack[SofascoreTournamentInfoTextResponseParams]) -> str: ...
    @overload
    def tournament_info(self, **params: Unpack[SofascoreTournamentInfoDefaultParams]) -> SofascoreTournamentInfoResponse: ...
    @overload
    def tournament_player_of_the_season(self, **params: Unpack[SofascoreTournamentPlayerOfTheSeasonStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_player_of_the_season(self, **params: Unpack[SofascoreTournamentPlayerOfTheSeasonTextResponseParams]) -> str: ...
    @overload
    def tournament_player_of_the_season(self, **params: Unpack[SofascoreTournamentPlayerOfTheSeasonDefaultParams]) -> SofascoreTournamentPlayerOfTheSeasonResponse: ...
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
    def tournament_statistics_info(self, **params: Unpack[SofascoreTournamentStatisticsInfoStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_statistics_info(self, **params: Unpack[SofascoreTournamentStatisticsInfoTextResponseParams]) -> str: ...
    @overload
    def tournament_statistics_info(self, **params: Unpack[SofascoreTournamentStatisticsInfoDefaultParams]) -> SofascoreTournamentStatisticsInfoResponse: ...
    @overload
    def tournament_team_of_the_season(self, **params: Unpack[SofascoreTournamentTeamOfTheSeasonStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_team_of_the_season(self, **params: Unpack[SofascoreTournamentTeamOfTheSeasonTextResponseParams]) -> str: ...
    @overload
    def tournament_team_of_the_season(self, **params: Unpack[SofascoreTournamentTeamOfTheSeasonDefaultParams]) -> SofascoreTournamentTeamOfTheSeasonResponse: ...
    @overload
    def tournament_teams(self, **params: Unpack[SofascoreTournamentTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_teams(self, **params: Unpack[SofascoreTournamentTeamsTextResponseParams]) -> str: ...
    @overload
    def tournament_teams(self, **params: Unpack[SofascoreTournamentTeamsDefaultParams]) -> SofascoreTournamentTeamsResponse: ...
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
    @overload
    def tournament_venues(self, **params: Unpack[SofascoreTournamentVenuesStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_venues(self, **params: Unpack[SofascoreTournamentVenuesTextResponseParams]) -> str: ...
    @overload
    def tournament_venues(self, **params: Unpack[SofascoreTournamentVenuesDefaultParams]) -> SofascoreTournamentVenuesResponse: ...
    @overload
    def tournament_winners(self, **params: Unpack[SofascoreTournamentWinnersStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_winners(self, **params: Unpack[SofascoreTournamentWinnersTextResponseParams]) -> str: ...
    @overload
    def tournament_winners(self, **params: Unpack[SofascoreTournamentWinnersDefaultParams]) -> SofascoreTournamentWinnersResponse: ...
    @overload
    def tournaments_with_feature(self, **params: Unpack[SofascoreTournamentsWithFeatureStreamParams]) -> BinaryIO: ...
    @overload
    def tournaments_with_feature(self, **params: Unpack[SofascoreTournamentsWithFeatureTextResponseParams]) -> str: ...
    @overload
    def tournaments_with_feature(self, **params: Unpack[SofascoreTournamentsWithFeatureDefaultParams]) -> SofascoreTournamentsWithFeatureResponse: ...
    @overload
    def trending_events(self, **params: Unpack[SofascoreTrendingEventsStreamParams]) -> BinaryIO: ...
    @overload
    def trending_events(self, **params: Unpack[SofascoreTrendingEventsTextResponseParams]) -> str: ...
    @overload
    def trending_events(self, **params: Unpack[SofascoreTrendingEventsDefaultParams]) -> SofascoreTrendingEventsResponse: ...
    @overload
    def trending_players(self, **params: Unpack[SofascoreTrendingPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def trending_players(self, **params: Unpack[SofascoreTrendingPlayersTextResponseParams]) -> str: ...
    @overload
    def trending_players(self, **params: Unpack[SofascoreTrendingPlayersDefaultParams]) -> SofascoreTrendingPlayersResponse: ...
    @overload
    def venue(self, **params: Unpack[SofascoreVenueStreamParams]) -> BinaryIO: ...
    @overload
    def venue(self, **params: Unpack[SofascoreVenueTextResponseParams]) -> str: ...
    @overload
    def venue(self, **params: Unpack[SofascoreVenueDefaultParams]) -> SofascoreVenueResponse: ...
    @overload
    def venue_events(self, **params: Unpack[SofascoreVenueEventsStreamParams]) -> BinaryIO: ...
    @overload
    def venue_events(self, **params: Unpack[SofascoreVenueEventsTextResponseParams]) -> str: ...
    @overload
    def venue_events(self, **params: Unpack[SofascoreVenueEventsDefaultParams]) -> SofascoreVenueEventsResponse: ...

OperationId = Literal[
    'sofascore-categories',
    'sofascore-category-tournaments',
    'sofascore-draft',
    'sofascore-draft-picks',
    'sofascore-esports-game',
    'sofascore-event',
    'sofascore-event-at-bat-pitches',
    'sofascore-event-at-bats',
    'sofascore-event-average-positions',
    'sofascore-event-baseball-top-performers',
    'sofascore-event-best-players',
    'sofascore-event-comments',
    'sofascore-event-esports-games',
    'sofascore-event-graph',
    'sofascore-event-h2h',
    'sofascore-event-highlights',
    'sofascore-event-incidents',
    'sofascore-event-innings',
    'sofascore-event-lineups',
    'sofascore-event-managers',
    'sofascore-event-odds',
    'sofascore-event-player-heatmap',
    'sofascore-event-player-statistics',
    'sofascore-event-point-by-point',
    'sofascore-event-pregame-form',
    'sofascore-event-shotmap',
    'sofascore-event-statistics',
    'sofascore-event-team-heatmap',
    'sofascore-event-team-streaks',
    'sofascore-event-tennis-power',
    'sofascore-event-tv-channels',
    'sofascore-event-votes',
    'sofascore-live-events',
    'sofascore-manager',
    'sofascore-manager-events',
    'sofascore-mma-card',
    'sofascore-mma-schedule',
    'sofascore-odds-dropping',
    'sofascore-odds-winning',
    'sofascore-player',
    'sofascore-player-attributes',
    'sofascore-player-events',
    'sofascore-player-last-year-summary',
    'sofascore-player-national-team-statistics',
    'sofascore-player-penalty-history',
    'sofascore-player-ratings',
    'sofascore-player-season-heatmap',
    'sofascore-player-season-statistics',
    'sofascore-player-statistical-rankings',
    'sofascore-player-statistics-seasons',
    'sofascore-player-tournaments',
    'sofascore-player-transfers',
    'sofascore-ranking-types',
    'sofascore-rankings',
    'sofascore-referee',
    'sofascore-referee-events',
    'sofascore-referee-statistics',
    'sofascore-round-events',
    'sofascore-scheduled-events',
    'sofascore-scheduled-tournaments',
    'sofascore-search',
    'sofascore-search-typed',
    'sofascore-season-events',
    'sofascore-sports',
    'sofascore-stage',
    'sofascore-stage-categories',
    'sofascore-stage-driver-performance',
    'sofascore-stage-featured',
    'sofascore-stage-schedule',
    'sofascore-stage-seasons',
    'sofascore-stage-standings',
    'sofascore-stage-substages',
    'sofascore-standings',
    'sofascore-team',
    'sofascore-team-achievements',
    'sofascore-team-events',
    'sofascore-team-goal-distributions',
    'sofascore-team-near-events',
    'sofascore-team-of-the-week',
    'sofascore-team-of-the-week-periods',
    'sofascore-team-performance',
    'sofascore-team-player-statistics',
    'sofascore-team-player-statistics-seasons',
    'sofascore-team-players',
    'sofascore-team-rankings',
    'sofascore-team-season-statistics',
    'sofascore-team-statistics-seasons',
    'sofascore-team-top-players',
    'sofascore-team-tournaments',
    'sofascore-team-transfers',
    'sofascore-tennis-player-grand-slam-results',
    'sofascore-tournament-cuptree',
    'sofascore-tournament-info',
    'sofascore-tournament-player-of-the-season',
    'sofascore-tournament-player-statistics',
    'sofascore-tournament-rounds',
    'sofascore-tournament-seasons',
    'sofascore-tournament-statistics-info',
    'sofascore-tournament-team-of-the-season',
    'sofascore-tournament-teams',
    'sofascore-tournament-top-players',
    'sofascore-tournament-top-teams',
    'sofascore-tournament-venues',
    'sofascore-tournament-winners',
    'sofascore-tournaments-with-feature',
    'sofascore-trending-events',
    'sofascore-trending-players',
    'sofascore-venue',
    'sofascore-venue-events',
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
        operation_id: Literal['sofascore-draft'],
        params: SofascoreDraftParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreDraftResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-draft-picks'],
        params: SofascoreDraftPicksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreDraftPicksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-esports-game'],
        params: SofascoreEsportsGameParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEsportsGameResponse: ...
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
        operation_id: Literal['sofascore-event-at-bat-pitches'],
        params: SofascoreEventAtBatPitchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventAtBatPitchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-at-bats'],
        params: SofascoreEventAtBatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventAtBatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-average-positions'],
        params: SofascoreEventAveragePositionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventAveragePositionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-baseball-top-performers'],
        params: SofascoreEventBaseballTopPerformersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventBaseballTopPerformersResponse: ...
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
        operation_id: Literal['sofascore-event-esports-games'],
        params: SofascoreEventEsportsGamesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventEsportsGamesResponse: ...
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
        operation_id: Literal['sofascore-event-highlights'],
        params: SofascoreEventHighlightsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventHighlightsResponse: ...
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
        operation_id: Literal['sofascore-event-innings'],
        params: SofascoreEventInningsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventInningsResponse: ...
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
        operation_id: Literal['sofascore-event-managers'],
        params: SofascoreEventManagersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventManagersResponse: ...
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
        operation_id: Literal['sofascore-event-player-heatmap'],
        params: SofascoreEventPlayerHeatmapParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventPlayerHeatmapResponse: ...
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
        operation_id: Literal['sofascore-event-point-by-point'],
        params: SofascoreEventPointByPointParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventPointByPointResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-pregame-form'],
        params: SofascoreEventPregameFormParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventPregameFormResponse: ...
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
        operation_id: Literal['sofascore-event-team-heatmap'],
        params: SofascoreEventTeamHeatmapParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventTeamHeatmapResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-team-streaks'],
        params: SofascoreEventTeamStreaksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventTeamStreaksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-tennis-power'],
        params: SofascoreEventTennisPowerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventTennisPowerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-tv-channels'],
        params: SofascoreEventTvChannelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventTvChannelsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-event-votes'],
        params: SofascoreEventVotesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventVotesResponse: ...
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
        operation_id: Literal['sofascore-mma-card'],
        params: SofascoreMmaCardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreMmaCardResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-mma-schedule'],
        params: SofascoreMmaScheduleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreMmaScheduleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-odds-dropping'],
        params: SofascoreOddsDroppingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreOddsDroppingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-odds-winning'],
        params: SofascoreOddsWinningParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreOddsWinningResponse: ...
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
        operation_id: Literal['sofascore-player-attributes'],
        params: SofascorePlayerAttributesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerAttributesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-player-events'],
        params: SofascorePlayerEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-player-last-year-summary'],
        params: SofascorePlayerLastYearSummaryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerLastYearSummaryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-player-national-team-statistics'],
        params: SofascorePlayerNationalTeamStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerNationalTeamStatisticsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-player-penalty-history'],
        params: SofascorePlayerPenaltyHistoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerPenaltyHistoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-player-ratings'],
        params: SofascorePlayerRatingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerRatingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-player-season-heatmap'],
        params: SofascorePlayerSeasonHeatmapParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerSeasonHeatmapResponse: ...
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
        operation_id: Literal['sofascore-player-statistical-rankings'],
        params: SofascorePlayerStatisticalRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerStatisticalRankingsResponse: ...
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
        operation_id: Literal['sofascore-player-tournaments'],
        params: SofascorePlayerTournamentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerTournamentsResponse: ...
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
        operation_id: Literal['sofascore-referee'],
        params: SofascoreRefereeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreRefereeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-referee-events'],
        params: SofascoreRefereeEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreRefereeEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-referee-statistics'],
        params: SofascoreRefereeStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreRefereeStatisticsResponse: ...
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
        operation_id: Literal['sofascore-search-typed'],
        params: SofascoreSearchTypedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreSearchTypedResponse: ...
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
        operation_id: Literal['sofascore-stage'],
        params: SofascoreStageParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-stage-categories'],
        params: SofascoreStageCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-stage-driver-performance'],
        params: SofascoreStageDriverPerformanceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageDriverPerformanceResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-stage-featured'],
        params: SofascoreStageFeaturedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageFeaturedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-stage-schedule'],
        params: SofascoreStageScheduleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageScheduleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-stage-seasons'],
        params: SofascoreStageSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageSeasonsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-stage-standings'],
        params: SofascoreStageStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageStandingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-stage-substages'],
        params: SofascoreStageSubstagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageSubstagesResponse: ...
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
        operation_id: Literal['sofascore-team-achievements'],
        params: SofascoreTeamAchievementsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamAchievementsResponse: ...
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
        operation_id: Literal['sofascore-team-goal-distributions'],
        params: SofascoreTeamGoalDistributionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamGoalDistributionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-team-near-events'],
        params: SofascoreTeamNearEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamNearEventsResponse: ...
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
        operation_id: Literal['sofascore-team-performance'],
        params: SofascoreTeamPerformanceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamPerformanceResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-team-player-statistics'],
        params: SofascoreTeamPlayerStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamPlayerStatisticsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-team-player-statistics-seasons'],
        params: SofascoreTeamPlayerStatisticsSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamPlayerStatisticsSeasonsResponse: ...
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
        operation_id: Literal['sofascore-team-rankings'],
        params: SofascoreTeamRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamRankingsResponse: ...
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
        operation_id: Literal['sofascore-team-top-players'],
        params: SofascoreTeamTopPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamTopPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-team-tournaments'],
        params: SofascoreTeamTournamentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamTournamentsResponse: ...
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
        operation_id: Literal['sofascore-tennis-player-grand-slam-results'],
        params: SofascoreTennisPlayerGrandSlamResultsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTennisPlayerGrandSlamResultsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-tournament-cuptree'],
        params: SofascoreTournamentCuptreeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentCuptreeResponse: ...
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
        operation_id: Literal['sofascore-tournament-player-of-the-season'],
        params: SofascoreTournamentPlayerOfTheSeasonParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentPlayerOfTheSeasonResponse: ...
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
        operation_id: Literal['sofascore-tournament-statistics-info'],
        params: SofascoreTournamentStatisticsInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentStatisticsInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-tournament-team-of-the-season'],
        params: SofascoreTournamentTeamOfTheSeasonParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentTeamOfTheSeasonResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-tournament-teams'],
        params: SofascoreTournamentTeamsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentTeamsResponse: ...
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
        operation_id: Literal['sofascore-tournament-venues'],
        params: SofascoreTournamentVenuesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentVenuesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-tournament-winners'],
        params: SofascoreTournamentWinnersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentWinnersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-tournaments-with-feature'],
        params: SofascoreTournamentsWithFeatureParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentsWithFeatureResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-trending-events'],
        params: SofascoreTrendingEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTrendingEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-trending-players'],
        params: SofascoreTrendingPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTrendingPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-venue'],
        params: SofascoreVenueParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreVenueResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['sofascore-venue-events'],
        params: SofascoreVenueEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreVenueEventsResponse: ...
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
        operation_id: Literal['sofascore-draft'],
        params: SofascoreDraftParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreDraftResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-draft-picks'],
        params: SofascoreDraftPicksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreDraftPicksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-esports-game'],
        params: SofascoreEsportsGameParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEsportsGameResponse: ...
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
        operation_id: Literal['sofascore-event-at-bat-pitches'],
        params: SofascoreEventAtBatPitchesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventAtBatPitchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-at-bats'],
        params: SofascoreEventAtBatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventAtBatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-average-positions'],
        params: SofascoreEventAveragePositionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventAveragePositionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-baseball-top-performers'],
        params: SofascoreEventBaseballTopPerformersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventBaseballTopPerformersResponse: ...
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
        operation_id: Literal['sofascore-event-esports-games'],
        params: SofascoreEventEsportsGamesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventEsportsGamesResponse: ...
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
        operation_id: Literal['sofascore-event-highlights'],
        params: SofascoreEventHighlightsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventHighlightsResponse: ...
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
        operation_id: Literal['sofascore-event-innings'],
        params: SofascoreEventInningsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventInningsResponse: ...
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
        operation_id: Literal['sofascore-event-managers'],
        params: SofascoreEventManagersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventManagersResponse: ...
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
        operation_id: Literal['sofascore-event-player-heatmap'],
        params: SofascoreEventPlayerHeatmapParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventPlayerHeatmapResponse: ...
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
        operation_id: Literal['sofascore-event-point-by-point'],
        params: SofascoreEventPointByPointParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventPointByPointResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-pregame-form'],
        params: SofascoreEventPregameFormParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventPregameFormResponse: ...
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
        operation_id: Literal['sofascore-event-team-heatmap'],
        params: SofascoreEventTeamHeatmapParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventTeamHeatmapResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-team-streaks'],
        params: SofascoreEventTeamStreaksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventTeamStreaksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-tennis-power'],
        params: SofascoreEventTennisPowerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventTennisPowerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-tv-channels'],
        params: SofascoreEventTvChannelsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventTvChannelsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-event-votes'],
        params: SofascoreEventVotesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreEventVotesResponse: ...
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
        operation_id: Literal['sofascore-mma-card'],
        params: SofascoreMmaCardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreMmaCardResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-mma-schedule'],
        params: SofascoreMmaScheduleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreMmaScheduleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-odds-dropping'],
        params: SofascoreOddsDroppingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreOddsDroppingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-odds-winning'],
        params: SofascoreOddsWinningParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreOddsWinningResponse: ...
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
        operation_id: Literal['sofascore-player-attributes'],
        params: SofascorePlayerAttributesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerAttributesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-player-events'],
        params: SofascorePlayerEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-player-last-year-summary'],
        params: SofascorePlayerLastYearSummaryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerLastYearSummaryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-player-national-team-statistics'],
        params: SofascorePlayerNationalTeamStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerNationalTeamStatisticsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-player-penalty-history'],
        params: SofascorePlayerPenaltyHistoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerPenaltyHistoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-player-ratings'],
        params: SofascorePlayerRatingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerRatingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-player-season-heatmap'],
        params: SofascorePlayerSeasonHeatmapParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerSeasonHeatmapResponse: ...
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
        operation_id: Literal['sofascore-player-statistical-rankings'],
        params: SofascorePlayerStatisticalRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerStatisticalRankingsResponse: ...
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
        operation_id: Literal['sofascore-player-tournaments'],
        params: SofascorePlayerTournamentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascorePlayerTournamentsResponse: ...
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
        operation_id: Literal['sofascore-referee'],
        params: SofascoreRefereeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreRefereeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-referee-events'],
        params: SofascoreRefereeEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreRefereeEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-referee-statistics'],
        params: SofascoreRefereeStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreRefereeStatisticsResponse: ...
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
        operation_id: Literal['sofascore-search-typed'],
        params: SofascoreSearchTypedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreSearchTypedResponse: ...
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
        operation_id: Literal['sofascore-stage'],
        params: SofascoreStageParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-stage-categories'],
        params: SofascoreStageCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-stage-driver-performance'],
        params: SofascoreStageDriverPerformanceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageDriverPerformanceResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-stage-featured'],
        params: SofascoreStageFeaturedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageFeaturedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-stage-schedule'],
        params: SofascoreStageScheduleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageScheduleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-stage-seasons'],
        params: SofascoreStageSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageSeasonsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-stage-standings'],
        params: SofascoreStageStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageStandingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-stage-substages'],
        params: SofascoreStageSubstagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreStageSubstagesResponse: ...
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
        operation_id: Literal['sofascore-team-achievements'],
        params: SofascoreTeamAchievementsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamAchievementsResponse: ...
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
        operation_id: Literal['sofascore-team-goal-distributions'],
        params: SofascoreTeamGoalDistributionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamGoalDistributionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-team-near-events'],
        params: SofascoreTeamNearEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamNearEventsResponse: ...
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
        operation_id: Literal['sofascore-team-performance'],
        params: SofascoreTeamPerformanceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamPerformanceResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-team-player-statistics'],
        params: SofascoreTeamPlayerStatisticsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamPlayerStatisticsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-team-player-statistics-seasons'],
        params: SofascoreTeamPlayerStatisticsSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamPlayerStatisticsSeasonsResponse: ...
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
        operation_id: Literal['sofascore-team-rankings'],
        params: SofascoreTeamRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamRankingsResponse: ...
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
        operation_id: Literal['sofascore-team-top-players'],
        params: SofascoreTeamTopPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamTopPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-team-tournaments'],
        params: SofascoreTeamTournamentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTeamTournamentsResponse: ...
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
        operation_id: Literal['sofascore-tennis-player-grand-slam-results'],
        params: SofascoreTennisPlayerGrandSlamResultsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTennisPlayerGrandSlamResultsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-tournament-cuptree'],
        params: SofascoreTournamentCuptreeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentCuptreeResponse: ...
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
        operation_id: Literal['sofascore-tournament-player-of-the-season'],
        params: SofascoreTournamentPlayerOfTheSeasonParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentPlayerOfTheSeasonResponse: ...
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
        operation_id: Literal['sofascore-tournament-statistics-info'],
        params: SofascoreTournamentStatisticsInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentStatisticsInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-tournament-team-of-the-season'],
        params: SofascoreTournamentTeamOfTheSeasonParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentTeamOfTheSeasonResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-tournament-teams'],
        params: SofascoreTournamentTeamsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentTeamsResponse: ...
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
        operation_id: Literal['sofascore-tournament-venues'],
        params: SofascoreTournamentVenuesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentVenuesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-tournament-winners'],
        params: SofascoreTournamentWinnersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentWinnersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-tournaments-with-feature'],
        params: SofascoreTournamentsWithFeatureParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTournamentsWithFeatureResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-trending-events'],
        params: SofascoreTrendingEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTrendingEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-trending-players'],
        params: SofascoreTrendingPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreTrendingPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-venue'],
        params: SofascoreVenueParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreVenueResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['sofascore-venue-events'],
        params: SofascoreVenueEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> SofascoreVenueEventsResponse: ...
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
    def draft(self, **params: Unpack[SofascoreDraftStreamParams]) -> BinaryIO: ...
    @overload
    def draft(self, **params: Unpack[SofascoreDraftTextResponseParams]) -> str: ...
    @overload
    def draft(self, **params: Unpack[SofascoreDraftDefaultParams]) -> SofascoreDraftResponse: ...
    @overload
    def draft_picks(self, **params: Unpack[SofascoreDraftPicksStreamParams]) -> BinaryIO: ...
    @overload
    def draft_picks(self, **params: Unpack[SofascoreDraftPicksTextResponseParams]) -> str: ...
    @overload
    def draft_picks(self, **params: Unpack[SofascoreDraftPicksDefaultParams]) -> SofascoreDraftPicksResponse: ...
    @overload
    def esports_game(self, **params: Unpack[SofascoreEsportsGameStreamParams]) -> BinaryIO: ...
    @overload
    def esports_game(self, **params: Unpack[SofascoreEsportsGameTextResponseParams]) -> str: ...
    @overload
    def esports_game(self, **params: Unpack[SofascoreEsportsGameDefaultParams]) -> SofascoreEsportsGameResponse: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventStreamParams]) -> BinaryIO: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventTextResponseParams]) -> str: ...
    @overload
    def event(self, **params: Unpack[SofascoreEventDefaultParams]) -> SofascoreEventResponse: ...
    @overload
    def event_at_bat_pitches(self, **params: Unpack[SofascoreEventAtBatPitchesStreamParams]) -> BinaryIO: ...
    @overload
    def event_at_bat_pitches(self, **params: Unpack[SofascoreEventAtBatPitchesTextResponseParams]) -> str: ...
    @overload
    def event_at_bat_pitches(self, **params: Unpack[SofascoreEventAtBatPitchesDefaultParams]) -> SofascoreEventAtBatPitchesResponse: ...
    @overload
    def event_at_bats(self, **params: Unpack[SofascoreEventAtBatsStreamParams]) -> BinaryIO: ...
    @overload
    def event_at_bats(self, **params: Unpack[SofascoreEventAtBatsTextResponseParams]) -> str: ...
    @overload
    def event_at_bats(self, **params: Unpack[SofascoreEventAtBatsDefaultParams]) -> SofascoreEventAtBatsResponse: ...
    @overload
    def event_average_positions(self, **params: Unpack[SofascoreEventAveragePositionsStreamParams]) -> BinaryIO: ...
    @overload
    def event_average_positions(self, **params: Unpack[SofascoreEventAveragePositionsTextResponseParams]) -> str: ...
    @overload
    def event_average_positions(self, **params: Unpack[SofascoreEventAveragePositionsDefaultParams]) -> SofascoreEventAveragePositionsResponse: ...
    @overload
    def event_baseball_top_performers(self, **params: Unpack[SofascoreEventBaseballTopPerformersStreamParams]) -> BinaryIO: ...
    @overload
    def event_baseball_top_performers(self, **params: Unpack[SofascoreEventBaseballTopPerformersTextResponseParams]) -> str: ...
    @overload
    def event_baseball_top_performers(self, **params: Unpack[SofascoreEventBaseballTopPerformersDefaultParams]) -> SofascoreEventBaseballTopPerformersResponse: ...
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
    def event_esports_games(self, **params: Unpack[SofascoreEventEsportsGamesStreamParams]) -> BinaryIO: ...
    @overload
    def event_esports_games(self, **params: Unpack[SofascoreEventEsportsGamesTextResponseParams]) -> str: ...
    @overload
    def event_esports_games(self, **params: Unpack[SofascoreEventEsportsGamesDefaultParams]) -> SofascoreEventEsportsGamesResponse: ...
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
    def event_highlights(self, **params: Unpack[SofascoreEventHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    def event_highlights(self, **params: Unpack[SofascoreEventHighlightsTextResponseParams]) -> str: ...
    @overload
    def event_highlights(self, **params: Unpack[SofascoreEventHighlightsDefaultParams]) -> SofascoreEventHighlightsResponse: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsStreamParams]) -> BinaryIO: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsTextResponseParams]) -> str: ...
    @overload
    def event_incidents(self, **params: Unpack[SofascoreEventIncidentsDefaultParams]) -> SofascoreEventIncidentsResponse: ...
    @overload
    def event_innings(self, **params: Unpack[SofascoreEventInningsStreamParams]) -> BinaryIO: ...
    @overload
    def event_innings(self, **params: Unpack[SofascoreEventInningsTextResponseParams]) -> str: ...
    @overload
    def event_innings(self, **params: Unpack[SofascoreEventInningsDefaultParams]) -> SofascoreEventInningsResponse: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsStreamParams]) -> BinaryIO: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsTextResponseParams]) -> str: ...
    @overload
    def event_lineups(self, **params: Unpack[SofascoreEventLineupsDefaultParams]) -> SofascoreEventLineupsResponse: ...
    @overload
    def event_managers(self, **params: Unpack[SofascoreEventManagersStreamParams]) -> BinaryIO: ...
    @overload
    def event_managers(self, **params: Unpack[SofascoreEventManagersTextResponseParams]) -> str: ...
    @overload
    def event_managers(self, **params: Unpack[SofascoreEventManagersDefaultParams]) -> SofascoreEventManagersResponse: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsStreamParams]) -> BinaryIO: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsTextResponseParams]) -> str: ...
    @overload
    def event_odds(self, **params: Unpack[SofascoreEventOddsDefaultParams]) -> SofascoreEventOddsResponse: ...
    @overload
    def event_player_heatmap(self, **params: Unpack[SofascoreEventPlayerHeatmapStreamParams]) -> BinaryIO: ...
    @overload
    def event_player_heatmap(self, **params: Unpack[SofascoreEventPlayerHeatmapTextResponseParams]) -> str: ...
    @overload
    def event_player_heatmap(self, **params: Unpack[SofascoreEventPlayerHeatmapDefaultParams]) -> SofascoreEventPlayerHeatmapResponse: ...
    @overload
    def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsDefaultParams]) -> SofascoreEventPlayerStatisticsResponse: ...
    @overload
    def event_point_by_point(self, **params: Unpack[SofascoreEventPointByPointStreamParams]) -> BinaryIO: ...
    @overload
    def event_point_by_point(self, **params: Unpack[SofascoreEventPointByPointTextResponseParams]) -> str: ...
    @overload
    def event_point_by_point(self, **params: Unpack[SofascoreEventPointByPointDefaultParams]) -> SofascoreEventPointByPointResponse: ...
    @overload
    def event_pregame_form(self, **params: Unpack[SofascoreEventPregameFormStreamParams]) -> BinaryIO: ...
    @overload
    def event_pregame_form(self, **params: Unpack[SofascoreEventPregameFormTextResponseParams]) -> str: ...
    @overload
    def event_pregame_form(self, **params: Unpack[SofascoreEventPregameFormDefaultParams]) -> SofascoreEventPregameFormResponse: ...
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
    def event_team_heatmap(self, **params: Unpack[SofascoreEventTeamHeatmapStreamParams]) -> BinaryIO: ...
    @overload
    def event_team_heatmap(self, **params: Unpack[SofascoreEventTeamHeatmapTextResponseParams]) -> str: ...
    @overload
    def event_team_heatmap(self, **params: Unpack[SofascoreEventTeamHeatmapDefaultParams]) -> SofascoreEventTeamHeatmapResponse: ...
    @overload
    def event_team_streaks(self, **params: Unpack[SofascoreEventTeamStreaksStreamParams]) -> BinaryIO: ...
    @overload
    def event_team_streaks(self, **params: Unpack[SofascoreEventTeamStreaksTextResponseParams]) -> str: ...
    @overload
    def event_team_streaks(self, **params: Unpack[SofascoreEventTeamStreaksDefaultParams]) -> SofascoreEventTeamStreaksResponse: ...
    @overload
    def event_tennis_power(self, **params: Unpack[SofascoreEventTennisPowerStreamParams]) -> BinaryIO: ...
    @overload
    def event_tennis_power(self, **params: Unpack[SofascoreEventTennisPowerTextResponseParams]) -> str: ...
    @overload
    def event_tennis_power(self, **params: Unpack[SofascoreEventTennisPowerDefaultParams]) -> SofascoreEventTennisPowerResponse: ...
    @overload
    def event_tv_channels(self, **params: Unpack[SofascoreEventTvChannelsStreamParams]) -> BinaryIO: ...
    @overload
    def event_tv_channels(self, **params: Unpack[SofascoreEventTvChannelsTextResponseParams]) -> str: ...
    @overload
    def event_tv_channels(self, **params: Unpack[SofascoreEventTvChannelsDefaultParams]) -> SofascoreEventTvChannelsResponse: ...
    @overload
    def event_votes(self, **params: Unpack[SofascoreEventVotesStreamParams]) -> BinaryIO: ...
    @overload
    def event_votes(self, **params: Unpack[SofascoreEventVotesTextResponseParams]) -> str: ...
    @overload
    def event_votes(self, **params: Unpack[SofascoreEventVotesDefaultParams]) -> SofascoreEventVotesResponse: ...
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
    def mma_card(self, **params: Unpack[SofascoreMmaCardStreamParams]) -> BinaryIO: ...
    @overload
    def mma_card(self, **params: Unpack[SofascoreMmaCardTextResponseParams]) -> str: ...
    @overload
    def mma_card(self, **params: Unpack[SofascoreMmaCardDefaultParams]) -> SofascoreMmaCardResponse: ...
    @overload
    def mma_schedule(self, **params: Unpack[SofascoreMmaScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def mma_schedule(self, **params: Unpack[SofascoreMmaScheduleTextResponseParams]) -> str: ...
    @overload
    def mma_schedule(self, **params: Unpack[SofascoreMmaScheduleDefaultParams]) -> SofascoreMmaScheduleResponse: ...
    @overload
    def odds_dropping(self, **params: Unpack[SofascoreOddsDroppingStreamParams]) -> BinaryIO: ...
    @overload
    def odds_dropping(self, **params: Unpack[SofascoreOddsDroppingTextResponseParams]) -> str: ...
    @overload
    def odds_dropping(self, **params: Unpack[SofascoreOddsDroppingDefaultParams]) -> SofascoreOddsDroppingResponse: ...
    @overload
    def odds_winning(self, **params: Unpack[SofascoreOddsWinningStreamParams]) -> BinaryIO: ...
    @overload
    def odds_winning(self, **params: Unpack[SofascoreOddsWinningTextResponseParams]) -> str: ...
    @overload
    def odds_winning(self, **params: Unpack[SofascoreOddsWinningDefaultParams]) -> SofascoreOddsWinningResponse: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[SofascorePlayerDefaultParams]) -> SofascorePlayerResponse: ...
    @overload
    def player_attributes(self, **params: Unpack[SofascorePlayerAttributesStreamParams]) -> BinaryIO: ...
    @overload
    def player_attributes(self, **params: Unpack[SofascorePlayerAttributesTextResponseParams]) -> str: ...
    @overload
    def player_attributes(self, **params: Unpack[SofascorePlayerAttributesDefaultParams]) -> SofascorePlayerAttributesResponse: ...
    @overload
    def player_events(self, **params: Unpack[SofascorePlayerEventsStreamParams]) -> BinaryIO: ...
    @overload
    def player_events(self, **params: Unpack[SofascorePlayerEventsTextResponseParams]) -> str: ...
    @overload
    def player_events(self, **params: Unpack[SofascorePlayerEventsDefaultParams]) -> SofascorePlayerEventsResponse: ...
    @overload
    def player_last_year_summary(self, **params: Unpack[SofascorePlayerLastYearSummaryStreamParams]) -> BinaryIO: ...
    @overload
    def player_last_year_summary(self, **params: Unpack[SofascorePlayerLastYearSummaryTextResponseParams]) -> str: ...
    @overload
    def player_last_year_summary(self, **params: Unpack[SofascorePlayerLastYearSummaryDefaultParams]) -> SofascorePlayerLastYearSummaryResponse: ...
    @overload
    def player_national_team_statistics(self, **params: Unpack[SofascorePlayerNationalTeamStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def player_national_team_statistics(self, **params: Unpack[SofascorePlayerNationalTeamStatisticsTextResponseParams]) -> str: ...
    @overload
    def player_national_team_statistics(self, **params: Unpack[SofascorePlayerNationalTeamStatisticsDefaultParams]) -> SofascorePlayerNationalTeamStatisticsResponse: ...
    @overload
    def player_penalty_history(self, **params: Unpack[SofascorePlayerPenaltyHistoryStreamParams]) -> BinaryIO: ...
    @overload
    def player_penalty_history(self, **params: Unpack[SofascorePlayerPenaltyHistoryTextResponseParams]) -> str: ...
    @overload
    def player_penalty_history(self, **params: Unpack[SofascorePlayerPenaltyHistoryDefaultParams]) -> SofascorePlayerPenaltyHistoryResponse: ...
    @overload
    def player_ratings(self, **params: Unpack[SofascorePlayerRatingsStreamParams]) -> BinaryIO: ...
    @overload
    def player_ratings(self, **params: Unpack[SofascorePlayerRatingsTextResponseParams]) -> str: ...
    @overload
    def player_ratings(self, **params: Unpack[SofascorePlayerRatingsDefaultParams]) -> SofascorePlayerRatingsResponse: ...
    @overload
    def player_season_heatmap(self, **params: Unpack[SofascorePlayerSeasonHeatmapStreamParams]) -> BinaryIO: ...
    @overload
    def player_season_heatmap(self, **params: Unpack[SofascorePlayerSeasonHeatmapTextResponseParams]) -> str: ...
    @overload
    def player_season_heatmap(self, **params: Unpack[SofascorePlayerSeasonHeatmapDefaultParams]) -> SofascorePlayerSeasonHeatmapResponse: ...
    @overload
    def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsTextResponseParams]) -> str: ...
    @overload
    def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsDefaultParams]) -> SofascorePlayerSeasonStatisticsResponse: ...
    @overload
    def player_statistical_rankings(self, **params: Unpack[SofascorePlayerStatisticalRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def player_statistical_rankings(self, **params: Unpack[SofascorePlayerStatisticalRankingsTextResponseParams]) -> str: ...
    @overload
    def player_statistical_rankings(self, **params: Unpack[SofascorePlayerStatisticalRankingsDefaultParams]) -> SofascorePlayerStatisticalRankingsResponse: ...
    @overload
    def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsDefaultParams]) -> SofascorePlayerStatisticsSeasonsResponse: ...
    @overload
    def player_tournaments(self, **params: Unpack[SofascorePlayerTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def player_tournaments(self, **params: Unpack[SofascorePlayerTournamentsTextResponseParams]) -> str: ...
    @overload
    def player_tournaments(self, **params: Unpack[SofascorePlayerTournamentsDefaultParams]) -> SofascorePlayerTournamentsResponse: ...
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
    def referee(self, **params: Unpack[SofascoreRefereeStreamParams]) -> BinaryIO: ...
    @overload
    def referee(self, **params: Unpack[SofascoreRefereeTextResponseParams]) -> str: ...
    @overload
    def referee(self, **params: Unpack[SofascoreRefereeDefaultParams]) -> SofascoreRefereeResponse: ...
    @overload
    def referee_events(self, **params: Unpack[SofascoreRefereeEventsStreamParams]) -> BinaryIO: ...
    @overload
    def referee_events(self, **params: Unpack[SofascoreRefereeEventsTextResponseParams]) -> str: ...
    @overload
    def referee_events(self, **params: Unpack[SofascoreRefereeEventsDefaultParams]) -> SofascoreRefereeEventsResponse: ...
    @overload
    def referee_statistics(self, **params: Unpack[SofascoreRefereeStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def referee_statistics(self, **params: Unpack[SofascoreRefereeStatisticsTextResponseParams]) -> str: ...
    @overload
    def referee_statistics(self, **params: Unpack[SofascoreRefereeStatisticsDefaultParams]) -> SofascoreRefereeStatisticsResponse: ...
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
    def search_typed(self, **params: Unpack[SofascoreSearchTypedStreamParams]) -> BinaryIO: ...
    @overload
    def search_typed(self, **params: Unpack[SofascoreSearchTypedTextResponseParams]) -> str: ...
    @overload
    def search_typed(self, **params: Unpack[SofascoreSearchTypedDefaultParams]) -> SofascoreSearchTypedResponse: ...
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
    def stage(self, **params: Unpack[SofascoreStageStreamParams]) -> BinaryIO: ...
    @overload
    def stage(self, **params: Unpack[SofascoreStageTextResponseParams]) -> str: ...
    @overload
    def stage(self, **params: Unpack[SofascoreStageDefaultParams]) -> SofascoreStageResponse: ...
    @overload
    def stage_categories(self, **params: Unpack[SofascoreStageCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def stage_categories(self, **params: Unpack[SofascoreStageCategoriesTextResponseParams]) -> str: ...
    @overload
    def stage_categories(self, **params: Unpack[SofascoreStageCategoriesDefaultParams]) -> SofascoreStageCategoriesResponse: ...
    @overload
    def stage_driver_performance(self, **params: Unpack[SofascoreStageDriverPerformanceStreamParams]) -> BinaryIO: ...
    @overload
    def stage_driver_performance(self, **params: Unpack[SofascoreStageDriverPerformanceTextResponseParams]) -> str: ...
    @overload
    def stage_driver_performance(self, **params: Unpack[SofascoreStageDriverPerformanceDefaultParams]) -> SofascoreStageDriverPerformanceResponse: ...
    @overload
    def stage_featured(self, **params: Unpack[SofascoreStageFeaturedStreamParams]) -> BinaryIO: ...
    @overload
    def stage_featured(self, **params: Unpack[SofascoreStageFeaturedTextResponseParams]) -> str: ...
    @overload
    def stage_featured(self, **params: Unpack[SofascoreStageFeaturedDefaultParams]) -> SofascoreStageFeaturedResponse: ...
    @overload
    def stage_schedule(self, **params: Unpack[SofascoreStageScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def stage_schedule(self, **params: Unpack[SofascoreStageScheduleTextResponseParams]) -> str: ...
    @overload
    def stage_schedule(self, **params: Unpack[SofascoreStageScheduleDefaultParams]) -> SofascoreStageScheduleResponse: ...
    @overload
    def stage_seasons(self, **params: Unpack[SofascoreStageSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def stage_seasons(self, **params: Unpack[SofascoreStageSeasonsTextResponseParams]) -> str: ...
    @overload
    def stage_seasons(self, **params: Unpack[SofascoreStageSeasonsDefaultParams]) -> SofascoreStageSeasonsResponse: ...
    @overload
    def stage_standings(self, **params: Unpack[SofascoreStageStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def stage_standings(self, **params: Unpack[SofascoreStageStandingsTextResponseParams]) -> str: ...
    @overload
    def stage_standings(self, **params: Unpack[SofascoreStageStandingsDefaultParams]) -> SofascoreStageStandingsResponse: ...
    @overload
    def stage_substages(self, **params: Unpack[SofascoreStageSubstagesStreamParams]) -> BinaryIO: ...
    @overload
    def stage_substages(self, **params: Unpack[SofascoreStageSubstagesTextResponseParams]) -> str: ...
    @overload
    def stage_substages(self, **params: Unpack[SofascoreStageSubstagesDefaultParams]) -> SofascoreStageSubstagesResponse: ...
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
    def team_achievements(self, **params: Unpack[SofascoreTeamAchievementsStreamParams]) -> BinaryIO: ...
    @overload
    def team_achievements(self, **params: Unpack[SofascoreTeamAchievementsTextResponseParams]) -> str: ...
    @overload
    def team_achievements(self, **params: Unpack[SofascoreTeamAchievementsDefaultParams]) -> SofascoreTeamAchievementsResponse: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsStreamParams]) -> BinaryIO: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsTextResponseParams]) -> str: ...
    @overload
    def team_events(self, **params: Unpack[SofascoreTeamEventsDefaultParams]) -> SofascoreTeamEventsResponse: ...
    @overload
    def team_goal_distributions(self, **params: Unpack[SofascoreTeamGoalDistributionsStreamParams]) -> BinaryIO: ...
    @overload
    def team_goal_distributions(self, **params: Unpack[SofascoreTeamGoalDistributionsTextResponseParams]) -> str: ...
    @overload
    def team_goal_distributions(self, **params: Unpack[SofascoreTeamGoalDistributionsDefaultParams]) -> SofascoreTeamGoalDistributionsResponse: ...
    @overload
    def team_near_events(self, **params: Unpack[SofascoreTeamNearEventsStreamParams]) -> BinaryIO: ...
    @overload
    def team_near_events(self, **params: Unpack[SofascoreTeamNearEventsTextResponseParams]) -> str: ...
    @overload
    def team_near_events(self, **params: Unpack[SofascoreTeamNearEventsDefaultParams]) -> SofascoreTeamNearEventsResponse: ...
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
    def team_performance(self, **params: Unpack[SofascoreTeamPerformanceStreamParams]) -> BinaryIO: ...
    @overload
    def team_performance(self, **params: Unpack[SofascoreTeamPerformanceTextResponseParams]) -> str: ...
    @overload
    def team_performance(self, **params: Unpack[SofascoreTeamPerformanceDefaultParams]) -> SofascoreTeamPerformanceResponse: ...
    @overload
    def team_player_statistics(self, **params: Unpack[SofascoreTeamPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    def team_player_statistics(self, **params: Unpack[SofascoreTeamPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    def team_player_statistics(self, **params: Unpack[SofascoreTeamPlayerStatisticsDefaultParams]) -> SofascoreTeamPlayerStatisticsResponse: ...
    @overload
    def team_player_statistics_seasons(self, **params: Unpack[SofascoreTeamPlayerStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def team_player_statistics_seasons(self, **params: Unpack[SofascoreTeamPlayerStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    def team_player_statistics_seasons(self, **params: Unpack[SofascoreTeamPlayerStatisticsSeasonsDefaultParams]) -> SofascoreTeamPlayerStatisticsSeasonsResponse: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersTextResponseParams]) -> str: ...
    @overload
    def team_players(self, **params: Unpack[SofascoreTeamPlayersDefaultParams]) -> SofascoreTeamPlayersResponse: ...
    @overload
    def team_rankings(self, **params: Unpack[SofascoreTeamRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def team_rankings(self, **params: Unpack[SofascoreTeamRankingsTextResponseParams]) -> str: ...
    @overload
    def team_rankings(self, **params: Unpack[SofascoreTeamRankingsDefaultParams]) -> SofascoreTeamRankingsResponse: ...
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
    def team_top_players(self, **params: Unpack[SofascoreTeamTopPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def team_top_players(self, **params: Unpack[SofascoreTeamTopPlayersTextResponseParams]) -> str: ...
    @overload
    def team_top_players(self, **params: Unpack[SofascoreTeamTopPlayersDefaultParams]) -> SofascoreTeamTopPlayersResponse: ...
    @overload
    def team_tournaments(self, **params: Unpack[SofascoreTeamTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def team_tournaments(self, **params: Unpack[SofascoreTeamTournamentsTextResponseParams]) -> str: ...
    @overload
    def team_tournaments(self, **params: Unpack[SofascoreTeamTournamentsDefaultParams]) -> SofascoreTeamTournamentsResponse: ...
    @overload
    def team_transfers(self, **params: Unpack[SofascoreTeamTransfersStreamParams]) -> BinaryIO: ...
    @overload
    def team_transfers(self, **params: Unpack[SofascoreTeamTransfersTextResponseParams]) -> str: ...
    @overload
    def team_transfers(self, **params: Unpack[SofascoreTeamTransfersDefaultParams]) -> SofascoreTeamTransfersResponse: ...
    @overload
    def tennis_player_grand_slam_results(self, **params: Unpack[SofascoreTennisPlayerGrandSlamResultsStreamParams]) -> BinaryIO: ...
    @overload
    def tennis_player_grand_slam_results(self, **params: Unpack[SofascoreTennisPlayerGrandSlamResultsTextResponseParams]) -> str: ...
    @overload
    def tennis_player_grand_slam_results(self, **params: Unpack[SofascoreTennisPlayerGrandSlamResultsDefaultParams]) -> SofascoreTennisPlayerGrandSlamResultsResponse: ...
    @overload
    def tournament_cuptree(self, **params: Unpack[SofascoreTournamentCuptreeStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_cuptree(self, **params: Unpack[SofascoreTournamentCuptreeTextResponseParams]) -> str: ...
    @overload
    def tournament_cuptree(self, **params: Unpack[SofascoreTournamentCuptreeDefaultParams]) -> SofascoreTournamentCuptreeResponse: ...
    @overload
    def tournament_info(self, **params: Unpack[SofascoreTournamentInfoStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_info(self, **params: Unpack[SofascoreTournamentInfoTextResponseParams]) -> str: ...
    @overload
    def tournament_info(self, **params: Unpack[SofascoreTournamentInfoDefaultParams]) -> SofascoreTournamentInfoResponse: ...
    @overload
    def tournament_player_of_the_season(self, **params: Unpack[SofascoreTournamentPlayerOfTheSeasonStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_player_of_the_season(self, **params: Unpack[SofascoreTournamentPlayerOfTheSeasonTextResponseParams]) -> str: ...
    @overload
    def tournament_player_of_the_season(self, **params: Unpack[SofascoreTournamentPlayerOfTheSeasonDefaultParams]) -> SofascoreTournamentPlayerOfTheSeasonResponse: ...
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
    def tournament_statistics_info(self, **params: Unpack[SofascoreTournamentStatisticsInfoStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_statistics_info(self, **params: Unpack[SofascoreTournamentStatisticsInfoTextResponseParams]) -> str: ...
    @overload
    def tournament_statistics_info(self, **params: Unpack[SofascoreTournamentStatisticsInfoDefaultParams]) -> SofascoreTournamentStatisticsInfoResponse: ...
    @overload
    def tournament_team_of_the_season(self, **params: Unpack[SofascoreTournamentTeamOfTheSeasonStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_team_of_the_season(self, **params: Unpack[SofascoreTournamentTeamOfTheSeasonTextResponseParams]) -> str: ...
    @overload
    def tournament_team_of_the_season(self, **params: Unpack[SofascoreTournamentTeamOfTheSeasonDefaultParams]) -> SofascoreTournamentTeamOfTheSeasonResponse: ...
    @overload
    def tournament_teams(self, **params: Unpack[SofascoreTournamentTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_teams(self, **params: Unpack[SofascoreTournamentTeamsTextResponseParams]) -> str: ...
    @overload
    def tournament_teams(self, **params: Unpack[SofascoreTournamentTeamsDefaultParams]) -> SofascoreTournamentTeamsResponse: ...
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
    @overload
    def tournament_venues(self, **params: Unpack[SofascoreTournamentVenuesStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_venues(self, **params: Unpack[SofascoreTournamentVenuesTextResponseParams]) -> str: ...
    @overload
    def tournament_venues(self, **params: Unpack[SofascoreTournamentVenuesDefaultParams]) -> SofascoreTournamentVenuesResponse: ...
    @overload
    def tournament_winners(self, **params: Unpack[SofascoreTournamentWinnersStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_winners(self, **params: Unpack[SofascoreTournamentWinnersTextResponseParams]) -> str: ...
    @overload
    def tournament_winners(self, **params: Unpack[SofascoreTournamentWinnersDefaultParams]) -> SofascoreTournamentWinnersResponse: ...
    @overload
    def tournaments_with_feature(self, **params: Unpack[SofascoreTournamentsWithFeatureStreamParams]) -> BinaryIO: ...
    @overload
    def tournaments_with_feature(self, **params: Unpack[SofascoreTournamentsWithFeatureTextResponseParams]) -> str: ...
    @overload
    def tournaments_with_feature(self, **params: Unpack[SofascoreTournamentsWithFeatureDefaultParams]) -> SofascoreTournamentsWithFeatureResponse: ...
    @overload
    def trending_events(self, **params: Unpack[SofascoreTrendingEventsStreamParams]) -> BinaryIO: ...
    @overload
    def trending_events(self, **params: Unpack[SofascoreTrendingEventsTextResponseParams]) -> str: ...
    @overload
    def trending_events(self, **params: Unpack[SofascoreTrendingEventsDefaultParams]) -> SofascoreTrendingEventsResponse: ...
    @overload
    def trending_players(self, **params: Unpack[SofascoreTrendingPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def trending_players(self, **params: Unpack[SofascoreTrendingPlayersTextResponseParams]) -> str: ...
    @overload
    def trending_players(self, **params: Unpack[SofascoreTrendingPlayersDefaultParams]) -> SofascoreTrendingPlayersResponse: ...
    @overload
    def venue(self, **params: Unpack[SofascoreVenueStreamParams]) -> BinaryIO: ...
    @overload
    def venue(self, **params: Unpack[SofascoreVenueTextResponseParams]) -> str: ...
    @overload
    def venue(self, **params: Unpack[SofascoreVenueDefaultParams]) -> SofascoreVenueResponse: ...
    @overload
    def venue_events(self, **params: Unpack[SofascoreVenueEventsStreamParams]) -> BinaryIO: ...
    @overload
    def venue_events(self, **params: Unpack[SofascoreVenueEventsTextResponseParams]) -> str: ...
    @overload
    def venue_events(self, **params: Unpack[SofascoreVenueEventsDefaultParams]) -> SofascoreVenueEventsResponse: ...

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
    async def draft(self, **params: Unpack[SofascoreDraftStreamParams]) -> BinaryIO: ...
    @overload
    async def draft(self, **params: Unpack[SofascoreDraftTextResponseParams]) -> str: ...
    @overload
    async def draft(self, **params: Unpack[SofascoreDraftDefaultParams]) -> SofascoreDraftResponse: ...
    @overload
    async def draft_picks(self, **params: Unpack[SofascoreDraftPicksStreamParams]) -> BinaryIO: ...
    @overload
    async def draft_picks(self, **params: Unpack[SofascoreDraftPicksTextResponseParams]) -> str: ...
    @overload
    async def draft_picks(self, **params: Unpack[SofascoreDraftPicksDefaultParams]) -> SofascoreDraftPicksResponse: ...
    @overload
    async def esports_game(self, **params: Unpack[SofascoreEsportsGameStreamParams]) -> BinaryIO: ...
    @overload
    async def esports_game(self, **params: Unpack[SofascoreEsportsGameTextResponseParams]) -> str: ...
    @overload
    async def esports_game(self, **params: Unpack[SofascoreEsportsGameDefaultParams]) -> SofascoreEsportsGameResponse: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventStreamParams]) -> BinaryIO: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventTextResponseParams]) -> str: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventDefaultParams]) -> SofascoreEventResponse: ...
    @overload
    async def event_at_bat_pitches(self, **params: Unpack[SofascoreEventAtBatPitchesStreamParams]) -> BinaryIO: ...
    @overload
    async def event_at_bat_pitches(self, **params: Unpack[SofascoreEventAtBatPitchesTextResponseParams]) -> str: ...
    @overload
    async def event_at_bat_pitches(self, **params: Unpack[SofascoreEventAtBatPitchesDefaultParams]) -> SofascoreEventAtBatPitchesResponse: ...
    @overload
    async def event_at_bats(self, **params: Unpack[SofascoreEventAtBatsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_at_bats(self, **params: Unpack[SofascoreEventAtBatsTextResponseParams]) -> str: ...
    @overload
    async def event_at_bats(self, **params: Unpack[SofascoreEventAtBatsDefaultParams]) -> SofascoreEventAtBatsResponse: ...
    @overload
    async def event_average_positions(self, **params: Unpack[SofascoreEventAveragePositionsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_average_positions(self, **params: Unpack[SofascoreEventAveragePositionsTextResponseParams]) -> str: ...
    @overload
    async def event_average_positions(self, **params: Unpack[SofascoreEventAveragePositionsDefaultParams]) -> SofascoreEventAveragePositionsResponse: ...
    @overload
    async def event_baseball_top_performers(self, **params: Unpack[SofascoreEventBaseballTopPerformersStreamParams]) -> BinaryIO: ...
    @overload
    async def event_baseball_top_performers(self, **params: Unpack[SofascoreEventBaseballTopPerformersTextResponseParams]) -> str: ...
    @overload
    async def event_baseball_top_performers(self, **params: Unpack[SofascoreEventBaseballTopPerformersDefaultParams]) -> SofascoreEventBaseballTopPerformersResponse: ...
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
    async def event_esports_games(self, **params: Unpack[SofascoreEventEsportsGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def event_esports_games(self, **params: Unpack[SofascoreEventEsportsGamesTextResponseParams]) -> str: ...
    @overload
    async def event_esports_games(self, **params: Unpack[SofascoreEventEsportsGamesDefaultParams]) -> SofascoreEventEsportsGamesResponse: ...
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
    async def event_highlights(self, **params: Unpack[SofascoreEventHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_highlights(self, **params: Unpack[SofascoreEventHighlightsTextResponseParams]) -> str: ...
    @overload
    async def event_highlights(self, **params: Unpack[SofascoreEventHighlightsDefaultParams]) -> SofascoreEventHighlightsResponse: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsTextResponseParams]) -> str: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsDefaultParams]) -> SofascoreEventIncidentsResponse: ...
    @overload
    async def event_innings(self, **params: Unpack[SofascoreEventInningsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_innings(self, **params: Unpack[SofascoreEventInningsTextResponseParams]) -> str: ...
    @overload
    async def event_innings(self, **params: Unpack[SofascoreEventInningsDefaultParams]) -> SofascoreEventInningsResponse: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsTextResponseParams]) -> str: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsDefaultParams]) -> SofascoreEventLineupsResponse: ...
    @overload
    async def event_managers(self, **params: Unpack[SofascoreEventManagersStreamParams]) -> BinaryIO: ...
    @overload
    async def event_managers(self, **params: Unpack[SofascoreEventManagersTextResponseParams]) -> str: ...
    @overload
    async def event_managers(self, **params: Unpack[SofascoreEventManagersDefaultParams]) -> SofascoreEventManagersResponse: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsTextResponseParams]) -> str: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsDefaultParams]) -> SofascoreEventOddsResponse: ...
    @overload
    async def event_player_heatmap(self, **params: Unpack[SofascoreEventPlayerHeatmapStreamParams]) -> BinaryIO: ...
    @overload
    async def event_player_heatmap(self, **params: Unpack[SofascoreEventPlayerHeatmapTextResponseParams]) -> str: ...
    @overload
    async def event_player_heatmap(self, **params: Unpack[SofascoreEventPlayerHeatmapDefaultParams]) -> SofascoreEventPlayerHeatmapResponse: ...
    @overload
    async def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    async def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsDefaultParams]) -> SofascoreEventPlayerStatisticsResponse: ...
    @overload
    async def event_point_by_point(self, **params: Unpack[SofascoreEventPointByPointStreamParams]) -> BinaryIO: ...
    @overload
    async def event_point_by_point(self, **params: Unpack[SofascoreEventPointByPointTextResponseParams]) -> str: ...
    @overload
    async def event_point_by_point(self, **params: Unpack[SofascoreEventPointByPointDefaultParams]) -> SofascoreEventPointByPointResponse: ...
    @overload
    async def event_pregame_form(self, **params: Unpack[SofascoreEventPregameFormStreamParams]) -> BinaryIO: ...
    @overload
    async def event_pregame_form(self, **params: Unpack[SofascoreEventPregameFormTextResponseParams]) -> str: ...
    @overload
    async def event_pregame_form(self, **params: Unpack[SofascoreEventPregameFormDefaultParams]) -> SofascoreEventPregameFormResponse: ...
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
    async def event_team_heatmap(self, **params: Unpack[SofascoreEventTeamHeatmapStreamParams]) -> BinaryIO: ...
    @overload
    async def event_team_heatmap(self, **params: Unpack[SofascoreEventTeamHeatmapTextResponseParams]) -> str: ...
    @overload
    async def event_team_heatmap(self, **params: Unpack[SofascoreEventTeamHeatmapDefaultParams]) -> SofascoreEventTeamHeatmapResponse: ...
    @overload
    async def event_team_streaks(self, **params: Unpack[SofascoreEventTeamStreaksStreamParams]) -> BinaryIO: ...
    @overload
    async def event_team_streaks(self, **params: Unpack[SofascoreEventTeamStreaksTextResponseParams]) -> str: ...
    @overload
    async def event_team_streaks(self, **params: Unpack[SofascoreEventTeamStreaksDefaultParams]) -> SofascoreEventTeamStreaksResponse: ...
    @overload
    async def event_tennis_power(self, **params: Unpack[SofascoreEventTennisPowerStreamParams]) -> BinaryIO: ...
    @overload
    async def event_tennis_power(self, **params: Unpack[SofascoreEventTennisPowerTextResponseParams]) -> str: ...
    @overload
    async def event_tennis_power(self, **params: Unpack[SofascoreEventTennisPowerDefaultParams]) -> SofascoreEventTennisPowerResponse: ...
    @overload
    async def event_tv_channels(self, **params: Unpack[SofascoreEventTvChannelsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_tv_channels(self, **params: Unpack[SofascoreEventTvChannelsTextResponseParams]) -> str: ...
    @overload
    async def event_tv_channels(self, **params: Unpack[SofascoreEventTvChannelsDefaultParams]) -> SofascoreEventTvChannelsResponse: ...
    @overload
    async def event_votes(self, **params: Unpack[SofascoreEventVotesStreamParams]) -> BinaryIO: ...
    @overload
    async def event_votes(self, **params: Unpack[SofascoreEventVotesTextResponseParams]) -> str: ...
    @overload
    async def event_votes(self, **params: Unpack[SofascoreEventVotesDefaultParams]) -> SofascoreEventVotesResponse: ...
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
    async def mma_card(self, **params: Unpack[SofascoreMmaCardStreamParams]) -> BinaryIO: ...
    @overload
    async def mma_card(self, **params: Unpack[SofascoreMmaCardTextResponseParams]) -> str: ...
    @overload
    async def mma_card(self, **params: Unpack[SofascoreMmaCardDefaultParams]) -> SofascoreMmaCardResponse: ...
    @overload
    async def mma_schedule(self, **params: Unpack[SofascoreMmaScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def mma_schedule(self, **params: Unpack[SofascoreMmaScheduleTextResponseParams]) -> str: ...
    @overload
    async def mma_schedule(self, **params: Unpack[SofascoreMmaScheduleDefaultParams]) -> SofascoreMmaScheduleResponse: ...
    @overload
    async def odds_dropping(self, **params: Unpack[SofascoreOddsDroppingStreamParams]) -> BinaryIO: ...
    @overload
    async def odds_dropping(self, **params: Unpack[SofascoreOddsDroppingTextResponseParams]) -> str: ...
    @overload
    async def odds_dropping(self, **params: Unpack[SofascoreOddsDroppingDefaultParams]) -> SofascoreOddsDroppingResponse: ...
    @overload
    async def odds_winning(self, **params: Unpack[SofascoreOddsWinningStreamParams]) -> BinaryIO: ...
    @overload
    async def odds_winning(self, **params: Unpack[SofascoreOddsWinningTextResponseParams]) -> str: ...
    @overload
    async def odds_winning(self, **params: Unpack[SofascoreOddsWinningDefaultParams]) -> SofascoreOddsWinningResponse: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerDefaultParams]) -> SofascorePlayerResponse: ...
    @overload
    async def player_attributes(self, **params: Unpack[SofascorePlayerAttributesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_attributes(self, **params: Unpack[SofascorePlayerAttributesTextResponseParams]) -> str: ...
    @overload
    async def player_attributes(self, **params: Unpack[SofascorePlayerAttributesDefaultParams]) -> SofascorePlayerAttributesResponse: ...
    @overload
    async def player_events(self, **params: Unpack[SofascorePlayerEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_events(self, **params: Unpack[SofascorePlayerEventsTextResponseParams]) -> str: ...
    @overload
    async def player_events(self, **params: Unpack[SofascorePlayerEventsDefaultParams]) -> SofascorePlayerEventsResponse: ...
    @overload
    async def player_last_year_summary(self, **params: Unpack[SofascorePlayerLastYearSummaryStreamParams]) -> BinaryIO: ...
    @overload
    async def player_last_year_summary(self, **params: Unpack[SofascorePlayerLastYearSummaryTextResponseParams]) -> str: ...
    @overload
    async def player_last_year_summary(self, **params: Unpack[SofascorePlayerLastYearSummaryDefaultParams]) -> SofascorePlayerLastYearSummaryResponse: ...
    @overload
    async def player_national_team_statistics(self, **params: Unpack[SofascorePlayerNationalTeamStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_national_team_statistics(self, **params: Unpack[SofascorePlayerNationalTeamStatisticsTextResponseParams]) -> str: ...
    @overload
    async def player_national_team_statistics(self, **params: Unpack[SofascorePlayerNationalTeamStatisticsDefaultParams]) -> SofascorePlayerNationalTeamStatisticsResponse: ...
    @overload
    async def player_penalty_history(self, **params: Unpack[SofascorePlayerPenaltyHistoryStreamParams]) -> BinaryIO: ...
    @overload
    async def player_penalty_history(self, **params: Unpack[SofascorePlayerPenaltyHistoryTextResponseParams]) -> str: ...
    @overload
    async def player_penalty_history(self, **params: Unpack[SofascorePlayerPenaltyHistoryDefaultParams]) -> SofascorePlayerPenaltyHistoryResponse: ...
    @overload
    async def player_ratings(self, **params: Unpack[SofascorePlayerRatingsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_ratings(self, **params: Unpack[SofascorePlayerRatingsTextResponseParams]) -> str: ...
    @overload
    async def player_ratings(self, **params: Unpack[SofascorePlayerRatingsDefaultParams]) -> SofascorePlayerRatingsResponse: ...
    @overload
    async def player_season_heatmap(self, **params: Unpack[SofascorePlayerSeasonHeatmapStreamParams]) -> BinaryIO: ...
    @overload
    async def player_season_heatmap(self, **params: Unpack[SofascorePlayerSeasonHeatmapTextResponseParams]) -> str: ...
    @overload
    async def player_season_heatmap(self, **params: Unpack[SofascorePlayerSeasonHeatmapDefaultParams]) -> SofascorePlayerSeasonHeatmapResponse: ...
    @overload
    async def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsTextResponseParams]) -> str: ...
    @overload
    async def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsDefaultParams]) -> SofascorePlayerSeasonStatisticsResponse: ...
    @overload
    async def player_statistical_rankings(self, **params: Unpack[SofascorePlayerStatisticalRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_statistical_rankings(self, **params: Unpack[SofascorePlayerStatisticalRankingsTextResponseParams]) -> str: ...
    @overload
    async def player_statistical_rankings(self, **params: Unpack[SofascorePlayerStatisticalRankingsDefaultParams]) -> SofascorePlayerStatisticalRankingsResponse: ...
    @overload
    async def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    async def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsDefaultParams]) -> SofascorePlayerStatisticsSeasonsResponse: ...
    @overload
    async def player_tournaments(self, **params: Unpack[SofascorePlayerTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_tournaments(self, **params: Unpack[SofascorePlayerTournamentsTextResponseParams]) -> str: ...
    @overload
    async def player_tournaments(self, **params: Unpack[SofascorePlayerTournamentsDefaultParams]) -> SofascorePlayerTournamentsResponse: ...
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
    async def referee(self, **params: Unpack[SofascoreRefereeStreamParams]) -> BinaryIO: ...
    @overload
    async def referee(self, **params: Unpack[SofascoreRefereeTextResponseParams]) -> str: ...
    @overload
    async def referee(self, **params: Unpack[SofascoreRefereeDefaultParams]) -> SofascoreRefereeResponse: ...
    @overload
    async def referee_events(self, **params: Unpack[SofascoreRefereeEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def referee_events(self, **params: Unpack[SofascoreRefereeEventsTextResponseParams]) -> str: ...
    @overload
    async def referee_events(self, **params: Unpack[SofascoreRefereeEventsDefaultParams]) -> SofascoreRefereeEventsResponse: ...
    @overload
    async def referee_statistics(self, **params: Unpack[SofascoreRefereeStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def referee_statistics(self, **params: Unpack[SofascoreRefereeStatisticsTextResponseParams]) -> str: ...
    @overload
    async def referee_statistics(self, **params: Unpack[SofascoreRefereeStatisticsDefaultParams]) -> SofascoreRefereeStatisticsResponse: ...
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
    async def search_typed(self, **params: Unpack[SofascoreSearchTypedStreamParams]) -> BinaryIO: ...
    @overload
    async def search_typed(self, **params: Unpack[SofascoreSearchTypedTextResponseParams]) -> str: ...
    @overload
    async def search_typed(self, **params: Unpack[SofascoreSearchTypedDefaultParams]) -> SofascoreSearchTypedResponse: ...
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
    async def stage(self, **params: Unpack[SofascoreStageStreamParams]) -> BinaryIO: ...
    @overload
    async def stage(self, **params: Unpack[SofascoreStageTextResponseParams]) -> str: ...
    @overload
    async def stage(self, **params: Unpack[SofascoreStageDefaultParams]) -> SofascoreStageResponse: ...
    @overload
    async def stage_categories(self, **params: Unpack[SofascoreStageCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_categories(self, **params: Unpack[SofascoreStageCategoriesTextResponseParams]) -> str: ...
    @overload
    async def stage_categories(self, **params: Unpack[SofascoreStageCategoriesDefaultParams]) -> SofascoreStageCategoriesResponse: ...
    @overload
    async def stage_driver_performance(self, **params: Unpack[SofascoreStageDriverPerformanceStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_driver_performance(self, **params: Unpack[SofascoreStageDriverPerformanceTextResponseParams]) -> str: ...
    @overload
    async def stage_driver_performance(self, **params: Unpack[SofascoreStageDriverPerformanceDefaultParams]) -> SofascoreStageDriverPerformanceResponse: ...
    @overload
    async def stage_featured(self, **params: Unpack[SofascoreStageFeaturedStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_featured(self, **params: Unpack[SofascoreStageFeaturedTextResponseParams]) -> str: ...
    @overload
    async def stage_featured(self, **params: Unpack[SofascoreStageFeaturedDefaultParams]) -> SofascoreStageFeaturedResponse: ...
    @overload
    async def stage_schedule(self, **params: Unpack[SofascoreStageScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_schedule(self, **params: Unpack[SofascoreStageScheduleTextResponseParams]) -> str: ...
    @overload
    async def stage_schedule(self, **params: Unpack[SofascoreStageScheduleDefaultParams]) -> SofascoreStageScheduleResponse: ...
    @overload
    async def stage_seasons(self, **params: Unpack[SofascoreStageSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_seasons(self, **params: Unpack[SofascoreStageSeasonsTextResponseParams]) -> str: ...
    @overload
    async def stage_seasons(self, **params: Unpack[SofascoreStageSeasonsDefaultParams]) -> SofascoreStageSeasonsResponse: ...
    @overload
    async def stage_standings(self, **params: Unpack[SofascoreStageStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_standings(self, **params: Unpack[SofascoreStageStandingsTextResponseParams]) -> str: ...
    @overload
    async def stage_standings(self, **params: Unpack[SofascoreStageStandingsDefaultParams]) -> SofascoreStageStandingsResponse: ...
    @overload
    async def stage_substages(self, **params: Unpack[SofascoreStageSubstagesStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_substages(self, **params: Unpack[SofascoreStageSubstagesTextResponseParams]) -> str: ...
    @overload
    async def stage_substages(self, **params: Unpack[SofascoreStageSubstagesDefaultParams]) -> SofascoreStageSubstagesResponse: ...
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
    async def team_achievements(self, **params: Unpack[SofascoreTeamAchievementsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_achievements(self, **params: Unpack[SofascoreTeamAchievementsTextResponseParams]) -> str: ...
    @overload
    async def team_achievements(self, **params: Unpack[SofascoreTeamAchievementsDefaultParams]) -> SofascoreTeamAchievementsResponse: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsTextResponseParams]) -> str: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsDefaultParams]) -> SofascoreTeamEventsResponse: ...
    @overload
    async def team_goal_distributions(self, **params: Unpack[SofascoreTeamGoalDistributionsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_goal_distributions(self, **params: Unpack[SofascoreTeamGoalDistributionsTextResponseParams]) -> str: ...
    @overload
    async def team_goal_distributions(self, **params: Unpack[SofascoreTeamGoalDistributionsDefaultParams]) -> SofascoreTeamGoalDistributionsResponse: ...
    @overload
    async def team_near_events(self, **params: Unpack[SofascoreTeamNearEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_near_events(self, **params: Unpack[SofascoreTeamNearEventsTextResponseParams]) -> str: ...
    @overload
    async def team_near_events(self, **params: Unpack[SofascoreTeamNearEventsDefaultParams]) -> SofascoreTeamNearEventsResponse: ...
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
    async def team_performance(self, **params: Unpack[SofascoreTeamPerformanceStreamParams]) -> BinaryIO: ...
    @overload
    async def team_performance(self, **params: Unpack[SofascoreTeamPerformanceTextResponseParams]) -> str: ...
    @overload
    async def team_performance(self, **params: Unpack[SofascoreTeamPerformanceDefaultParams]) -> SofascoreTeamPerformanceResponse: ...
    @overload
    async def team_player_statistics(self, **params: Unpack[SofascoreTeamPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_player_statistics(self, **params: Unpack[SofascoreTeamPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    async def team_player_statistics(self, **params: Unpack[SofascoreTeamPlayerStatisticsDefaultParams]) -> SofascoreTeamPlayerStatisticsResponse: ...
    @overload
    async def team_player_statistics_seasons(self, **params: Unpack[SofascoreTeamPlayerStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_player_statistics_seasons(self, **params: Unpack[SofascoreTeamPlayerStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    async def team_player_statistics_seasons(self, **params: Unpack[SofascoreTeamPlayerStatisticsSeasonsDefaultParams]) -> SofascoreTeamPlayerStatisticsSeasonsResponse: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersTextResponseParams]) -> str: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersDefaultParams]) -> SofascoreTeamPlayersResponse: ...
    @overload
    async def team_rankings(self, **params: Unpack[SofascoreTeamRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_rankings(self, **params: Unpack[SofascoreTeamRankingsTextResponseParams]) -> str: ...
    @overload
    async def team_rankings(self, **params: Unpack[SofascoreTeamRankingsDefaultParams]) -> SofascoreTeamRankingsResponse: ...
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
    async def team_top_players(self, **params: Unpack[SofascoreTeamTopPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_top_players(self, **params: Unpack[SofascoreTeamTopPlayersTextResponseParams]) -> str: ...
    @overload
    async def team_top_players(self, **params: Unpack[SofascoreTeamTopPlayersDefaultParams]) -> SofascoreTeamTopPlayersResponse: ...
    @overload
    async def team_tournaments(self, **params: Unpack[SofascoreTeamTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_tournaments(self, **params: Unpack[SofascoreTeamTournamentsTextResponseParams]) -> str: ...
    @overload
    async def team_tournaments(self, **params: Unpack[SofascoreTeamTournamentsDefaultParams]) -> SofascoreTeamTournamentsResponse: ...
    @overload
    async def team_transfers(self, **params: Unpack[SofascoreTeamTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_transfers(self, **params: Unpack[SofascoreTeamTransfersTextResponseParams]) -> str: ...
    @overload
    async def team_transfers(self, **params: Unpack[SofascoreTeamTransfersDefaultParams]) -> SofascoreTeamTransfersResponse: ...
    @overload
    async def tennis_player_grand_slam_results(self, **params: Unpack[SofascoreTennisPlayerGrandSlamResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def tennis_player_grand_slam_results(self, **params: Unpack[SofascoreTennisPlayerGrandSlamResultsTextResponseParams]) -> str: ...
    @overload
    async def tennis_player_grand_slam_results(self, **params: Unpack[SofascoreTennisPlayerGrandSlamResultsDefaultParams]) -> SofascoreTennisPlayerGrandSlamResultsResponse: ...
    @overload
    async def tournament_cuptree(self, **params: Unpack[SofascoreTournamentCuptreeStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_cuptree(self, **params: Unpack[SofascoreTournamentCuptreeTextResponseParams]) -> str: ...
    @overload
    async def tournament_cuptree(self, **params: Unpack[SofascoreTournamentCuptreeDefaultParams]) -> SofascoreTournamentCuptreeResponse: ...
    @overload
    async def tournament_info(self, **params: Unpack[SofascoreTournamentInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_info(self, **params: Unpack[SofascoreTournamentInfoTextResponseParams]) -> str: ...
    @overload
    async def tournament_info(self, **params: Unpack[SofascoreTournamentInfoDefaultParams]) -> SofascoreTournamentInfoResponse: ...
    @overload
    async def tournament_player_of_the_season(self, **params: Unpack[SofascoreTournamentPlayerOfTheSeasonStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_player_of_the_season(self, **params: Unpack[SofascoreTournamentPlayerOfTheSeasonTextResponseParams]) -> str: ...
    @overload
    async def tournament_player_of_the_season(self, **params: Unpack[SofascoreTournamentPlayerOfTheSeasonDefaultParams]) -> SofascoreTournamentPlayerOfTheSeasonResponse: ...
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
    async def tournament_statistics_info(self, **params: Unpack[SofascoreTournamentStatisticsInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_statistics_info(self, **params: Unpack[SofascoreTournamentStatisticsInfoTextResponseParams]) -> str: ...
    @overload
    async def tournament_statistics_info(self, **params: Unpack[SofascoreTournamentStatisticsInfoDefaultParams]) -> SofascoreTournamentStatisticsInfoResponse: ...
    @overload
    async def tournament_team_of_the_season(self, **params: Unpack[SofascoreTournamentTeamOfTheSeasonStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_team_of_the_season(self, **params: Unpack[SofascoreTournamentTeamOfTheSeasonTextResponseParams]) -> str: ...
    @overload
    async def tournament_team_of_the_season(self, **params: Unpack[SofascoreTournamentTeamOfTheSeasonDefaultParams]) -> SofascoreTournamentTeamOfTheSeasonResponse: ...
    @overload
    async def tournament_teams(self, **params: Unpack[SofascoreTournamentTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_teams(self, **params: Unpack[SofascoreTournamentTeamsTextResponseParams]) -> str: ...
    @overload
    async def tournament_teams(self, **params: Unpack[SofascoreTournamentTeamsDefaultParams]) -> SofascoreTournamentTeamsResponse: ...
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
    @overload
    async def tournament_venues(self, **params: Unpack[SofascoreTournamentVenuesStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_venues(self, **params: Unpack[SofascoreTournamentVenuesTextResponseParams]) -> str: ...
    @overload
    async def tournament_venues(self, **params: Unpack[SofascoreTournamentVenuesDefaultParams]) -> SofascoreTournamentVenuesResponse: ...
    @overload
    async def tournament_winners(self, **params: Unpack[SofascoreTournamentWinnersStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_winners(self, **params: Unpack[SofascoreTournamentWinnersTextResponseParams]) -> str: ...
    @overload
    async def tournament_winners(self, **params: Unpack[SofascoreTournamentWinnersDefaultParams]) -> SofascoreTournamentWinnersResponse: ...
    @overload
    async def tournaments_with_feature(self, **params: Unpack[SofascoreTournamentsWithFeatureStreamParams]) -> BinaryIO: ...
    @overload
    async def tournaments_with_feature(self, **params: Unpack[SofascoreTournamentsWithFeatureTextResponseParams]) -> str: ...
    @overload
    async def tournaments_with_feature(self, **params: Unpack[SofascoreTournamentsWithFeatureDefaultParams]) -> SofascoreTournamentsWithFeatureResponse: ...
    @overload
    async def trending_events(self, **params: Unpack[SofascoreTrendingEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_events(self, **params: Unpack[SofascoreTrendingEventsTextResponseParams]) -> str: ...
    @overload
    async def trending_events(self, **params: Unpack[SofascoreTrendingEventsDefaultParams]) -> SofascoreTrendingEventsResponse: ...
    @overload
    async def trending_players(self, **params: Unpack[SofascoreTrendingPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_players(self, **params: Unpack[SofascoreTrendingPlayersTextResponseParams]) -> str: ...
    @overload
    async def trending_players(self, **params: Unpack[SofascoreTrendingPlayersDefaultParams]) -> SofascoreTrendingPlayersResponse: ...
    @overload
    async def venue(self, **params: Unpack[SofascoreVenueStreamParams]) -> BinaryIO: ...
    @overload
    async def venue(self, **params: Unpack[SofascoreVenueTextResponseParams]) -> str: ...
    @overload
    async def venue(self, **params: Unpack[SofascoreVenueDefaultParams]) -> SofascoreVenueResponse: ...
    @overload
    async def venue_events(self, **params: Unpack[SofascoreVenueEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def venue_events(self, **params: Unpack[SofascoreVenueEventsTextResponseParams]) -> str: ...
    @overload
    async def venue_events(self, **params: Unpack[SofascoreVenueEventsDefaultParams]) -> SofascoreVenueEventsResponse: ...

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
    async def draft(self, **params: Unpack[SofascoreDraftStreamParams]) -> BinaryIO: ...
    @overload
    async def draft(self, **params: Unpack[SofascoreDraftTextResponseParams]) -> str: ...
    @overload
    async def draft(self, **params: Unpack[SofascoreDraftDefaultParams]) -> SofascoreDraftResponse: ...
    @overload
    async def draft_picks(self, **params: Unpack[SofascoreDraftPicksStreamParams]) -> BinaryIO: ...
    @overload
    async def draft_picks(self, **params: Unpack[SofascoreDraftPicksTextResponseParams]) -> str: ...
    @overload
    async def draft_picks(self, **params: Unpack[SofascoreDraftPicksDefaultParams]) -> SofascoreDraftPicksResponse: ...
    @overload
    async def esports_game(self, **params: Unpack[SofascoreEsportsGameStreamParams]) -> BinaryIO: ...
    @overload
    async def esports_game(self, **params: Unpack[SofascoreEsportsGameTextResponseParams]) -> str: ...
    @overload
    async def esports_game(self, **params: Unpack[SofascoreEsportsGameDefaultParams]) -> SofascoreEsportsGameResponse: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventStreamParams]) -> BinaryIO: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventTextResponseParams]) -> str: ...
    @overload
    async def event(self, **params: Unpack[SofascoreEventDefaultParams]) -> SofascoreEventResponse: ...
    @overload
    async def event_at_bat_pitches(self, **params: Unpack[SofascoreEventAtBatPitchesStreamParams]) -> BinaryIO: ...
    @overload
    async def event_at_bat_pitches(self, **params: Unpack[SofascoreEventAtBatPitchesTextResponseParams]) -> str: ...
    @overload
    async def event_at_bat_pitches(self, **params: Unpack[SofascoreEventAtBatPitchesDefaultParams]) -> SofascoreEventAtBatPitchesResponse: ...
    @overload
    async def event_at_bats(self, **params: Unpack[SofascoreEventAtBatsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_at_bats(self, **params: Unpack[SofascoreEventAtBatsTextResponseParams]) -> str: ...
    @overload
    async def event_at_bats(self, **params: Unpack[SofascoreEventAtBatsDefaultParams]) -> SofascoreEventAtBatsResponse: ...
    @overload
    async def event_average_positions(self, **params: Unpack[SofascoreEventAveragePositionsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_average_positions(self, **params: Unpack[SofascoreEventAveragePositionsTextResponseParams]) -> str: ...
    @overload
    async def event_average_positions(self, **params: Unpack[SofascoreEventAveragePositionsDefaultParams]) -> SofascoreEventAveragePositionsResponse: ...
    @overload
    async def event_baseball_top_performers(self, **params: Unpack[SofascoreEventBaseballTopPerformersStreamParams]) -> BinaryIO: ...
    @overload
    async def event_baseball_top_performers(self, **params: Unpack[SofascoreEventBaseballTopPerformersTextResponseParams]) -> str: ...
    @overload
    async def event_baseball_top_performers(self, **params: Unpack[SofascoreEventBaseballTopPerformersDefaultParams]) -> SofascoreEventBaseballTopPerformersResponse: ...
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
    async def event_esports_games(self, **params: Unpack[SofascoreEventEsportsGamesStreamParams]) -> BinaryIO: ...
    @overload
    async def event_esports_games(self, **params: Unpack[SofascoreEventEsportsGamesTextResponseParams]) -> str: ...
    @overload
    async def event_esports_games(self, **params: Unpack[SofascoreEventEsportsGamesDefaultParams]) -> SofascoreEventEsportsGamesResponse: ...
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
    async def event_highlights(self, **params: Unpack[SofascoreEventHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_highlights(self, **params: Unpack[SofascoreEventHighlightsTextResponseParams]) -> str: ...
    @overload
    async def event_highlights(self, **params: Unpack[SofascoreEventHighlightsDefaultParams]) -> SofascoreEventHighlightsResponse: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsTextResponseParams]) -> str: ...
    @overload
    async def event_incidents(self, **params: Unpack[SofascoreEventIncidentsDefaultParams]) -> SofascoreEventIncidentsResponse: ...
    @overload
    async def event_innings(self, **params: Unpack[SofascoreEventInningsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_innings(self, **params: Unpack[SofascoreEventInningsTextResponseParams]) -> str: ...
    @overload
    async def event_innings(self, **params: Unpack[SofascoreEventInningsDefaultParams]) -> SofascoreEventInningsResponse: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsTextResponseParams]) -> str: ...
    @overload
    async def event_lineups(self, **params: Unpack[SofascoreEventLineupsDefaultParams]) -> SofascoreEventLineupsResponse: ...
    @overload
    async def event_managers(self, **params: Unpack[SofascoreEventManagersStreamParams]) -> BinaryIO: ...
    @overload
    async def event_managers(self, **params: Unpack[SofascoreEventManagersTextResponseParams]) -> str: ...
    @overload
    async def event_managers(self, **params: Unpack[SofascoreEventManagersDefaultParams]) -> SofascoreEventManagersResponse: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsTextResponseParams]) -> str: ...
    @overload
    async def event_odds(self, **params: Unpack[SofascoreEventOddsDefaultParams]) -> SofascoreEventOddsResponse: ...
    @overload
    async def event_player_heatmap(self, **params: Unpack[SofascoreEventPlayerHeatmapStreamParams]) -> BinaryIO: ...
    @overload
    async def event_player_heatmap(self, **params: Unpack[SofascoreEventPlayerHeatmapTextResponseParams]) -> str: ...
    @overload
    async def event_player_heatmap(self, **params: Unpack[SofascoreEventPlayerHeatmapDefaultParams]) -> SofascoreEventPlayerHeatmapResponse: ...
    @overload
    async def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    async def event_player_statistics(self, **params: Unpack[SofascoreEventPlayerStatisticsDefaultParams]) -> SofascoreEventPlayerStatisticsResponse: ...
    @overload
    async def event_point_by_point(self, **params: Unpack[SofascoreEventPointByPointStreamParams]) -> BinaryIO: ...
    @overload
    async def event_point_by_point(self, **params: Unpack[SofascoreEventPointByPointTextResponseParams]) -> str: ...
    @overload
    async def event_point_by_point(self, **params: Unpack[SofascoreEventPointByPointDefaultParams]) -> SofascoreEventPointByPointResponse: ...
    @overload
    async def event_pregame_form(self, **params: Unpack[SofascoreEventPregameFormStreamParams]) -> BinaryIO: ...
    @overload
    async def event_pregame_form(self, **params: Unpack[SofascoreEventPregameFormTextResponseParams]) -> str: ...
    @overload
    async def event_pregame_form(self, **params: Unpack[SofascoreEventPregameFormDefaultParams]) -> SofascoreEventPregameFormResponse: ...
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
    async def event_team_heatmap(self, **params: Unpack[SofascoreEventTeamHeatmapStreamParams]) -> BinaryIO: ...
    @overload
    async def event_team_heatmap(self, **params: Unpack[SofascoreEventTeamHeatmapTextResponseParams]) -> str: ...
    @overload
    async def event_team_heatmap(self, **params: Unpack[SofascoreEventTeamHeatmapDefaultParams]) -> SofascoreEventTeamHeatmapResponse: ...
    @overload
    async def event_team_streaks(self, **params: Unpack[SofascoreEventTeamStreaksStreamParams]) -> BinaryIO: ...
    @overload
    async def event_team_streaks(self, **params: Unpack[SofascoreEventTeamStreaksTextResponseParams]) -> str: ...
    @overload
    async def event_team_streaks(self, **params: Unpack[SofascoreEventTeamStreaksDefaultParams]) -> SofascoreEventTeamStreaksResponse: ...
    @overload
    async def event_tennis_power(self, **params: Unpack[SofascoreEventTennisPowerStreamParams]) -> BinaryIO: ...
    @overload
    async def event_tennis_power(self, **params: Unpack[SofascoreEventTennisPowerTextResponseParams]) -> str: ...
    @overload
    async def event_tennis_power(self, **params: Unpack[SofascoreEventTennisPowerDefaultParams]) -> SofascoreEventTennisPowerResponse: ...
    @overload
    async def event_tv_channels(self, **params: Unpack[SofascoreEventTvChannelsStreamParams]) -> BinaryIO: ...
    @overload
    async def event_tv_channels(self, **params: Unpack[SofascoreEventTvChannelsTextResponseParams]) -> str: ...
    @overload
    async def event_tv_channels(self, **params: Unpack[SofascoreEventTvChannelsDefaultParams]) -> SofascoreEventTvChannelsResponse: ...
    @overload
    async def event_votes(self, **params: Unpack[SofascoreEventVotesStreamParams]) -> BinaryIO: ...
    @overload
    async def event_votes(self, **params: Unpack[SofascoreEventVotesTextResponseParams]) -> str: ...
    @overload
    async def event_votes(self, **params: Unpack[SofascoreEventVotesDefaultParams]) -> SofascoreEventVotesResponse: ...
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
    async def mma_card(self, **params: Unpack[SofascoreMmaCardStreamParams]) -> BinaryIO: ...
    @overload
    async def mma_card(self, **params: Unpack[SofascoreMmaCardTextResponseParams]) -> str: ...
    @overload
    async def mma_card(self, **params: Unpack[SofascoreMmaCardDefaultParams]) -> SofascoreMmaCardResponse: ...
    @overload
    async def mma_schedule(self, **params: Unpack[SofascoreMmaScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def mma_schedule(self, **params: Unpack[SofascoreMmaScheduleTextResponseParams]) -> str: ...
    @overload
    async def mma_schedule(self, **params: Unpack[SofascoreMmaScheduleDefaultParams]) -> SofascoreMmaScheduleResponse: ...
    @overload
    async def odds_dropping(self, **params: Unpack[SofascoreOddsDroppingStreamParams]) -> BinaryIO: ...
    @overload
    async def odds_dropping(self, **params: Unpack[SofascoreOddsDroppingTextResponseParams]) -> str: ...
    @overload
    async def odds_dropping(self, **params: Unpack[SofascoreOddsDroppingDefaultParams]) -> SofascoreOddsDroppingResponse: ...
    @overload
    async def odds_winning(self, **params: Unpack[SofascoreOddsWinningStreamParams]) -> BinaryIO: ...
    @overload
    async def odds_winning(self, **params: Unpack[SofascoreOddsWinningTextResponseParams]) -> str: ...
    @overload
    async def odds_winning(self, **params: Unpack[SofascoreOddsWinningDefaultParams]) -> SofascoreOddsWinningResponse: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[SofascorePlayerDefaultParams]) -> SofascorePlayerResponse: ...
    @overload
    async def player_attributes(self, **params: Unpack[SofascorePlayerAttributesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_attributes(self, **params: Unpack[SofascorePlayerAttributesTextResponseParams]) -> str: ...
    @overload
    async def player_attributes(self, **params: Unpack[SofascorePlayerAttributesDefaultParams]) -> SofascorePlayerAttributesResponse: ...
    @overload
    async def player_events(self, **params: Unpack[SofascorePlayerEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_events(self, **params: Unpack[SofascorePlayerEventsTextResponseParams]) -> str: ...
    @overload
    async def player_events(self, **params: Unpack[SofascorePlayerEventsDefaultParams]) -> SofascorePlayerEventsResponse: ...
    @overload
    async def player_last_year_summary(self, **params: Unpack[SofascorePlayerLastYearSummaryStreamParams]) -> BinaryIO: ...
    @overload
    async def player_last_year_summary(self, **params: Unpack[SofascorePlayerLastYearSummaryTextResponseParams]) -> str: ...
    @overload
    async def player_last_year_summary(self, **params: Unpack[SofascorePlayerLastYearSummaryDefaultParams]) -> SofascorePlayerLastYearSummaryResponse: ...
    @overload
    async def player_national_team_statistics(self, **params: Unpack[SofascorePlayerNationalTeamStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_national_team_statistics(self, **params: Unpack[SofascorePlayerNationalTeamStatisticsTextResponseParams]) -> str: ...
    @overload
    async def player_national_team_statistics(self, **params: Unpack[SofascorePlayerNationalTeamStatisticsDefaultParams]) -> SofascorePlayerNationalTeamStatisticsResponse: ...
    @overload
    async def player_penalty_history(self, **params: Unpack[SofascorePlayerPenaltyHistoryStreamParams]) -> BinaryIO: ...
    @overload
    async def player_penalty_history(self, **params: Unpack[SofascorePlayerPenaltyHistoryTextResponseParams]) -> str: ...
    @overload
    async def player_penalty_history(self, **params: Unpack[SofascorePlayerPenaltyHistoryDefaultParams]) -> SofascorePlayerPenaltyHistoryResponse: ...
    @overload
    async def player_ratings(self, **params: Unpack[SofascorePlayerRatingsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_ratings(self, **params: Unpack[SofascorePlayerRatingsTextResponseParams]) -> str: ...
    @overload
    async def player_ratings(self, **params: Unpack[SofascorePlayerRatingsDefaultParams]) -> SofascorePlayerRatingsResponse: ...
    @overload
    async def player_season_heatmap(self, **params: Unpack[SofascorePlayerSeasonHeatmapStreamParams]) -> BinaryIO: ...
    @overload
    async def player_season_heatmap(self, **params: Unpack[SofascorePlayerSeasonHeatmapTextResponseParams]) -> str: ...
    @overload
    async def player_season_heatmap(self, **params: Unpack[SofascorePlayerSeasonHeatmapDefaultParams]) -> SofascorePlayerSeasonHeatmapResponse: ...
    @overload
    async def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsTextResponseParams]) -> str: ...
    @overload
    async def player_season_statistics(self, **params: Unpack[SofascorePlayerSeasonStatisticsDefaultParams]) -> SofascorePlayerSeasonStatisticsResponse: ...
    @overload
    async def player_statistical_rankings(self, **params: Unpack[SofascorePlayerStatisticalRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_statistical_rankings(self, **params: Unpack[SofascorePlayerStatisticalRankingsTextResponseParams]) -> str: ...
    @overload
    async def player_statistical_rankings(self, **params: Unpack[SofascorePlayerStatisticalRankingsDefaultParams]) -> SofascorePlayerStatisticalRankingsResponse: ...
    @overload
    async def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    async def player_statistics_seasons(self, **params: Unpack[SofascorePlayerStatisticsSeasonsDefaultParams]) -> SofascorePlayerStatisticsSeasonsResponse: ...
    @overload
    async def player_tournaments(self, **params: Unpack[SofascorePlayerTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_tournaments(self, **params: Unpack[SofascorePlayerTournamentsTextResponseParams]) -> str: ...
    @overload
    async def player_tournaments(self, **params: Unpack[SofascorePlayerTournamentsDefaultParams]) -> SofascorePlayerTournamentsResponse: ...
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
    async def referee(self, **params: Unpack[SofascoreRefereeStreamParams]) -> BinaryIO: ...
    @overload
    async def referee(self, **params: Unpack[SofascoreRefereeTextResponseParams]) -> str: ...
    @overload
    async def referee(self, **params: Unpack[SofascoreRefereeDefaultParams]) -> SofascoreRefereeResponse: ...
    @overload
    async def referee_events(self, **params: Unpack[SofascoreRefereeEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def referee_events(self, **params: Unpack[SofascoreRefereeEventsTextResponseParams]) -> str: ...
    @overload
    async def referee_events(self, **params: Unpack[SofascoreRefereeEventsDefaultParams]) -> SofascoreRefereeEventsResponse: ...
    @overload
    async def referee_statistics(self, **params: Unpack[SofascoreRefereeStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def referee_statistics(self, **params: Unpack[SofascoreRefereeStatisticsTextResponseParams]) -> str: ...
    @overload
    async def referee_statistics(self, **params: Unpack[SofascoreRefereeStatisticsDefaultParams]) -> SofascoreRefereeStatisticsResponse: ...
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
    async def search_typed(self, **params: Unpack[SofascoreSearchTypedStreamParams]) -> BinaryIO: ...
    @overload
    async def search_typed(self, **params: Unpack[SofascoreSearchTypedTextResponseParams]) -> str: ...
    @overload
    async def search_typed(self, **params: Unpack[SofascoreSearchTypedDefaultParams]) -> SofascoreSearchTypedResponse: ...
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
    async def stage(self, **params: Unpack[SofascoreStageStreamParams]) -> BinaryIO: ...
    @overload
    async def stage(self, **params: Unpack[SofascoreStageTextResponseParams]) -> str: ...
    @overload
    async def stage(self, **params: Unpack[SofascoreStageDefaultParams]) -> SofascoreStageResponse: ...
    @overload
    async def stage_categories(self, **params: Unpack[SofascoreStageCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_categories(self, **params: Unpack[SofascoreStageCategoriesTextResponseParams]) -> str: ...
    @overload
    async def stage_categories(self, **params: Unpack[SofascoreStageCategoriesDefaultParams]) -> SofascoreStageCategoriesResponse: ...
    @overload
    async def stage_driver_performance(self, **params: Unpack[SofascoreStageDriverPerformanceStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_driver_performance(self, **params: Unpack[SofascoreStageDriverPerformanceTextResponseParams]) -> str: ...
    @overload
    async def stage_driver_performance(self, **params: Unpack[SofascoreStageDriverPerformanceDefaultParams]) -> SofascoreStageDriverPerformanceResponse: ...
    @overload
    async def stage_featured(self, **params: Unpack[SofascoreStageFeaturedStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_featured(self, **params: Unpack[SofascoreStageFeaturedTextResponseParams]) -> str: ...
    @overload
    async def stage_featured(self, **params: Unpack[SofascoreStageFeaturedDefaultParams]) -> SofascoreStageFeaturedResponse: ...
    @overload
    async def stage_schedule(self, **params: Unpack[SofascoreStageScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_schedule(self, **params: Unpack[SofascoreStageScheduleTextResponseParams]) -> str: ...
    @overload
    async def stage_schedule(self, **params: Unpack[SofascoreStageScheduleDefaultParams]) -> SofascoreStageScheduleResponse: ...
    @overload
    async def stage_seasons(self, **params: Unpack[SofascoreStageSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_seasons(self, **params: Unpack[SofascoreStageSeasonsTextResponseParams]) -> str: ...
    @overload
    async def stage_seasons(self, **params: Unpack[SofascoreStageSeasonsDefaultParams]) -> SofascoreStageSeasonsResponse: ...
    @overload
    async def stage_standings(self, **params: Unpack[SofascoreStageStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_standings(self, **params: Unpack[SofascoreStageStandingsTextResponseParams]) -> str: ...
    @overload
    async def stage_standings(self, **params: Unpack[SofascoreStageStandingsDefaultParams]) -> SofascoreStageStandingsResponse: ...
    @overload
    async def stage_substages(self, **params: Unpack[SofascoreStageSubstagesStreamParams]) -> BinaryIO: ...
    @overload
    async def stage_substages(self, **params: Unpack[SofascoreStageSubstagesTextResponseParams]) -> str: ...
    @overload
    async def stage_substages(self, **params: Unpack[SofascoreStageSubstagesDefaultParams]) -> SofascoreStageSubstagesResponse: ...
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
    async def team_achievements(self, **params: Unpack[SofascoreTeamAchievementsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_achievements(self, **params: Unpack[SofascoreTeamAchievementsTextResponseParams]) -> str: ...
    @overload
    async def team_achievements(self, **params: Unpack[SofascoreTeamAchievementsDefaultParams]) -> SofascoreTeamAchievementsResponse: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsTextResponseParams]) -> str: ...
    @overload
    async def team_events(self, **params: Unpack[SofascoreTeamEventsDefaultParams]) -> SofascoreTeamEventsResponse: ...
    @overload
    async def team_goal_distributions(self, **params: Unpack[SofascoreTeamGoalDistributionsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_goal_distributions(self, **params: Unpack[SofascoreTeamGoalDistributionsTextResponseParams]) -> str: ...
    @overload
    async def team_goal_distributions(self, **params: Unpack[SofascoreTeamGoalDistributionsDefaultParams]) -> SofascoreTeamGoalDistributionsResponse: ...
    @overload
    async def team_near_events(self, **params: Unpack[SofascoreTeamNearEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_near_events(self, **params: Unpack[SofascoreTeamNearEventsTextResponseParams]) -> str: ...
    @overload
    async def team_near_events(self, **params: Unpack[SofascoreTeamNearEventsDefaultParams]) -> SofascoreTeamNearEventsResponse: ...
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
    async def team_performance(self, **params: Unpack[SofascoreTeamPerformanceStreamParams]) -> BinaryIO: ...
    @overload
    async def team_performance(self, **params: Unpack[SofascoreTeamPerformanceTextResponseParams]) -> str: ...
    @overload
    async def team_performance(self, **params: Unpack[SofascoreTeamPerformanceDefaultParams]) -> SofascoreTeamPerformanceResponse: ...
    @overload
    async def team_player_statistics(self, **params: Unpack[SofascoreTeamPlayerStatisticsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_player_statistics(self, **params: Unpack[SofascoreTeamPlayerStatisticsTextResponseParams]) -> str: ...
    @overload
    async def team_player_statistics(self, **params: Unpack[SofascoreTeamPlayerStatisticsDefaultParams]) -> SofascoreTeamPlayerStatisticsResponse: ...
    @overload
    async def team_player_statistics_seasons(self, **params: Unpack[SofascoreTeamPlayerStatisticsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_player_statistics_seasons(self, **params: Unpack[SofascoreTeamPlayerStatisticsSeasonsTextResponseParams]) -> str: ...
    @overload
    async def team_player_statistics_seasons(self, **params: Unpack[SofascoreTeamPlayerStatisticsSeasonsDefaultParams]) -> SofascoreTeamPlayerStatisticsSeasonsResponse: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersTextResponseParams]) -> str: ...
    @overload
    async def team_players(self, **params: Unpack[SofascoreTeamPlayersDefaultParams]) -> SofascoreTeamPlayersResponse: ...
    @overload
    async def team_rankings(self, **params: Unpack[SofascoreTeamRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_rankings(self, **params: Unpack[SofascoreTeamRankingsTextResponseParams]) -> str: ...
    @overload
    async def team_rankings(self, **params: Unpack[SofascoreTeamRankingsDefaultParams]) -> SofascoreTeamRankingsResponse: ...
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
    async def team_top_players(self, **params: Unpack[SofascoreTeamTopPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_top_players(self, **params: Unpack[SofascoreTeamTopPlayersTextResponseParams]) -> str: ...
    @overload
    async def team_top_players(self, **params: Unpack[SofascoreTeamTopPlayersDefaultParams]) -> SofascoreTeamTopPlayersResponse: ...
    @overload
    async def team_tournaments(self, **params: Unpack[SofascoreTeamTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_tournaments(self, **params: Unpack[SofascoreTeamTournamentsTextResponseParams]) -> str: ...
    @overload
    async def team_tournaments(self, **params: Unpack[SofascoreTeamTournamentsDefaultParams]) -> SofascoreTeamTournamentsResponse: ...
    @overload
    async def team_transfers(self, **params: Unpack[SofascoreTeamTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_transfers(self, **params: Unpack[SofascoreTeamTransfersTextResponseParams]) -> str: ...
    @overload
    async def team_transfers(self, **params: Unpack[SofascoreTeamTransfersDefaultParams]) -> SofascoreTeamTransfersResponse: ...
    @overload
    async def tennis_player_grand_slam_results(self, **params: Unpack[SofascoreTennisPlayerGrandSlamResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def tennis_player_grand_slam_results(self, **params: Unpack[SofascoreTennisPlayerGrandSlamResultsTextResponseParams]) -> str: ...
    @overload
    async def tennis_player_grand_slam_results(self, **params: Unpack[SofascoreTennisPlayerGrandSlamResultsDefaultParams]) -> SofascoreTennisPlayerGrandSlamResultsResponse: ...
    @overload
    async def tournament_cuptree(self, **params: Unpack[SofascoreTournamentCuptreeStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_cuptree(self, **params: Unpack[SofascoreTournamentCuptreeTextResponseParams]) -> str: ...
    @overload
    async def tournament_cuptree(self, **params: Unpack[SofascoreTournamentCuptreeDefaultParams]) -> SofascoreTournamentCuptreeResponse: ...
    @overload
    async def tournament_info(self, **params: Unpack[SofascoreTournamentInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_info(self, **params: Unpack[SofascoreTournamentInfoTextResponseParams]) -> str: ...
    @overload
    async def tournament_info(self, **params: Unpack[SofascoreTournamentInfoDefaultParams]) -> SofascoreTournamentInfoResponse: ...
    @overload
    async def tournament_player_of_the_season(self, **params: Unpack[SofascoreTournamentPlayerOfTheSeasonStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_player_of_the_season(self, **params: Unpack[SofascoreTournamentPlayerOfTheSeasonTextResponseParams]) -> str: ...
    @overload
    async def tournament_player_of_the_season(self, **params: Unpack[SofascoreTournamentPlayerOfTheSeasonDefaultParams]) -> SofascoreTournamentPlayerOfTheSeasonResponse: ...
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
    async def tournament_statistics_info(self, **params: Unpack[SofascoreTournamentStatisticsInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_statistics_info(self, **params: Unpack[SofascoreTournamentStatisticsInfoTextResponseParams]) -> str: ...
    @overload
    async def tournament_statistics_info(self, **params: Unpack[SofascoreTournamentStatisticsInfoDefaultParams]) -> SofascoreTournamentStatisticsInfoResponse: ...
    @overload
    async def tournament_team_of_the_season(self, **params: Unpack[SofascoreTournamentTeamOfTheSeasonStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_team_of_the_season(self, **params: Unpack[SofascoreTournamentTeamOfTheSeasonTextResponseParams]) -> str: ...
    @overload
    async def tournament_team_of_the_season(self, **params: Unpack[SofascoreTournamentTeamOfTheSeasonDefaultParams]) -> SofascoreTournamentTeamOfTheSeasonResponse: ...
    @overload
    async def tournament_teams(self, **params: Unpack[SofascoreTournamentTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_teams(self, **params: Unpack[SofascoreTournamentTeamsTextResponseParams]) -> str: ...
    @overload
    async def tournament_teams(self, **params: Unpack[SofascoreTournamentTeamsDefaultParams]) -> SofascoreTournamentTeamsResponse: ...
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
    @overload
    async def tournament_venues(self, **params: Unpack[SofascoreTournamentVenuesStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_venues(self, **params: Unpack[SofascoreTournamentVenuesTextResponseParams]) -> str: ...
    @overload
    async def tournament_venues(self, **params: Unpack[SofascoreTournamentVenuesDefaultParams]) -> SofascoreTournamentVenuesResponse: ...
    @overload
    async def tournament_winners(self, **params: Unpack[SofascoreTournamentWinnersStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_winners(self, **params: Unpack[SofascoreTournamentWinnersTextResponseParams]) -> str: ...
    @overload
    async def tournament_winners(self, **params: Unpack[SofascoreTournamentWinnersDefaultParams]) -> SofascoreTournamentWinnersResponse: ...
    @overload
    async def tournaments_with_feature(self, **params: Unpack[SofascoreTournamentsWithFeatureStreamParams]) -> BinaryIO: ...
    @overload
    async def tournaments_with_feature(self, **params: Unpack[SofascoreTournamentsWithFeatureTextResponseParams]) -> str: ...
    @overload
    async def tournaments_with_feature(self, **params: Unpack[SofascoreTournamentsWithFeatureDefaultParams]) -> SofascoreTournamentsWithFeatureResponse: ...
    @overload
    async def trending_events(self, **params: Unpack[SofascoreTrendingEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_events(self, **params: Unpack[SofascoreTrendingEventsTextResponseParams]) -> str: ...
    @overload
    async def trending_events(self, **params: Unpack[SofascoreTrendingEventsDefaultParams]) -> SofascoreTrendingEventsResponse: ...
    @overload
    async def trending_players(self, **params: Unpack[SofascoreTrendingPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def trending_players(self, **params: Unpack[SofascoreTrendingPlayersTextResponseParams]) -> str: ...
    @overload
    async def trending_players(self, **params: Unpack[SofascoreTrendingPlayersDefaultParams]) -> SofascoreTrendingPlayersResponse: ...
    @overload
    async def venue(self, **params: Unpack[SofascoreVenueStreamParams]) -> BinaryIO: ...
    @overload
    async def venue(self, **params: Unpack[SofascoreVenueTextResponseParams]) -> str: ...
    @overload
    async def venue(self, **params: Unpack[SofascoreVenueDefaultParams]) -> SofascoreVenueResponse: ...
    @overload
    async def venue_events(self, **params: Unpack[SofascoreVenueEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def venue_events(self, **params: Unpack[SofascoreVenueEventsTextResponseParams]) -> str: ...
    @overload
    async def venue_events(self, **params: Unpack[SofascoreVenueEventsDefaultParams]) -> SofascoreVenueEventsResponse: ...

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

SofascoreDraftDefaultParams = TypedDict('SofascoreDraftDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nba', 'nfl']],
    'season': Required[str],
}, total=False)

SofascoreDraftTextResponseParams = TypedDict('SofascoreDraftTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nba', 'nfl']],
    'season': Required[str],
}, total=False)

SofascoreDraftStreamParams = TypedDict('SofascoreDraftStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nba', 'nfl']],
    'season': Required[str],
}, total=False)

SofascoreDraftPicksDefaultParams = TypedDict('SofascoreDraftPicksDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'league': Required[Literal['nba', 'nfl']],
    'year': Required[str],
    'round': Required[int],
}, total=False)

SofascoreDraftPicksTextResponseParams = TypedDict('SofascoreDraftPicksTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'league': Required[Literal['nba', 'nfl']],
    'year': Required[str],
    'round': Required[int],
}, total=False)

SofascoreDraftPicksStreamParams = TypedDict('SofascoreDraftPicksStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'league': Required[Literal['nba', 'nfl']],
    'year': Required[str],
    'round': Required[int],
}, total=False)

SofascoreEsportsGameDefaultParams = TypedDict('SofascoreEsportsGameDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'part': Required[Literal['statistics', 'lineups', 'bans', 'rounds']],
}, total=False)

SofascoreEsportsGameTextResponseParams = TypedDict('SofascoreEsportsGameTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'part': Required[Literal['statistics', 'lineups', 'bans', 'rounds']],
}, total=False)

SofascoreEsportsGameStreamParams = TypedDict('SofascoreEsportsGameStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'part': Required[Literal['statistics', 'lineups', 'bans', 'rounds']],
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

SofascoreEventAtBatPitchesDefaultParams = TypedDict('SofascoreEventAtBatPitchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'at_bat_id': Required[str],
}, total=False)

SofascoreEventAtBatPitchesTextResponseParams = TypedDict('SofascoreEventAtBatPitchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'at_bat_id': Required[str],
}, total=False)

SofascoreEventAtBatPitchesStreamParams = TypedDict('SofascoreEventAtBatPitchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'at_bat_id': Required[str],
}, total=False)

SofascoreEventAtBatsDefaultParams = TypedDict('SofascoreEventAtBatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventAtBatsTextResponseParams = TypedDict('SofascoreEventAtBatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventAtBatsStreamParams = TypedDict('SofascoreEventAtBatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventAveragePositionsDefaultParams = TypedDict('SofascoreEventAveragePositionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventAveragePositionsTextResponseParams = TypedDict('SofascoreEventAveragePositionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventAveragePositionsStreamParams = TypedDict('SofascoreEventAveragePositionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventBaseballTopPerformersDefaultParams = TypedDict('SofascoreEventBaseballTopPerformersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventBaseballTopPerformersTextResponseParams = TypedDict('SofascoreEventBaseballTopPerformersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventBaseballTopPerformersStreamParams = TypedDict('SofascoreEventBaseballTopPerformersStreamParams', {
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

SofascoreEventEsportsGamesDefaultParams = TypedDict('SofascoreEventEsportsGamesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventEsportsGamesTextResponseParams = TypedDict('SofascoreEventEsportsGamesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventEsportsGamesStreamParams = TypedDict('SofascoreEventEsportsGamesStreamParams', {
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

SofascoreEventHighlightsDefaultParams = TypedDict('SofascoreEventHighlightsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventHighlightsTextResponseParams = TypedDict('SofascoreEventHighlightsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventHighlightsStreamParams = TypedDict('SofascoreEventHighlightsStreamParams', {
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

SofascoreEventInningsDefaultParams = TypedDict('SofascoreEventInningsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventInningsTextResponseParams = TypedDict('SofascoreEventInningsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventInningsStreamParams = TypedDict('SofascoreEventInningsStreamParams', {
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

SofascoreEventManagersDefaultParams = TypedDict('SofascoreEventManagersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventManagersTextResponseParams = TypedDict('SofascoreEventManagersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventManagersStreamParams = TypedDict('SofascoreEventManagersStreamParams', {
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

SofascoreEventPlayerHeatmapDefaultParams = TypedDict('SofascoreEventPlayerHeatmapDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'player_id': Required[str],
}, total=False)

SofascoreEventPlayerHeatmapTextResponseParams = TypedDict('SofascoreEventPlayerHeatmapTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'player_id': Required[str],
}, total=False)

SofascoreEventPlayerHeatmapStreamParams = TypedDict('SofascoreEventPlayerHeatmapStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'player_id': Required[str],
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

SofascoreEventPointByPointDefaultParams = TypedDict('SofascoreEventPointByPointDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventPointByPointTextResponseParams = TypedDict('SofascoreEventPointByPointTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventPointByPointStreamParams = TypedDict('SofascoreEventPointByPointStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventPregameFormDefaultParams = TypedDict('SofascoreEventPregameFormDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventPregameFormTextResponseParams = TypedDict('SofascoreEventPregameFormTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventPregameFormStreamParams = TypedDict('SofascoreEventPregameFormStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
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

SofascoreEventTeamHeatmapDefaultParams = TypedDict('SofascoreEventTeamHeatmapDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'team_id': Required[str],
}, total=False)

SofascoreEventTeamHeatmapTextResponseParams = TypedDict('SofascoreEventTeamHeatmapTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'team_id': Required[str],
}, total=False)

SofascoreEventTeamHeatmapStreamParams = TypedDict('SofascoreEventTeamHeatmapStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'team_id': Required[str],
}, total=False)

SofascoreEventTeamStreaksDefaultParams = TypedDict('SofascoreEventTeamStreaksDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventTeamStreaksTextResponseParams = TypedDict('SofascoreEventTeamStreaksTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventTeamStreaksStreamParams = TypedDict('SofascoreEventTeamStreaksStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventTennisPowerDefaultParams = TypedDict('SofascoreEventTennisPowerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventTennisPowerTextResponseParams = TypedDict('SofascoreEventTennisPowerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventTennisPowerStreamParams = TypedDict('SofascoreEventTennisPowerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreEventTvChannelsDefaultParams = TypedDict('SofascoreEventTvChannelsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'country': NotRequired[str],
}, total=False)

SofascoreEventTvChannelsTextResponseParams = TypedDict('SofascoreEventTvChannelsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'country': NotRequired[str],
}, total=False)

SofascoreEventTvChannelsStreamParams = TypedDict('SofascoreEventTvChannelsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'country': NotRequired[str],
}, total=False)

SofascoreEventVotesDefaultParams = TypedDict('SofascoreEventVotesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreEventVotesTextResponseParams = TypedDict('SofascoreEventVotesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreEventVotesStreamParams = TypedDict('SofascoreEventVotesStreamParams', {
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

SofascoreMmaCardDefaultParams = TypedDict('SofascoreMmaCardDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'org_id': Required[str],
    'card_id': Required[str],
    'part': Required[Literal['all', 'maincard', 'prelims', 'earlyprelims']],
}, total=False)

SofascoreMmaCardTextResponseParams = TypedDict('SofascoreMmaCardTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'org_id': Required[str],
    'card_id': Required[str],
    'part': Required[Literal['all', 'maincard', 'prelims', 'earlyprelims']],
}, total=False)

SofascoreMmaCardStreamParams = TypedDict('SofascoreMmaCardStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'org_id': Required[str],
    'card_id': Required[str],
    'part': Required[Literal['all', 'maincard', 'prelims', 'earlyprelims']],
}, total=False)

SofascoreMmaScheduleDefaultParams = TypedDict('SofascoreMmaScheduleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'org_id': Required[str],
    'month': Required[str],
}, total=False)

SofascoreMmaScheduleTextResponseParams = TypedDict('SofascoreMmaScheduleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'org_id': Required[str],
    'month': Required[str],
}, total=False)

SofascoreMmaScheduleStreamParams = TypedDict('SofascoreMmaScheduleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'org_id': Required[str],
    'month': Required[str],
}, total=False)

SofascoreOddsDroppingDefaultParams = TypedDict('SofascoreOddsDroppingDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': NotRequired[Literal['all', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreOddsDroppingTextResponseParams = TypedDict('SofascoreOddsDroppingTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': NotRequired[Literal['all', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreOddsDroppingStreamParams = TypedDict('SofascoreOddsDroppingStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': NotRequired[Literal['all', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreOddsWinningDefaultParams = TypedDict('SofascoreOddsWinningDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': NotRequired[Literal['all', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreOddsWinningTextResponseParams = TypedDict('SofascoreOddsWinningTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': NotRequired[Literal['all', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreOddsWinningStreamParams = TypedDict('SofascoreOddsWinningStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': NotRequired[Literal['all', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
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

SofascorePlayerAttributesDefaultParams = TypedDict('SofascorePlayerAttributesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascorePlayerAttributesTextResponseParams = TypedDict('SofascorePlayerAttributesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascorePlayerAttributesStreamParams = TypedDict('SofascorePlayerAttributesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascorePlayerEventsDefaultParams = TypedDict('SofascorePlayerEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascorePlayerEventsTextResponseParams = TypedDict('SofascorePlayerEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascorePlayerEventsStreamParams = TypedDict('SofascorePlayerEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascorePlayerLastYearSummaryDefaultParams = TypedDict('SofascorePlayerLastYearSummaryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascorePlayerLastYearSummaryTextResponseParams = TypedDict('SofascorePlayerLastYearSummaryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascorePlayerLastYearSummaryStreamParams = TypedDict('SofascorePlayerLastYearSummaryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascorePlayerNationalTeamStatisticsDefaultParams = TypedDict('SofascorePlayerNationalTeamStatisticsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascorePlayerNationalTeamStatisticsTextResponseParams = TypedDict('SofascorePlayerNationalTeamStatisticsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascorePlayerNationalTeamStatisticsStreamParams = TypedDict('SofascorePlayerNationalTeamStatisticsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascorePlayerPenaltyHistoryDefaultParams = TypedDict('SofascorePlayerPenaltyHistoryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascorePlayerPenaltyHistoryTextResponseParams = TypedDict('SofascorePlayerPenaltyHistoryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascorePlayerPenaltyHistoryStreamParams = TypedDict('SofascorePlayerPenaltyHistoryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascorePlayerRatingsDefaultParams = TypedDict('SofascorePlayerRatingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascorePlayerRatingsTextResponseParams = TypedDict('SofascorePlayerRatingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascorePlayerRatingsStreamParams = TypedDict('SofascorePlayerRatingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascorePlayerSeasonHeatmapDefaultParams = TypedDict('SofascorePlayerSeasonHeatmapDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
}, total=False)

SofascorePlayerSeasonHeatmapTextResponseParams = TypedDict('SofascorePlayerSeasonHeatmapTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
}, total=False)

SofascorePlayerSeasonHeatmapStreamParams = TypedDict('SofascorePlayerSeasonHeatmapStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
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

SofascorePlayerStatisticalRankingsDefaultParams = TypedDict('SofascorePlayerStatisticalRankingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall']],
}, total=False)

SofascorePlayerStatisticalRankingsTextResponseParams = TypedDict('SofascorePlayerStatisticalRankingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall']],
}, total=False)

SofascorePlayerStatisticalRankingsStreamParams = TypedDict('SofascorePlayerStatisticalRankingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall']],
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

SofascorePlayerTournamentsDefaultParams = TypedDict('SofascorePlayerTournamentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascorePlayerTournamentsTextResponseParams = TypedDict('SofascorePlayerTournamentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascorePlayerTournamentsStreamParams = TypedDict('SofascorePlayerTournamentsStreamParams', {
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

SofascoreRefereeDefaultParams = TypedDict('SofascoreRefereeDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreRefereeTextResponseParams = TypedDict('SofascoreRefereeTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreRefereeStreamParams = TypedDict('SofascoreRefereeStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreRefereeEventsDefaultParams = TypedDict('SofascoreRefereeEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreRefereeEventsTextResponseParams = TypedDict('SofascoreRefereeEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreRefereeEventsStreamParams = TypedDict('SofascoreRefereeEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreRefereeStatisticsDefaultParams = TypedDict('SofascoreRefereeStatisticsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreRefereeStatisticsTextResponseParams = TypedDict('SofascoreRefereeStatisticsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreRefereeStatisticsStreamParams = TypedDict('SofascoreRefereeStatisticsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
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

SofascoreSearchTypedDefaultParams = TypedDict('SofascoreSearchTypedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'type': Required[Literal['events', 'teams', 'players', 'managers', 'referees', 'venues', 'unique_tournaments']],
    'q': Required[str],
    'page': NotRequired[int],
    'sport': NotRequired[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreSearchTypedTextResponseParams = TypedDict('SofascoreSearchTypedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'type': Required[Literal['events', 'teams', 'players', 'managers', 'referees', 'venues', 'unique_tournaments']],
    'q': Required[str],
    'page': NotRequired[int],
    'sport': NotRequired[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreSearchTypedStreamParams = TypedDict('SofascoreSearchTypedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'type': Required[Literal['events', 'teams', 'players', 'managers', 'referees', 'venues', 'unique_tournaments']],
    'q': Required[str],
    'page': NotRequired[int],
    'sport': NotRequired[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
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

SofascoreStageDefaultParams = TypedDict('SofascoreStageDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreStageTextResponseParams = TypedDict('SofascoreStageTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreStageStreamParams = TypedDict('SofascoreStageStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreStageCategoriesDefaultParams = TypedDict('SofascoreStageCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': Required[Literal['motorsport', 'cycling']],
}, total=False)

SofascoreStageCategoriesTextResponseParams = TypedDict('SofascoreStageCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': Required[Literal['motorsport', 'cycling']],
}, total=False)

SofascoreStageCategoriesStreamParams = TypedDict('SofascoreStageCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': Required[Literal['motorsport', 'cycling']],
}, total=False)

SofascoreStageDriverPerformanceDefaultParams = TypedDict('SofascoreStageDriverPerformanceDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreStageDriverPerformanceTextResponseParams = TypedDict('SofascoreStageDriverPerformanceTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreStageDriverPerformanceStreamParams = TypedDict('SofascoreStageDriverPerformanceStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreStageFeaturedDefaultParams = TypedDict('SofascoreStageFeaturedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': Required[Literal['motorsport', 'cycling']],
}, total=False)

SofascoreStageFeaturedTextResponseParams = TypedDict('SofascoreStageFeaturedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': Required[Literal['motorsport', 'cycling']],
}, total=False)

SofascoreStageFeaturedStreamParams = TypedDict('SofascoreStageFeaturedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': Required[Literal['motorsport', 'cycling']],
}, total=False)

SofascoreStageScheduleDefaultParams = TypedDict('SofascoreStageScheduleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': Required[Literal['motorsport', 'cycling']],
    'date': Required[str],
}, total=False)

SofascoreStageScheduleTextResponseParams = TypedDict('SofascoreStageScheduleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': Required[Literal['motorsport', 'cycling']],
    'date': Required[str],
}, total=False)

SofascoreStageScheduleStreamParams = TypedDict('SofascoreStageScheduleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': Required[Literal['motorsport', 'cycling']],
    'date': Required[str],
}, total=False)

SofascoreStageSeasonsDefaultParams = TypedDict('SofascoreStageSeasonsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreStageSeasonsTextResponseParams = TypedDict('SofascoreStageSeasonsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreStageSeasonsStreamParams = TypedDict('SofascoreStageSeasonsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreStageStandingsDefaultParams = TypedDict('SofascoreStageStandingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'type': Required[Literal['competitor', 'team']],
}, total=False)

SofascoreStageStandingsTextResponseParams = TypedDict('SofascoreStageStandingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'type': Required[Literal['competitor', 'team']],
}, total=False)

SofascoreStageStandingsStreamParams = TypedDict('SofascoreStageStandingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'type': Required[Literal['competitor', 'team']],
}, total=False)

SofascoreStageSubstagesDefaultParams = TypedDict('SofascoreStageSubstagesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreStageSubstagesTextResponseParams = TypedDict('SofascoreStageSubstagesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreStageSubstagesStreamParams = TypedDict('SofascoreStageSubstagesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
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

SofascoreTeamAchievementsDefaultParams = TypedDict('SofascoreTeamAchievementsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreTeamAchievementsTextResponseParams = TypedDict('SofascoreTeamAchievementsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreTeamAchievementsStreamParams = TypedDict('SofascoreTeamAchievementsStreamParams', {
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

SofascoreTeamGoalDistributionsDefaultParams = TypedDict('SofascoreTeamGoalDistributionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTeamGoalDistributionsTextResponseParams = TypedDict('SofascoreTeamGoalDistributionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTeamGoalDistributionsStreamParams = TypedDict('SofascoreTeamGoalDistributionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTeamNearEventsDefaultParams = TypedDict('SofascoreTeamNearEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreTeamNearEventsTextResponseParams = TypedDict('SofascoreTeamNearEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreTeamNearEventsStreamParams = TypedDict('SofascoreTeamNearEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
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

SofascoreTeamPerformanceDefaultParams = TypedDict('SofascoreTeamPerformanceDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreTeamPerformanceTextResponseParams = TypedDict('SofascoreTeamPerformanceTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreTeamPerformanceStreamParams = TypedDict('SofascoreTeamPerformanceStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreTeamPlayerStatisticsDefaultParams = TypedDict('SofascoreTeamPlayerStatisticsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascoreTeamPlayerStatisticsTextResponseParams = TypedDict('SofascoreTeamPlayerStatisticsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascoreTeamPlayerStatisticsStreamParams = TypedDict('SofascoreTeamPlayerStatisticsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'home', 'away', 'regular_season', 'playoffs']],
}, total=False)

SofascoreTeamPlayerStatisticsSeasonsDefaultParams = TypedDict('SofascoreTeamPlayerStatisticsSeasonsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreTeamPlayerStatisticsSeasonsTextResponseParams = TypedDict('SofascoreTeamPlayerStatisticsSeasonsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreTeamPlayerStatisticsSeasonsStreamParams = TypedDict('SofascoreTeamPlayerStatisticsSeasonsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
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

SofascoreTeamRankingsDefaultParams = TypedDict('SofascoreTeamRankingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreTeamRankingsTextResponseParams = TypedDict('SofascoreTeamRankingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreTeamRankingsStreamParams = TypedDict('SofascoreTeamRankingsStreamParams', {
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

SofascoreTeamTopPlayersDefaultParams = TypedDict('SofascoreTeamTopPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'regular_season', 'playoffs']],
    'limit': NotRequired[int],
}, total=False)

SofascoreTeamTopPlayersTextResponseParams = TypedDict('SofascoreTeamTopPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'regular_season', 'playoffs']],
    'limit': NotRequired[int],
}, total=False)

SofascoreTeamTopPlayersStreamParams = TypedDict('SofascoreTeamTopPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'tournament_id': Required[str],
    'season': Required[str],
    'type': NotRequired[Literal['overall', 'regular_season', 'playoffs']],
    'limit': NotRequired[int],
}, total=False)

SofascoreTeamTournamentsDefaultParams = TypedDict('SofascoreTeamTournamentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'all': NotRequired[bool],
}, total=False)

SofascoreTeamTournamentsTextResponseParams = TypedDict('SofascoreTeamTournamentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'all': NotRequired[bool],
}, total=False)

SofascoreTeamTournamentsStreamParams = TypedDict('SofascoreTeamTournamentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'all': NotRequired[bool],
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

SofascoreTennisPlayerGrandSlamResultsDefaultParams = TypedDict('SofascoreTennisPlayerGrandSlamResultsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreTennisPlayerGrandSlamResultsTextResponseParams = TypedDict('SofascoreTennisPlayerGrandSlamResultsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreTennisPlayerGrandSlamResultsStreamParams = TypedDict('SofascoreTennisPlayerGrandSlamResultsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreTournamentCuptreeDefaultParams = TypedDict('SofascoreTournamentCuptreeDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentCuptreeTextResponseParams = TypedDict('SofascoreTournamentCuptreeTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentCuptreeStreamParams = TypedDict('SofascoreTournamentCuptreeStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
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

SofascoreTournamentPlayerOfTheSeasonDefaultParams = TypedDict('SofascoreTournamentPlayerOfTheSeasonDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentPlayerOfTheSeasonTextResponseParams = TypedDict('SofascoreTournamentPlayerOfTheSeasonTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentPlayerOfTheSeasonStreamParams = TypedDict('SofascoreTournamentPlayerOfTheSeasonStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
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
    'team': NotRequired[list[str]],
    'nationality': NotRequired[list[str]],
    'position': NotRequired[list[Literal['G', 'D', 'M', 'F']]],
    'min_appearances': NotRequired[int],
    'min_minutes': NotRequired[int],
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
    'team': NotRequired[list[str]],
    'nationality': NotRequired[list[str]],
    'position': NotRequired[list[Literal['G', 'D', 'M', 'F']]],
    'min_appearances': NotRequired[int],
    'min_minutes': NotRequired[int],
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
    'team': NotRequired[list[str]],
    'nationality': NotRequired[list[str]],
    'position': NotRequired[list[Literal['G', 'D', 'M', 'F']]],
    'min_appearances': NotRequired[int],
    'min_minutes': NotRequired[int],
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

SofascoreTournamentStatisticsInfoDefaultParams = TypedDict('SofascoreTournamentStatisticsInfoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentStatisticsInfoTextResponseParams = TypedDict('SofascoreTournamentStatisticsInfoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentStatisticsInfoStreamParams = TypedDict('SofascoreTournamentStatisticsInfoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentTeamOfTheSeasonDefaultParams = TypedDict('SofascoreTournamentTeamOfTheSeasonDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentTeamOfTheSeasonTextResponseParams = TypedDict('SofascoreTournamentTeamOfTheSeasonTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentTeamOfTheSeasonStreamParams = TypedDict('SofascoreTournamentTeamOfTheSeasonStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentTeamsDefaultParams = TypedDict('SofascoreTournamentTeamsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentTeamsTextResponseParams = TypedDict('SofascoreTournamentTeamsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentTeamsStreamParams = TypedDict('SofascoreTournamentTeamsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
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

SofascoreTournamentVenuesDefaultParams = TypedDict('SofascoreTournamentVenuesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentVenuesTextResponseParams = TypedDict('SofascoreTournamentVenuesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentVenuesStreamParams = TypedDict('SofascoreTournamentVenuesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'season': Required[str],
}, total=False)

SofascoreTournamentWinnersDefaultParams = TypedDict('SofascoreTournamentWinnersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreTournamentWinnersTextResponseParams = TypedDict('SofascoreTournamentWinnersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreTournamentWinnersStreamParams = TypedDict('SofascoreTournamentWinnersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

SofascoreTournamentsWithFeatureDefaultParams = TypedDict('SofascoreTournamentsWithFeatureDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'feature': Required[Literal['cuptree', 'standings', 'totw', 'power_rankings']],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'minifootball', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreTournamentsWithFeatureTextResponseParams = TypedDict('SofascoreTournamentsWithFeatureTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'feature': Required[Literal['cuptree', 'standings', 'totw', 'power_rankings']],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'minifootball', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreTournamentsWithFeatureStreamParams = TypedDict('SofascoreTournamentsWithFeatureStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'feature': Required[Literal['cuptree', 'standings', 'totw', 'power_rankings']],
    'sport': Required[Literal['american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'minifootball', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
}, total=False)

SofascoreTrendingEventsDefaultParams = TypedDict('SofascoreTrendingEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country': Required[str],
}, total=False)

SofascoreTrendingEventsTextResponseParams = TypedDict('SofascoreTrendingEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country': Required[str],
}, total=False)

SofascoreTrendingEventsStreamParams = TypedDict('SofascoreTrendingEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country': Required[str],
}, total=False)

SofascoreTrendingPlayersDefaultParams = TypedDict('SofascoreTrendingPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': Required[Literal['football', 'basketball']],
}, total=False)

SofascoreTrendingPlayersTextResponseParams = TypedDict('SofascoreTrendingPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': Required[Literal['football', 'basketball']],
}, total=False)

SofascoreTrendingPlayersStreamParams = TypedDict('SofascoreTrendingPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': Required[Literal['football', 'basketball']],
}, total=False)

SofascoreVenueDefaultParams = TypedDict('SofascoreVenueDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

SofascoreVenueTextResponseParams = TypedDict('SofascoreVenueTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

SofascoreVenueStreamParams = TypedDict('SofascoreVenueStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

SofascoreVenueEventsDefaultParams = TypedDict('SofascoreVenueEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'direction': Required[Literal['next', 'last']],
    'sport': NotRequired[Literal['all', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
    'page': NotRequired[int],
    'tournament': NotRequired[str],
    'season': NotRequired[str],
}, total=False)

SofascoreVenueEventsTextResponseParams = TypedDict('SofascoreVenueEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'direction': Required[Literal['next', 'last']],
    'sport': NotRequired[Literal['all', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
    'page': NotRequired[int],
    'tournament': NotRequired[str],
    'season': NotRequired[str],
}, total=False)

SofascoreVenueEventsStreamParams = TypedDict('SofascoreVenueEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'direction': Required[Literal['next', 'last']],
    'sport': NotRequired[Literal['all', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'baseball', 'basketball', 'beach-volley', 'cricket', 'darts', 'esports', 'floorball', 'football', 'futsal', 'handball', 'ice-hockey', 'mma', 'minifootball', 'padel', 'rugby', 'snooker', 'table-tennis', 'tennis', 'volleyball', 'waterpolo']],
    'page': NotRequired[int],
    'tournament': NotRequired[str],
    'season': NotRequired[str],
}, total=False)
