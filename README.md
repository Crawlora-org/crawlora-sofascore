# SofaScore clients for Crawlora

Official Crawlora client packages for the hosted SofaScore API. These packages send requests to Crawlora's API and require a Crawlora account and `CRAWLORA_API_KEY`; service usage follows your Crawlora account billing plan.

The packages do not run a browser or scrape SofaScore locally. Crawlora is an independent service and is not affiliated with or endorsed by SofaScore or its owners.

- JavaScript / TypeScript: [`@crawlora-org/sofascore`](javascript/README.md)
- Python: [`crawlora-sofascore`](python/README.md)
- Full endpoint and parameter reference: [docs/usage.md](docs/usage.md)
- Runnable samples: [examples/](examples/)
- Source repository: [https://github.com/Crawlora-org/crawlora-sofascore](https://github.com/Crawlora-org/crawlora-sofascore)

## Install

```sh
npm install @crawlora-org/sofascore
python -m pip install crawlora-sofascore
```

Set your Crawlora key in the environment before running a client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

Do not commit API keys. See the language-specific READMEs for sync and async use.

## Run examples from a source checkout

From the repository root, set `CRAWLORA_API_KEY` as shown above and run:

```sh
node examples/javascript.mjs
python -m pip install ./python
python examples/python.py
```

The checked-in JavaScript example imports the generated local source at `javascript/src/index.js`. The Python command installs this checkout's package before running its example. The import snippets in the language-specific READMEs are for separate projects using installed npm and PyPI packages; copy those snippets into your own project after installing the package.

## Contract

This package release is `0.1.0`. The generated client methods follow the bundled `openapi/public.json` contract at revision `sha256:8dc2e500465b7b7f98054def2f9794e0e433d8bbbcba6cfb688e0b6ed0ecbfcd`. `scripts/generate.py` regenerates both language clients and the documentation from the shared source.

## License

MIT. See [LICENSE](LICENSE).
