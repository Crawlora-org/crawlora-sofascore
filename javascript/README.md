# @crawlora-org/sofascore

JavaScript and TypeScript client for Crawlora's hosted SofaScore API.
It calls Crawlora's service; it does not run a browser or scrape SofaScore locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by SofaScore or its owners.

## Install

```sh
npm install @crawlora-org/sofascore
```

## Use

```js
import { SofascoreClient } from "@crawlora-org/sofascore";

const client = new SofascoreClient({ apiKey: process.env.CRAWLORA_API_KEY });
const result = await client.search({ q: "Liverpool" });
console.log(result);
```

The client also exports `Client` as an alias for `SofascoreClient`. Operation
methods are available directly in camelCase and through the `sofascore`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-sofascore/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-sofascore/blob/main/examples/javascript.mjs) for contract-backed examples and text transcript output where supported.

The import snippet above is for a project where this npm package is installed. The checked-in repository example instead imports `../javascript/src/index.js` so it runs directly from the repository root; see the [source-checkout instructions](https://github.com/Crawlora-org/crawlora-sofascore#run-examples-from-a-source-checkout).

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API; response data and availability follow that
service's current contract.
