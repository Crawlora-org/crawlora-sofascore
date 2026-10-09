# SofaScore client usage

The `@crawlora-org/sofascore` and `crawlora-sofascore` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape SofaScore locally; Crawlora is independent from and not endorsed by SofaScore or its owners.

The package tracks the public API contract revision `sha256:645115670262bb86bf9c49f16ddbfdd94bbec67befb2aa8497f10f86ee2d5e46` bundled with release `0.3.3`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 109 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `sofascore` group and the generated `Client` alias.

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
| `draft` / `draft` | `GET /sofascore/draft` | `league` (query, required; values: `nba`, `nfl`), `season` (query, required) | SofaScore league draft |
| `draftPicks` / `draft_picks` | `GET /sofascore/draft-picks` | `league` (query, required; values: `nba`, `nfl`), `year` (query, required), `round` (query, required) | SofaScore league draft picks |
| `esportsGame` / `esports_game` | `GET /sofascore/esports-game` | `id` (query, required), `part` (query, required; values: `statistics`, `lineups`, `bans`, `rounds`) | SofaScore esports game detail |
| `event` / `event` | `GET /sofascore/event` | `id` (query, required) | SofaScore event detail |
| `eventAtBatPitches` / `event_at_bat_pitches` | `GET /sofascore/event-at-bat-pitches` | `id` (query, required), `at_bat_id` (query, required) | SofaScore event at-bat pitches |
| `eventAtBats` / `event_at_bats` | `GET /sofascore/event-at-bats` | `id` (query, required) | SofaScore event at-bats |
| `eventAveragePositions` / `event_average_positions` | `GET /sofascore/event-average-positions` | `id` (query, required) | SofaScore event average positions |
| `eventBaseballTopPerformers` / `event_baseball_top_performers` | `GET /sofascore/event-baseball-top-performers` | `id` (query, required) | SofaScore event baseball top performers |
| `eventBestPlayers` / `event_best_players` | `GET /sofascore/event-best-players` | `id` (query, required) | SofaScore event best players |
| `eventComments` / `event_comments` | `GET /sofascore/event-comments` | `id` (query, required) | SofaScore event commentary |
| `eventEsportsGames` / `event_esports_games` | `GET /sofascore/event-esports-games` | `id` (query, required) | SofaScore event esports games |
| `eventGraph` / `event_graph` | `GET /sofascore/event-graph` | `id` (query, required) | SofaScore event momentum graph |
| `eventH2h` / `event_h2h` | `GET /sofascore/event-h2h` | `id` (query, required) | SofaScore event head-to-head |
| `eventHighlights` / `event_highlights` | `GET /sofascore/event-highlights` | `id` (query, required) | SofaScore event highlights |
| `eventIncidents` / `event_incidents` | `GET /sofascore/event-incidents` | `id` (query, required) | SofaScore event incidents |
| `eventInnings` / `event_innings` | `GET /sofascore/event-innings` | `id` (query, required) | SofaScore event innings |
| `eventLineups` / `event_lineups` | `GET /sofascore/event-lineups` | `id` (query, required) | SofaScore event lineups |
| `eventManagers` / `event_managers` | `GET /sofascore/event-managers` | `id` (query, required) | SofaScore event managers |
| `eventOdds` / `event_odds` | `GET /sofascore/event-odds` | `id` (query, required) | SofaScore event odds |
| `eventPlayerHeatmap` / `event_player_heatmap` | `GET /sofascore/event-player-heatmap` | `id` (query, required), `player_id` (query, required) | SofaScore event player heatmap |
| `eventPlayerStatistics` / `event_player_statistics` | `GET /sofascore/event-player-statistics` | `id` (query, required), `player_id` (query, required) | SofaScore event player statistics |
| `eventPointByPoint` / `event_point_by_point` | `GET /sofascore/event-point-by-point` | `id` (query, required) | SofaScore event point-by-point |
| `eventPregameForm` / `event_pregame_form` | `GET /sofascore/event-pregame-form` | `id` (query, required) | SofaScore event pre-game form |
| `eventShotmap` / `event_shotmap` | `GET /sofascore/event-shotmap` | `id` (query, required) | SofaScore event shot map |
| `eventStatistics` / `event_statistics` | `GET /sofascore/event-statistics` | `id` (query, required) | SofaScore event statistics |
| `eventTeamHeatmap` / `event_team_heatmap` | `GET /sofascore/event-team-heatmap` | `id` (query, required), `team_id` (query, required) | SofaScore event team heatmap |
| `eventTeamStreaks` / `event_team_streaks` | `GET /sofascore/event-team-streaks` | `id` (query, required) | SofaScore event team streaks |
| `eventTennisPower` / `event_tennis_power` | `GET /sofascore/event-tennis-power` | `id` (query, required) | SofaScore event tennis power |
| `eventTvChannels` / `event_tv_channels` | `GET /sofascore/event-tv-channels` | `id` (query, required), `country` (query, optional) | SofaScore event TV channels |
| `eventVotes` / `event_votes` | `GET /sofascore/event-votes` | `id` (query, required) | SofaScore event votes |
| `liveEvents` / `live_events` | `GET /sofascore/live-events` | `sport` (query, required; values: `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `mma`, `minifootball`, `padel`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, `waterpolo`) | SofaScore live events |
| `manager` / `manager` | `GET /sofascore/manager` | `id` (query, required) | SofaScore manager detail |
| `managerEvents` / `manager_events` | `GET /sofascore/manager-events` | `id` (query, required), `page` (query, optional) | SofaScore manager recent matches |
| `mmaCard` / `mma_card` | `GET /sofascore/mma-card` | `org_id` (query, required), `card_id` (query, required), `part` (query, required; values: `all`, `maincard`, `prelims`, `earlyprelims`) | SofaScore MMA card |
| `mmaSchedule` / `mma_schedule` | `GET /sofascore/mma-schedule` | `org_id` (query, required), `month` (query, required) | SofaScore MMA schedule |
| `oddsDropping` / `odds_dropping` | `GET /sofascore/odds-dropping` | `sport` (query, optional; values: `all`, `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `mma`, `minifootball`, `padel`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, `waterpolo`) | SofaScore dropping odds |
| `oddsWinning` / `odds_winning` | `GET /sofascore/odds-winning` | `sport` (query, optional; values: `all`, `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `mma`, `minifootball`, `padel`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, `waterpolo`) | SofaScore winning odds |
| `player` / `player` | `GET /sofascore/player` | `id` (query, required) | SofaScore player detail |
| `playerAttributes` / `player_attributes` | `GET /sofascore/player-attributes` | `id` (query, required) | SofaScore player attributes and characteristics |
| `playerEvents` / `player_events` | `GET /sofascore/player-events` | `id` (query, required), `page` (query, optional) | SofaScore player matches with per-match numbers |
| `playerLastYearSummary` / `player_last_year_summary` | `GET /sofascore/player-last-year-summary` | `id` (query, required) | SofaScore player form over the last year |
| `playerNationalTeamStatistics` / `player_national_team_statistics` | `GET /sofascore/player-national-team-statistics` | `id` (query, required) | SofaScore player national team record |
| `playerPenaltyHistory` / `player_penalty_history` | `GET /sofascore/player-penalty-history` | `id` (query, required) | SofaScore player penalty history |
| `playerRatings` / `player_ratings` | `GET /sofascore/player-ratings` | `id` (query, required), `tournament_id` (query, required), `season` (query, required), `type` (query, optional; values: `overall`, `home`, `away`, `regular_season`, `playoffs`) | SofaScore player match ratings for a season |
| `playerSeasonHeatmap` / `player_season_heatmap` | `GET /sofascore/player-season-heatmap` | `id` (query, required), `tournament_id` (query, required), `season` (query, required) | SofaScore player season heatmap |
| `playerSeasonStatistics` / `player_season_statistics` | `GET /sofascore/player-season-statistics` | `id` (query, required), `tournament_id` (query, required), `season` (query, required), `type` (query, optional; values: `overall`, `home`, `away`, `regular_season`, `playoffs`) | SofaScore player season statistics |
| `playerStatisticalRankings` / `player_statistical_rankings` | `GET /sofascore/player-statistical-rankings` | `id` (query, required), `season` (query, required), `type` (query, optional; values: `overall`) | SofaScore player ranking among all players in a season |
| `playerStatisticsSeasons` / `player_statistics_seasons` | `GET /sofascore/player-statistics-seasons` | `id` (query, required) | SofaScore player statistics seasons |
| `playerTournaments` / `player_tournaments` | `GET /sofascore/player-tournaments` | `id` (query, required) | SofaScore player competitions |
| `playerTransfers` / `player_transfers` | `GET /sofascore/player-transfers` | `id` (query, required) | SofaScore player transfer history |
| `rankings` / `rankings` | `GET /sofascore/rankings` | `type` (query, required; values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `34`, `35`, `36`, `37`, `40`, `41`, `42`, `43`, `44`, `45`, `46`), `limit` (query, optional) | SofaScore rankings |
| `rankingTypes` / `ranking_types` | `GET /sofascore/ranking-types` | — | SofaScore ranking catalogue |
| `referee` / `referee` | `GET /sofascore/referee` | `id` (query, required) | SofaScore referee profile |
| `refereeEvents` / `referee_events` | `GET /sofascore/referee-events` | `id` (query, required), `page` (query, optional) | SofaScore referee officiated matches |
| `refereeStatistics` / `referee_statistics` | `GET /sofascore/referee-statistics` | `id` (query, required) | SofaScore referee card statistics |
| `roundEvents` / `round_events` | `GET /sofascore/round-events` | `id` (query, required), `season` (query, required), `round` (query, required), `slug` (query, optional), `prefix` (query, optional) | SofaScore round fixtures |
| `scheduledEvents` / `scheduled_events` | `GET /sofascore/scheduled-events` | `category_id` (query, required), `date` (query, required) | SofaScore events scheduled in a category on a date |
| `scheduledTournaments` / `scheduled_tournaments` | `GET /sofascore/scheduled-tournaments` | `sport` (query, required; values: `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `mma`, `minifootball`, `padel`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, `waterpolo`), `date` (query, required), `page` (query, optional) | SofaScore tournaments scheduled on a date |
| `search` / `search` | `GET /sofascore/search` | `q` (query, required) | SofaScore universal search |
| `searchTyped` / `search_typed` | `GET /sofascore/search-typed` | `type` (query, required; values: `events`, `teams`, `players`, `managers`, `referees`, `venues`, `unique_tournaments`), `q` (query, required), `page` (query, optional), `sport` (query, optional; values: `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `mma`, `minifootball`, `padel`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, `waterpolo`) | SofaScore search by entity type |
| `seasonEvents` / `season_events` | `GET /sofascore/season-events` | `id` (query, required), `season` (query, required), `direction` (query, required; values: `next`, `last`), `page` (query, optional) | SofaScore season fixtures and results |
| `sports` / `sports` | `GET /sofascore/sports` | — | SofaScore supported sports |
| `stage` / `stage` | `GET /sofascore/stage` | `id` (query, required) | SofaScore motorsport and cycling stage |
| `stageCategories` / `stage_categories` | `GET /sofascore/stage-categories` | `sport` (query, required; values: `motorsport`, `cycling`) | SofaScore motorsport and cycling categories and competitions |
| `stageDriverPerformance` / `stage_driver_performance` | `GET /sofascore/stage-driver-performance` | `id` (query, required) | SofaScore motorsport race progress per driver |
| `stageFeatured` / `stage_featured` | `GET /sofascore/stage-featured` | `sport` (query, required; values: `motorsport`, `cycling`) | SofaScore featured motorsport and cycling events |
| `stageSchedule` / `stage_schedule` | `GET /sofascore/stage-schedule` | `sport` (query, required; values: `motorsport`, `cycling`), `date` (query, required) | SofaScore motorsport and cycling events around a date |
| `stageSeasons` / `stage_seasons` | `GET /sofascore/stage-seasons` | `id` (query, required) | SofaScore seasons of a motorsport or cycling competition |
| `stageStandings` / `stage_standings` | `GET /sofascore/stage-standings` | `id` (query, required), `type` (query, required; values: `competitor`, `team`) | SofaScore motorsport and cycling stage standings |
| `stageSubstages` / `stage_substages` | `GET /sofascore/stage-substages` | `id` (query, required) | SofaScore children of a motorsport or cycling stage |
| `standings` / `standings` | `GET /sofascore/standings` | `id` (query, required), `season` (query, required), `type` (query, required; values: `total`, `home`, `away`) | SofaScore standings |
| `team` / `team` | `GET /sofascore/team` | `id` (query, required) | SofaScore team detail |
| `teamAchievements` / `team_achievements` | `GET /sofascore/team-achievements` | `id` (query, required) | SofaScore team trophies |
| `teamEvents` / `team_events` | `GET /sofascore/team-events` | `id` (query, required), `direction` (query, required; values: `next`, `last`), `page` (query, optional) | SofaScore team fixtures |
| `teamGoalDistributions` / `team_goal_distributions` | `GET /sofascore/team-goal-distributions` | `id` (query, required), `tournament_id` (query, required), `season` (query, required) | SofaScore team goals by match minute |
| `teamNearEvents` / `team_near_events` | `GET /sofascore/team-near-events` | `id` (query, required) | SofaScore team previous and next match |
| `teamOfTheWeek` / `team_of_the_week` | `GET /sofascore/team-of-the-week` | `id` (query, required), `season` (query, required), `period` (query, required) | SofaScore team of the week |
| `teamOfTheWeekPeriods` / `team_of_the_week_periods` | `GET /sofascore/team-of-the-week-periods` | `id` (query, required), `season` (query, required) | SofaScore team of the week periods |
| `teamPerformance` / `team_performance` | `GET /sofascore/team-performance` | `id` (query, required) | SofaScore team recent performance |
| `teamPlayers` / `team_players` | `GET /sofascore/team-players` | `id` (query, required) | SofaScore team players |
| `teamPlayerStatistics` / `team_player_statistics` | `GET /sofascore/team-player-statistics` | `id` (query, required), `tournament_id` (query, required), `season` (query, required), `type` (query, optional; values: `overall`, `home`, `away`, `regular_season`, `playoffs`) | SofaScore team player statistics |
| `teamPlayerStatisticsSeasons` / `team_player_statistics_seasons` | `GET /sofascore/team-player-statistics-seasons` | `id` (query, required) | SofaScore team player statistics seasons |
| `teamRankings` / `team_rankings` | `GET /sofascore/team-rankings` | `id` (query, required) | SofaScore team rankings |
| `teamSeasonStatistics` / `team_season_statistics` | `GET /sofascore/team-season-statistics` | `id` (query, required), `tournament_id` (query, required), `season` (query, required), `type` (query, optional; values: `overall`, `home`, `away`, `regular_season`, `playoffs`) | SofaScore team season statistics |
| `teamStatisticsSeasons` / `team_statistics_seasons` | `GET /sofascore/team-statistics-seasons` | `id` (query, required) | SofaScore team statistics seasons |
| `teamTopPlayers` / `team_top_players` | `GET /sofascore/team-top-players` | `id` (query, required), `tournament_id` (query, required), `season` (query, required), `type` (query, optional; values: `overall`, `regular_season`, `playoffs`), `limit` (query, optional) | SofaScore team top players |
| `teamTournaments` / `team_tournaments` | `GET /sofascore/team-tournaments` | `id` (query, required), `all` (query, optional) | SofaScore team competitions |
| `teamTransfers` / `team_transfers` | `GET /sofascore/team-transfers` | `id` (query, required) | SofaScore team transfers |
| `tennisPlayerGrandSlamResults` / `tennis_player_grand_slam_results` | `GET /sofascore/tennis-player-grand-slam-results` | `id` (query, required) | SofaScore tennis player grand slam results |
| `tournamentCuptree` / `tournament_cuptree` | `GET /sofascore/tournament-cuptree` | `id` (query, required), `season` (query, required) | SofaScore competition knockout tree |
| `tournamentInfo` / `tournament_info` | `GET /sofascore/tournament-info` | `id` (query, required), `season` (query, optional) | SofaScore competition info |
| `tournamentPlayerOfTheSeason` / `tournament_player_of_the_season` | `GET /sofascore/tournament-player-of-the-season` | `id` (query, required), `season` (query, required) | SofaScore player of the season |
| `tournamentPlayerStatistics` / `tournament_player_statistics` | `GET /sofascore/tournament-player-statistics` | `id` (query, required), `season` (query, required), `order` (query, optional; values: `rating`, `goals`, `expectedGoals`, `assists`, `successfulDribbles`, `tackles`, `accuratePassesPercentage`, `bigChancesMissed`, `totalShots`, `goalConversionPercentage`, `interceptions`, `clearances`, `errorLeadToGoal`, `outfielderBlocks`, `bigChancesCreated`, `accuratePasses`, `keyPasses`, `saves`, `cleanSheet`, `penaltySave`, `savedShotsFromInsideTheBox`, `runsOut`), `direction` (query, optional; values: `desc`, `asc`), `accumulation` (query, optional; values: `total`, `perGame`, `per90`), `group` (query, optional; values: `summary`, `attack`, `defence`, `passing`, `goalkeeper`), `limit` (query, optional), `offset` (query, optional), `team` (query, optional), `nationality` (query, optional), `position` (query, optional; values: `G`, `D`, `M`, `F`), `min_appearances` (query, optional), `min_minutes` (query, optional) | SofaScore season player statistics table |
| `tournamentRounds` / `tournament_rounds` | `GET /sofascore/tournament-rounds` | `id` (query, required), `season` (query, required) | SofaScore competition season rounds |
| `tournamentSeasons` / `tournament_seasons` | `GET /sofascore/tournament-seasons` | `id` (query, required) | SofaScore competition seasons |
| `tournamentStatisticsInfo` / `tournament_statistics_info` | `GET /sofascore/tournament-statistics-info` | `id` (query, required), `season` (query, required) | SofaScore player statistics table filters |
| `tournamentsWithFeature` / `tournaments_with_feature` | `GET /sofascore/tournaments-with-feature` | `feature` (query, required; values: `cuptree`, `standings`, `totw`, `power_rankings`), `sport` (query, required; values: `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `minifootball`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, `waterpolo`) | SofaScore competitions that carry a feature |
| `tournamentTeamOfTheSeason` / `tournament_team_of_the_season` | `GET /sofascore/tournament-team-of-the-season` | `id` (query, required), `season` (query, required) | SofaScore team of the season |
| `tournamentTeams` / `tournament_teams` | `GET /sofascore/tournament-teams` | `id` (query, required), `season` (query, required) | SofaScore teams of a competition season |
| `tournamentTopPlayers` / `tournament_top_players` | `GET /sofascore/tournament-top-players` | `id` (query, required), `season` (query, required), `type` (query, optional; values: `overall`, `regular_season`, `playoffs`), `limit` (query, optional) | SofaScore season top players |
| `tournamentTopTeams` / `tournament_top_teams` | `GET /sofascore/tournament-top-teams` | `id` (query, required), `season` (query, required), `type` (query, optional; values: `overall`, `regular_season`, `playoffs`), `limit` (query, optional) | SofaScore season top teams |
| `tournamentVenues` / `tournament_venues` | `GET /sofascore/tournament-venues` | `id` (query, required), `season` (query, required) | SofaScore venues of a competition season |
| `tournamentWinners` / `tournament_winners` | `GET /sofascore/tournament-winners` | `id` (query, required), `page` (query, optional) | SofaScore past winners of a competition |
| `trendingEvents` / `trending_events` | `GET /sofascore/trending-events` | `country` (query, required) | SofaScore trending events |
| `trendingPlayers` / `trending_players` | `GET /sofascore/trending-players` | `sport` (query, required; values: `football`, `basketball`) | SofaScore trending players |
| `venue` / `venue` | `GET /sofascore/venue` | `id` (query, required) | SofaScore venue |
| `venueEvents` / `venue_events` | `GET /sofascore/venue-events` | `id` (query, required), `direction` (query, required; values: `next`, `last`), `sport` (query, optional; values: `all`, `american-football`, `aussie-rules`, `badminton`, `bandy`, `baseball`, `basketball`, `beach-volley`, `cricket`, `darts`, `esports`, `floorball`, `football`, `futsal`, `handball`, `ice-hockey`, `mma`, `minifootball`, `padel`, `rugby`, `snooker`, `table-tennis`, `tennis`, `volleyball`, `waterpolo`), `page` (query, optional), `tournament` (query, optional), `season` (query, optional) | SofaScore matches at a venue |

## Client forms

- JavaScript: import `SofascoreClient` (also exported as `Client`) from `@crawlora-org/sofascore`; use `new SofascoreClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `SofascoreClient` (also exported as `Client`) from `crawlora_sofascore`; use `with SofascoreClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncSofascoreClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
