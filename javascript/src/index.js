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
    super({ ...options, userAgent: options.userAgent ?? "crawlora-sofascore-js/0.1.3" });
    this["event"] = (...args) => this.request("sofascore-event", ...args);
    this["eventH2h"] = (...args) => this.request("sofascore-event-h2h", ...args);
    this["eventIncidents"] = (...args) => this.request("sofascore-event-incidents", ...args);
    this["eventLineups"] = (...args) => this.request("sofascore-event-lineups", ...args);
    this["eventOdds"] = (...args) => this.request("sofascore-event-odds", ...args);
    this["eventStatistics"] = (...args) => this.request("sofascore-event-statistics", ...args);
    this["liveEvents"] = (...args) => this.request("sofascore-live-events", ...args);
    this["player"] = (...args) => this.request("sofascore-player", ...args);
    this["roundEvents"] = (...args) => this.request("sofascore-round-events", ...args);
    this["search"] = (...args) => this.request("sofascore-search", ...args);
    this["standings"] = (...args) => this.request("sofascore-standings", ...args);
    this["team"] = (...args) => this.request("sofascore-team", ...args);
    this["teamEvents"] = (...args) => this.request("sofascore-team-events", ...args);
    this["teamPlayers"] = (...args) => this.request("sofascore-team-players", ...args);
    this["tournamentSeasons"] = (...args) => this.request("sofascore-tournament-seasons", ...args);
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
export const VERSION = "0.1.3";
export default SofascoreClient;
