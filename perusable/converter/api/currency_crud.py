import requests
from decouple import config
from fastapi import APIRouter, Depends

from converter.auth.auth_bearer import JWTBearer
from converter.models.model import ConversionSchema, HistorySchema

router = APIRouter()

apiKey = config("APIKEY")


@router.get("/currency/list", tags=["currency"])
async def get_currency_list():
    """
    Gets the list of supported currencies
    """
    url = f"https://v6.exchangerate-api.com/v6/{apiKey}/codes"
    response = requests.get(url).json()
    codes = response["supported_codes"]
    return codes


@router.post(
    "/currency/exchange", dependencies=[Depends(JWTBearer())], tags=["currency"]
)
async def exchange_currency(conversion: ConversionSchema):
    """
    Converts a currency from base currency to target currency
    """
    url = f"https://v6.exchangerate-api.com/v6/{apiKey}/pair/{conversion.base_code}/{conversion.target_code}/"
    response = requests.get(url).json()

    value = response["conversion_rate"]
    Amount = conversion.amount * value

    converted = {
        "Base Currency": conversion.base_code,
        "Target Currency": conversion.target_code,
        "Base Amount": conversion.amount,
        "Converted Amount": Amount,
    }
    return converted


@router.post(
    "/currency/history/exchange", dependencies=[Depends(JWTBearer())], tags=["currency"]
)
async def history_exchange(conversion: HistorySchema):
    """
    Converts a currency from base currency to target currency,
    based on the exchange rate on a previous date
    """
    url = f"https://v6.exchangerate-api.com/v6/{apiKey}/history/{conversion.base_code}/{conversion.year}/{conversion.month}/{conversion.day}"
    response = requests.get(url).json()

    value = response["conversion_rates"][f"{conversion.target_code}"]
    Amount = conversion.amount * value

    converted = {
        "Period": f"{conversion.day}-{conversion.month}-{conversion.year}",
        "Base Currency": conversion.base_code,
        "Target Currency": conversion.target_code,
        "Base Amount": conversion.amount,
        "Converted Amount": Amount,
    }
    return converted
