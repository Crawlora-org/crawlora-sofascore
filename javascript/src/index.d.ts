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
  event(params: OperationParamsMap["sofascore-event"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventH2h(params: OperationParamsMap["sofascore-event-h2h"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventIncidents(params: OperationParamsMap["sofascore-event-incidents"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventLineups(params: OperationParamsMap["sofascore-event-lineups"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventOdds(params: OperationParamsMap["sofascore-event-odds"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  eventStatistics(params: OperationParamsMap["sofascore-event-statistics"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  liveEvents(params: OperationParamsMap["sofascore-live-events"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  player(params: OperationParamsMap["sofascore-player"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  roundEvents(params: OperationParamsMap["sofascore-round-events"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["sofascore-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  standings(params: OperationParamsMap["sofascore-standings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  team(params: OperationParamsMap["sofascore-team"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamEvents(params: OperationParamsMap["sofascore-team-events"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamPlayers(params: OperationParamsMap["sofascore-team-players"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentSeasons(params: OperationParamsMap["sofascore-tournament-seasons"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  event(params: OperationParamsMap["sofascore-event"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventH2h(params: OperationParamsMap["sofascore-event-h2h"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventIncidents(params: OperationParamsMap["sofascore-event-incidents"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventLineups(params: OperationParamsMap["sofascore-event-lineups"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventOdds(params: OperationParamsMap["sofascore-event-odds"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  eventStatistics(params: OperationParamsMap["sofascore-event-statistics"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  liveEvents(params: OperationParamsMap["sofascore-live-events"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  player(params: OperationParamsMap["sofascore-player"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  roundEvents(params: OperationParamsMap["sofascore-round-events"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["sofascore-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  standings(params: OperationParamsMap["sofascore-standings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  team(params: OperationParamsMap["sofascore-team"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamEvents(params: OperationParamsMap["sofascore-team-events"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamPlayers(params: OperationParamsMap["sofascore-team-players"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentSeasons(params: OperationParamsMap["sofascore-tournament-seasons"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  event(...args: OperationRequestArgs<"sofascore-event">): Promise<OperationResponseMap["sofascore-event"]>;
  eventH2h(...args: OperationRequestArgs<"sofascore-event-h2h">): Promise<OperationResponseMap["sofascore-event-h2h"]>;
  eventIncidents(...args: OperationRequestArgs<"sofascore-event-incidents">): Promise<OperationResponseMap["sofascore-event-incidents"]>;
  eventLineups(...args: OperationRequestArgs<"sofascore-event-lineups">): Promise<OperationResponseMap["sofascore-event-lineups"]>;
  eventOdds(...args: OperationRequestArgs<"sofascore-event-odds">): Promise<OperationResponseMap["sofascore-event-odds"]>;
  eventStatistics(...args: OperationRequestArgs<"sofascore-event-statistics">): Promise<OperationResponseMap["sofascore-event-statistics"]>;
  liveEvents(...args: OperationRequestArgs<"sofascore-live-events">): Promise<OperationResponseMap["sofascore-live-events"]>;
  player(...args: OperationRequestArgs<"sofascore-player">): Promise<OperationResponseMap["sofascore-player"]>;
  roundEvents(...args: OperationRequestArgs<"sofascore-round-events">): Promise<OperationResponseMap["sofascore-round-events"]>;
  search(...args: OperationRequestArgs<"sofascore-search">): Promise<OperationResponseMap["sofascore-search"]>;
  standings(...args: OperationRequestArgs<"sofascore-standings">): Promise<OperationResponseMap["sofascore-standings"]>;
  team(...args: OperationRequestArgs<"sofascore-team">): Promise<OperationResponseMap["sofascore-team"]>;
  teamEvents(...args: OperationRequestArgs<"sofascore-team-events">): Promise<OperationResponseMap["sofascore-team-events"]>;
  teamPlayers(...args: OperationRequestArgs<"sofascore-team-players">): Promise<OperationResponseMap["sofascore-team-players"]>;
  tournamentSeasons(...args: OperationRequestArgs<"sofascore-tournament-seasons">): Promise<OperationResponseMap["sofascore-tournament-seasons"]>;
}
export { SofascoreClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default SofascoreClient;
