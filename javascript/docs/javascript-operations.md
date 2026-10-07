# Crawlora SofaScore JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `15`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sofascore | `sofascore.event` | `sofascore-event` | `GET /sofascore/event` | `id` (query string required) | `ApiKeyAuth` | `SofascoreEventResponse` |  |
| sofascore | `sofascore.eventH2h` | `sofascore-event-h2h` | `GET /sofascore/event-h2h` | `id` (query string required) | `ApiKeyAuth` | `SofascoreEventH2hResponse` |  |
| sofascore | `sofascore.eventIncidents` | `sofascore-event-incidents` | `GET /sofascore/event-incidents` | `id` (query string required) | `ApiKeyAuth` | `SofascoreEventIncidentsResponse` |  |
| sofascore | `sofascore.eventLineups` | `sofascore-event-lineups` | `GET /sofascore/event-lineups` | `id` (query string required) | `ApiKeyAuth` | `SofascoreEventLineupsResponse` |  |
| sofascore | `sofascore.eventOdds` | `sofascore-event-odds` | `GET /sofascore/event-odds` | `id` (query string required) | `ApiKeyAuth` | `SofascoreEventOddsResponse` |  |
| sofascore | `sofascore.eventStatistics` | `sofascore-event-statistics` | `GET /sofascore/event-statistics` | `id` (query string required) | `ApiKeyAuth` | `SofascoreEventStatisticsResponse` |  |
| sofascore | `sofascore.liveEvents` | `sofascore-live-events` | `GET /sofascore/live-events` | `sport` (query "football" \| "basketball" \| "tennis" required) | `ApiKeyAuth` | `SofascoreLiveEventsResponse` |  |
| sofascore | `sofascore.player` | `sofascore-player` | `GET /sofascore/player` | `id` (query string required) | `ApiKeyAuth` | `SofascorePlayerResponse` |  |
| sofascore | `sofascore.roundEvents` | `sofascore-round-events` | `GET /sofascore/round-events` | `id` (query string required)<br>`season` (query string required)<br>`round` (query number required) | `ApiKeyAuth` | `SofascoreRoundEventsResponse` |  |
| sofascore | `sofascore.search` | `sofascore-search` | `GET /sofascore/search` | `q` (query string required) | `ApiKeyAuth` | `SofascoreSearchResponse` |  |
| sofascore | `sofascore.standings` | `sofascore-standings` | `GET /sofascore/standings` | `id` (query string required)<br>`season` (query string required)<br>`type` (query "total" \| "home" \| "away" required) | `ApiKeyAuth` | `SofascoreStandingsResponse` |  |
| sofascore | `sofascore.team` | `sofascore-team` | `GET /sofascore/team` | `id` (query string required) | `ApiKeyAuth` | `SofascoreTeamResponse` |  |
| sofascore | `sofascore.teamEvents` | `sofascore-team-events` | `GET /sofascore/team-events` | `id` (query string required)<br>`direction` (query "next" \| "last" required)<br>`page` (query number) | `ApiKeyAuth` | `SofascoreTeamEventsResponse` |  |
| sofascore | `sofascore.teamPlayers` | `sofascore-team-players` | `GET /sofascore/team-players` | `id` (query string required) | `ApiKeyAuth` | `SofascoreTeamPlayersResponse` |  |
| sofascore | `sofascore.tournamentSeasons` | `sofascore-tournament-seasons` | `GET /sofascore/tournament-seasons` | `id` (query string required) | `ApiKeyAuth` | `SofascoreTournamentSeasonsResponse` |  |
