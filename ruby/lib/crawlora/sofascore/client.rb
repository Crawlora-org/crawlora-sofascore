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
      {"sofascore-categories": {"id": "sofascore-categories", "method": "GET", "params": [{"description": "Sport key", "enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "football"}], "path": "/sofascore/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-category-tournaments": {"id": "sofascore-category-tournaments", "method": "GET", "params": [{"description": "Numeric SofaScore category id from the categories endpoint", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "1"}], "path": "/sofascore/category-tournaments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event": {"id": "sofascore-event", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-best-players": {"id": "sofascore-event-best-players", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-best-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-comments": {"id": "sofascore-event-comments", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-comments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-graph": {"id": "sofascore-event-graph", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-graph", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-h2h": {"id": "sofascore-event-h2h", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-h2h", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-incidents": {"id": "sofascore-event-incidents", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-incidents", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-lineups": {"id": "sofascore-event-lineups", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-lineups", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-odds": {"id": "sofascore-event-odds", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-odds", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-player-statistics": {"id": "sofascore-event-player-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}, {"description": "Numeric SofaScore player id that took part in the match", "in": "query", "name": "player_id", "required": true, "type": "string", "x-example": "839956"}], "path": "/sofascore/event-player-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "player_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-shotmap": {"id": "sofascore-event-shotmap", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "16363867"}], "path": "/sofascore/event-shotmap", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-statistics": {"id": "sofascore-event-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-live-events": {"id": "sofascore-live-events", "method": "GET", "params": [{"description": "Sport key", "enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "football"}], "path": "/sofascore/live-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-manager": {"id": "sofascore-manager", "method": "GET", "params": [{"description": "Numeric SofaScore manager id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "794873"}], "path": "/sofascore/manager", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-manager-events": {"id": "sofascore-manager-events", "method": "GET", "params": [{"description": "Numeric SofaScore manager id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "794873"}, {"description": "Zero-based page number", "in": "query", "name": "page", "type": "integer", "x-example": 0}], "path": "/sofascore/manager-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-player": {"id": "sofascore-player", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "855833"}], "path": "/sofascore/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-season-statistics": {"id": "sofascore-player-season-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}, {"description": "Numeric SofaScore unique-tournament (competition) id from player-statistics-seasons", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id from player-statistics-seasons", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"default": "overall", "description": "Statistics view", "enum": ["overall", "home", "away", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}], "path": "/sofascore/player-season-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["overall", "home", "away", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-statistics-seasons": {"id": "sofascore-player-statistics-seasons", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}], "path": "/sofascore/player-statistics-seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player-transfers": {"id": "sofascore-player-transfers", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "839956"}], "path": "/sofascore/player-transfers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-ranking-types": {"id": "sofascore-ranking-types", "method": "GET", "params": [], "path": "/sofascore/ranking-types", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "sofascore-rankings": {"id": "sofascore-rankings", "method": "GET", "params": [{"description": "Ranking id from sofascore-ranking-types", "enum": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 34, 35, 36, 37, 40, 41, 42, 43, 44, 45, 46], "in": "query", "name": "type", "required": true, "type": "integer", "x-example": 5}, {"description": "Return only the first N rows, 1 to 500. Omit to return every row", "in": "query", "maximum": 500, "minimum": 1, "name": "limit", "type": "integer", "x-example": 10}], "path": "/sofascore/rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "34", "35", "36", "37", "40", "41", "42", "43", "44", "45", "46"], "in": "query", "name": "type", "required": true, "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-round-events": {"id": "sofascore-round-events", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "76986"}, {"description": "Round number", "in": "query", "name": "round", "required": true, "type": "integer", "x-example": 1}, {"description": "Round slug from tournament-rounds, for example round-of-16; required for knockout and named cup rounds", "in": "query", "name": "slug", "type": "string", "x-example": "round-of-16"}, {"description": "Round prefix from tournament-rounds, for example Qualification; only valid together with slug", "in": "query", "name": "prefix", "type": "string", "x-example": "Qualification"}], "path": "/sofascore/round-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"in": "query", "name": "round", "required": true, "type": "integer"}, {"in": "query", "name": "slug", "type": "string"}, {"in": "query", "name": "prefix", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-scheduled-events": {"id": "sofascore-scheduled-events", "method": "GET", "params": [{"description": "Numeric SofaScore category id from the categories endpoint", "in": "query", "name": "category_id", "required": true, "type": "string", "x-example": "13"}, {"description": "UTC calendar date, YYYY-MM-DD", "in": "query", "name": "date", "required": true, "type": "string", "x-example": "2026-10-08"}], "path": "/sofascore/scheduled-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "category_id", "required": true, "type": "string"}, {"in": "query", "name": "date", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-scheduled-tournaments": {"id": "sofascore-scheduled-tournaments", "method": "GET", "params": [{"description": "Sport key", "enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "football"}, {"description": "UTC calendar date, YYYY-MM-DD", "in": "query", "name": "date", "required": true, "type": "string", "x-example": "2026-10-08"}, {"description": "One-based page number; defaults to 1", "in": "query", "maximum": 100, "minimum": 1, "name": "page", "type": "integer", "x-example": 1}], "path": "/sofascore/scheduled-tournaments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["american-football", "aussie-rules", "badminton", "bandy", "baseball", "basketball", "beach-volley", "cricket", "darts", "esports", "floorball", "football", "futsal", "handball", "ice-hockey", "mma", "minifootball", "padel", "rugby", "snooker", "table-tennis", "tennis", "volleyball", "waterpolo"], "in": "query", "name": "sport", "required": true, "type": "string"}, {"in": "query", "name": "date", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-search": {"id": "sofascore-search", "method": "GET", "params": [{"description": "Free-text search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "barcelona"}], "path": "/sofascore/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-season-events": {"id": "sofascore-season-events", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"description": "Upcoming fixtures or finished results", "enum": ["next", "last"], "in": "query", "name": "direction", "required": true, "type": "string", "x-example": "last"}, {"description": "Zero-based page number. Defaults to 0", "in": "query", "minimum": 0, "name": "page", "type": "integer", "x-example": 0}], "path": "/sofascore/season-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["next", "last"], "in": "query", "name": "direction", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-sports": {"id": "sofascore-sports", "method": "GET", "params": [], "path": "/sofascore/sports", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "sofascore-standings": {"id": "sofascore-standings", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "76986"}, {"description": "Standings variant", "enum": ["total", "home", "away"], "in": "query", "name": "type", "required": true, "type": "string", "x-example": "total"}], "path": "/sofascore/standings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["total", "home", "away"], "in": "query", "name": "type", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team": {"id": "sofascore-team", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2817"}], "path": "/sofascore/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-events": {"id": "sofascore-team-events", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2817"}, {"description": "Fixture direction", "enum": ["next", "last"], "in": "query", "name": "direction", "required": true, "type": "string", "x-example": "next"}, {"description": "Zero-based page number", "in": "query", "name": "page", "type": "integer", "x-example": 0}], "path": "/sofascore/team-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["next", "last"], "in": "query", "name": "direction", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-team-of-the-week": {"id": "sofascore-team-of-the-week", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"description": "Numeric period id from sofascore-team-of-the-week-periods", "in": "query", "name": "period", "required": true, "type": "string", "x-example": "29321"}], "path": "/sofascore/team-of-the-week", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"in": "query", "name": "period", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-of-the-week-periods": {"id": "sofascore-team-of-the-week-periods", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}], "path": "/sofascore/team-of-the-week-periods", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-players": {"id": "sofascore-team-players", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2817"}], "path": "/sofascore/team-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-season-statistics": {"id": "sofascore-team-season-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore unique-tournament (competition) id from team-statistics-seasons", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id from team-statistics-seasons", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"default": "overall", "description": "Statistics view", "enum": ["overall", "home", "away", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}], "path": "/sofascore/team-season-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["overall", "home", "away", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-statistics-seasons": {"id": "sofascore-team-statistics-seasons", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}], "path": "/sofascore/team-statistics-seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-transfers": {"id": "sofascore-team-transfers", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}], "path": "/sofascore/team-transfers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-info": {"id": "sofascore-tournament-info", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id. Omit for competition metadata only", "in": "query", "name": "season", "type": "string", "x-example": "96668"}], "path": "/sofascore/tournament-info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-player-statistics": {"id": "sofascore-tournament-player-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id of a football competition", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"description": "Statistic to sort by. Defaults to rating", "enum": ["rating", "goals", "expectedGoals", "assists", "successfulDribbles", "tackles", "accuratePassesPercentage", "bigChancesMissed", "totalShots", "goalConversionPercentage", "interceptions", "clearances", "errorLeadToGoal", "outfielderBlocks", "bigChancesCreated", "accuratePasses", "keyPasses", "saves", "cleanSheet", "penaltySave", "savedShotsFromInsideTheBox", "runsOut"], "in": "query", "name": "order", "type": "string", "x-example": "goals"}, {"description": "Sort direction. Defaults to desc", "enum": ["desc", "asc"], "in": "query", "name": "direction", "type": "string", "x-example": "desc"}, {"description": "How statistics are accumulated. Defaults to total", "enum": ["total", "perGame", "per90"], "in": "query", "name": "accumulation", "type": "string", "x-example": "total"}, {"description": "Statistic columns returned. Defaults to summary", "enum": ["summary", "attack", "defence", "passing", "goalkeeper"], "in": "query", "name": "group", "type": "string", "x-example": "summary"}, {"description": "Rows per page, 1 to 100. Defaults to 20", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer", "x-example": 20}, {"description": "Rows to skip. Defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer", "x-example": 0}], "path": "/sofascore/tournament-player-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["rating", "goals", "expectedGoals", "assists", "successfulDribbles", "tackles", "accuratePassesPercentage", "bigChancesMissed", "totalShots", "goalConversionPercentage", "interceptions", "clearances", "errorLeadToGoal", "outfielderBlocks", "bigChancesCreated", "accuratePasses", "keyPasses", "saves", "cleanSheet", "penaltySave", "savedShotsFromInsideTheBox", "runsOut"], "in": "query", "name": "order", "type": "string"}, {"enum": ["desc", "asc"], "in": "query", "name": "direction", "type": "string"}, {"enum": ["total", "perGame", "per90"], "in": "query", "name": "accumulation", "type": "string"}, {"enum": ["summary", "attack", "defence", "passing", "goalkeeper"], "in": "query", "name": "group", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-rounds": {"id": "sofascore-tournament-rounds", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "7"}, {"description": "Numeric SofaScore season id from tournament-seasons", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "76953"}], "path": "/sofascore/tournament-rounds", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-seasons": {"id": "sofascore-tournament-seasons", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}], "path": "/sofascore/tournament-seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-top-players": {"id": "sofascore-tournament-top-players", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"description": "Statistics scope. Defaults to overall", "enum": ["overall", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string", "x-example": "overall"}, {"description": "Rows per category, 1 to 50. Omit to return every row", "in": "query", "maximum": 50, "minimum": 1, "name": "limit", "type": "integer", "x-example": 5}], "path": "/sofascore/tournament-top-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["overall", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-top-teams": {"id": "sofascore-tournament-top-teams", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "96668"}, {"description": "Statistics scope. Defaults to overall", "enum": ["overall", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string", "x-example": "overall"}, {"description": "Rows per category, 1 to 50. Omit to return every row", "in": "query", "maximum": 50, "minimum": 1, "name": "limit", "type": "integer", "x-example": 5}], "path": "/sofascore/tournament-top-teams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["overall", "regular_season", "playoffs"], "in": "query", "name": "type", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["sofascore-categories", "sofascore-category-tournaments", "sofascore-event", "sofascore-event-best-players", "sofascore-event-comments", "sofascore-event-graph", "sofascore-event-h2h", "sofascore-event-incidents", "sofascore-event-lineups", "sofascore-event-odds", "sofascore-event-player-statistics", "sofascore-event-shotmap", "sofascore-event-statistics", "sofascore-live-events", "sofascore-manager", "sofascore-manager-events", "sofascore-player", "sofascore-player-season-statistics", "sofascore-player-statistics-seasons", "sofascore-player-transfers", "sofascore-ranking-types", "sofascore-rankings", "sofascore-round-events", "sofascore-scheduled-events", "sofascore-scheduled-tournaments", "sofascore-search", "sofascore-season-events", "sofascore-sports", "sofascore-standings", "sofascore-team", "sofascore-team-events", "sofascore-team-of-the-week", "sofascore-team-of-the-week-periods", "sofascore-team-players", "sofascore-team-season-statistics", "sofascore-team-statistics-seasons", "sofascore-team-transfers", "sofascore-tournament-info", "sofascore-tournament-player-statistics", "sofascore-tournament-rounds", "sofascore-tournament-seasons", "sofascore-tournament-top-players", "sofascore-tournament-top-teams"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-sofascore-ruby/0.2.0", transport: nil)
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
      define_method('event') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event', params, response_type: response_type)
      end
      define_method('event_best_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-best-players', params, response_type: response_type)
      end
      define_method('event_comments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-comments', params, response_type: response_type)
      end
      define_method('event_graph') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-graph', params, response_type: response_type)
      end
      define_method('event_h2h') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-h2h', params, response_type: response_type)
      end
      define_method('event_incidents') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-incidents', params, response_type: response_type)
      end
      define_method('event_lineups') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-lineups', params, response_type: response_type)
      end
      define_method('event_odds') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-odds', params, response_type: response_type)
      end
      define_method('event_player_statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-player-statistics', params, response_type: response_type)
      end
      define_method('event_shotmap') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-shotmap', params, response_type: response_type)
      end
      define_method('event_statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-statistics', params, response_type: response_type)
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
      define_method('player') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player', params, response_type: response_type)
      end
      define_method('player_season_statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-season-statistics', params, response_type: response_type)
      end
      define_method('player_statistics_seasons') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player-statistics-seasons', params, response_type: response_type)
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
      define_method('season_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-season-events', params, response_type: response_type)
      end
      define_method('sports') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-sports', params, response_type: response_type)
      end
      define_method('standings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-standings', params, response_type: response_type)
      end
      define_method('team') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team', params, response_type: response_type)
      end
      define_method('team_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-events', params, response_type: response_type)
      end
      define_method('team_of_the_week') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-of-the-week', params, response_type: response_type)
      end
      define_method('team_of_the_week_periods') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-of-the-week-periods', params, response_type: response_type)
      end
      define_method('team_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-players', params, response_type: response_type)
      end
      define_method('team_season_statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-season-statistics', params, response_type: response_type)
      end
      define_method('team_statistics_seasons') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-statistics-seasons', params, response_type: response_type)
      end
      define_method('team_transfers') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-transfers', params, response_type: response_type)
      end
      define_method('tournament_info') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-info', params, response_type: response_type)
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
      define_method('tournament_top_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-top-players', params, response_type: response_type)
      end
      define_method('tournament_top_teams') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-top-teams', params, response_type: response_type)
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
