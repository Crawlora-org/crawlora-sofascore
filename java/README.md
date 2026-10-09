# Crawlora SofaScore Java Client

The official Java client for Crawlora's hosted SofaScore API. It calls Crawlora's hosted API with your `x-api-key`; it does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-sofascore</artifactId>
  <version>0.3.1</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=sofascore-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=sofascore-java-console) to get an API key.

```java
import net.crawlora.sofascore.Client;
import java.time.Duration;
import java.util.List;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.categories(Map.ofEntries(Map.entry("sport", "american-football")));
    System.out.println(result);
}
```

Each supported operation has a direct method that accepts its endpoint parameters. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. YouTube transcript formats that return text are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=sofascore-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-sofascore)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=sofascore-java-api-docs)
