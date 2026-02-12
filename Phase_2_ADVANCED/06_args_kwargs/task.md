# Task Description

**Scenario: The Universal Event Bus**

You are designing a flexible "Event Bus" for a smart home system. Devices send signals (events) with all kinds of different data. A "Light Turned On" event might just have a timestamp, but a "Thermostat Changed" event might have temperature, humidity, and mode.

You cannot predict every possible argument that future devices might send. If you hardcode specific parameters, the system will break when a new device is added.

**Your Goal:**
Create a universal `EventDispatcher` system that can accept *any* event with *any* number of positional or keyword arguments and route them correctly.

**Objectives:**
1.  Examine how `*args` and `**kwargs` allow functions to accept arbitrary inputs.
2.  Create a function `dispatch_event(event_type, *args, **kwargs)` that acts as the central hub.
3.  It should accept a primary `event_type` (like "LOGIN", "LOGOUT", "ALARM") and then capture *everything else* passed to it.
4.  Print out a formatted log showing the event type, the positional arguments (maybe IDs or flags), and the keyword arguments (metadata like `user="admin"`, `temperature=24.5`).

**Success Condition:**
You can call your function with completely different signatures:
- `dispatch_event("BOOT", "system_start")`
- `dispatch_event("CLICK", x=100, y=200, button="left")`
- `dispatch_event("ERROR", 404, "Not Found", retry=True, severity="High")`
...and it handles them all gracefully without crashing, printing all details clearly.
