# Forbes Global 2000 Scraper

## Project Overview
This project includes a Scrapy spider named 'name_forbs' designed to collect data from the Forbes Global 2000 list. The list features rankings of the top 2000 public companies worldwide, as published on Forbes.com.

## Features
- Spider: 'name_forbs'
- Target Website: Forbes Global 2000 List
- Extracted Data:
  - Company Rank
  - Company Name
  - Company Profile URL

## Output
The scraped data is stored in JSON format in the file 'name_forbs.json'.

## Usage
To run this spider, navigate to the project's root directory and execute:
  ```bash
  scrapy crawl name_forbs
  ```
