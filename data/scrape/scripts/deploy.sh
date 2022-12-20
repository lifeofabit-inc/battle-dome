#!/usr/bin/env bash

# Global defaults
: "${SCRAPE_HOME:="/usr/local/scrape"}"

if [[ ! -d "${SCRAPE_HOME}/scrapebot" ]]; then
  scrapy startproject scrapebot ${SCRAPE_HOME}
fi

bash
