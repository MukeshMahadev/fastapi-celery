import asyncio
import websockets


async def websocket_client(task_id):
    print("Running")
    uri = f"ws://localhost:7777/ws/tasks/{task_id}"  # Replace with your WebSocket endpoint URL

    while True:
        try:
            async with websockets.connect(uri) as websocket:
                # Send a message
                await websocket.send("Hello, WebSocket!")

                # Receive a message
                response = await websocket.recv()
                print("Received:", response)

                # Check if the response is "Success"
                if response == "Success":
                    break  # Exit the loop if we received "Success"

        except websockets.exceptions.ConnectionClosedError as e:
            # Handle connection closed error
            print(e)
            break
            pass

        # Sleep for some time before retrying
        await asyncio.sleep(5)

asyncio.run(websocket_client("f79d0e06-4aa2-45f6-ab0a-0745cc1df270"))
