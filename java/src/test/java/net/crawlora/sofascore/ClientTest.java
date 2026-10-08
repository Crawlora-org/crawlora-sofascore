package net.crawlora.sofascore;

import com.sun.net.httpserver.HttpServer;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.net.InetSocketAddress;
import java.time.Duration;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicReference;

import static org.junit.jupiter.api.Assertions.*;

class ClientTest {
    private HttpServer server;
    private volatile int status = 200;
    private volatile String contentType = "application/json";
    private volatile String body = "{\"ok\":true}";
    private volatile long delayMillis;
    private final AtomicReference<String> seenKey = new AtomicReference<>();
    private final AtomicReference<String> seenUri = new AtomicReference<>();
    private String baseUrl;

    @BeforeEach void startServer() throws Exception {
        server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        server.createContext("/", exchange -> {
            seenKey.set(exchange.getRequestHeaders().getFirst("x-api-key"));
            seenUri.set(exchange.getRequestURI().toASCIIString());
            try { if (delayMillis > 0) Thread.sleep(delayMillis); }
            catch (InterruptedException error) { Thread.currentThread().interrupt(); }
            byte[] bytes = body.getBytes(java.nio.charset.StandardCharsets.UTF_8);
            exchange.getResponseHeaders().set("Content-Type", contentType);
            exchange.sendResponseHeaders(status, bytes.length);
            try (var output = exchange.getResponseBody()) { output.write(bytes); }
        });
        server.start();
        baseUrl = "http://127.0.0.1:" + server.getAddress().getPort() + "/api/v1";
    }

    @AfterEach void stopServer() { if (server != null) server.stop(0); }

    @Test void platformCatalogIsAnExactAllowlistAndExposesDirectMethod() throws Exception {
        assertEquals(109, Client.OPERATION_IDS.size());
        assertEquals(List.of("sofascore-categories", "sofascore-category-tournaments", "sofascore-draft", "sofascore-draft-picks", "sofascore-esports-game", "sofascore-event", "sofascore-event-at-bat-pitches", "sofascore-event-at-bats", "sofascore-event-average-positions", "sofascore-event-baseball-top-performers", "sofascore-event-best-players", "sofascore-event-comments", "sofascore-event-esports-games", "sofascore-event-graph", "sofascore-event-h2h", "sofascore-event-highlights", "sofascore-event-incidents", "sofascore-event-innings", "sofascore-event-lineups", "sofascore-event-managers", "sofascore-event-odds", "sofascore-event-player-heatmap", "sofascore-event-player-statistics", "sofascore-event-point-by-point", "sofascore-event-pregame-form", "sofascore-event-shotmap", "sofascore-event-statistics", "sofascore-event-team-heatmap", "sofascore-event-team-streaks", "sofascore-event-tennis-power", "sofascore-event-tv-channels", "sofascore-event-votes", "sofascore-live-events", "sofascore-manager", "sofascore-manager-events", "sofascore-mma-card", "sofascore-mma-schedule", "sofascore-odds-dropping", "sofascore-odds-winning", "sofascore-player", "sofascore-player-attributes", "sofascore-player-events", "sofascore-player-last-year-summary", "sofascore-player-national-team-statistics", "sofascore-player-penalty-history", "sofascore-player-ratings", "sofascore-player-season-heatmap", "sofascore-player-season-statistics", "sofascore-player-statistical-rankings", "sofascore-player-statistics-seasons", "sofascore-player-tournaments", "sofascore-player-transfers", "sofascore-ranking-types", "sofascore-rankings", "sofascore-referee", "sofascore-referee-events", "sofascore-referee-statistics", "sofascore-round-events", "sofascore-scheduled-events", "sofascore-scheduled-tournaments", "sofascore-search", "sofascore-search-typed", "sofascore-season-events", "sofascore-sports", "sofascore-stage", "sofascore-stage-categories", "sofascore-stage-driver-performance", "sofascore-stage-featured", "sofascore-stage-schedule", "sofascore-stage-seasons", "sofascore-stage-standings", "sofascore-stage-substages", "sofascore-standings", "sofascore-team", "sofascore-team-achievements", "sofascore-team-events", "sofascore-team-goal-distributions", "sofascore-team-near-events", "sofascore-team-of-the-week", "sofascore-team-of-the-week-periods", "sofascore-team-performance", "sofascore-team-player-statistics", "sofascore-team-player-statistics-seasons", "sofascore-team-players", "sofascore-team-rankings", "sofascore-team-season-statistics", "sofascore-team-statistics-seasons", "sofascore-team-top-players", "sofascore-team-tournaments", "sofascore-team-transfers", "sofascore-tennis-player-grand-slam-results", "sofascore-tournament-cuptree", "sofascore-tournament-info", "sofascore-tournament-player-of-the-season", "sofascore-tournament-player-statistics", "sofascore-tournament-rounds", "sofascore-tournament-seasons", "sofascore-tournament-statistics-info", "sofascore-tournament-team-of-the-season", "sofascore-tournament-teams", "sofascore-tournament-top-players", "sofascore-tournament-top-teams", "sofascore-tournament-venues", "sofascore-tournament-winners", "sofascore-tournaments-with-feature", "sofascore-trending-events", "sofascore-trending-players", "sofascore-venue", "sofascore-venue-events"), Client.OPERATION_IDS);
        assertEquals(new java.util.TreeSet<>(Client.OPERATION_IDS), new java.util.TreeSet<>(Client.operations().keySet()));
        assertEquals(Client.OPERATION_IDS.size(), new Client("key").getOperationCount());
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertThrows(IllegalArgumentException.class, () -> client.request("instagram-search", Map.of()));
            Object result = client.request("sofascore-category-tournaments", Map.ofEntries(Map.entry("id", "value &/one")));
            assertInstanceOf(Map.class, result);
            assertEquals("test-key", seenKey.get());
            assertTrue(seenUri.get().startsWith("/api/v1/"));
            assertTrue(seenUri.get().contains("%26"), "query values should be URL encoded");
            // This operation has no path parameters to encode.
        }
    }

    @Test void directMethodUsesTheSameOperationDispatch() throws Exception {
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            Object result = Client.class.getMethod("categoryTournaments", Map.class).invoke(client, Map.ofEntries(Map.entry("id", "value &/one")));
            assertInstanceOf(Map.class, result);
        }
    }

    @Test void returnsPlainTextWhenTheHostedResponseIsText() {
        contentType = "text/plain; charset=utf-8";
        body = "line one\nline two";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            assertEquals("line one\nline two", client.request("sofascore-categories", Map.ofEntries(Map.entry("sport", "american-football"))));
        }
    }

    @Test void surfacesHttpErrorsAndTimeouts() {
        status = 422;
        body = "{\"code\":422,\"msg\":\"bad input\"}";
        try (Client client = new Client("test-key", baseUrl, Duration.ofSeconds(2))) {
            CrawloraException error = assertThrows(CrawloraException.class,
                    () -> client.request("sofascore-category-tournaments", Map.ofEntries(Map.entry("id", "value &/one"))));
            assertEquals(422, error.statusCode());
            assertTrue(error.getMessage().contains("bad input"));
        }
        status = 200;
        delayMillis = 250;
        try (Client client = new Client("test-key", baseUrl, Duration.ofMillis(20))) {
            assertThrows(CrawloraException.class, () -> client.request("sofascore-category-tournaments", Map.ofEntries(Map.entry("id", "value &/one"))));
        }
    }

    @Test void rejectsInvalidEnumsAndClosedClientCalls() {
        assertThrows(IllegalArgumentException.class, () -> new Client("key", baseUrl, Duration.ofSeconds(1)).request("sofascore-categories", Map.ofEntries(Map.entry("sport", "__invalid_java_test_enum__"))));
        Client client = new Client("key", baseUrl, Duration.ofSeconds(1));
        client.close();
        assertThrows(IllegalStateException.class, () -> client.request("sofascore-category-tournaments", Map.ofEntries(Map.entry("id", "value &/one"))));
    }
}
