from .base import ServiceController
from .utils import lambda_method, make_data


class AuthServiceController(ServiceController):
    SERVICE_TYPE = 'auth'

    def __init__(self, resource, app_id):
        super(AuthServiceController, self).__init__(resource, app_id)

    @lambda_method
    def create_user(self, email, password, extra):
        import cloud.auth.register as method
        params = {
            'email': email,
            'password': password,
            'extra': extra,
        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def set_user(self, user_id, email, password, extra):
        import cloud.auth.set_user as method
        params = {
            'user_id': user_id,
            'email': email,
            'password': password,
            'extra': extra,
        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def delete_user(self, user_id):
        import cloud.auth.delete_user as method
        params = {
            'user_id': user_id,
        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def get_user(self, user_id):
        import cloud.auth.get_user as method
        params = {
            'user_id': user_id,
        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def get_user_count(self):
        import cloud.auth.get_user_count as method
        params = {

        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def get_users(self, start_key, limit):
        import cloud.auth.get_users as method
        params = {'start_key': start_key,
                  'limit': limit}
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def create_session(self, email, password):
        import cloud.auth.login as method
        params = {
            'email': email,
            'password': password
        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def delete_session(self, session_id):
        import cloud.auth.logout as method
        params = {
            'session_id': session_id
        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def delete_sessions(self, session_ids):
        import cloud.auth.delete_sessions as method
        params = {
            'session_ids': session_ids
        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def get_session(self, session_id):
        import cloud.auth.get_session as method
        params = {
            'session_id': session_id
        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def get_sessions(self, start_key, limit):
        import cloud.auth.get_sessions as method
        params = {'start_key': start_key,
                  'limit': limit}
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def get_session_count(self):
        import cloud.auth.get_session_count as method
        params = {}
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def create_admin(self, email, password, extra):
        import cloud.auth.register_admin as method
        params = {
            'email': email,
            'password': password,
            'extra': extra,
        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def get_user_groups(self):
        import cloud.auth.get_user_groups as method
        params = {}
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def put_user_group(self, name, description):
        import cloud.auth.put_user_group as method
        params = {
            'name': name,
            'description': description,
        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def delete_user_group(self, name):
        import cloud.auth.delete_user_group as method
        params = {
            'name': name,
        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def set_email_login(self, enabled, default_group_name):
        import cloud.auth.set_email_login as method
        params = {
            'enabled': enabled,
            'default_group_name': default_group_name
        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def set_guest_login(self, enabled, default_group_name):
        import cloud.auth.set_guest_login as method
        params = {
            'enabled': enabled,
            'default_group_name': default_group_name
        }
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def get_email_login(self):
        import cloud.auth.get_email_login as method
        params = {}
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)

    @lambda_method
    def get_guest_login(self):
        import cloud.auth.get_guest_login as method
        params = {}
        data = make_data(self.app_id, params)
        return method.do(data, self.resource)
