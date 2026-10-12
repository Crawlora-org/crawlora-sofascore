# crawlora-sofascore — SofaScore API client for Python

Python client for Crawlora's hosted SofaScore API. It exposes 109 API endpoints covering live events, match details, lineups, statistics, tournaments, and player/team data. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=sofascore-python-homepage); the package does not run a browser or scrape
SofaScore locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
SofaScore or its owners.

## Install

```sh
python -m pip install crawlora-sofascore
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=sofascore-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=sofascore-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_sofascore import SofascoreClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with SofascoreClient(api_key=api_key) as client:
    result_1 = client.search(q='Liverpool')
    print(result_1)
    result_2 = client.live_events(sport='football')
    print(result_2)
```

The package also exports `Client` as an alias for `SofascoreClient`. Operation
methods are available directly in snake_case and through the `sofascore`
group. The async package client is `AsyncSofascoreClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-sofascore/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-sofascore/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_sofascore import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.search(q='Liverpool')
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-sofascore/blob/main/examples/python.py) for a complete usage example.

## Supported SofaScore API endpoints

This package exposes every route below through direct snake_case methods and the `sofascore` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-sofascore/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/sofascore/categories` | `sofascore-categories` | SofaScore categories for a sport |
| `GET` | `/sofascore/category-tournaments` | `sofascore-category-tournaments` | SofaScore competitions in a category |
| `GET` | `/sofascore/draft` | `sofascore-draft` | SofaScore league draft |
| `GET` | `/sofascore/draft-picks` | `sofascore-draft-picks` | SofaScore league draft picks |
| `GET` | `/sofascore/esports-game` | `sofascore-esports-game` | SofaScore esports game detail |
| `GET` | `/sofascore/event` | `sofascore-event` | SofaScore event detail |
| `GET` | `/sofascore/event-at-bat-pitches` | `sofascore-event-at-bat-pitches` | SofaScore event at-bat pitches |
| `GET` | `/sofascore/event-at-bats` | `sofascore-event-at-bats` | SofaScore event at-bats |
| `GET` | `/sofascore/event-average-positions` | `sofascore-event-average-positions` | SofaScore event average positions |
| `GET` | `/sofascore/event-baseball-top-performers` | `sofascore-event-baseball-top-performers` | SofaScore event baseball top performers |
| `GET` | `/sofascore/event-best-players` | `sofascore-event-best-players` | SofaScore event best players |
| `GET` | `/sofascore/event-comments` | `sofascore-event-comments` | SofaScore event commentary |
| `GET` | `/sofascore/event-esports-games` | `sofascore-event-esports-games` | SofaScore event esports games |
| `GET` | `/sofascore/event-graph` | `sofascore-event-graph` | SofaScore event momentum graph |
| `GET` | `/sofascore/event-h2h` | `sofascore-event-h2h` | SofaScore event head-to-head |
| `GET` | `/sofascore/event-highlights` | `sofascore-event-highlights` | SofaScore event highlights |
| `GET` | `/sofascore/event-incidents` | `sofascore-event-incidents` | SofaScore event incidents |
| `GET` | `/sofascore/event-innings` | `sofascore-event-innings` | SofaScore event innings |
| `GET` | `/sofascore/event-lineups` | `sofascore-event-lineups` | SofaScore event lineups |
| `GET` | `/sofascore/event-managers` | `sofascore-event-managers` | SofaScore event managers |
| `GET` | `/sofascore/event-odds` | `sofascore-event-odds` | SofaScore event odds |
| `GET` | `/sofascore/event-player-heatmap` | `sofascore-event-player-heatmap` | SofaScore event player heatmap |
| `GET` | `/sofascore/event-player-statistics` | `sofascore-event-player-statistics` | SofaScore event player statistics |
| `GET` | `/sofascore/event-point-by-point` | `sofascore-event-point-by-point` | SofaScore event point-by-point |
| `GET` | `/sofascore/event-pregame-form` | `sofascore-event-pregame-form` | SofaScore event pre-game form |
| `GET` | `/sofascore/event-shotmap` | `sofascore-event-shotmap` | SofaScore event shot map |
| `GET` | `/sofascore/event-statistics` | `sofascore-event-statistics` | SofaScore event statistics |
| `GET` | `/sofascore/event-team-heatmap` | `sofascore-event-team-heatmap` | SofaScore event team heatmap |
| `GET` | `/sofascore/event-team-streaks` | `sofascore-event-team-streaks` | SofaScore event team streaks |
| `GET` | `/sofascore/event-tennis-power` | `sofascore-event-tennis-power` | SofaScore event tennis power |
| `GET` | `/sofascore/event-tv-channels` | `sofascore-event-tv-channels` | SofaScore event TV channels |
| `GET` | `/sofascore/event-votes` | `sofascore-event-votes` | SofaScore event votes |
| `GET` | `/sofascore/live-events` | `sofascore-live-events` | SofaScore live events |
| `GET` | `/sofascore/manager` | `sofascore-manager` | SofaScore manager detail |
| `GET` | `/sofascore/manager-events` | `sofascore-manager-events` | SofaScore manager recent matches |
| `GET` | `/sofascore/mma-card` | `sofascore-mma-card` | SofaScore MMA card |
| `GET` | `/sofascore/mma-schedule` | `sofascore-mma-schedule` | SofaScore MMA schedule |
| `GET` | `/sofascore/odds-dropping` | `sofascore-odds-dropping` | SofaScore dropping odds |
| `GET` | `/sofascore/odds-winning` | `sofascore-odds-winning` | SofaScore winning odds |
| `GET` | `/sofascore/player` | `sofascore-player` | SofaScore player detail |
| `GET` | `/sofascore/player-attributes` | `sofascore-player-attributes` | SofaScore player attributes and characteristics |
| `GET` | `/sofascore/player-events` | `sofascore-player-events` | SofaScore player matches with per-match numbers |
| `GET` | `/sofascore/player-last-year-summary` | `sofascore-player-last-year-summary` | SofaScore player form over the last year |
| `GET` | `/sofascore/player-national-team-statistics` | `sofascore-player-national-team-statistics` | SofaScore player national team record |
| `GET` | `/sofascore/player-penalty-history` | `sofascore-player-penalty-history` | SofaScore player penalty history |
| `GET` | `/sofascore/player-ratings` | `sofascore-player-ratings` | SofaScore player match ratings for a season |
| `GET` | `/sofascore/player-season-heatmap` | `sofascore-player-season-heatmap` | SofaScore player season heatmap |
| `GET` | `/sofascore/player-season-statistics` | `sofascore-player-season-statistics` | SofaScore player season statistics |
| `GET` | `/sofascore/player-statistical-rankings` | `sofascore-player-statistical-rankings` | SofaScore player ranking among all players in a season |
| `GET` | `/sofascore/player-statistics-seasons` | `sofascore-player-statistics-seasons` | SofaScore player statistics seasons |
| `GET` | `/sofascore/player-tournaments` | `sofascore-player-tournaments` | SofaScore player competitions |
| `GET` | `/sofascore/player-transfers` | `sofascore-player-transfers` | SofaScore player transfer history |
| `GET` | `/sofascore/ranking-types` | `sofascore-ranking-types` | SofaScore ranking catalogue |
| `GET` | `/sofascore/rankings` | `sofascore-rankings` | SofaScore rankings |
| `GET` | `/sofascore/referee` | `sofascore-referee` | SofaScore referee profile |
| `GET` | `/sofascore/referee-events` | `sofascore-referee-events` | SofaScore referee officiated matches |
| `GET` | `/sofascore/referee-statistics` | `sofascore-referee-statistics` | SofaScore referee card statistics |
| `GET` | `/sofascore/round-events` | `sofascore-round-events` | SofaScore round fixtures |
| `GET` | `/sofascore/scheduled-events` | `sofascore-scheduled-events` | SofaScore events scheduled in a category on a date |
| `GET` | `/sofascore/scheduled-tournaments` | `sofascore-scheduled-tournaments` | SofaScore tournaments scheduled on a date |
| `GET` | `/sofascore/search` | `sofascore-search` | SofaScore universal search |
| `GET` | `/sofascore/search-typed` | `sofascore-search-typed` | SofaScore search by entity type |
| `GET` | `/sofascore/season-events` | `sofascore-season-events` | SofaScore season fixtures and results |
| `GET` | `/sofascore/sports` | `sofascore-sports` | SofaScore supported sports |
| `GET` | `/sofascore/stage` | `sofascore-stage` | SofaScore motorsport and cycling stage |
| `GET` | `/sofascore/stage-categories` | `sofascore-stage-categories` | SofaScore motorsport and cycling categories and competitions |
| `GET` | `/sofascore/stage-driver-performance` | `sofascore-stage-driver-performance` | SofaScore motorsport race progress per driver |
| `GET` | `/sofascore/stage-featured` | `sofascore-stage-featured` | SofaScore featured motorsport and cycling events |
| `GET` | `/sofascore/stage-schedule` | `sofascore-stage-schedule` | SofaScore motorsport and cycling events around a date |
| `GET` | `/sofascore/stage-seasons` | `sofascore-stage-seasons` | SofaScore seasons of a motorsport or cycling competition |
| `GET` | `/sofascore/stage-standings` | `sofascore-stage-standings` | SofaScore motorsport and cycling stage standings |
| `GET` | `/sofascore/stage-substages` | `sofascore-stage-substages` | SofaScore children of a motorsport or cycling stage |
| `GET` | `/sofascore/standings` | `sofascore-standings` | SofaScore standings |
| `GET` | `/sofascore/team` | `sofascore-team` | SofaScore team detail |
| `GET` | `/sofascore/team-achievements` | `sofascore-team-achievements` | SofaScore team trophies |
| `GET` | `/sofascore/team-events` | `sofascore-team-events` | SofaScore team fixtures |
| `GET` | `/sofascore/team-goal-distributions` | `sofascore-team-goal-distributions` | SofaScore team goals by match minute |
| `GET` | `/sofascore/team-near-events` | `sofascore-team-near-events` | SofaScore team previous and next match |
| `GET` | `/sofascore/team-of-the-week` | `sofascore-team-of-the-week` | SofaScore team of the week |
| `GET` | `/sofascore/team-of-the-week-periods` | `sofascore-team-of-the-week-periods` | SofaScore team of the week periods |
| `GET` | `/sofascore/team-performance` | `sofascore-team-performance` | SofaScore team recent performance |
| `GET` | `/sofascore/team-player-statistics` | `sofascore-team-player-statistics` | SofaScore team player statistics |
| `GET` | `/sofascore/team-player-statistics-seasons` | `sofascore-team-player-statistics-seasons` | SofaScore team player statistics seasons |
| `GET` | `/sofascore/team-players` | `sofascore-team-players` | SofaScore team players |
| `GET` | `/sofascore/team-rankings` | `sofascore-team-rankings` | SofaScore team rankings |
| `GET` | `/sofascore/team-season-statistics` | `sofascore-team-season-statistics` | SofaScore team season statistics |
| `GET` | `/sofascore/team-statistics-seasons` | `sofascore-team-statistics-seasons` | SofaScore team statistics seasons |
| `GET` | `/sofascore/team-top-players` | `sofascore-team-top-players` | SofaScore team top players |
| `GET` | `/sofascore/team-tournaments` | `sofascore-team-tournaments` | SofaScore team competitions |
| `GET` | `/sofascore/team-transfers` | `sofascore-team-transfers` | SofaScore team transfers |
| `GET` | `/sofascore/tennis-player-grand-slam-results` | `sofascore-tennis-player-grand-slam-results` | SofaScore tennis player grand slam results |
| `GET` | `/sofascore/tournament-cuptree` | `sofascore-tournament-cuptree` | SofaScore competition knockout tree |
| `GET` | `/sofascore/tournament-info` | `sofascore-tournament-info` | SofaScore competition info |
| `GET` | `/sofascore/tournament-player-of-the-season` | `sofascore-tournament-player-of-the-season` | SofaScore player of the season |
| `GET` | `/sofascore/tournament-player-statistics` | `sofascore-tournament-player-statistics` | SofaScore season player statistics table |
| `GET` | `/sofascore/tournament-rounds` | `sofascore-tournament-rounds` | SofaScore competition season rounds |
| `GET` | `/sofascore/tournament-seasons` | `sofascore-tournament-seasons` | SofaScore competition seasons |
| `GET` | `/sofascore/tournament-statistics-info` | `sofascore-tournament-statistics-info` | SofaScore player statistics table filters |
| `GET` | `/sofascore/tournament-team-of-the-season` | `sofascore-tournament-team-of-the-season` | SofaScore team of the season |
| `GET` | `/sofascore/tournament-teams` | `sofascore-tournament-teams` | SofaScore teams of a competition season |
| `GET` | `/sofascore/tournament-top-players` | `sofascore-tournament-top-players` | SofaScore season top players |
| `GET` | `/sofascore/tournament-top-teams` | `sofascore-tournament-top-teams` | SofaScore season top teams |
| `GET` | `/sofascore/tournament-venues` | `sofascore-tournament-venues` | SofaScore venues of a competition season |
| `GET` | `/sofascore/tournament-winners` | `sofascore-tournament-winners` | SofaScore past winners of a competition |
| `GET` | `/sofascore/tournaments-with-feature` | `sofascore-tournaments-with-feature` | SofaScore competitions that carry a feature |
| `GET` | `/sofascore/trending-events` | `sofascore-trending-events` | SofaScore trending events |
| `GET` | `/sofascore/trending-players` | `sofascore-trending-players` | SofaScore trending players |
| `GET` | `/sofascore/venue` | `sofascore-venue` | SofaScore venue |
| `GET` | `/sofascore/venue-events` | `sofascore-venue-events` | SofaScore matches at a venue |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
