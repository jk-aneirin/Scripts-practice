#!/usr/bin/env python
import ldap
import getpass

if __name__=="__main__":
    ldap_server='ldaps://ldapserver:port'
    username=raw_input('input your ldap user:')
    password=getpass.getpass("Please enter the ldap password: ")
    user_dn="uid={},cn=users,cn=accounts,dc=example,dc=com".format(username)
    base_dn="cn=users,cn=accounts,dc=examle,dc=com"
    #ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_ALLOW)
    ldapconn=ldap.initialize(ldap_server)
    search_filter='uid='+username
    try:
        ldapconn.simple_bind_s(user_dn,password)
        result=ldapconn.search_s(base_dn,ldap.SCOPE_SUBTREE,search_filter)
        print result
    except ldap.LDAPError,e:
        print e
    finally:
        ldapconn.unbind_s()
