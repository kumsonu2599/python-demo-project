import httpx

from app.core.config import settings


class ExternalAPIClient:

    async def get_posts(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.EXTERNAL_API}/posts"
            )
            return response.json()


external_client = ExternalAPIClient()
