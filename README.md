# aoc-dashboard-plugin-twitch

This plugin updates a Twitch channel title based on the Dashboard's game title.

## About plugins

Dashboard plugins operate on a pub/sub model. The plugin subscribes to message types, and provides a callback function for each. As the dashboard analysis engine runs, it publishes messages to all subscribers, including plugins.

All plugins require the following two methods:
- init(conf): Called by the dashboard as it loads plugins. Argument is a dictionary generated from the [Configuration] section of the plugin definition file.
- registration(): Called by the dashboard to get subscriptions. Return a dictionary of message type to callback function.

Python module dependencies used in plugins must either be already linked in the dashboard executable or included in the package.

All plugins must have a plugin definition file. This is a configuration file that is used to load the plugin. It is also a convenient place for plugin-specific configuration options, though a separate system could be used.
