# django-demo

deployment:

1. install nginx
		yum install pcre-devel zlib-devel
		tar zxvf nginx-1.7.12.tar.gz
		./configure
		make
		make install
2. install uwsgi
		sudo yum install libxml2-devel uwsgi-plugin-python 
		sudo pip install uwsgi
3. configure nginx
     server {
             listen 80;
             server_name localhost;
             location / {
                 include    uwsgi_params;
                 uwsgi_pass  127.0.0.1:9090;
                 uwsgi_param UWSGI_CHDIR  /root/django-demo/blog;
                 uwsgi_param UWSGI_SCRIPT django_wsgi;
                 access_log /usr/local/nginx/logs/access.log;
                 }
             location /static {
               root /root/django-demo/blog;
             }

	chang 'user nginx' to 'user root'
4. configure uwsgi
	in the dir where manager.py lies, create two files:
	1. django_wsgi.py
        #!/usr/bin/env python
        # coding: utf-8
        import os
        import sys
        reload(sys)
        sys.setdefaultencoding('utf8')
        os.environ["DJANGO_SETTINGS_MODULE"] = "blog.settings"
        from django.core.handlers.wsgi import WSGIHandler
        application = WSGIHandler()
	2. uwsgi_socket.xml
        <uwsgi>
        <socket>127.0.0.1:9090</socket>
        <chdir>/root/django-demo/blog</chdir>
        <module>django_wsgi</module>
        <processes>4</processes>
        <daemonize>uwsgi.log</daemonize>
        </uwsgi>

   REPLACE /root/django-demo/blog with actual path.

5. start uwsgi
	in the dir where manager.py lies, 
	uwsgi -x uwsgi_socket.xml
6. start nginx
	nginx
