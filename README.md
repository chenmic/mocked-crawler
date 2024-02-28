# Crawler

This project implements a mocked crawler using Tornado for the web app, SQLite for the DB, and RQ (Redis Queue) for background task processing.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/chenmic/mocked-crawler.git
    ```

2. Create and activate a virtual environment:

    ```bash
    cd mocked-crawler
    python3 -m venv venv
    . venv/bin/activate  
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Start Redis server:

    Make sure you have Redis server running. You can install and start Redis using your package manager or by downloading it from [Redis' website](https://redis.io/docs/install/install-redis/).

## Configuration

Ensure that your Redis server is accessible. You may need to configure the connection settings in the Tornado application and RQ worker if Redis is not running locally or has non-default connection settings.

## Usage

1. Start the RQ worker:

    ```bash
    rq worker
    ```

    This command starts the RQ worker, which listens for tasks in the Redis queue and processes them asynchronously.

2. Run the Tornado web application:

    ```bash
    python main.py
    ```

    This command starts the Tornado web application, which serves the API endpoints for initiating web crawls and checking their status.

3. Access the API endpoints:

    - `/api/ingest`: Request a web crawl.
    - `/api/status/<crawl_id>`: Check the status of a crawl.

    Example:

    ```bash
    # Request a web crawl to url <url> and receive notifications at <notify_at> (space seperated lsit of email / slack) to <notify_to> (space seperated list of recipients)
    curl --location '<server_address>:8888/api/ingest' --form 'url="<url>"' --form 'notify_at="<notify_at>"' --form 'notify_to="<notify_to>"'
    # for example
    curl --location '<server_address>:8888/api/ingest' --form 'url="https://www.google.com"' --form 'notify_at="email"' --form 'notify_to="a@hello.com b@hello.com"'

    # Check the status of a crawl (replace <crawl_id> with the actual crawl ID)
    curl --location '<server_address>:8888/api/status/<crawl_id>'
    ```

## License

[MIT](https://choosealicense.com/licenses/mit/)
