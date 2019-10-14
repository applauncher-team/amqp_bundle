Amqp bundle
===========

Just a bundle to get an Amqp connection.

`pip install amqp_bundle`

and inject a connection

```python
import inject
from kombu.connection import Connection
connection = inject.instance(Connection)

```

This bundle is  basically a piece for other bigger bundles, like [remote_event_bundle](https://github.com/applauncher-team/remote_event_bundle)