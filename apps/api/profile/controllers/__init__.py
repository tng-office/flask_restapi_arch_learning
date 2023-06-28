from flask_restx import Namespace

avatar_api = Namespace('avatar', description='Avatar Image Endpoints')
member_api = Namespace('member', description='Member Resource Endpoints')
search_api = Namespace('search', description='Profile Search Endpoints')
