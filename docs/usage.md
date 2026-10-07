# SofaScore client usage

The `@crawlora-org/sofascore` and `crawlora-sofascore` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape SofaScore locally; Crawlora is independent from and not endorsed by SofaScore or its owners.

The package tracks the public API contract revision `sha256:91686922e3c5ab6569dbe0abd882fbbbc86c4395a86f151582a2291fb11de036` bundled with release `0.2.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 43 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `sofascore` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `categories` / `categories` | `GET /sofascore/categories` | `sport` (query, required; values: `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `mma`, `minifootball`, `padel`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, `waterpolo`) | SofaScore categories for a sport |
| `categoryTournaments` / `category_tournaments` | `GET /sofascore/category-tournaments` | `id` (query, required) | SofaScore competitions in a category |
| `event` / `event` | `GET /sofascore/event` | `id` (query, required) | SofaScore event detail |
| `eventBestPlayers` / `event_best_players` | `GET /sofascore/event-best-players` | `id` (query, required) | SofaScore event best players |
| `eventComments` / `event_comments` | `GET /sofascore/event-comments` | `id` (query, required) | SofaScore event commentary |
| `eventGraph` / `event_graph` | `GET /sofascore/event-graph` | `id` (query, required) | SofaScore event momentum graph |
| `eventH2h` / `event_h2h` | `GET /sofascore/event-h2h` | `id` (query, required) | SofaScore event head-to-head |
| `eventIncidents` / `event_incidents` | `GET /sofascore/event-incidents` | `id` (query, required) | SofaScore event incidents |
| `eventLineups` / `event_lineups` | `GET /sofascore/event-lineups` | `id` (query, required) | SofaScore event lineups |
| `eventOdds` / `event_odds` | `GET /sofascore/event-odds` | `id` (query, required) | SofaScore event odds |
| `eventPlayerStatistics` / `event_player_statistics` | `GET /sofascore/event-player-statistics` | `id` (query, required), `player_id` (query, required) | SofaScore event player statistics |
| `eventShotmap` / `event_shotmap` | `GET /sofascore/event-shotmap` | `id` (query, required) | SofaScore event shot map |
| `eventStatistics` / `event_statistics` | `GET /sofascore/event-statistics` | `id` (query, required) | SofaScore event statistics |
| `liveEvents` / `live_events` | `GET /sofascore/live-events` | `sport` (query, required; values: `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `mma`, `minifootball`, `padel`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, `waterpolo`) | SofaScore live events |
| `manager` / `manager` | `GET /sofascore/manager` | `id` (query, required) | SofaScore manager detail |
| `managerEvents` / `manager_events` | `GET /sofascore/manager-events` | `id` (query, required), `page` (query, optional) | SofaScore manager recent matches |
| `player` / `player` | `GET /sofascore/player` | `id` (query, required) | SofaScore player detail |
| `playerSeasonStatistics` / `player_season_statistics` | `GET /sofascore/player-season-statistics` | `id` (query, required), `tournament_id` (query, required), `season` (query, required), `type` (query, optional; values: `overall`, `home`, `away`, `regular_season`, `playoffs`) | SofaScore player season statistics |
| `playerStatisticsSeasons` / `player_statistics_seasons` | `GET /sofascore/player-statistics-seasons` | `id` (query, required) | SofaScore player statistics seasons |
| `playerTransfers` / `player_transfers` | `GET /sofascore/player-transfers` | `id` (query, required) | SofaScore player transfer history |
| `rankings` / `rankings` | `GET /sofascore/rankings` | `type` (query, required; values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `34`, `35`, `36`, `37`, `40`, `41`, `42`, `43`, `44`, `45`, `46`), `limit` (query, optional) | SofaScore rankings |
| `rankingTypes` / `ranking_types` | `GET /sofascore/ranking-types` | — | SofaScore ranking catalogue |
| `roundEvents` / `round_events` | `GET /sofascore/round-events` | `id` (query, required), `season` (query, required), `round` (query, required), `slug` (query, optional), `prefix` (query, optional) | SofaScore round fixtures |
| `scheduledEvents` / `scheduled_events` | `GET /sofascore/scheduled-events` | `category_id` (query, required), `date` (query, required) | SofaScore events scheduled in a category on a date |
| `scheduledTournaments` / `scheduled_tournaments` | `GET /sofascore/scheduled-tournaments` | `sport` (query, required; values: `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `mma`, `minifootball`, `padel`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, `waterpolo`), `date` (query, required), `page` (query, optional) | SofaScore tournaments scheduled on a date |
| `search` / `search` | `GET /sofascore/search` | `q` (query, required) | SofaScore universal search |
| `seasonEvents` / `season_events` | `GET /sofascore/season-events` | `id` (query, required), `season` (query, required), `direction` (query, required; values: `next`, `last`), `page` (query, optional) | SofaScore season fixtures and results |
| `sports` / `sports` | `GET /sofascore/sports` | — | SofaScore supported sports |
| `standings` / `standings` | `GET /sofascore/standings` | `id` (query, required), `season` (query, required), `type` (query, required; values: `total`, `home`, `away`) | SofaScore standings |
| `team` / `team` | `GET /sofascore/team` | `id` (query, required) | SofaScore team detail |
| `teamEvents` / `team_events` | `GET /sofascore/team-events` | `id` (query, required), `direction` (query, required; values: `next`, `last`), `page` (query, optional) | SofaScore team fixtures |
| `teamOfTheWeek` / `team_of_the_week` | `GET /sofascore/team-of-the-week` | `id` (query, required), `season` (query, required), `period` (query, required) | SofaScore team of the week |
| `teamOfTheWeekPeriods` / `team_of_the_week_periods` | `GET /sofascore/team-of-the-week-periods` | `id` (query, required), `season` (query, required) | SofaScore team of the week periods |
| `teamPlayers` / `team_players` | `GET /sofascore/team-players` | `id` (query, required) | SofaScore team players |
| `teamSeasonStatistics` / `team_season_statistics` | `GET /sofascore/team-season-statistics` | `id` (query, required), `tournament_id` (query, required), `season` (query, required), `type` (query, optional; values: `overall`, `home`, `away`, `regular_season`, `playoffs`) | SofaScore team season statistics |
| `teamStatisticsSeasons` / `team_statistics_seasons` | `GET /sofascore/team-statistics-seasons` | `id` (query, required) | SofaScore team statistics seasons |
| `teamTransfers` / `team_transfers` | `GET /sofascore/team-transfers` | `id` (query, required) | SofaScore team transfers |
| `tournamentInfo` / `tournament_info` | `GET /sofascore/tournament-info` | `id` (query, required), `season` (query, optional) | SofaScore competition info |
| `tournamentPlayerStatistics` / `tournament_player_statistics` | `GET /sofascore/tournament-player-statistics` | `id` (query, required), `season` (query, required), `order` (query, optional; values: `rating`, `goals`, `expectedGoals`, `assists`, `successfulDribbles`, `tackles`, `accuratePassesPercentage`, `bigChancesMissed`, `totalShots`, `goalConversionPercentage`, `interceptions`, `clearances`, `errorLeadToGoal`, `outfielderBlocks`, `bigChancesCreated`, `accuratePasses`, `keyPasses`, `saves`, `cleanSheet`, `penaltySave`, `savedShotsFromInsideTheBox`, `runsOut`), `direction` (query, optional; values: `desc`, `asc`), `accumulation` (query, optional; values: `total`, `perGame`, `per90`), `group` (query, optional; values: `summary`, `attack`, `defence`, `passing`, `goalkeeper`), `limit` (query, optional), `offset` (query, optional) | SofaScore season player statistics table |
| `tournamentRounds` / `tournament_rounds` | `GET /sofascore/tournament-rounds` | `id` (query, required), `season` (query, required) | SofaScore competition season rounds |
| `tournamentSeasons` / `tournament_seasons` | `GET /sofascore/tournament-seasons` | `id` (query, required) | SofaScore competition seasons |
| `tournamentTopPlayers` / `tournament_top_players` | `GET /sofascore/tournament-top-players` | `id` (query, required), `season` (query, required), `type` (query, optional; values: `overall`, `regular_season`, `playoffs`), `limit` (query, optional) | SofaScore season top players |
| `tournamentTopTeams` / `tournament_top_teams` | `GET /sofascore/tournament-top-teams` | `id` (query, required), `season` (query, required), `type` (query, optional; values: `overall`, `regular_season`, `playoffs`), `limit` (query, optional) | SofaScore season top teams |

## Client forms

- JavaScript: import `SofascoreClient` (also exported as `Client`) from `@crawlora-org/sofascore`; use `new SofascoreClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `SofascoreClient` (also exported as `Client`) from `crawlora_sofascore`; use `with SofascoreClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncSofascoreClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
