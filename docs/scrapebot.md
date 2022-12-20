# ScrapeBot

ScrapeBot is designed to extract data from the web.  It utilizes the [Scrapy](https://doc.scrapy.org/en/latest/index.html) web crawling library in a Docker container to provide an interface for scraping the web.

## Docker

In order to execute building and running the Scrapy Docker container, a `Makefile` has been provided for convenience.  Executing `make run` will build the container, execute start-up instructions, and start the bash shell inside the container.

## Examples

Once inside the docker container, commands can be run to debug, design, and run crawlers. Here's a list of commonly used commands:
- Run the Scrapy shell and work with some scraped web data: 
  - `>>> scrapy shell '<url>'`
- Execute a defined Scrapy spider:
  - `>>> scrapy crawl heroes -O raw/heroes.jsonl`

## Important Notes for Scrapy

- Scrapy supports the following file formats 
  - .json, .jsonlines, .jsonl, .jl
  - .csv 
  - .xml
  - .marshal
  - .pickle




