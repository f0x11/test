from ldap3 import Server, Connection, SUBTREE


# Configure an OpenLDAP server
ldap_host = 'admin1.frontrace.com'
ldap_port = 389
ldap_tls = False
ldap_service_account_username = 'cn=admin,dc=admin1,dc=frontrace,dc=com'
ldap_service_account_password = 'a87654321'
ldap_search_base = 'dc=admin1,dc=frontrace,dc=com'

# Customize Schema
ldap_user_object_class = 'inetOrgPerson'
ldap_user_search_field = 'uid'
ldap_user_login_field = 'uid'
ldap_user_name_field = 'givenName'


def login(username, password):
    server = Server(ldap_host)
    c = Connection(server, ldap_service_account_username, ldap_service_account_password, auto_bind=True)

    c.search(search_base=ldap_search_base,
             search_filter='(&(objectClass={0})({1}={2}))'.format(
                 ldap_user_object_class, ldap_user_search_field, username
             ),
             search_scope=SUBTREE,
             attributes=[ldap_user_search_field, ldap_user_name_field])

    user_dn = c.response[0]['dn']
    # print(entry['dn'], entry['attributes'])

    c = Connection(server, user_dn, password)

    if not c.bind():
        print(c.result)

if __name__ == '__main__':
    login('user2', 'a87654321')
