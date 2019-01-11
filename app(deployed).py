<VirtualHost *:80>
                ServerName 13.67.70.117
                ServerAdmin sziddhant@gmail.com
                WSGIScriptAlias / /var/www/FlaskApp/Bo.wsgi
                <Directory /var/www/Bo/Bo/>
                        Order allow,deny
                        Allow from all
                </Directory>
                Alias /static /var/www/Bo/Bo/static
                <Directory /var/www/Bo/Bo/static/>
                        Order allow,deny
                        Allow from all
                </Directory>
                ErrorLog ${APACHE_LOG_DIR}/error.log
                LogLevel warn
                CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>