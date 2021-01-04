import urllib
import json
import sys
import codecs
import urllib.request
from django.http import HttpResponse
from .models import Stock
from .forms import StockForm
from django.views.generic import ListView
from django.views.generic import CreateView


# Create your views here.
# webAPIからJSONの形式の文字列の結果をもらう

"""
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
"""

#def index(request):
class StockIndexView(ListView):
  model = Stock
  template_name = 'stocks/stock_list.html'
  queryset = Stock.objects.order_by('-updated_at')
  paginate_by = 10

class StockCreateView(CreateView):
  model = Stock
  template_name = 'stocks/stock_form.html'
  form_class = StockForm