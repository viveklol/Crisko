import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


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

@csrf_exempt
def extension_login(request):
    print(request)
    if request.method == 'POST':
        data = json.loads(request.body)
        session_key = data['sessionid']

        # Retrieve the session object
        session = Session.objects.filter(session_key=session_key)

        if not session.exists():
            return JsonResponse({
                'error': 'Authentication required in www.mywebsite.com',
            }, status=401)

        # Get the session data
        session_data = session.first().get_decoded()

        # Get the user ID from the session data
        user_id = session_data.get('_auth_user_id')

        if user_id:
            # Retrieve the user object using the user ID
            user = User.objects.get(pk=user_id)
            username = user.username

            return JsonResponse({
                'message': f'You are logged in as {username} in www.mywebsite.com',
            }, status=200)
        else:
            return JsonResponse({
                'error': 'User not authenticated',
            }, status=401)
