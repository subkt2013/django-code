import urllib
import json
import sys
import codecs
import urllib.request
from django.http import HttpResponse


# Create your views here.
# webAPIからJSONの形式の文字列の結果をもらう
def index(request):

    # URIスキーム
    url = 'https://www.alphavantage.co/query?'

    # URIパラメータのデータ 
    param = {
    'function': 'TIME_SERIES_INTRADAY',    # 取得したい人のID
    'symbol': 'ZM',           # 取得するデータの指定
    'interval': '60min',
    'apikey': '7ANZPFSO0RDV402N.'
    }

    # URIパラメータの文字列の作成
    paramStr = urllib.parse.urlencode(param)  # type=json&user=tamago324_pad と整形される

    # 読み込むオブジェクトの作成
    readObj = urllib.request.urlopen(url + paramStr)

    # webAPIからのJSONを取得
    response = readObj.read()

    return HttpResponse(response)
