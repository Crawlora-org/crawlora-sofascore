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
    super({ ...options, userAgent: options.userAgent ?? "crawlora-sofascore-js/0.2.0" });
    this["categories"] = (...args) => this.request("sofascore-categories", ...args);
    this["categoryTournaments"] = (...args) => this.request("sofascore-category-tournaments", ...args);
    this["event"] = (...args) => this.request("sofascore-event", ...args);
    this["eventBestPlayers"] = (...args) => this.request("sofascore-event-best-players", ...args);
    this["eventComments"] = (...args) => this.request("sofascore-event-comments", ...args);
    this["eventGraph"] = (...args) => this.request("sofascore-event-graph", ...args);
    this["eventH2h"] = (...args) => this.request("sofascore-event-h2h", ...args);
    this["eventIncidents"] = (...args) => this.request("sofascore-event-incidents", ...args);
    this["eventLineups"] = (...args) => this.request("sofascore-event-lineups", ...args);
    this["eventOdds"] = (...args) => this.request("sofascore-event-odds", ...args);
    this["eventPlayerStatistics"] = (...args) => this.request("sofascore-event-player-statistics", ...args);
    this["eventShotmap"] = (...args) => this.request("sofascore-event-shotmap", ...args);
    this["eventStatistics"] = (...args) => this.request("sofascore-event-statistics", ...args);
    this["liveEvents"] = (...args) => this.request("sofascore-live-events", ...args);
    this["manager"] = (...args) => this.request("sofascore-manager", ...args);
    this["managerEvents"] = (...args) => this.request("sofascore-manager-events", ...args);
    this["player"] = (...args) => this.request("sofascore-player", ...args);
    this["playerSeasonStatistics"] = (...args) => this.request("sofascore-player-season-statistics", ...args);
    this["playerStatisticsSeasons"] = (...args) => this.request("sofascore-player-statistics-seasons", ...args);
    this["playerTransfers"] = (...args) => this.request("sofascore-player-transfers", ...args);
    this["rankingTypes"] = (...args) => this.request("sofascore-ranking-types", ...args);
    this["rankings"] = (...args) => this.request("sofascore-rankings", ...args);
    this["roundEvents"] = (...args) => this.request("sofascore-round-events", ...args);
    this["scheduledEvents"] = (...args) => this.request("sofascore-scheduled-events", ...args);
    this["scheduledTournaments"] = (...args) => this.request("sofascore-scheduled-tournaments", ...args);
    this["search"] = (...args) => this.request("sofascore-search", ...args);
    this["seasonEvents"] = (...args) => this.request("sofascore-season-events", ...args);
    this["sports"] = (...args) => this.request("sofascore-sports", ...args);
    this["standings"] = (...args) => this.request("sofascore-standings", ...args);
    this["team"] = (...args) => this.request("sofascore-team", ...args);
    this["teamEvents"] = (...args) => this.request("sofascore-team-events", ...args);
    this["teamOfTheWeek"] = (...args) => this.request("sofascore-team-of-the-week", ...args);
    this["teamOfTheWeekPeriods"] = (...args) => this.request("sofascore-team-of-the-week-periods", ...args);
    this["teamPlayers"] = (...args) => this.request("sofascore-team-players", ...args);
    this["teamSeasonStatistics"] = (...args) => this.request("sofascore-team-season-statistics", ...args);
    this["teamStatisticsSeasons"] = (...args) => this.request("sofascore-team-statistics-seasons", ...args);
    this["teamTransfers"] = (...args) => this.request("sofascore-team-transfers", ...args);
    this["tournamentInfo"] = (...args) => this.request("sofascore-tournament-info", ...args);
    this["tournamentPlayerStatistics"] = (...args) => this.request("sofascore-tournament-player-statistics", ...args);
    this["tournamentRounds"] = (...args) => this.request("sofascore-tournament-rounds", ...args);
    this["tournamentSeasons"] = (...args) => this.request("sofascore-tournament-seasons", ...args);
    this["tournamentTopPlayers"] = (...args) => this.request("sofascore-tournament-top-players", ...args);
    this["tournamentTopTeams"] = (...args) => this.request("sofascore-tournament-top-teams", ...args);
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
export const VERSION = "0.2.0";
export default SofascoreClient;
