from eve import Eve
from eve.auth import BasicAuth

class MyAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        if username == "admin" and password == "loule":
            return True
        else:
            accounts = app.data.driver.db['insoumeetic']
            account = accounts.find({"username": username, "password": password})
            print(account)
            if account is not None:
                return True
        return False


app = Eve(auth=MyAuth)

if __name__ == "__main__":
    app.run()