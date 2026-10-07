import { SofascoreClient } from "@crawlora-org/sofascore";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new SofascoreClient({ apiKey });

  const search = await client.search({ q: "Liverpool" });
  console.log("search", search);
  const liveEvents = await client.liveEvents({ sport: "football" });
  console.log("liveEvents", liveEvents);
