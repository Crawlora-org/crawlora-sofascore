require_relative "lib/crawlora/sofascore/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-sofascore"
  spec.version = Crawlora::Sofascore::VERSION
  spec.summary = "SofaScore client for the Crawlora hosted API"
  spec.description = "Credential-free SofaScore API access through Crawlora's hosted service."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=sofascore-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-sofascore", "documentation_uri" => "https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=sofascore-ruby-api-docs", "rubygems_mfa_required" => "true" }

end
