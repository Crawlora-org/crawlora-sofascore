import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class SofascoreClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-sofascore-js/0.3.3" });
    this["categories"] = (...args) => this.request("sofascore-categories", ...args);
    this["categoryTournaments"] = (...args) => this.request("sofascore-category-tournaments", ...args);
    this["draft"] = (...args) => this.request("sofascore-draft", ...args);
    this["draftPicks"] = (...args) => this.request("sofascore-draft-picks", ...args);
    this["esportsGame"] = (...args) => this.request("sofascore-esports-game", ...args);
    this["event"] = (...args) => this.request("sofascore-event", ...args);
    this["eventAtBatPitches"] = (...args) => this.request("sofascore-event-at-bat-pitches", ...args);
    this["eventAtBats"] = (...args) => this.request("sofascore-event-at-bats", ...args);
    this["eventAveragePositions"] = (...args) => this.request("sofascore-event-average-positions", ...args);
    this["eventBaseballTopPerformers"] = (...args) => this.request("sofascore-event-baseball-top-performers", ...args);
    this["eventBestPlayers"] = (...args) => this.request("sofascore-event-best-players", ...args);
    this["eventComments"] = (...args) => this.request("sofascore-event-comments", ...args);
    this["eventEsportsGames"] = (...args) => this.request("sofascore-event-esports-games", ...args);
    this["eventGraph"] = (...args) => this.request("sofascore-event-graph", ...args);
    this["eventH2h"] = (...args) => this.request("sofascore-event-h2h", ...args);
    this["eventHighlights"] = (...args) => this.request("sofascore-event-highlights", ...args);
    this["eventIncidents"] = (...args) => this.request("sofascore-event-incidents", ...args);
    this["eventInnings"] = (...args) => this.request("sofascore-event-innings", ...args);
    this["eventLineups"] = (...args) => this.request("sofascore-event-lineups", ...args);
    this["eventManagers"] = (...args) => this.request("sofascore-event-managers", ...args);
    this["eventOdds"] = (...args) => this.request("sofascore-event-odds", ...args);
    this["eventPlayerHeatmap"] = (...args) => this.request("sofascore-event-player-heatmap", ...args);
    this["eventPlayerStatistics"] = (...args) => this.request("sofascore-event-player-statistics", ...args);
    this["eventPointByPoint"] = (...args) => this.request("sofascore-event-point-by-point", ...args);
    this["eventPregameForm"] = (...args) => this.request("sofascore-event-pregame-form", ...args);
    this["eventShotmap"] = (...args) => this.request("sofascore-event-shotmap", ...args);
    this["eventStatistics"] = (...args) => this.request("sofascore-event-statistics", ...args);
    this["eventTeamHeatmap"] = (...args) => this.request("sofascore-event-team-heatmap", ...args);
    this["eventTeamStreaks"] = (...args) => this.request("sofascore-event-team-streaks", ...args);
    this["eventTennisPower"] = (...args) => this.request("sofascore-event-tennis-power", ...args);
    this["eventTvChannels"] = (...args) => this.request("sofascore-event-tv-channels", ...args);
    this["eventVotes"] = (...args) => this.request("sofascore-event-votes", ...args);
    this["liveEvents"] = (...args) => this.request("sofascore-live-events", ...args);
    this["manager"] = (...args) => this.request("sofascore-manager", ...args);
    this["managerEvents"] = (...args) => this.request("sofascore-manager-events", ...args);
    this["mmaCard"] = (...args) => this.request("sofascore-mma-card", ...args);
    this["mmaSchedule"] = (...args) => this.request("sofascore-mma-schedule", ...args);
    this["oddsDropping"] = (...args) => this.request("sofascore-odds-dropping", ...args);
    this["oddsWinning"] = (...args) => this.request("sofascore-odds-winning", ...args);
    this["player"] = (...args) => this.request("sofascore-player", ...args);
    this["playerAttributes"] = (...args) => this.request("sofascore-player-attributes", ...args);
    this["playerEvents"] = (...args) => this.request("sofascore-player-events", ...args);
    this["playerLastYearSummary"] = (...args) => this.request("sofascore-player-last-year-summary", ...args);
    this["playerNationalTeamStatistics"] = (...args) => this.request("sofascore-player-national-team-statistics", ...args);
    this["playerPenaltyHistory"] = (...args) => this.request("sofascore-player-penalty-history", ...args);
    this["playerRatings"] = (...args) => this.request("sofascore-player-ratings", ...args);
    this["playerSeasonHeatmap"] = (...args) => this.request("sofascore-player-season-heatmap", ...args);
    this["playerSeasonStatistics"] = (...args) => this.request("sofascore-player-season-statistics", ...args);
    this["playerStatisticalRankings"] = (...args) => this.request("sofascore-player-statistical-rankings", ...args);
    this["playerStatisticsSeasons"] = (...args) => this.request("sofascore-player-statistics-seasons", ...args);
    this["playerTournaments"] = (...args) => this.request("sofascore-player-tournaments", ...args);
    this["playerTransfers"] = (...args) => this.request("sofascore-player-transfers", ...args);
    this["rankingTypes"] = (...args) => this.request("sofascore-ranking-types", ...args);
    this["rankings"] = (...args) => this.request("sofascore-rankings", ...args);
    this["referee"] = (...args) => this.request("sofascore-referee", ...args);
    this["refereeEvents"] = (...args) => this.request("sofascore-referee-events", ...args);
    this["refereeStatistics"] = (...args) => this.request("sofascore-referee-statistics", ...args);
    this["roundEvents"] = (...args) => this.request("sofascore-round-events", ...args);
    this["scheduledEvents"] = (...args) => this.request("sofascore-scheduled-events", ...args);
    this["scheduledTournaments"] = (...args) => this.request("sofascore-scheduled-tournaments", ...args);
    this["search"] = (...args) => this.request("sofascore-search", ...args);
    this["searchTyped"] = (...args) => this.request("sofascore-search-typed", ...args);
    this["seasonEvents"] = (...args) => this.request("sofascore-season-events", ...args);
    this["sports"] = (...args) => this.request("sofascore-sports", ...args);
    this["stage"] = (...args) => this.request("sofascore-stage", ...args);
    this["stageCategories"] = (...args) => this.request("sofascore-stage-categories", ...args);
    this["stageDriverPerformance"] = (...args) => this.request("sofascore-stage-driver-performance", ...args);
    this["stageFeatured"] = (...args) => this.request("sofascore-stage-featured", ...args);
    this["stageSchedule"] = (...args) => this.request("sofascore-stage-schedule", ...args);
    this["stageSeasons"] = (...args) => this.request("sofascore-stage-seasons", ...args);
    this["stageStandings"] = (...args) => this.request("sofascore-stage-standings", ...args);
    this["stageSubstages"] = (...args) => this.request("sofascore-stage-substages", ...args);
    this["standings"] = (...args) => this.request("sofascore-standings", ...args);
    this["team"] = (...args) => this.request("sofascore-team", ...args);
    this["teamAchievements"] = (...args) => this.request("sofascore-team-achievements", ...args);
    this["teamEvents"] = (...args) => this.request("sofascore-team-events", ...args);
    this["teamGoalDistributions"] = (...args) => this.request("sofascore-team-goal-distributions", ...args);
    this["teamNearEvents"] = (...args) => this.request("sofascore-team-near-events", ...args);
    this["teamOfTheWeek"] = (...args) => this.request("sofascore-team-of-the-week", ...args);
    this["teamOfTheWeekPeriods"] = (...args) => this.request("sofascore-team-of-the-week-periods", ...args);
    this["teamPerformance"] = (...args) => this.request("sofascore-team-performance", ...args);
    this["teamPlayerStatistics"] = (...args) => this.request("sofascore-team-player-statistics", ...args);
    this["teamPlayerStatisticsSeasons"] = (...args) => this.request("sofascore-team-player-statistics-seasons", ...args);
    this["teamPlayers"] = (...args) => this.request("sofascore-team-players", ...args);
    this["teamRankings"] = (...args) => this.request("sofascore-team-rankings", ...args);
    this["teamSeasonStatistics"] = (...args) => this.request("sofascore-team-season-statistics", ...args);
    this["teamStatisticsSeasons"] = (...args) => this.request("sofascore-team-statistics-seasons", ...args);
    this["teamTopPlayers"] = (...args) => this.request("sofascore-team-top-players", ...args);
    this["teamTournaments"] = (...args) => this.request("sofascore-team-tournaments", ...args);
    this["teamTransfers"] = (...args) => this.request("sofascore-team-transfers", ...args);
    this["tennisPlayerGrandSlamResults"] = (...args) => this.request("sofascore-tennis-player-grand-slam-results", ...args);
    this["tournamentCuptree"] = (...args) => this.request("sofascore-tournament-cuptree", ...args);
    this["tournamentInfo"] = (...args) => this.request("sofascore-tournament-info", ...args);
    this["tournamentPlayerOfTheSeason"] = (...args) => this.request("sofascore-tournament-player-of-the-season", ...args);
    this["tournamentPlayerStatistics"] = (...args) => this.request("sofascore-tournament-player-statistics", ...args);
    this["tournamentRounds"] = (...args) => this.request("sofascore-tournament-rounds", ...args);
    this["tournamentSeasons"] = (...args) => this.request("sofascore-tournament-seasons", ...args);
    this["tournamentStatisticsInfo"] = (...args) => this.request("sofascore-tournament-statistics-info", ...args);
    this["tournamentTeamOfTheSeason"] = (...args) => this.request("sofascore-tournament-team-of-the-season", ...args);
    this["tournamentTeams"] = (...args) => this.request("sofascore-tournament-teams", ...args);
    this["tournamentTopPlayers"] = (...args) => this.request("sofascore-tournament-top-players", ...args);
    this["tournamentTopTeams"] = (...args) => this.request("sofascore-tournament-top-teams", ...args);
    this["tournamentVenues"] = (...args) => this.request("sofascore-tournament-venues", ...args);
    this["tournamentWinners"] = (...args) => this.request("sofascore-tournament-winners", ...args);
    this["tournamentsWithFeature"] = (...args) => this.request("sofascore-tournaments-with-feature", ...args);
    this["trendingEvents"] = (...args) => this.request("sofascore-trending-events", ...args);
    this["trendingPlayers"] = (...args) => this.request("sofascore-trending-players", ...args);
    this["venue"] = (...args) => this.request("sofascore-venue", ...args);
    this["venueEvents"] = (...args) => this.request("sofascore-venue-events", ...args);
  }
}

export { SofascoreClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.3.3";
export default SofascoreClient;
