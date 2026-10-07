import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class SofascoreClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categories(params: OperationParamsMap["sofascore-categories"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categoryTournaments(params: OperationParamsMap["sofascore-category-tournaments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  event(params: OperationParamsMap["sofascore-event"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventBestPlayers(params: OperationParamsMap["sofascore-event-best-players"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventComments(params: OperationParamsMap["sofascore-event-comments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventGraph(params: OperationParamsMap["sofascore-event-graph"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventH2h(params: OperationParamsMap["sofascore-event-h2h"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventIncidents(params: OperationParamsMap["sofascore-event-incidents"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventLineups(params: OperationParamsMap["sofascore-event-lineups"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventOdds(params: OperationParamsMap["sofascore-event-odds"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventPlayerStatistics(params: OperationParamsMap["sofascore-event-player-statistics"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventShotmap(params: OperationParamsMap["sofascore-event-shotmap"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventStatistics(params: OperationParamsMap["sofascore-event-statistics"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  liveEvents(params: OperationParamsMap["sofascore-live-events"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  manager(params: OperationParamsMap["sofascore-manager"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  managerEvents(params: OperationParamsMap["sofascore-manager-events"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  player(params: OperationParamsMap["sofascore-player"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerSeasonStatistics(params: OperationParamsMap["sofascore-player-season-statistics"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerStatisticsSeasons(params: OperationParamsMap["sofascore-player-statistics-seasons"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerTransfers(params: OperationParamsMap["sofascore-player-transfers"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  rankingTypes(params?: OperationParamsMap["sofascore-ranking-types"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  rankings(params: OperationParamsMap["sofascore-rankings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  roundEvents(params: OperationParamsMap["sofascore-round-events"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  scheduledEvents(params: OperationParamsMap["sofascore-scheduled-events"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  scheduledTournaments(params: OperationParamsMap["sofascore-scheduled-tournaments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["sofascore-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  seasonEvents(params: OperationParamsMap["sofascore-season-events"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sports(params?: OperationParamsMap["sofascore-sports"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  standings(params: OperationParamsMap["sofascore-standings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  team(params: OperationParamsMap["sofascore-team"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamEvents(params: OperationParamsMap["sofascore-team-events"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamOfTheWeek(params: OperationParamsMap["sofascore-team-of-the-week"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamOfTheWeekPeriods(params: OperationParamsMap["sofascore-team-of-the-week-periods"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamPlayers(params: OperationParamsMap["sofascore-team-players"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamSeasonStatistics(params: OperationParamsMap["sofascore-team-season-statistics"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamStatisticsSeasons(params: OperationParamsMap["sofascore-team-statistics-seasons"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamTransfers(params: OperationParamsMap["sofascore-team-transfers"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentInfo(params: OperationParamsMap["sofascore-tournament-info"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentPlayerStatistics(params: OperationParamsMap["sofascore-tournament-player-statistics"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentRounds(params: OperationParamsMap["sofascore-tournament-rounds"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentSeasons(params: OperationParamsMap["sofascore-tournament-seasons"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentTopPlayers(params: OperationParamsMap["sofascore-tournament-top-players"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentTopTeams(params: OperationParamsMap["sofascore-tournament-top-teams"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categories(params: OperationParamsMap["sofascore-categories"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categoryTournaments(params: OperationParamsMap["sofascore-category-tournaments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  event(params: OperationParamsMap["sofascore-event"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventBestPlayers(params: OperationParamsMap["sofascore-event-best-players"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventComments(params: OperationParamsMap["sofascore-event-comments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventGraph(params: OperationParamsMap["sofascore-event-graph"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventH2h(params: OperationParamsMap["sofascore-event-h2h"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventIncidents(params: OperationParamsMap["sofascore-event-incidents"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventLineups(params: OperationParamsMap["sofascore-event-lineups"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventOdds(params: OperationParamsMap["sofascore-event-odds"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventPlayerStatistics(params: OperationParamsMap["sofascore-event-player-statistics"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventShotmap(params: OperationParamsMap["sofascore-event-shotmap"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventStatistics(params: OperationParamsMap["sofascore-event-statistics"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  liveEvents(params: OperationParamsMap["sofascore-live-events"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  manager(params: OperationParamsMap["sofascore-manager"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  managerEvents(params: OperationParamsMap["sofascore-manager-events"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  player(params: OperationParamsMap["sofascore-player"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerSeasonStatistics(params: OperationParamsMap["sofascore-player-season-statistics"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerStatisticsSeasons(params: OperationParamsMap["sofascore-player-statistics-seasons"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerTransfers(params: OperationParamsMap["sofascore-player-transfers"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  rankingTypes(params?: OperationParamsMap["sofascore-ranking-types"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  rankings(params: OperationParamsMap["sofascore-rankings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  roundEvents(params: OperationParamsMap["sofascore-round-events"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  scheduledEvents(params: OperationParamsMap["sofascore-scheduled-events"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  scheduledTournaments(params: OperationParamsMap["sofascore-scheduled-tournaments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["sofascore-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  seasonEvents(params: OperationParamsMap["sofascore-season-events"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sports(params?: OperationParamsMap["sofascore-sports"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  standings(params: OperationParamsMap["sofascore-standings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  team(params: OperationParamsMap["sofascore-team"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamEvents(params: OperationParamsMap["sofascore-team-events"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamOfTheWeek(params: OperationParamsMap["sofascore-team-of-the-week"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamOfTheWeekPeriods(params: OperationParamsMap["sofascore-team-of-the-week-periods"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamPlayers(params: OperationParamsMap["sofascore-team-players"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamSeasonStatistics(params: OperationParamsMap["sofascore-team-season-statistics"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamStatisticsSeasons(params: OperationParamsMap["sofascore-team-statistics-seasons"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamTransfers(params: OperationParamsMap["sofascore-team-transfers"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentInfo(params: OperationParamsMap["sofascore-tournament-info"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentPlayerStatistics(params: OperationParamsMap["sofascore-tournament-player-statistics"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentRounds(params: OperationParamsMap["sofascore-tournament-rounds"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentSeasons(params: OperationParamsMap["sofascore-tournament-seasons"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentTopPlayers(params: OperationParamsMap["sofascore-tournament-top-players"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentTopTeams(params: OperationParamsMap["sofascore-tournament-top-teams"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  categories(...args: OperationRequestArgs<"sofascore-categories">): Promise<OperationResponseMap["sofascore-categories"]>;
  categoryTournaments(...args: OperationRequestArgs<"sofascore-category-tournaments">): Promise<OperationResponseMap["sofascore-category-tournaments"]>;
  event(...args: OperationRequestArgs<"sofascore-event">): Promise<OperationResponseMap["sofascore-event"]>;
  eventBestPlayers(...args: OperationRequestArgs<"sofascore-event-best-players">): Promise<OperationResponseMap["sofascore-event-best-players"]>;
  eventComments(...args: OperationRequestArgs<"sofascore-event-comments">): Promise<OperationResponseMap["sofascore-event-comments"]>;
  eventGraph(...args: OperationRequestArgs<"sofascore-event-graph">): Promise<OperationResponseMap["sofascore-event-graph"]>;
  eventH2h(...args: OperationRequestArgs<"sofascore-event-h2h">): Promise<OperationResponseMap["sofascore-event-h2h"]>;
  eventIncidents(...args: OperationRequestArgs<"sofascore-event-incidents">): Promise<OperationResponseMap["sofascore-event-incidents"]>;
  eventLineups(...args: OperationRequestArgs<"sofascore-event-lineups">): Promise<OperationResponseMap["sofascore-event-lineups"]>;
  eventOdds(...args: OperationRequestArgs<"sofascore-event-odds">): Promise<OperationResponseMap["sofascore-event-odds"]>;
  eventPlayerStatistics(...args: OperationRequestArgs<"sofascore-event-player-statistics">): Promise<OperationResponseMap["sofascore-event-player-statistics"]>;
  eventShotmap(...args: OperationRequestArgs<"sofascore-event-shotmap">): Promise<OperationResponseMap["sofascore-event-shotmap"]>;
  eventStatistics(...args: OperationRequestArgs<"sofascore-event-statistics">): Promise<OperationResponseMap["sofascore-event-statistics"]>;
  liveEvents(...args: OperationRequestArgs<"sofascore-live-events">): Promise<OperationResponseMap["sofascore-live-events"]>;
  manager(...args: OperationRequestArgs<"sofascore-manager">): Promise<OperationResponseMap["sofascore-manager"]>;
  managerEvents(...args: OperationRequestArgs<"sofascore-manager-events">): Promise<OperationResponseMap["sofascore-manager-events"]>;
  player(...args: OperationRequestArgs<"sofascore-player">): Promise<OperationResponseMap["sofascore-player"]>;
  playerSeasonStatistics(...args: OperationRequestArgs<"sofascore-player-season-statistics">): Promise<OperationResponseMap["sofascore-player-season-statistics"]>;
  playerStatisticsSeasons(...args: OperationRequestArgs<"sofascore-player-statistics-seasons">): Promise<OperationResponseMap["sofascore-player-statistics-seasons"]>;
  playerTransfers(...args: OperationRequestArgs<"sofascore-player-transfers">): Promise<OperationResponseMap["sofascore-player-transfers"]>;
  rankingTypes(...args: OperationRequestArgs<"sofascore-ranking-types">): Promise<OperationResponseMap["sofascore-ranking-types"]>;
  rankings(...args: OperationRequestArgs<"sofascore-rankings">): Promise<OperationResponseMap["sofascore-rankings"]>;
  roundEvents(...args: OperationRequestArgs<"sofascore-round-events">): Promise<OperationResponseMap["sofascore-round-events"]>;
  scheduledEvents(...args: OperationRequestArgs<"sofascore-scheduled-events">): Promise<OperationResponseMap["sofascore-scheduled-events"]>;
  scheduledTournaments(...args: OperationRequestArgs<"sofascore-scheduled-tournaments">): Promise<OperationResponseMap["sofascore-scheduled-tournaments"]>;
  search(...args: OperationRequestArgs<"sofascore-search">): Promise<OperationResponseMap["sofascore-search"]>;
  seasonEvents(...args: OperationRequestArgs<"sofascore-season-events">): Promise<OperationResponseMap["sofascore-season-events"]>;
  sports(...args: OperationRequestArgs<"sofascore-sports">): Promise<OperationResponseMap["sofascore-sports"]>;
  standings(...args: OperationRequestArgs<"sofascore-standings">): Promise<OperationResponseMap["sofascore-standings"]>;
  team(...args: OperationRequestArgs<"sofascore-team">): Promise<OperationResponseMap["sofascore-team"]>;
  teamEvents(...args: OperationRequestArgs<"sofascore-team-events">): Promise<OperationResponseMap["sofascore-team-events"]>;
  teamOfTheWeek(...args: OperationRequestArgs<"sofascore-team-of-the-week">): Promise<OperationResponseMap["sofascore-team-of-the-week"]>;
  teamOfTheWeekPeriods(...args: OperationRequestArgs<"sofascore-team-of-the-week-periods">): Promise<OperationResponseMap["sofascore-team-of-the-week-periods"]>;
  teamPlayers(...args: OperationRequestArgs<"sofascore-team-players">): Promise<OperationResponseMap["sofascore-team-players"]>;
  teamSeasonStatistics(...args: OperationRequestArgs<"sofascore-team-season-statistics">): Promise<OperationResponseMap["sofascore-team-season-statistics"]>;
  teamStatisticsSeasons(...args: OperationRequestArgs<"sofascore-team-statistics-seasons">): Promise<OperationResponseMap["sofascore-team-statistics-seasons"]>;
  teamTransfers(...args: OperationRequestArgs<"sofascore-team-transfers">): Promise<OperationResponseMap["sofascore-team-transfers"]>;
  tournamentInfo(...args: OperationRequestArgs<"sofascore-tournament-info">): Promise<OperationResponseMap["sofascore-tournament-info"]>;
  tournamentPlayerStatistics(...args: OperationRequestArgs<"sofascore-tournament-player-statistics">): Promise<OperationResponseMap["sofascore-tournament-player-statistics"]>;
  tournamentRounds(...args: OperationRequestArgs<"sofascore-tournament-rounds">): Promise<OperationResponseMap["sofascore-tournament-rounds"]>;
  tournamentSeasons(...args: OperationRequestArgs<"sofascore-tournament-seasons">): Promise<OperationResponseMap["sofascore-tournament-seasons"]>;
  tournamentTopPlayers(...args: OperationRequestArgs<"sofascore-tournament-top-players">): Promise<OperationResponseMap["sofascore-tournament-top-players"]>;
  tournamentTopTeams(...args: OperationRequestArgs<"sofascore-tournament-top-teams">): Promise<OperationResponseMap["sofascore-tournament-top-teams"]>;
}
export { SofascoreClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default SofascoreClient;
