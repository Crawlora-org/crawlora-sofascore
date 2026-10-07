import { SofascoreClient } from "../src/index.js";

const client = new SofascoreClient({ apiKey: "test-key" });
void client.event({"id": "sample"});
void client.request("sofascore-event", {"id": "sample"});
const streamResponse: Promise<Response> = client.request("sofascore-event", {"id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("sofascore-event", {"id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.event({"id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("sofascore-event", {"id": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("sofascore-event", {"id": "sample"}, { responseType: "text" });
void rawText;



// @ts-expect-error The selected operation requires its documented params.
void client.event();
