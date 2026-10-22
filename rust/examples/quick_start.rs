use crawlora_sofascore::{Client, ModelSofascoreSearchResponseDoc, SofascoreSearchParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .sofascore
        .search(SofascoreSearchParams {
            q: Some("Liverpool".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelSofascoreSearchResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
