import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def parse_html(request):
    if request.method == 'POST':
        # Parse JSON data received from the extension
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            # Now `json_data` is a Python dictionary containing the parsed data
        except json.JSONDecodeError as e:
            return JsonResponse({'result': 'error', 'message': 'Invalid JSON format'})

        # Perform parsing or other operations as needed
        # Access data using keys, for example:
        html_content = json_data.get('htmlContent', '')
        # Your parsing logic here...
        print(json_data)
        # Return a response
        response_data = {'result': 'success', 'parsedData': html_content}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'result': 'error', 'message': 'Invalid request method'})
