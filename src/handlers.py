from views import index, form, web_response


class Handler:

    def __init__(self):
        pass

    @staticmethod
    async def handle_home(request):
        print(request)
        return await index(request)

    @staticmethod
    async def handle_greeting(request):
        return await web_response(request)

    async def handle_form(self, request):

        if request.method == "POST":
            await self.handle_form_post(request)

        return await form(request)

    @staticmethod
    async def handle_form_post(request):
        data = await request.post()
        print(data["facultyId"])
