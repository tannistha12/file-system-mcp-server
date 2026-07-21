# What is MCP Server?

It is a program that exposes capabilities (called tools, resources, and prompts) to an AI using the Model Context Protocol. The server doesn't contain the AI model. Its responsibility is to advertise available capabilities, receive requests from an MCP client, execute them, and return structured responses.

---

# Why does an AI need tools?

ChatGPT only knows information already in its context.

It cannot
- open files
- search folders
- access GitHub
- call APIs
- query databases

Tools extend its capabilities.

Think of the LLM as the "brain" and tools as the "hands."

