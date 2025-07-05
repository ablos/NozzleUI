import httpx

class MoonrakerClient:
    def __init__ (self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(
            base_url = base_url,
            timeout = httpx.Timeout(10.0),
            limits = httpx.Limits(max_connections = 20, max_keepalive_connections = 5)
        )
        
    async def get(self, endpoint: str) -> dict:
        try:
            response = await self.client.get(endpoint)
            response.raise_for_status()
            return response.json()
        
        # Connection errors / timeouts / etc.
        except httpx.RequestError as e:
            return {"error": "Failed to connect to Moonraker", "connected": False}
        
        # 4xx/5xx HTTP errors
        except httpx.HTTPStatusError as e:
            return {"error": f"Moonraker error: {e.response.status_code}", "connected": True}
        
        # Other errors
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}", "connected": False}
        
# Singleton
moonraker = MoonrakerClient("http://192.168.1.3:7125")