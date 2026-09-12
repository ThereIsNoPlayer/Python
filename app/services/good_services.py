from schemas.goods import GoodsCreate, GoodsInfo

_goods_db:list[dict]=[]
_next_id=1

def create_goods(goods:GoodsCreate)-> GoodsInfo:
    '''新增商品'''
    global _next_id
    goods={
        'id':_next_id,
        'name':goods.name,
        'price':goods.price,
        'stock':goods.stock,
    }
    _goods_db.append(goods)
    _next_id+=1
    return GoodsInfo(**goods)

def list_goods() -> list[GoodsInfo]:
    '''查询商品列表'''
    return [GoodsInfo(**goods) for goods in _goods_db]

