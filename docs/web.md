
# Web

## SSL/TLS HTTPS

### Theory

* `SSL Certificate / Server Certificate` : ID of the server + public key
* `CA / Certificate Authority` : Can confirm that the certificate signature comes from the right entity. Then the client can be certain that the server it connected to is legitimate.

<div class="mermaid">
sequenceDiagram
	participant 1 as Client
	participant 2 as Server
	participant 3 as CA

	1 ->> 2: Request Encrypted connection (over HTTP)
	2 ->> 1: SSL Certificate
	1 ->> 3: Check if certificate is valid
	Note over 1: Create an encryption KEY (Encrypted with public key)
	1 ->> 2: Encryption KEY
	Note over 2: decrypt the encryption KEY
	Note over 1, 2: Only server & Client knows the encryption KEY
	2 ->> 1: Communication over HTTPS

</div>

### Documentation

* https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https
* https://wiki.mozilla.org/Security/Server_Side_TLS
* https://www.e-tinkers.com/2016/12/hosting-wordpress-on-raspberry-pi-part-6-implement-ssl/
* Tuto to create CA/server key/client key and test it with curl/httpie https://tech-habit.info/posts/https-cert-based-auth-with-flask-and-gunicorn/

### generate private key

```sh
openssl req -x509 -newkey rsa:4096 -nodes -out certificate.pem -keyout private_key.pem -days 365
```




