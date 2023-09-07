from .controllers import YahooFinance
from django.http import JsonResponse, HttpResponse
from .serializers import serialize_dividend

def get_dividends(request, symbol, year):
    if request.method == "GET":
        response = YahooFinance.get_finance_data(symbol)
        if response["success"]:
            serialized_data = serialize_dividend(symbol, year)
            return JsonResponse({"success": True, "data": serialized_data}, status=200)
        else:
            return JsonResponse(response)
    else:
        return JsonResponse({"error": f"Method {request.method} not allowed!"}, status=405)
