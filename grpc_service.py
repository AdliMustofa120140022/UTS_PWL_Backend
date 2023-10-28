# grpc_service.py
# Implementasi layanan gRPC untuk menangani komunikasi dengan frontend
from concurrent import futures
import grpc
from product_pb2 import Product, GetProductsRequest, GetProductsResponse, AddProductRequest, AddProductResponse, DeleteProductRequest, DeleteProductResponse
from product_pb2_grpc import ProductServiceServicer, add_ProductServiceServicer_to_server

class ProductServiceImplementation(ProductServiceServicer):
    def GetProducts(self, request, context):
        # Implementasi logika untuk mendapatkan produk dari database

    def AddProduct(self, request, context):
        # Implementasi logika untuk menambahkan produk ke database

    def DeleteProduct(self, request, context):
        # Implementasi logika untuk menghapus produk dari database

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ProductServiceServicer_to_server(ProductServiceImplementation(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
