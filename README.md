# Market job Classifier

The code demonstrates how to gather information regarding job market by providing the job title as the input.
The code provides the probability, count and similarity with the input job title as the final output.

![output](/figures/output.png)

## How to use

    python main.py --title "management trainee"

Arguments:

* `--title` default: "machine learning"
* `--threshold` default: 0.5, Minimum similarity required.
* `--top` default: 5, Number of top results to be show

Scrapper:

    python scrapper.py

It uses Selenium to scrape data with chrome driver. Chrome browser is necessary for it to work. The scrapper collects data from [indeed.com](https://www.indeed.co.uk/jobs?q=london&l=norwich) for different cities like london, glasgow, birmingham, manchester etc.

## Installation

Pip:

    pip install -r requirements.txt

