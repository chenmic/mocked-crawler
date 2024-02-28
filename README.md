# Crawler

This project implements a mocked crawler using Tornado for the web app, SQLite for the DB, and RQ (Redis Queue) for background task processing.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/chenmic/mocked-crawler.git
    ```

2. Install dependencies:

    ```bash
    cd mocked-crawler
    pip install -r requirements.txt
    ```

3. Start Redis server:

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

    - `/api/ingest`: Initiate a web crawl by sending a POST request with JSON data containing the URL to crawl.
    - `/api/status/<crawl_id>`: Check the status of a crawl by providing the crawl ID.

    Example:

    ```bash
    # Initiate a web crawl
    curl -X POST -H "Content-Type: application/json" -d '{"url": "https://example.com"}' http://localhost:8888/api/ingest

    # Check the status of a crawl (replace <crawl_id> with the actual crawl ID)
    curl http://localhost:8888/api/status/<crawl_id>
    ```

## License

[MIT](https://choosealicense.com/licenses/mit/)
