class SuffixResource:
    async def on_get_all(self, req, resp):
        resp.text = 'all'

    async def on_get_list(self, req, resp):
        resp.text = 'list'