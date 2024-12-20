# encoding: utf-8
import os

from fastapi import Path, HTTPException
from pydantic import BaseModel

from server import app, karlsend_client

KARLSEN_ADDRESS_PREFIX = os.getenv("ADDRESS_PREFIX", "karlsen")


class BalanceResponse(BaseModel):
    address: str = KARLSEN_ADDRESS_PREFIX + ":pzhh76qc82wzduvsrd9xh4zde9qhp0xc8rl7qu2mvl2e42uvdqt75zrcgpm00"
    balance: int = 38240000000


@app.get("/addresses/{karlsenAddress}/balance", response_model=BalanceResponse, tags=["Karlsen addresses"])
async def get_balance_from_karlsen_address(
        karlsenAddress: str = Path(
            description="Karlsen address as string e.g. " + KARLSEN_ADDRESS_PREFIX + ":pzhh76qc82wzduvsrd9xh4zde9qhp0xc8rl7qu2mvl2e42uvdqt75zrcgpm00",
            regex="^" + KARLSEN_ADDRESS_PREFIX + "\:[a-z0-9]{61,63}$")):
    """
    Get balance for a given karlsen address
    """
    resp = await karlsend_client.request("getBalanceByAddressRequest",
                                       params={
                                           "address": karlsenAddress
                                       })

    try:
        resp = resp["getBalanceByAddressResponse"]
    except KeyError:
        if "getUtxosByAddressesResponse" in resp and "error" in resp["getUtxosByAddressesResponse"]:
            raise HTTPException(status_code=400, detail=resp["getUtxosByAddressesResponse"]["error"])
        else:
            raise

    try:
        balance = int(resp["balance"])

    # return 0 if address is ok, but no utxos there
    except KeyError:
        balance = 0

    return {
        "address": karlsenAddress,
        "balance": balance
    }
