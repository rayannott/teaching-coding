# Telegram Messages Analyzer

This project is a simple tool to analyze your chat history which can be [exported as JSON](https://telegram.org/blog/export-and-more) from Telegram.


See the Message json schema [here](https://core.telegram.org/import-export#message) (official Telegram documentation).


## Short Description
Message history statistics and visualization tool for Telegram chats.


## Features

### Essential
- `Chat` class: represents a message history of a chat between two users
    - initialized from a JSON file exported from Telegram
    - contains a list of `Message` objects
    - contains all the methods for statistics and visualization

- `Message` class: represents a single message
    - initialized from a corresponding JSON object
    - contains the message's:
        - `id` int
        - `text` str
        - `dt` datetime.datetime
        - `sender` str

### Additional
- `Chats` class: represents a collection of chats
    - initialized from a directory with JSON files exported from Telegram
    - contains a list of `Chat` objects
    - contains all the methods for **comparison** of the statistics and visualization between the chats (e.g. graphs with multiple lines for different chats, grouped bar charts, etc.)
- more fields for the `Message` class:
    - OPTIONAL `attachment_type` attachment type (image, video, video message, voice message, sticker, gif, file, etc.)
    - OPTIONAL `reply_to` int: id of the message this message is a reply to
    - OPTIONAL `edited_dt` datetime.datetime: if the message was edited, the time of the last edit
    - `has_link` bool: if the message contains a link (use regex to find links)
- interesting things to look at:
    - maximum length chain of message replies (e.g. if message $m_n$ is a reply to message $m_{n-1}$, which is a reply to message $m_{n-2}$, etc., then the chain length is $n$)

### Possible Extensions
- map backend analysis to a web interface (e.g. Plotly Dash)
    - this would require us to use plotly for plotting the graphs
- 