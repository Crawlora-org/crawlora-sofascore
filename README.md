# SofaScore clients for Crawlora

Official Crawlora client packages for the hosted SofaScore API. These packages send requests to Crawlora's API and require a Crawlora account and `CRAWLORA_API_KEY`; service usage follows your Crawlora account billing plan.

The packages do not run a browser or scrape SofaScore locally. Crawlora is an independent service and is not affiliated with or endorsed by SofaScore or its owners.

- JavaScript / TypeScript: [`@crawlora-org/sofascore`](javascript/README.md)
- Python: [`crawlora-sofascore`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-sofascore`](go.mod)
- Ruby: [`crawlora-sofascore`](ruby/README.md)
- Java: [`net.crawlora:crawlora-sofascore:0.2.0`](java/README.md)
- PHP: [`crawlora/sofascore`](php/README.md)
- Full endpoint and parameter reference: [docs/usage.md](docs/usage.md)
- Runnable samples: [examples/](examples/)
- Source repository: [https://github.com/Crawlora-org/crawlora-sofascore](https://github.com/Crawlora-org/crawlora-sofascore)

Create an account at [crawlora.net](https://crawlora.net/signup), open the [Crawlora console](https://crawlora.net/app) to get an API key, or read the [API documentation](https://crawlora.net/docs).

## Install

```sh
npm install @crawlora-org/sofascore
python -m pip install crawlora-sofascore
go get github.com/Crawlora-org/crawlora-sofascore@latest
gem install crawlora-sofascore
composer require crawlora/sofascore
```

For Java, add `net.crawlora:crawlora-sofascore:0.2.0` to your Maven dependencies; see [java/README.md](java/README.md).

Set your Crawlora key in the environment before running a client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

Do not commit API keys. See the language-specific READMEs for sync and async use.

## PHP example

The Packagist package is available as `crawlora/sofascore`:

```sh
composer require crawlora/sofascore
```

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$apiKey = getenv('CRAWLORA_API_KEY');
if (!$apiKey) throw new RuntimeException('Set CRAWLORA_API_KEY before running this example.');
$client = new \Crawlora\Sofascore\Client(apiKey: $apiKey);
$result = $client->request("sofascore-search", ['q' => 'Liverpool']);
print_r($result);
$client->close();
```

The same example and install details are in [php/README.md](php/README.md).

## License

MIT. See [LICENSE](LICENSE).
