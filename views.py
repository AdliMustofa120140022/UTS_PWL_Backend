# Definisi rute dan views untuk Pyramid yang mengakses layanan gRPC
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults
import grpc
from product_pb2 import Product, GetProductsRequest, GetProductsResponse, AddProductRequest, AddProductResponse, DeleteProductRequest, DeleteProductResponse
from product_pb2_grpc import ProductServiceStub

@view_config(route_name='grpc_get_products', renderer='json')
def grpc_get_products(request):      # View untuk mendapatkan produk melalui layanan gRPC
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ProductServiceStub(channel)
        response = stub.GetProducts(GetProductsRequest())
        products = [{'id': p.id, 'name': p.name, 'price': p.price, 'stock': p.stock} for p in response.products]
        return {'products': products}

@view_config(route_name='grpc_add_product', request_method='POST', renderer='json')
def grpc_add_product(request):       # View untuk menambahkan produk melalui layanan gRPC
    data = request.json_body
    add_request = AddProductRequest(name=data['name'], price=data['price'], stock=data['stock'])
    
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ProductServiceStub(channel)
        response = stub.AddProduct(add_request)
    
    return {'status': 'success', 'message': response.message}

@view_config(route_name='grpc_delete_product', request_method='DELETE', renderer='json')
def grpc_delete_product(request):   # View untuk menghapus produk melalui layanan gRPC
    product_id = int(request.matchdict['id'])
    delete_request = DeleteProductRequest(id=product_id)
    
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = ProductServiceStub(channel)
        response = stub.DeleteProduct(delete_request)
    
    return {'status': 'success', 'message': response.message}
