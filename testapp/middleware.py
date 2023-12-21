# middleware.py
import re

class GoogleAnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        try:
            name_param = re.search(r'name=([^&]+)', request.get_full_path()).group(1)
        except AttributeError:
            name_param = "Unknown"

        self.send_to_google_analytics(response, name_param)

        return response

    def send_to_google_analytics(self, response, name_param):
        ga_measurement_id = 'G-Z4T04C1CFD'
        ga_script = f"gtag('event', 'page_view', {{ 'User Name': '{name_param}' }});"
        ga_code = f"<script>{ga_script}</script>"

        response_content = response.content.decode('utf-8')
        response_content = response_content.replace('</head>', f'{ga_code}</head>', 1)
        response.content = response_content.encode('utf-8')
