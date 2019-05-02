# Sentry Eve support

Easy to use package for Eve framework with support for Sentry

## Install

```bash
pip install sentry-eve
```

## Configuration

`SENTRY_DSN` - Your sentry DSN url

Add it in your `settings.py`:
```python
SENTRY_DSN = "<Your sentry dsn url>"
```

## Use
```python
from SentryEve import SentryEve

app = SentryEve(__name__)
```