require "json"
require "net/http"
require "uri"

module Crawlora
  module Sofascore
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"sofascore-categories": {"id": "sofascore-categories", "method": "GET", "params": [{"description": "Sport key", "enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "football"}], "path": "/sofascore/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-category-tournaments": {"id": "sofascore-category-tournaments", "method": "GET", "params": [{"description": "Numeric SofaScore category id from the categories endpoint", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "1"}], "path": "/sofascore/category-tournaments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-draft": {"id": "sofascore-draft", "method": "GET", "params": [{"description": "League whose draft to return", "enum": ["nba", "nfl"], "in": "query", "name": "league", "required": true, "type": "string", "x-example": "nba"}, {"description": "Numeric SofaScore season id of the league", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "80229"}], "path": "/sofascore/draft", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["nba", "nfl"], "in": "query", "name": "league", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-draft-picks": {"id": "sofascore-draft-picks", "method": "GET", "params": [{"description": "League whose draft to return", "enum": ["nba", "nfl"], "in": "query", "name": "league", "required": true, "type": "string", "x-example": "nba"}, {"description": "Four-digit draft year", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2025"}, {"description": "Draft round: 1 to 2 for nba, 1 to 7 for nfl", "in": "query", "maximum": 7, "minimum": 1, "name": "round", "required": true, "type": "integer", "x-example": 1}], "path": "/sofascore/draft-picks", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["nba", "nfl"], "in": "query", "name": "league", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "round", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-esports-game": {"id": "sofascore-esports-game", "method": "GET", "params": [{"description": "Numeric SofaScore esports game id from sofascore-event-esports-games", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "588883"}, {"description": "Which resource of the game to return", "enum": ["statistics", "lineups", "bans", "rounds"], "in": "query", "name": "part", "required": true, "type": "string", "x-example": "lineups"}], "path": "/sofascore/esports-game", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["statistics", "lineups", "bans", "rounds"], "in": "query", "name": "part", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event": {"id": "sofascore-event", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-at-bat-pitches": {"id": "sofascore-event-at-bat-pitches", "method": "GET", "params": [{"description": "Numeric SofaScore baseball event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17199139"}, {"description": "Numeric at-bat id from sofascore-event-at-bats for the same event", "in": "query", "name": "at_bat_id", "required": true, "type": "string", "x-example": "2595879"}], "path": "/sofascore/event-at-bat-pitches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "at_bat_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-at-bats": {"id": "sofascore-event-at-bats", "method": "GET", "params": [{"description": "Numeric SofaScore baseball event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17199139"}], "path": "/sofascore/event-at-bats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-average-positions": {"id": "sofascore-event-average-positions", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-average-positions", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-baseball-top-performers": {"id": "sofascore-event-baseball-top-performers", "method": "GET", "params": [{"description": "Numeric SofaScore baseball event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17199139"}], "path": "/sofascore/event-baseball-top-performers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-best-players": {"id": "sofascore-event-best-players", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-best-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-comments": {"id": "sofascore-event-comments", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-comments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-esports-games": {"id": "sofascore-event-esports-games", "method": "GET", "params": [{"description": "Numeric SofaScore esports event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17260338"}], "path": "/sofascore/event-esports-games", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-graph": {"id": "sofascore-event-graph", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-graph", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-h2h": {"id": "sofascore-event-h2h", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-h2h", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-highlights": {"id": "sofascore-event-highlights", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-highlights", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-incidents": {"id": "sofascore-event-incidents", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-incidents", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-innings": {"id": "sofascore-event-innings", "method": "GET", "params": [{"description": "Numeric SofaScore cricket event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16253632"}], "path": "/sofascore/event-innings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-lineups": {"id": "sofascore-event-lineups", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-lineups", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-managers": {"id": "sofascore-event-managers", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-managers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-odds": {"id": "sofascore-event-odds", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-odds", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-player-heatmap": {"id": "sofascore-event-player-heatmap", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}, {"description": "Numeric SofaScore player id that played in the match", "in": "query", "name": "player_id", "required": true, "type": "string", "x-example": "839956"}], "path": "/sofascore/event-player-heatmap", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "player_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-player-statistics": {"id": "sofascore-event-player-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}, {"description": "Numeric SofaScore player id that took part in the match", "in": "query", "name": "player_id", "required": true, "type": "string", "x-example": "839956"}], "path": "/sofascore/event-player-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "player_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-point-by-point": {"id": "sofascore-event-point-by-point", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17257382"}], "path": "/sofascore/event-point-by-point", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-pregame-form": {"id": "sofascore-event-pregame-form", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-pregame-form", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-shotmap": {"id": "sofascore-event-shotmap", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-shotmap", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-statistics": {"id": "sofascore-event-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-team-heatmap": {"id": "sofascore-event-team-heatmap", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}, {"description": "Numeric SofaScore team id of the home or away side", "in": "query", "name": "team_id", "required": true, "type": "string", "x-example": "17"}], "path": "/sofascore/event-team-heatmap", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "team_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-team-streaks": {"id": "sofascore-event-team-streaks", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-team-streaks", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-tennis-power": {"id": "sofascore-event-tennis-power", "method": "GET", "params": [{"description": "Numeric SofaScore tennis event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17257382"}], "path": "/sofascore/event-tennis-power", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-tv-channels": {"id": "sofascore-event-tv-channels", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}, {"description": "Two-letter ISO 3166-1 alpha-2 country code. Omit to list the broadcasting countries only", "in": "query", "name": "country", "type": "string", "x-example": "GB"}], "path": "/sofascore/event-tv-channels", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "country", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-votes": {"id": "sofascore-event-votes", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-votes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-live-events": {"id": "sofascore-live-events", "method": "GET", "params": [{"description": "Sport key", "enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "football"}], "path": "/sofascore/live-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-manager": {"id": "sofascore-manager", "method": "GET", "params": [{"description": "Numeric SofaScore manager id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "794873"}], "path": "/sofascore/manager", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-manager-events": {"id": "sofascore-manager-events", "method": "GET", "params": [{"description": "Numeric SofaScore manager id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "794873"}, {"description": "Zero-based page number", "in": "query", "name": "page", "type": "integer", "x-example": 0}], "path": "/sofascore/manager-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-mma-card": {"id": "sofascore-mma-card", "method": "GET", "params": [{"description": "Numeric SofaScore MMA organisation id", "in": "query", "name": "org_id", "required": true, "type": "string", "x-example": "19906"}, {"description": "Numeric card id (card_id) from sofascore-mma-schedule", "in": "query", "name": "card_id", "required": true, "type": "string", "x-example": "197311"}, {"description": "Which segment of the card to return", "enum": ["all", "maincard", "prelims", "earlyprelims"], "in": "query", "name": "part", "required": true, "type": "string", "x-example": "all"}], "path": "/sofascore/mma-card", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "org_id", "required": true, "type": "string"}, {"in": "query", "name": "card_id", "required": true, "type": "string"}, {"enum": ["all", "maincard", "prelims", "earlyprelims"], "in": "query", "name": "part", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-mma-schedule": {"id": "sofascore-mma-schedule", "method": "GET", "params": [{"description": "Numeric SofaScore MMA organisation id", "in": "query", "name": "org_id", "required": true, "type": "string", "x-example": "19906"}, {"description": "Calendar month as YYYY-MM", "in": "query", "name": "month", "required": true, "type": "string", "x-example": "2026-10"}], "path": "/sofascore/mma-schedule", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "org_id", "required": true, "type": "string"}, {"in": "query", "name": "month", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-odds-dropping": {"id": "sofascore-odds-dropping", "method": "GET", "params": [{"description": "Sport key, or all for every sport. Defaults to all", "enum": ["all", "american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "type": "string", "x-example": "football"}], "path": "/sofascore/odds-dropping", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["all", "american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-odds-winning": {"id": "sofascore-odds-winning", "method": "GET", "params": [{"description": "Sport key, or all for every sport. Defaults to all", "enum": ["all", "american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "type": "string", "x-example": "football"}], "path": "/sofascore/odds-winning", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["all", "american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player": {"id": "sofascore-player", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "855833"}], "path": "/sofascore/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-attributes": {"id": "sofascore-player-attributes", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}], "path": "/sofascore/player-attributes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-events": {"id": "sofascore-player-events", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}, {"description": "Zero-based page number. Defaults to 0", "in": "query", "minimum": 0, "name": "page", "type": "integer", "x-example": 0}], "path": "/sofascore/player-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-player-last-year-summary": {"id": "sofascore-player-last-year-summary", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}], "path": "/sofascore/player-last-year-summary", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-national-team-statistics": {"id": "sofascore-player-national-team-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}], "path": "/sofascore/player-national-team-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-penalty-history": {"id": "sofascore-player-penalty-history", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}], "path": "/sofascore/player-penalty-history", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-ratings": {"id": "sofascore-player-ratings", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}, {"description": "Numeric SofaScore unique-tournament (competition) id from player-statistics-seasons", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id from player-statistics-seasons", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "76986"}, {"default": "overall", "description": "Statistics view", "enum": ["overall", "home", "away", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}], "path": "/sofascore/player-ratings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["overall", "home", "away", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-season-heatmap": {"id": "sofascore-player-season-heatmap", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}, {"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "76986"}], "path": "/sofascore/player-season-heatmap", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-season-statistics": {"id": "sofascore-player-season-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}, {"description": "Numeric SofaScore unique-tournament (competition) id from player-statistics-seasons", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id from player-statistics-seasons", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"default": "overall", "description": "Statistics view", "enum": ["overall", "home", "away", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}], "path": "/sofascore/player-season-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["overall", "home", "away", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-statistical-rankings": {"id": "sofascore-player-statistical-rankings", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}, {"description": "Numeric SofaScore season id from player-statistics-seasons", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"default": "overall", "description": "Statistics view", "enum": ["overall"], "in": "query", "name": "type", "type": "string"}], "path": "/sofascore/player-statistical-rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["overall"], "in": "query", "name": "type", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-statistics-seasons": {"id": "sofascore-player-statistics-seasons", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}], "path": "/sofascore/player-statistics-seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-tournaments": {"id": "sofascore-player-tournaments", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}], "path": "/sofascore/player-tournaments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-transfers": {"id": "sofascore-player-transfers", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}], "path": "/sofascore/player-transfers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-ranking-types": {"id": "sofascore-ranking-types", "method": "GET", "params": [], "path": "/sofascore/ranking-types", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "sofascore-rankings": {"id": "sofascore-rankings", "method": "GET", "params": [{"description": "Ranking id from sofascore-ranking-types", "enum": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46], "in": "query", "name": "type", "required": true, "type": "integer", "x-example": 5}, {"description": "Return only the first N rows, 1 to 500. Omit to return every row", "in": "query", "maximum": 500, "minimum": 1, "name": "limit", "type": "integer", "x-example": 10}], "path": "/sofascore/rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "34", "35", "36", "37", "40", "41", "42", "43", "44", "45", "46"], "in": "query", "name": "type", "required": true, "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-referee": {"id": "sofascore-referee", "method": "GET", "params": [{"description": "Numeric SofaScore referee id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "74264"}], "path": "/sofascore/referee", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-referee-events": {"id": "sofascore-referee-events", "method": "GET", "params": [{"description": "Numeric SofaScore referee id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "74264"}, {"description": "Zero-based page number. Defaults to 0", "in": "query", "minimum": 0, "name": "page", "type": "integer", "x-example": 0}], "path": "/sofascore/referee-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-referee-statistics": {"id": "sofascore-referee-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore referee id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "74264"}], "path": "/sofascore/referee-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-round-events": {"id": "sofascore-round-events", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "76986"}, {"description": "Round number", "in": "query", "name": "round", "required": true, "type": "integer", "x-example": 1}, {"description": "Round slug from tournament-rounds, for example round-of-16; required for knockout and named cup rounds", "in": "query", "name": "slug", "type": "string", "x-example": "round-of-16"}, {"description": "Round prefix from tournament-rounds, for example Qualification; only valid together with slug", "in": "query", "name": "prefix", "type": "string", "x-example": "Qualification"}], "path": "/sofascore/round-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"in": "query", "name": "round", "required": true, "type": "integer"}, {"in": "query", "name": "slug", "type": "string"}, {"in": "query", "name": "prefix", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-scheduled-events": {"id": "sofascore-scheduled-events", "method": "GET", "params": [{"description": "Numeric SofaScore category id from the categories endpoint", "in": "query", "name": "category_id", "required": true, "type": "string", "x-example": "13"}, {"description": "UTC calendar date, YYYY-MM-DD", "in": "query", "name": "date", "required": true, "type": "string", "x-example": "2026-10-08"}], "path": "/sofascore/scheduled-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "category_id", "required": true, "type": "string"}, {"in": "query", "name": "date", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-scheduled-tournaments": {"id": "sofascore-scheduled-tournaments", "method": "GET", "params": [{"description": "Sport key", "enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "football"}, {"description": "UTC calendar date, YYYY-MM-DD", "in": "query", "name": "date", "required": true, "type": "string", "x-example": "2026-10-08"}, {"description": "One-based page number; defaults to 1", "in": "query", "maximum": 100, "minimum": 1, "name": "page", "type": "integer", "x-example": 1}], "path": "/sofascore/scheduled-tournaments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string"}, {"in": "query", "name": "date", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-search": {"id": "sofascore-search", "method": "GET", "params": [{"description": "Free-text search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "barcelona"}], "path": "/sofascore/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-search-typed": {"id": "sofascore-search-typed", "method": "GET", "params": [{"description": "Entity type to search", "enum": ["events", "teams", "players", "managers", "referees", "venues", "unique_tournaments"], "in": "query", "name": "type", "required": true, "type": "string", "x-example": "teams"}, {"description": "Search text, up to 128 characters", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "arsenal"}, {"description": "Zero-based page number. Defaults to 0", "in": "query", "minimum": 0, "name": "page", "type": "integer", "x-example": 0}, {"description": "Restrict teams, players, managers or unique_tournaments to one sport", "enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "type": "string", "x-example": "football"}], "path": "/sofascore/search-typed", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["events", "teams", "players", "managers", "referees", "venues", "unique_tournaments"], "in": "query", "name": "type", "required": true, "type": "string"}, {"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-season-events": {"id": "sofascore-season-events", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"description": "Upcoming fixtures or finished results", "enum": ["next", "last"], "in": "query", "name": "direction", "required": true, "type": "string", "x-example": "last"}, {"description": "Zero-based page number. Defaults to 0", "in": "query", "minimum": 0, "name": "page", "type": "integer", "x-example": 0}], "path": "/sofascore/season-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["next", "last"], "in": "query", "name": "direction", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-sports": {"id": "sofascore-sports", "method": "GET", "params": [], "path": "/sofascore/sports", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "sofascore-stage": {"id": "sofascore-stage", "method": "GET", "params": [{"description": "Numeric SofaScore stage id from stage-schedule, stage-seasons or stage-substages", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "214258"}], "path": "/sofascore/stage", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-stage-categories": {"id": "sofascore-stage-categories", "method": "GET", "params": [{"description": "Stage sport key", "enum": ["motorsport", "cycling"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "motorsport"}], "path": "/sofascore/stage-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["motorsport", "cycling"], "in": "query", "name": "sport", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-stage-driver-performance": {"id": "sofascore-stage-driver-performance", "method": "GET", "params": [{"description": "Numeric SofaScore stage id of a finished race, sprint or rally", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "214258"}], "path": "/sofascore/stage-driver-performance", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-stage-featured": {"id": "sofascore-stage-featured", "method": "GET", "params": [{"description": "Stage sport key", "enum": ["motorsport", "cycling"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "motorsport"}], "path": "/sofascore/stage-featured", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["motorsport", "cycling"], "in": "query", "name": "sport", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-stage-schedule": {"id": "sofascore-stage-schedule", "method": "GET", "params": [{"description": "Stage sport key", "enum": ["motorsport", "cycling"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "motorsport"}, {"description": "UTC calendar date, YYYY-MM-DD", "in": "query", "name": "date", "required": true, "type": "string", "x-example": "2026-10-04"}], "path": "/sofascore/stage-schedule", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["motorsport", "cycling"], "in": "query", "name": "sport", "required": true, "type": "string"}, {"in": "query", "name": "date", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-stage-seasons": {"id": "sofascore-stage-seasons", "method": "GET", "params": [{"description": "Numeric SofaScore competition id from stage-categories", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "40"}], "path": "/sofascore/stage-seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-stage-standings": {"id": "sofascore-stage-standings", "method": "GET", "params": [{"description": "Numeric SofaScore stage id of a season, event, session or cycling stage", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "214258"}, {"description": "Classification kind", "enum": ["competitor", "team"], "in": "query", "name": "type", "required": true, "type": "string", "x-example": "competitor"}], "path": "/sofascore/stage-standings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["competitor", "team"], "in": "query", "name": "type", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-stage-substages": {"id": "sofascore-stage-substages", "method": "GET", "params": [{"description": "Numeric SofaScore stage id of a season or an event", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "214253"}], "path": "/sofascore/stage-substages", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-standings": {"id": "sofascore-standings", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "76986"}, {"description": "Standings variant", "enum": ["total", "home", "away"], "in": "query", "name": "type", "required": true, "type": "string", "x-example": "total"}], "path": "/sofascore/standings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["total", "home", "away"], "in": "query", "name": "type", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team": {"id": "sofascore-team", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2817"}], "path": "/sofascore/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-achievements": {"id": "sofascore-team-achievements", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}], "path": "/sofascore/team-achievements", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-events": {"id": "sofascore-team-events", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2817"}, {"description": "Fixture direction", "enum": ["next", "last"], "in": "query", "name": "direction", "required": true, "type": "string", "x-example": "next"}, {"description": "Zero-based page number", "in": "query", "name": "page", "type": "integer", "x-example": 0}], "path": "/sofascore/team-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["next", "last"], "in": "query", "name": "direction", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-team-goal-distributions": {"id": "sofascore-team-goal-distributions", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore unique-tournament (competition) id of a football competition", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}], "path": "/sofascore/team-goal-distributions", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-near-events": {"id": "sofascore-team-near-events", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}], "path": "/sofascore/team-near-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-of-the-week": {"id": "sofascore-team-of-the-week", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"description": "Numeric period id from sofascore-team-of-the-week-periods", "in": "query", "name": "period", "required": true, "type": "string", "x-example": "29321"}], "path": "/sofascore/team-of-the-week", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"in": "query", "name": "period", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-of-the-week-periods": {"id": "sofascore-team-of-the-week-periods", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}], "path": "/sofascore/team-of-the-week-periods", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-performance": {"id": "sofascore-team-performance", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}], "path": "/sofascore/team-performance", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-player-statistics": {"id": "sofascore-team-player-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore unique-tournament (competition) id from team-player-statistics-seasons", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id from team-player-statistics-seasons", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"default": "overall", "description": "Statistics view", "enum": ["overall", "home", "away", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}], "path": "/sofascore/team-player-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["overall", "home", "away", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-player-statistics-seasons": {"id": "sofascore-team-player-statistics-seasons", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}], "path": "/sofascore/team-player-statistics-seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-players": {"id": "sofascore-team-players", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2817"}], "path": "/sofascore/team-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-rankings": {"id": "sofascore-team-rankings", "method": "GET", "params": [{"description": "Numeric SofaScore team id (a tennis player id for tennis)", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "112783"}], "path": "/sofascore/team-rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-season-statistics": {"id": "sofascore-team-season-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore unique-tournament (competition) id from team-statistics-seasons", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id from team-statistics-seasons", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"default": "overall", "description": "Statistics view", "enum": ["overall", "home", "away", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}], "path": "/sofascore/team-season-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["overall", "home", "away", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-statistics-seasons": {"id": "sofascore-team-statistics-seasons", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}], "path": "/sofascore/team-statistics-seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-top-players": {"id": "sofascore-team-top-players", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore unique-tournament (competition) id from team-player-statistics-seasons", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id from team-player-statistics-seasons", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"default": "overall", "description": "Statistics scope", "enum": ["overall", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}, {"description": "Rows per category, 1 to 50. Omit to return every row", "in": "query", "maximum": 50, "minimum": 1, "name": "limit", "type": "integer", "x-example": 5}], "path": "/sofascore/team-top-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["overall", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-team-tournaments": {"id": "sofascore-team-tournaments", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"default": false, "description": "false returns current competitions, true returns every recorded competition", "in": "query", "name": "all", "type": "boolean"}], "path": "/sofascore/team-tournaments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "all", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "sofascore-team-transfers": {"id": "sofascore-team-transfers", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}], "path": "/sofascore/team-transfers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tennis-player-grand-slam-results": {"id": "sofascore-tennis-player-grand-slam-results", "method": "GET", "params": [{"description": "Numeric SofaScore team id of a tennis player", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14882"}], "path": "/sofascore/tennis-player-grand-slam-results", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-cuptree": {"id": "sofascore-tournament-cuptree", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id of a cup or playoff competition", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "7"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "76953"}], "path": "/sofascore/tournament-cuptree", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-info": {"id": "sofascore-tournament-info", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id. Omit for competition metadata only", "in": "query", "name": "season", "type": "string", "x-example": "96668"}], "path": "/sofascore/tournament-info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-player-of-the-season": {"id": "sofascore-tournament-player-of-the-season", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id of a finished season", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "76986"}], "path": "/sofascore/tournament-player-of-the-season", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-player-statistics": {"id": "sofascore-tournament-player-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id of a football competition", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"description": "Statistic to sort by. Defaults to rating", "enum": ["rating", "goals", "expectedGoals", "assists", "successfulDribbles", "tackles", "accuratePassesPercentage", "bigChancesMissed", "totalShots", "goalConversionPercentage", "interceptions", "clearances", "errorLeadToGoal", "outfielderBlocks", "bigChancesCreated", "accuratePasses", "keyPasses", "saves", "cleanSheet", "penaltySave", "savedShotsFromInsideTheBox", "runsOut"], "in": "query", "name": "order", "type": "string", "x-example": "goals"}, {"description": "Sort direction. Defaults to desc", "enum": ["desc", "asc"], "in": "query", "name": "direction", "type": "string", "x-example": "desc"}, {"description": "How statistics are accumulated. Defaults to total", "enum": ["total", "perGame", "per90"], "in": "query", "name": "accumulation", "type": "string", "x-example": "total"}, {"description": "Statistic columns returned. Defaults to summary", "enum": ["summary", "attack", "defence", "passing", "goalkeeper"], "in": "query", "name": "group", "type": "string", "x-example": "summary"}, {"description": "Rows per page, 1 to 100. Defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer", "x-example": 20}, {"description": "Rows to skip. Defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer", "x-example": 0}, {"collectionFormat": "csv", "description": "Team ids to keep, comma separated, up to 20 (ids from tournament-statistics-info or tournament-teams)", "in": "query", "items": {"type": "string"}, "name": "team", "type": "array", "x-example": "42"}, {"collectionFormat": "csv", "description": "Nationality codes to keep, comma separated, up to 20 (codes from tournament-statistics-info)", "in": "query", "items": {"type": "string"}, "name": "nationality", "type": "array", "x-example": "EN"}, {"collectionFormat": "csv", "description": "Position codes to keep, comma separated", "in": "query", "items": {"enum": ["G", "D", "M", "F"], "type": "string"}, "name": "position", "type": "array", "x-example": "F"}, {"description": "Keep players with at least this many appearances, 0 to 1000. Omit for no minimum", "in": "query", "maximum": 1000, "minimum": 0, "name": "min_appearances", "type": "integer", "x-example": 10}, {"description": "Keep players with at least this many minutes played, 0 to 100000. Omit for no minimum", "in": "query", "maximum": 100000, "minimum": 0, "name": "min_minutes", "type": "integer", "x-example": 900}], "path": "/sofascore/tournament-player-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["rating", "goals", "expectedGoals", "assists", "successfulDribbles", "tackles", "accuratePassesPercentage", "bigChancesMissed", "totalShots", "goalConversionPercentage", "interceptions", "clearances", "errorLeadToGoal", "outfielderBlocks", "bigChancesCreated", "accuratePasses", "keyPasses", "saves", "cleanSheet", "penaltySave", "savedShotsFromInsideTheBox", "runsOut"], "in": "query", "name": "order", "type": "string"}, {"enum": ["desc", "asc"], "in": "query", "name": "direction", "type": "string"}, {"enum": ["total", "perGame", "per90"], "in": "query", "name": "accumulation", "type": "string"}, {"enum": ["summary", "attack", "defence", "passing", "goalkeeper"], "in": "query", "name": "group", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}, {"collectionFormat": "csv", "in": "query", "name": "team", "type": "array"}, {"collectionFormat": "csv", "in": "query", "name": "nationality", "type": "array"}, {"collectionFormat": "csv", "enum": ["G", "D", "M", "F"], "in": "query", "name": "position", "type": "array"}, {"in": "query", "name": "min_appearances", "type": "integer"}, {"in": "query", "name": "min_minutes", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-rounds": {"id": "sofascore-tournament-rounds", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "7"}, {"description": "Numeric SofaScore season id from tournament-seasons", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "76953"}], "path": "/sofascore/tournament-rounds", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-seasons": {"id": "sofascore-tournament-seasons", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}], "path": "/sofascore/tournament-seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-statistics-info": {"id": "sofascore-tournament-statistics-info", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id of a football competition", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}], "path": "/sofascore/tournament-statistics-info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-team-of-the-season": {"id": "sofascore-tournament-team-of-the-season", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id of a finished season", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "76986"}], "path": "/sofascore/tournament-team-of-the-season", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-teams": {"id": "sofascore-tournament-teams", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}], "path": "/sofascore/tournament-teams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-top-players": {"id": "sofascore-tournament-top-players", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"description": "Statistics scope. Defaults to overall", "enum": ["overall", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string", "x-example": "overall"}, {"description": "Rows per category, 1 to 50. Omit to return every row", "in": "query", "maximum": 50, "minimum": 1, "name": "limit", "type": "integer", "x-example": 5}], "path": "/sofascore/tournament-top-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["overall", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-top-teams": {"id": "sofascore-tournament-top-teams", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"description": "Statistics scope. Defaults to overall", "enum": ["overall", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string", "x-example": "overall"}, {"description": "Rows per category, 1 to 50. Omit to return every row", "in": "query", "maximum": 50, "minimum": 1, "name": "limit", "type": "integer", "x-example": 5}], "path": "/sofascore/tournament-top-teams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["overall", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-venues": {"id": "sofascore-tournament-venues", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}], "path": "/sofascore/tournament-venues", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-winners": {"id": "sofascore-tournament-winners", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Zero-based page number. Defaults to 0", "in": "query", "minimum": 0, "name": "page", "type": "integer", "x-example": 0}], "path": "/sofascore/tournament-winners", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-tournaments-with-feature": {"id": "sofascore-tournaments-with-feature", "method": "GET", "params": [{"description": "Competition feature", "enum": ["cuptree", "standings", "totw", "power_rankings"], "in": "query", "name": "feature", "required": true, "type": "string", "x-example": "cuptree"}, {"description": "Sport key", "enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "minifootball", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "football"}], "path": "/sofascore/tournaments-with-feature", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cuptree", "standings", "totw", "power_rankings"], "in": "query", "name": "feature", "required": true, "type": "string"}, {"enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "minifootball", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-trending-events": {"id": "sofascore-trending-events", "method": "GET", "params": [{"description": "Two-letter ISO 3166-1 alpha-2 country code", "in": "query", "name": "country", "required": true, "type": "string", "x-example": "GB"}], "path": "/sofascore/trending-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-trending-players": {"id": "sofascore-trending-players", "method": "GET", "params": [{"description": "Sport key", "enum": ["football", "basketball"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "football"}], "path": "/sofascore/trending-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["football", "basketball"], "in": "query", "name": "sport", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-venue": {"id": "sofascore-venue", "method": "GET", "params": [{"description": "Numeric SofaScore venue id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "624"}], "path": "/sofascore/venue", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-venue-events": {"id": "sofascore-venue-events", "method": "GET", "params": [{"description": "Numeric SofaScore venue id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "624"}, {"description": "Upcoming matches or finished matches", "enum": ["next", "last"], "in": "query", "name": "direction", "required": true, "type": "string", "x-example": "last"}, {"description": "Sport filter for the venue-wide list. Defaults to all", "enum": ["all", "american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "type": "string", "x-example": "football"}, {"description": "Zero-based page number. Defaults to 0", "in": "query", "minimum": 0, "name": "page", "type": "integer", "x-example": 0}, {"description": "Numeric unique-tournament id; with season, lists that competition season's matches at the venue", "in": "query", "name": "tournament", "type": "string", "x-example": "17"}, {"description": "Numeric season id; with tournament, lists that competition season's matches at the venue", "in": "query", "name": "season", "type": "string", "x-example": "96668"}], "path": "/sofascore/venue-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["next", "last"], "in": "query", "name": "direction", "required": true, "type": "string"}, {"enum": ["all", "american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "season", "type": "string"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["sofascore-categories", "sofascore-category-tournaments", "sofascore-draft", "sofascore-draft-picks", "sofascore-esports-game", "sofascore-event", "sofascore-event-at-bat-pitches", "sofascore-event-at-bats", "sofascore-event-average-positions", "sofascore-event-baseball-top-performers", "sofascore-event-best-players", "sofascore-event-comments", "sofascore-event-esports-games", "sofascore-event-graph", "sofascore-event-h2h", "sofascore-event-highlights", "sofascore-event-incidents", "sofascore-event-innings", "sofascore-event-lineups", "sofascore-event-managers", "sofascore-event-odds", "sofascore-event-player-heatmap", "sofascore-event-player-statistics", "sofascore-event-point-by-point", "sofascore-event-pregame-form", "sofascore-event-shotmap", "sofascore-event-statistics", "sofascore-event-team-heatmap", "sofascore-event-team-streaks", "sofascore-event-tennis-power", "sofascore-event-tv-channels", "sofascore-event-votes", "sofascore-live-events", "sofascore-manager", "sofascore-manager-events", "sofascore-mma-card", "sofascore-mma-schedule", "sofascore-odds-dropping", "sofascore-odds-winning", "sofascore-player", "sofascore-player-attributes", "sofascore-player-events", "sofascore-player-last-year-summary", "sofascore-player-national-team-statistics", "sofascore-player-penalty-history", "sofascore-player-ratings", "sofascore-player-season-heatmap", "sofascore-player-season-statistics", "sofascore-player-statistical-rankings", "sofascore-player-statistics-seasons", "sofascore-player-tournaments", "sofascore-player-transfers", "sofascore-ranking-types", "sofascore-rankings", "sofascore-referee", "sofascore-referee-events", "sofascore-referee-statistics", "sofascore-round-events", "sofascore-scheduled-events", "sofascore-scheduled-tournaments", "sofascore-search", "sofascore-search-typed", "sofascore-season-events", "sofascore-sports", "sofascore-stage", "sofascore-stage-categories", "sofascore-stage-driver-performance", "sofascore-stage-featured", "sofascore-stage-schedule", "sofascore-stage-seasons", "sofascore-stage-standings", "sofascore-stage-substages", "sofascore-standings", "sofascore-team", "sofascore-team-achievements", "sofascore-team-events", "sofascore-team-goal-distributions", "sofascore-team-near-events", "sofascore-team-of-the-week", "sofascore-team-of-the-week-periods", "sofascore-team-performance", "sofascore-team-player-statistics", "sofascore-team-player-statistics-seasons", "sofascore-team-players", "sofascore-team-rankings", "sofascore-team-season-statistics", "sofascore-team-statistics-seasons", "sofascore-team-top-players", "sofascore-team-tournaments", "sofascore-team-transfers", "sofascore-tennis-player-grand-slam-results", "sofascore-tournament-cuptree", "sofascore-tournament-info", "sofascore-tournament-player-of-the-season", "sofascore-tournament-player-statistics", "sofascore-tournament-rounds", "sofascore-tournament-seasons", "sofascore-tournament-statistics-info", "sofascore-tournament-team-of-the-season", "sofascore-tournament-teams", "sofascore-tournament-top-players", "sofascore-tournament-top-teams", "sofascore-tournament-venues", "sofascore-tournament-winners", "sofascore-tournaments-with-feature", "sofascore-trending-events", "sofascore-trending-players", "sofascore-venue", "sofascore-venue-events"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-sofascore-ruby/0.3.1", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = Net::HTTP::Get.new(uri)
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = @transport.call(url, request.to_hash, @timeout)
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-categories', params, response_type: response_type)
      end
      define_method('category_tournaments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-category-tournaments', params, response_type: response_type)
      end
      define_method('draft') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-draft', params, response_type: response_type)
      end
      define_method('draft_picks') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-draft-picks', params, response_type: response_type)
      end
      define_method('esports_game') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-esports-game', params, response_type: response_type)
      end
      define_method('event') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event', params, response_type: response_type)
      end
      define_method('event_at_bat_pitches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-at-bat-pitches', params, response_type: response_type)
      end
      define_method('event_at_bats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-at-bats', params, response_type: response_type)
      end
      define_method('event_average_positions') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-average-positions', params, response_type: response_type)
      end
      define_method('event_baseball_top_performers') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-baseball-top-performers', params, response_type: response_type)
      end
      define_method('event_best_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-best-players', params, response_type: response_type)
      end
      define_method('event_comments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-comments', params, response_type: response_type)
      end
      define_method('event_esports_games') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-esports-games', params, response_type: response_type)
      end
      define_method('event_graph') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-graph', params, response_type: response_type)
      end
      define_method('event_h2h') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-h2h', params, response_type: response_type)
      end
      define_method('event_highlights') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-highlights', params, response_type: response_type)
      end
      define_method('event_incidents') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-incidents', params, response_type: response_type)
      end
      define_method('event_innings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-innings', params, response_type: response_type)
      end
      define_method('event_lineups') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-lineups', params, response_type: response_type)
      end
      define_method('event_managers') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-managers', params, response_type: response_type)
      end
      define_method('event_odds') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-odds', params, response_type: response_type)
      end
      define_method('event_player_heatmap') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-player-heatmap', params, response_type: response_type)
      end
      define_method('event_player_statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-player-statistics', params, response_type: response_type)
      end
      define_method('event_point_by_point') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-point-by-point', params, response_type: response_type)
      end
      define_method('event_pregame_form') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-pregame-form', params, response_type: response_type)
      end
      define_method('event_shotmap') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-shotmap', params, response_type: response_type)
      end
      define_method('event_statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-statistics', params, response_type: response_type)
      end
      define_method('event_team_heatmap') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-team-heatmap', params, response_type: response_type)
      end
      define_method('event_team_streaks') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-team-streaks', params, response_type: response_type)
      end
      define_method('event_tennis_power') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-tennis-power', params, response_type: response_type)
      end
      define_method('event_tv_channels') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-tv-channels', params, response_type: response_type)
      end
      define_method('event_votes') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-votes', params, response_type: response_type)
      end
      define_method('live_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-live-events', params, response_type: response_type)
      end
      define_method('manager') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-manager', params, response_type: response_type)
      end
      define_method('manager_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-manager-events', params, response_type: response_type)
      end
      define_method('mma_card') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-mma-card', params, response_type: response_type)
      end
      define_method('mma_schedule') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-mma-schedule', params, response_type: response_type)
      end
      define_method('odds_dropping') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-odds-dropping', params, response_type: response_type)
      end
      define_method('odds_winning') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-odds-winning', params, response_type: response_type)
      end
      define_method('player') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player', params, response_type: response_type)
      end
      define_method('player_attributes') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-attributes', params, response_type: response_type)
      end
      define_method('player_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-events', params, response_type: response_type)
      end
      define_method('player_last_year_summary') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-last-year-summary', params, response_type: response_type)
      end
      define_method('player_national_team_statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-national-team-statistics', params, response_type: response_type)
      end
      define_method('player_penalty_history') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-penalty-history', params, response_type: response_type)
      end
      define_method('player_ratings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-ratings', params, response_type: response_type)
      end
      define_method('player_season_heatmap') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-season-heatmap', params, response_type: response_type)
      end
      define_method('player_season_statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-season-statistics', params, response_type: response_type)
      end
      define_method('player_statistical_rankings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-statistical-rankings', params, response_type: response_type)
      end
      define_method('player_statistics_seasons') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-statistics-seasons', params, response_type: response_type)
      end
      define_method('player_tournaments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-tournaments', params, response_type: response_type)
      end
      define_method('player_transfers') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-transfers', params, response_type: response_type)
      end
      define_method('ranking_types') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-ranking-types', params, response_type: response_type)
      end
      define_method('rankings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-rankings', params, response_type: response_type)
      end
      define_method('referee') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-referee', params, response_type: response_type)
      end
      define_method('referee_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-referee-events', params, response_type: response_type)
      end
      define_method('referee_statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-referee-statistics', params, response_type: response_type)
      end
      define_method('round_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-round-events', params, response_type: response_type)
      end
      define_method('scheduled_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-scheduled-events', params, response_type: response_type)
      end
      define_method('scheduled_tournaments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-scheduled-tournaments', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-search', params, response_type: response_type)
      end
      define_method('search_typed') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-search-typed', params, response_type: response_type)
      end
      define_method('season_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-season-events', params, response_type: response_type)
      end
      define_method('sports') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-sports', params, response_type: response_type)
      end
      define_method('stage') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-stage', params, response_type: response_type)
      end
      define_method('stage_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-stage-categories', params, response_type: response_type)
      end
      define_method('stage_driver_performance') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-stage-driver-performance', params, response_type: response_type)
      end
      define_method('stage_featured') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-stage-featured', params, response_type: response_type)
      end
      define_method('stage_schedule') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-stage-schedule', params, response_type: response_type)
      end
      define_method('stage_seasons') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-stage-seasons', params, response_type: response_type)
      end
      define_method('stage_standings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-stage-standings', params, response_type: response_type)
      end
      define_method('stage_substages') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-stage-substages', params, response_type: response_type)
      end
      define_method('standings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-standings', params, response_type: response_type)
      end
      define_method('team') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team', params, response_type: response_type)
      end
      define_method('team_achievements') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-achievements', params, response_type: response_type)
      end
      define_method('team_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-events', params, response_type: response_type)
      end
      define_method('team_goal_distributions') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-goal-distributions', params, response_type: response_type)
      end
      define_method('team_near_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-near-events', params, response_type: response_type)
      end
      define_method('team_of_the_week') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-of-the-week', params, response_type: response_type)
      end
      define_method('team_of_the_week_periods') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-of-the-week-periods', params, response_type: response_type)
      end
      define_method('team_performance') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-performance', params, response_type: response_type)
      end
      define_method('team_player_statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-player-statistics', params, response_type: response_type)
      end
      define_method('team_player_statistics_seasons') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-player-statistics-seasons', params, response_type: response_type)
      end
      define_method('team_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-players', params, response_type: response_type)
      end
      define_method('team_rankings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-rankings', params, response_type: response_type)
      end
      define_method('team_season_statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-season-statistics', params, response_type: response_type)
      end
      define_method('team_statistics_seasons') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-statistics-seasons', params, response_type: response_type)
      end
      define_method('team_top_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-top-players', params, response_type: response_type)
      end
      define_method('team_tournaments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-tournaments', params, response_type: response_type)
      end
      define_method('team_transfers') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-transfers', params, response_type: response_type)
      end
      define_method('tennis_player_grand_slam_results') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tennis-player-grand-slam-results', params, response_type: response_type)
      end
      define_method('tournament_cuptree') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-cuptree', params, response_type: response_type)
      end
      define_method('tournament_info') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-info', params, response_type: response_type)
      end
      define_method('tournament_player_of_the_season') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-player-of-the-season', params, response_type: response_type)
      end
      define_method('tournament_player_statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-player-statistics', params, response_type: response_type)
      end
      define_method('tournament_rounds') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-rounds', params, response_type: response_type)
      end
      define_method('tournament_seasons') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-seasons', params, response_type: response_type)
      end
      define_method('tournament_statistics_info') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-statistics-info', params, response_type: response_type)
      end
      define_method('tournament_team_of_the_season') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-team-of-the-season', params, response_type: response_type)
      end
      define_method('tournament_teams') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-teams', params, response_type: response_type)
      end
      define_method('tournament_top_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-top-players', params, response_type: response_type)
      end
      define_method('tournament_top_teams') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-top-teams', params, response_type: response_type)
      end
      define_method('tournament_venues') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-venues', params, response_type: response_type)
      end
      define_method('tournament_winners') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-winners', params, response_type: response_type)
      end
      define_method('tournaments_with_feature') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournaments-with-feature', params, response_type: response_type)
      end
      define_method('trending_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-trending-events', params, response_type: response_type)
      end
      define_method('trending_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-trending-players', params, response_type: response_type)
      end
      define_method('venue') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-venue', params, response_type: response_type)
      end
      define_method('venue_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-venue-events', params, response_type: response_type)
      end

      private

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
