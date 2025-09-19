from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@csrf_exempt
def messages(request):
    logger.info(f"Teams bot endpoint hit - Method: {request.method}")

    if request.method == "GET":
        return JsonResponse({"status": "Endpoint is running"}, status=200)
    
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
        logger.info(f"Received Teams message: {json.dumps(data, indent=2)}")
        return JsonResponse({"status": "success"}, status=200)

    except Exception as e:
        logger.error(f"Internal server error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        return JsonResponse({"error": "Internal server error"}, status=500)
