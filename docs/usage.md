# SofaScore client usage

The `@crawlora-org/sofascore` and `crawlora-sofascore` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape SofaScore locally; Crawlora is independent from and not endorsed by SofaScore or its owners.

The package tracks the public API contract revision `sha256:8dc2e500465b7b7f98054def2f9794e0e433d8bbbcba6cfb688e0b6ed0ecbfcd` bundled with release `0.1.2`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 15 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `sofascore` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `event` / `event` | `GET /sofascore/event` | `id` (query, required) | SofaScore event detail |
| `eventH2h` / `event_h2h` | `GET /sofascore/event-h2h` | `id` (query, required) | SofaScore event head-to-head |
| `eventIncidents` / `event_incidents` | `GET /sofascore/event-incidents` | `id` (query, required) | SofaScore event incidents |
| `eventLineups` / `event_lineups` | `GET /sofascore/event-lineups` | `id` (query, required) | SofaScore event lineups |
| `eventOdds` / `event_odds` | `GET /sofascore/event-odds` | `id` (query, required) | SofaScore event odds |
| `eventStatistics` / `event_statistics` | `GET /sofascore/event-statistics` | `id` (query, required) | SofaScore event statistics |
| `liveEvents` / `live_events` | `GET /sofascore/live-events` | `sport` (query, required; values: `football`, `basketball`, `tennis`) | SofaScore live events |
| `player` / `player` | `GET /sofascore/player` | `id` (query, required) | SofaScore player detail |
| `roundEvents` / `round_events` | `GET /sofascore/round-events` | `id` (query, required), `season` (query, required), `round` (query, required) | SofaScore round fixtures |
| `search` / `search` | `GET /sofascore/search` | `q` (query, required) | SofaScore universal search |
| `standings` / `standings` | `GET /sofascore/standings` | `id` (query, required), `season` (query, required), `type` (query, required; values: `total`, `home`, `away`) | SofaScore standings |
| `team` / `team` | `GET /sofascore/team` | `id` (query, required) | SofaScore team detail |
| `teamEvents` / `team_events` | `GET /sofascore/team-events` | `id` (query, required), `direction` (query, required; values: `next`, `last`), `page` (query, optional) | SofaScore team fixtures |
| `teamPlayers` / `team_players` | `GET /sofascore/team-players` | `id` (query, required) | SofaScore team players |
| `tournamentSeasons` / `tournament_seasons` | `GET /sofascore/tournament-seasons` | `id` (query, required) | SofaScore competition seasons |

## Client forms

- JavaScript: import `SofascoreClient` (also exported as `Client`) from `@crawlora-org/sofascore`; use `new SofascoreClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `SofascoreClient` (also exported as `Client`) from `crawlora_sofascore`; use `with SofascoreClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncSofascoreClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
