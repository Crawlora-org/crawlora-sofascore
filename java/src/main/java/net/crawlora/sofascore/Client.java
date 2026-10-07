package net.crawlora.sofascore;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the SofaScore endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 43;
    public static final List<String> OPERATION_IDS = List.of(
            "sofascore-categories",
            "sofascore-category-tournaments",
            "sofascore-event",
            "sofascore-event-best-players",
            "sofascore-event-comments",
            "sofascore-event-graph",
            "sofascore-event-h2h",
            "sofascore-event-incidents",
            "sofascore-event-lineups",
            "sofascore-event-odds",
            "sofascore-event-player-statistics",
            "sofascore-event-shotmap",
            "sofascore-event-statistics",
            "sofascore-live-events",
            "sofascore-manager",
            "sofascore-manager-events",
            "sofascore-player",
            "sofascore-player-season-statistics",
            "sofascore-player-statistics-seasons",
            "sofascore-player-transfers",
            "sofascore-ranking-types",
            "sofascore-rankings",
            "sofascore-round-events",
            "sofascore-scheduled-events",
            "sofascore-scheduled-tournaments",
            "sofascore-search",
            "sofascore-season-events",
            "sofascore-sports",
            "sofascore-standings",
            "sofascore-team",
            "sofascore-team-events",
            "sofascore-team-of-the-week",
            "sofascore-team-of-the-week-periods",
            "sofascore-team-players",
            "sofascore-team-season-statistics",
            "sofascore-team-statistics-seasons",
            "sofascore-team-transfers",
            "sofascore-tournament-info",
            "sofascore-tournament-player-statistics",
            "sofascore-tournament-rounds",
            "sofascore-tournament-seasons",
            "sofascore-tournament-top-players",
            "sofascore-tournament-top-teams"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("sofascore-categories", new Operation("sofascore-categories", "GET", "/sofascore/categories", Map.ofEntries(Map.entry("sport", new Param("sport", "query", true, "string", List.of("american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"), "csv"))), List.of("application/json")));
        operations.put("sofascore-category-tournaments", new Operation("sofascore-category-tournaments", "GET", "/sofascore/category-tournaments", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-event", new Operation("sofascore-event", "GET", "/sofascore/event", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-event-best-players", new Operation("sofascore-event-best-players", "GET", "/sofascore/event-best-players", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-event-comments", new Operation("sofascore-event-comments", "GET", "/sofascore/event-comments", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-event-graph", new Operation("sofascore-event-graph", "GET", "/sofascore/event-graph", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-event-h2h", new Operation("sofascore-event-h2h", "GET", "/sofascore/event-h2h", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-event-incidents", new Operation("sofascore-event-incidents", "GET", "/sofascore/event-incidents", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-event-lineups", new Operation("sofascore-event-lineups", "GET", "/sofascore/event-lineups", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-event-odds", new Operation("sofascore-event-odds", "GET", "/sofascore/event-odds", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-event-player-statistics", new Operation("sofascore-event-player-statistics", "GET", "/sofascore/event-player-statistics", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("player_id", new Param("player_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-event-shotmap", new Operation("sofascore-event-shotmap", "GET", "/sofascore/event-shotmap", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-event-statistics", new Operation("sofascore-event-statistics", "GET", "/sofascore/event-statistics", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-live-events", new Operation("sofascore-live-events", "GET", "/sofascore/live-events", Map.ofEntries(Map.entry("sport", new Param("sport", "query", true, "string", List.of("american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"), "csv"))), List.of("application/json")));
        operations.put("sofascore-manager", new Operation("sofascore-manager", "GET", "/sofascore/manager", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-manager-events", new Operation("sofascore-manager-events", "GET", "/sofascore/manager-events", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-player", new Operation("sofascore-player", "GET", "/sofascore/player", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-player-season-statistics", new Operation("sofascore-player-season-statistics", "GET", "/sofascore/player-season-statistics", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("tournament_id", new Param("tournament_id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("overall", "home", "away", "regular_season", "playoffs"), "csv"))), List.of("application/json")));
        operations.put("sofascore-player-statistics-seasons", new Operation("sofascore-player-statistics-seasons", "GET", "/sofascore/player-statistics-seasons", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-player-transfers", new Operation("sofascore-player-transfers", "GET", "/sofascore/player-transfers", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-ranking-types", new Operation("sofascore-ranking-types", "GET", "/sofascore/ranking-types", Map.of(), List.of("application/json")));
        operations.put("sofascore-rankings", new Operation("sofascore-rankings", "GET", "/sofascore/rankings", Map.ofEntries(Map.entry("type", new Param("type", "query", true, "integer", List.of("1", "2", "3", "4", "5", "6", "7", "8", "9", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "34", "35", "36", "37", "40", "41", "42", "43", "44", "45", "46"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-round-events", new Operation("sofascore-round-events", "GET", "/sofascore/round-events", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "string", List.of(), "csv")), Map.entry("round", new Param("round", "query", true, "integer", List.of(), "csv")), Map.entry("slug", new Param("slug", "query", false, "string", List.of(), "csv")), Map.entry("prefix", new Param("prefix", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-scheduled-events", new Operation("sofascore-scheduled-events", "GET", "/sofascore/scheduled-events", Map.ofEntries(Map.entry("category_id", new Param("category_id", "query", true, "string", List.of(), "csv")), Map.entry("date", new Param("date", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-scheduled-tournaments", new Operation("sofascore-scheduled-tournaments", "GET", "/sofascore/scheduled-tournaments", Map.ofEntries(Map.entry("sport", new Param("sport", "query", true, "string", List.of("american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"), "csv")), Map.entry("date", new Param("date", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-search", new Operation("sofascore-search", "GET", "/sofascore/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-season-events", new Operation("sofascore-season-events", "GET", "/sofascore/season-events", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "string", List.of(), "csv")), Map.entry("direction", new Param("direction", "query", true, "string", List.of("next", "last"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-sports", new Operation("sofascore-sports", "GET", "/sofascore/sports", Map.of(), List.of("application/json")));
        operations.put("sofascore-standings", new Operation("sofascore-standings", "GET", "/sofascore/standings", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", true, "string", List.of("total", "home", "away"), "csv"))), List.of("application/json")));
        operations.put("sofascore-team", new Operation("sofascore-team", "GET", "/sofascore/team", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-team-events", new Operation("sofascore-team-events", "GET", "/sofascore/team-events", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("direction", new Param("direction", "query", true, "string", List.of("next", "last"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-team-of-the-week", new Operation("sofascore-team-of-the-week", "GET", "/sofascore/team-of-the-week", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "string", List.of(), "csv")), Map.entry("period", new Param("period", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-team-of-the-week-periods", new Operation("sofascore-team-of-the-week-periods", "GET", "/sofascore/team-of-the-week-periods", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-team-players", new Operation("sofascore-team-players", "GET", "/sofascore/team-players", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-team-season-statistics", new Operation("sofascore-team-season-statistics", "GET", "/sofascore/team-season-statistics", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("tournament_id", new Param("tournament_id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("overall", "home", "away", "regular_season", "playoffs"), "csv"))), List.of("application/json")));
        operations.put("sofascore-team-statistics-seasons", new Operation("sofascore-team-statistics-seasons", "GET", "/sofascore/team-statistics-seasons", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-team-transfers", new Operation("sofascore-team-transfers", "GET", "/sofascore/team-transfers", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-tournament-info", new Operation("sofascore-tournament-info", "GET", "/sofascore/tournament-info", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-tournament-player-statistics", new Operation("sofascore-tournament-player-statistics", "GET", "/sofascore/tournament-player-statistics", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "string", List.of(), "csv")), Map.entry("order", new Param("order", "query", false, "string", List.of("rating", "goals", "expectedGoals", "assists", "successfulDribbles", "tackles", "accuratePassesPercentage", "bigChancesMissed", "totalShots", "goalConversionPercentage", "interceptions", "clearances", "errorLeadToGoal", "outfielderBlocks", "bigChancesCreated", "accuratePasses", "keyPasses", "saves", "cleanSheet", "penaltySave", "savedShotsFromInsideTheBox", "runsOut"), "csv")), Map.entry("direction", new Param("direction", "query", false, "string", List.of("desc", "asc"), "csv")), Map.entry("accumulation", new Param("accumulation", "query", false, "string", List.of("total", "perGame", "per90"), "csv")), Map.entry("group", new Param("group", "query", false, "string", List.of("summary", "attack", "defence", "passing", "goalkeeper"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("offset", new Param("offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-tournament-rounds", new Operation("sofascore-tournament-rounds", "GET", "/sofascore/tournament-rounds", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-tournament-seasons", new Operation("sofascore-tournament-seasons", "GET", "/sofascore/tournament-seasons", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-tournament-top-players", new Operation("sofascore-tournament-top-players", "GET", "/sofascore/tournament-top-players", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("overall", "regular_season", "playoffs"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("sofascore-tournament-top-teams", new Operation("sofascore-tournament-top-teams", "GET", "/sofascore/tournament-top-teams", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("season", new Param("season", "query", true, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("overall", "regular_season", "playoffs"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown SofaScore operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest request = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation))
                .GET().build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object categories(Map<String, ?> params) { return request("sofascore-categories", params); }
    public Object categoryTournaments(Map<String, ?> params) { return request("sofascore-category-tournaments", params); }
    public Object event(Map<String, ?> params) { return request("sofascore-event", params); }
    public Object eventBestPlayers(Map<String, ?> params) { return request("sofascore-event-best-players", params); }
    public Object eventComments(Map<String, ?> params) { return request("sofascore-event-comments", params); }
    public Object eventGraph(Map<String, ?> params) { return request("sofascore-event-graph", params); }
    public Object eventH2h(Map<String, ?> params) { return request("sofascore-event-h2h", params); }
    public Object eventIncidents(Map<String, ?> params) { return request("sofascore-event-incidents", params); }
    public Object eventLineups(Map<String, ?> params) { return request("sofascore-event-lineups", params); }
    public Object eventOdds(Map<String, ?> params) { return request("sofascore-event-odds", params); }
    public Object eventPlayerStatistics(Map<String, ?> params) { return request("sofascore-event-player-statistics", params); }
    public Object eventShotmap(Map<String, ?> params) { return request("sofascore-event-shotmap", params); }
    public Object eventStatistics(Map<String, ?> params) { return request("sofascore-event-statistics", params); }
    public Object liveEvents(Map<String, ?> params) { return request("sofascore-live-events", params); }
    public Object manager(Map<String, ?> params) { return request("sofascore-manager", params); }
    public Object managerEvents(Map<String, ?> params) { return request("sofascore-manager-events", params); }
    public Object player(Map<String, ?> params) { return request("sofascore-player", params); }
    public Object playerSeasonStatistics(Map<String, ?> params) { return request("sofascore-player-season-statistics", params); }
    public Object playerStatisticsSeasons(Map<String, ?> params) { return request("sofascore-player-statistics-seasons", params); }
    public Object playerTransfers(Map<String, ?> params) { return request("sofascore-player-transfers", params); }
    public Object rankingTypes(Map<String, ?> params) { return request("sofascore-ranking-types", params); }
    public Object rankings(Map<String, ?> params) { return request("sofascore-rankings", params); }
    public Object roundEvents(Map<String, ?> params) { return request("sofascore-round-events", params); }
    public Object scheduledEvents(Map<String, ?> params) { return request("sofascore-scheduled-events", params); }
    public Object scheduledTournaments(Map<String, ?> params) { return request("sofascore-scheduled-tournaments", params); }
    public Object search(Map<String, ?> params) { return request("sofascore-search", params); }
    public Object seasonEvents(Map<String, ?> params) { return request("sofascore-season-events", params); }
    public Object sports(Map<String, ?> params) { return request("sofascore-sports", params); }
    public Object standings(Map<String, ?> params) { return request("sofascore-standings", params); }
    public Object team(Map<String, ?> params) { return request("sofascore-team", params); }
    public Object teamEvents(Map<String, ?> params) { return request("sofascore-team-events", params); }
    public Object teamOfTheWeek(Map<String, ?> params) { return request("sofascore-team-of-the-week", params); }
    public Object teamOfTheWeekPeriods(Map<String, ?> params) { return request("sofascore-team-of-the-week-periods", params); }
    public Object teamPlayers(Map<String, ?> params) { return request("sofascore-team-players", params); }
    public Object teamSeasonStatistics(Map<String, ?> params) { return request("sofascore-team-season-statistics", params); }
    public Object teamStatisticsSeasons(Map<String, ?> params) { return request("sofascore-team-statistics-seasons", params); }
    public Object teamTransfers(Map<String, ?> params) { return request("sofascore-team-transfers", params); }
    public Object tournamentInfo(Map<String, ?> params) { return request("sofascore-tournament-info", params); }
    public Object tournamentPlayerStatistics(Map<String, ?> params) { return request("sofascore-tournament-player-statistics", params); }
    public Object tournamentRounds(Map<String, ?> params) { return request("sofascore-tournament-rounds", params); }
    public Object tournamentSeasons(Map<String, ?> params) { return request("sofascore-tournament-seasons", params); }
    public Object tournamentTopPlayers(Map<String, ?> params) { return request("sofascore-tournament-top-players", params); }
    public Object tournamentTopTeams(Map<String, ?> params) { return request("sofascore-tournament-top-teams", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
