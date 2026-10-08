# Crawlora SofaScore Ruby client

This gem calls the Crawlora hosted API at `https://api.crawlora.net/api/v1`. It does not call or scrape SofaScore directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-sofascore"
```

Create an account at [crawlora.net](https://crawlora.net/signup), open the [Crawlora console](https://crawlora.net/app) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/sofascore"

client = Crawlora::Sofascore::Client.new
result = client.request("sofascore-search", JSON.parse("{\"q\": \"Liverpool\"}"))
puts result
client.close
```

Use an operation method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem contains 43 operations.

```ruby
client = Crawlora::Sofascore::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON transport.

See [Crawlora](https://crawlora.net/), the [API documentation](https://crawlora.net/docs), and [the package repository](https://github.com/Crawlora-org/crawlora-sofascore) for account setup and the operation reference.
