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
      {"sofascore-event": {"id": "sofascore-event", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-h2h": {"id": "sofascore-event-h2h", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-h2h", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-incidents": {"id": "sofascore-event-incidents", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-incidents", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-lineups": {"id": "sofascore-event-lineups", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-lineups", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-odds": {"id": "sofascore-event-odds", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-odds", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-event-statistics": {"id": "sofascore-event-statistics", "method": "GET", "params": [{"description": "Numeric SofaScore event (match) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "14025013"}], "path": "/sofascore/event-statistics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-live-events": {"id": "sofascore-live-events", "method": "GET", "params": [{"description": "Sport key", "enum": ["football", "basketball", "tennis"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "football"}], "path": "/sofascore/live-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["football", "basketball", "tennis"], "in": "query", "name": "sport", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-player": {"id": "sofascore-player", "method": "GET", "params": [{"description": "Numeric SofaScore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "855833"}], "path": "/sofascore/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-round-events": {"id": "sofascore-round-events", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "76986"}, {"description": "Round number", "in": "query", "name": "round", "required": true, "type": "integer", "x-example": 1}], "path": "/sofascore/round-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"in": "query", "name": "round", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-search": {"id": "sofascore-search", "method": "GET", "params": [{"description": "Free-text search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "barcelona"}], "path": "/sofascore/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-standings": {"id": "sofascore-standings", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}, {"description": "Numeric SofaScore season id", "in": "query", "name": "season", "required": true, "type": "string", "x-example": "76986"}, {"description": "Standings variant", "enum": ["total", "home", "away"], "in": "query", "name": "type", "required": true, "type": "string", "x-example": "total"}], "path": "/sofascore/standings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "season", "required": true, "type": "string"}, {"enum": ["total", "home", "away"], "in": "query", "name": "type", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team": {"id": "sofascore-team", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2817"}], "path": "/sofascore/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-team-events": {"id": "sofascore-team-events", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2817"}, {"description": "Fixture direction", "enum": ["next", "last"], "in": "query", "name": "direction", "required": true, "type": "string", "x-example": "next"}, {"description": "Zero-based page number", "in": "query", "name": "page", "type": "integer", "x-example": 0}], "path": "/sofascore/team-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["next", "last"], "in": "query", "name": "direction", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "sofascore-team-players": {"id": "sofascore-team-players", "method": "GET", "params": [{"description": "Numeric SofaScore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "2817"}], "path": "/sofascore/team-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "sofascore-tournament-seasons": {"id": "sofascore-tournament-seasons", "method": "GET", "params": [{"description": "Numeric SofaScore unique-tournament (competition) id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "17"}], "path": "/sofascore/tournament-seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["sofascore-event", "sofascore-event-h2h", "sofascore-event-incidents", "sofascore-event-lineups", "sofascore-event-odds", "sofascore-event-statistics", "sofascore-live-events", "sofascore-player", "sofascore-round-events", "sofascore-search", "sofascore-standings", "sofascore-team", "sofascore-team-events", "sofascore-team-players", "sofascore-tournament-seasons"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-sofascore-ruby/0.1.4", transport: nil)
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

            define_method('event') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event', params, response_type: response_type)
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
      define_method('event_statistics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-event-statistics', params, response_type: response_type)
      end
      define_method('live_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-live-events', params, response_type: response_type)
      end
      define_method('player') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-player', params, response_type: response_type)
      end
      define_method('round_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-round-events', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-search', params, response_type: response_type)
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
      define_method('team_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-team-players', params, response_type: response_type)
      end
      define_method('tournament_seasons') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('sofascore-tournament-seasons', params, response_type: response_type)
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
