# Cleanup Expired Sessions

This is a Python automation script that automatically and periodically accesses the expired session check endpoint of a REST API.

## Features

- Automatic call the cleanup expired sessions route on the REST API's clean up expired sessions
- Scheduled execution to run periodically
- Error handling and response logging

## Prerequirement

- Python 3.x
- pip (Python package manager)

## Instalation

1. Clone the repository:

```bash
git clone [REPOSITORY_URL]
cd cleanup-expired-sessions
```

2. Install the required packages:

```bash
pip install requests python-dotenv schedule
```

## Configuaration

1. Create a `.env` file on root of the project, following the follow variables:

```env
API_URL=https://your-api.com/cleanup-sessions
API_KEY=your_api_key
```

## How to use

To start the script:

```bash
python cleanupExpiredSessions.py
```

The script will:

- Execute automatically every day at midnight(Defaiult Configuration)
- Make the request to the expired session check route of a REST API to clean up any expired sessions.
- Log the result of the operation to the console.

## Project Structure

```
cleanup-expired-sessions/
├── cleanupExpiredSessions.py    # Main Script
├── .env                         # Config File(not versioned)
└── README.md                    # Documentation
```

## Logs e OBservability

The script logs the following information to the console:

- Start of the cleanup operation
- Successful result with response details
- Errors encountered during execution

## Licença

MIT License
