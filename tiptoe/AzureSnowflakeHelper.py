import snowflake.connector
import os
from snowflake.connector import DictCursor
from snowflake.connector.converter_null import SnowflakeNoConverterToPython

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def Get_Azure_Secret_PrivateKey(keyvault_name, pk_secretname=None, pk_password=None):
    # _keyVaultName = os.environ["KEY_VAULT_NAME"]
    KVUri = f"https://{keyvault_name}.vault.azure.net"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)
    pk = str.encode(client.get_secret(pk_secretname).value)

    p_key = serialization.load_pem_private_key(
        pk,
        password=str.encode(pk_password),
        backend=default_backend()
    )

    pkb = p_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    return pkb


def Load_Local_PrivateKey(path_to_privatekey='.', pk_password=None, azure_function=False):
    with open(path_to_privatekey, "rb") as key:
        p_key= serialization.load_pem_private_key(
            key.read(),
            password=str.encode(pk_password),
            backend=default_backend()
        )

        pkb = p_key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption())
        return pkb


class SnowConn:
    cursor = ""
    login_method = ""
    user = ""
    password = ""
    private_key = ""
    account = ""
    warehouse = ""
    database = ""
    schema = ""


    def __init__(self, config_data: dict):
        self.cursor = config_data['cursor_type']
        self.login_method = config_data['login_method']
        self.user = config_data['user']
        self.private_key = config_data['private_key'] if 'private_key' in config_data else None
        self.account = config_data['account']
        self.warehouse = config_data['warehouse']
        self.database = config_data['database']
        self.schema = config_data['schema']
        self.password = config_data['password'] if 'password' in config_data else None


    def __enter__(self):
        params = {}
        params = {'user': self.user,
                  'account' : self.account,
                  'converter_class' : SnowflakeNoConverterToPython
                  }
        if self.login_method == 'password':
            params['password'] = self.password
        if self.login_method == 'private_key':
            params['private_key'] = self.private_key

        self.ctx = snowflake.connector.connect(**params)

        if self.cursor == 'dict':
            self.cur = self.ctx.cursor(DictCursor)
        else:
            self.cur = self.ctx.cursor()

        self.cur.execute("USE WAREHOUSE {}".format(self.warehouse))
        self.cur.execute("USE DATABASE {}".format(self.database))
        self.cur.execute("USE SCHEMA {}".format(self.schema))
        return self.cur


    def __exit__(self, exc_type, exc_value, traceback):
        self.cur.close()
        self.ctx.close()
