import { SofascoreClient } from "../src/index.js";

const client = new SofascoreClient({ apiKey: "test-key" });
void client.categories({"sport": "american-football"});
void client.request("sofascore-categories", {"sport": "american-football"});
const streamResponse: Promise<Response> = client.request("sofascore-categories", {"sport": "american-football"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("sofascore-categories", {"sport": "american-football"}, { responseType: "stream" });
const directStream: Promise<Response> = client.categories({"sport": "american-football"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("sofascore-categories", {"sport": "american-football"}, { responseType: "text" });
const rawText: Promise<string> = client.request("sofascore-categories", {"sport": "american-football"}, { responseType: "text" });
void rawText;


void client.rankingTypes();
void client.request("sofascore-ranking-types");
// @ts-expect-error The selected operation requires its documented params.
void client.categories();
