from pyramid.config import Configurator
from .grpc_service import serve

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('.models')
    config.include('.routes')
    config.scan()

    # Tambahkan rute untuk layanan gRPC
    config.add_route('grpc_get_products', '/grpc/products')
    config.add_route('grpc_add_product', '/grpc/products/add')
    config.add_route('grpc_delete_product', '/grpc/products/delete/{id}')

    # Jalankan layanan gRPC pada thread terpisah
    config.registry['grpc_thread'] = serve
    config.registry['grpc_thread']()

    return config.make_wsgi_app()
