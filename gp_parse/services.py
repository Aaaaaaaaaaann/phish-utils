from typing import Any, Dict, Optional, List
from urllib.parse import urlencode, urlparse, urlunparse, parse_qsl
from pprint import pprint

from aiohttp import ClientSession

from .utils import search_service_url


class SearchService:
    def __init__(self, url: str) -> None:
        self._url = url

    async def search_apps(self, query: str) -> List[Dict]:
        try:
            data = await self._get_data(query)
        except ValueError:
            return []

        return data

    async def _get_data(self, query: str) -> List[Dict]:
        apps_data = []

        url = self._add_url_query_params(params=dict(q=query))
        next_page_token = True

        while next_page_token:
            page_data = await self._get_page(url)
            apps = self._get_apps(page_data, query)
            apps_data.extend(apps)

            next_page_token = self._get_next_page_token(page_data)
            url = self._add_url_query_params(
                params=dict(next_page_token=next_page_token)
            )

        return apps_data
    
    def _add_url_query_params(self, params: Dict[str, Any]) -> str:
        parse_result = urlparse(self._url)

        query = dict(parse_qsl(parse_result.query))
        query.update(params)
        query = urlencode(query)

        url = urlunparse(
            (
                parse_result.scheme,
                parse_result.netloc,
                parse_result.path,
                parse_result.params,
                query,
                parse_result.fragment,
            )
        )
        return url

    async def _get_page(self, url: str) -> Dict[str, Any]:
        async with ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
    
    def _has_data(self, results: Dict[str, Any]) -> bool:
        if (
            results['search_information']['organic_results_state'] 
            == 'Fully empty'
        ):
            return False
        return True
    
    def _get_next_page_token(self, data: Dict[str, Any]) -> Optional[str]:
        token = data.get('pagination', {}).get('next_page_token')
        return token

    def _get_apps(self, data: Dict[str, Any], query: str) -> List[Dict]:
        apps = []

        for result in data.get('organic_results', []):
            for item in result['items']:
                data = dict(
                    title=item['title'],
                    link=item['link'],
                    author=item.get('extansion', {}).get('name'),
                    category=result['title'],
                    description=item['description'],
                    rating=item['rating'],
                )
                if not (query in data['title'] or query in data['description']):
                    continue

            apps.append(data)
        
        return apps


async def get_apps(query: str) -> None:
    search_service = SearchService(url=search_service_url)
    apps = await search_service.search_apps(query)

    if not apps:
        print('Apps not found.')
    else:
        pprint(apps)
