# Market job Classifier

The code demonstrates how to gather information regarding job market by providing the job title as the input.
The code provides the probability, count and similarity with the input job title as the final output.

![output](/figures/output.png)

## How to use

    python main.py --title "management trainee"

Arguments:

* `--title` default: "machine learning"
* `--threshold` default: 0.5, minimum similarity required
* `--top` default: 5, number of top results to be shown

Scrapper:

    python scrapper.py

The scrapper collects data from [indeed.com](https://www.indeed.co.uk/jobs?q=london&l=norwich) for different cities like london, glasgow, birmingham, manchester etc. It uses Selenium to scrape data with chrome driver. Chrome browser is necessary for it to work.

## Installation

Pip:

    pip install -r requirements.txt

