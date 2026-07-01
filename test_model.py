import asyncio
import os
from google.genai import types
from google.adk.models import Gemini
from google.adk.tools import ToolContext
from app.agent import google_drive_mcp

async def test():
    try:
        model = Gemini(model="gemini-3.1-flash-lite")
        tools = await google_drive_mcp.get_tools()
        print("Tools loaded:", [t.name for t in tools])
        
        prompt = "Search my Google Drive for files in the root directory. Use the query \"'root' in parents\""
        
        response = await model.generate_content_async(
            contents=[types.Content(role="user", parts=[types.Part.from_text(text=prompt)])],
            tools=tools,
            config=types.GenerateContentConfig(temperature=0)
        )
        print("Model Response:")
        if response.function_calls:
            for call in response.function_calls:
                print(f"Tool Call: {call.name}({call.args})")
        else:
            print(response.text)
            
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Error: {e}")

asyncio.run(test())
