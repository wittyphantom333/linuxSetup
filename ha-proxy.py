# wi-proxy install script for AlmaLinux 9.1
# author: wittyphantom333
# email: witt@allthingsops.io

# logger.debug("This is just a harmless debug message")
# logger.info("This is just an information for you")
# logger.warning("OOPS!!!Its a Warning")
# logger.error("Have you try to divide a number by zero")
# logger.critical("The Internet is not working....")

import os
import pwd
import contextlib
import sys


class DummyFile(object):
    def write(self, x): pass


@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = DummyFile()
    yield
    sys.stdout = save_stdout


def userRun():
    # uid = pwd.getpwnam('witt')[2]
    # os.setuid(uid)
    os.system('pip3 install matplotlib')
    os.system(
        'pip3 install -r /var/www/haproxy-wi/config_other/requirements_el9.txt')
    os.system('pip3 install paramiko-ng')
    # event.set(true)


with nostdout():
    def haProxyInstall():
        print("Disabling SELinux")
        os.system('setenforce 0')
        print("Adding user to apache group")
        os.system('usermod -aG apache witt')
        print("Install dependencies")
        os.system(
            'yum install -y httpd epel-release git nano && yum update')
        print("Cloning repository")
        os.system('mkdir /var/www/haproxy-wi')
        os.system('chown -R apache:apache /var/www/haproxy-wi/')
        os.system(
            'cd /var/www/ && git clone https://github.com/hap-wi/roxy-wi.git /var/www/haproxy-wi')
        os.system('chown -R apache:apache /var/www/haproxy-wi/')
        print("Installing required software")
        os.system('yum -y install fail2ban sshpass python3 python-pip python-devel python-cryptography python-jinja2 python-distro nmap-ncat net-tools lshw python-ldap python-paramiko rsync ansible dos2unix nmap mod_ssl httpd python-mod_wsgi libmodulemd python-psutil')
        userRun()
        # event.wait()
        os.system('chmod +x /var/www/haproxy-wi/app/*.py && cp /var/www/haproxy-wi/config_other/logrotate/* /etc/logrotate.d/ && cp /var/www/haproxy-wi/config_other/fail2ban/filter.d/* /etc/fail2ban/filter.d/ && cp /var/www/haproxy-wi/config_other/fail2ban/jail.d/* /etc/fail2ban/jail.d/')
        os.system('mkdir /var/lib/roxy-wi/configs/hap_config/ -p && mkdir /var/lib/roxy-wi/configs/kp_config/ && mkdir /var/lib/roxy-wi/configs/nginx_config/ && mkdir /var/lib/roxy-wi/configs/apache_config/ && mkdir /var/log/roxy-wi/ && mkdir /etc/roxy-wi/ && mkdir /usr/share/httpd/.ansible && touch /usr/share/httpd/.ansible_galaxy && mkdir /usr/share/httpd/.ssh && mv haproxy-wi/roxy-wi.cfg /etc/roxy-wi')
        os.system('openssl req -newkey rsa:4096 -nodes -keyout /var/www/haproxy-wi/app/certs/haproxy-wi.key -x509 -days 10365 -out /var/www/haproxy-wi/app/certs/haproxy-wi.crt -subj "/C=US/ST=Almaty/L=Springfield/O=Roxy-WI/OU=IT/CN=*.roxy-wi.org/emailAddress=aidaho@roxy-wi.org"')
        os.system('systemctl daemon-reload && systemctl restart httpd && systemctl restart rsyslog && systemctl start fail2ban && systemctl enable fail2ban')
        os.system('python3 /var/www/haproxy-wi/app/create_db.py')
        os.system('chown -R apache:apache /var/www/haproxy-wi/ && chown -R apache:apache /var/lib/roxy-wi/ && chown -R apache:apache /var/log/roxy-wi/ && chown -R apache:apache /etc/roxy-wi/ && chown apache:apache /usr/share/httpd/.* && echo "apache          ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers')


def haProxyRemove():
    os.system('rm -R /var/www/haproxy-wi/')
    os.system('rm -R /var/lib/roxy-wi/')
    os.system('rm -R /var/log/roxy-wi/')
    os.system('rm -R /etc/roxy-wi/')


while (True):
    print("1) Install HA-Proxy")
    print("2) Uninstall HA-Proxy")
    print("3) Clone repository")
    print("4) Install proxy")
    print("5) Run requirements.txt")
    print("6) Check Python Version")
    print("7) Check Java Version")
    print("8) Exit")

    selection = int(input("Enter Your Choice : "))

    if selection == 1:
        haProxyInstall()
    elif selection == 2:
        haProxyRemove()
    elif selection == 3:
        print("Cloning repository")
        os.system(
            'cd /var/www/ && git clone https://github.com/hap-wi/roxy-wi.git /var/www/haproxy-wi')
    elif selection == 4:
        os.system(' yum -y install fail2ban sshpass python3 python-pip python-devel python-cryptography python-jinja2 python-distro nmap-ncat net-tools lshw python-ldap python-paramiko rsync ansible dos2unix nmap mod_ssl httpd python-mod_wsgi libmodulemd python-psutil')
    elif selection == 5:
        os.system(
            'pip3 install matplotlib && pip3 install -r /var/www/haproxy-wi/config_other/requirements_el9.txt && pip3 install paramiko-ng')

    elif selection == 6:
        os.system('chmod +x /var/www/haproxy-wi/app/*.py && cp /var/www/haproxy-wi/config_other/logrotate/* /etc/logrotate.d/ && cp /var/www/haproxy-wi/config_other/fail2ban/filter.d/* /etc/fail2ban/filter.d/ && cp /var/www/haproxy-wi/config_other/fail2ban/jail.d/* /etc/fail2ban/jail.d/')

    elif selection == 7:
        os.system('mkdir /var/lib/roxy-wi/configs/hap_config/ -p && mkdir /var/lib/roxy-wi/configs/kp_config/ && mkdir /var/lib/roxy-wi/configs/nginx_config/ && mkdir /var/lib/roxy-wi/configs/apache_config/ && mkdir /var/log/roxy-wi/ && mkdir /etc/roxy-wi/ && mkdir /usr/share/httpd/.ansible && touch /usr/share/httpd/.ansible_galaxy && mkdir /usr/share/httpd/.ssh && mv haproxy-wi/roxy-wi.cfg /etc/roxy-wi')
        os.system('openssl req -newkey rsa:4096 -nodes -keyout /var/www/haproxy-wi/app/certs/haproxy-wi.key -x509 -days 10365 -out /var/www/haproxy-wi/app/certs/haproxy-wi.crt -subj "/C=US/ST=Almaty/L=Springfield/O=Roxy-WI/OU=IT/CN=*.roxy-wi.org/emailAddress=aidaho@roxy-wi.org"')
        os.system('systemctl daemon-reload && systemctl restart httpd && systemctl restart rsyslog && systemctl start fail2ban && systemctl enable fail2ban')
        os.system('python3 /var/www/haproxy-wi/app/create_db.py')
        os.system('chown -R apache:apache /var/www/haproxy-wi/ && chown -R apache:apache /var/lib/roxy-wi/ && chown -R apache:apache /var/log/roxy-wi/ && chown -R apache:apache /etc/roxy-wi/ && chown apache:apache /usr/share/httpd/.* && echo "apache          ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers')
    elif selection == 8:
        break
    else:
        print("Invalid Choice")


# [Roxy-WI]
# name = "Roxy-WI repo"
# baseurl = https://PushingStart:ZmNhZjEyYmFlMjI@repo.roxy-wi.org/el9/
# enabled = 1
# gpgcheck = 1
# gpgkey = file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Roxi-WI


# MariaDB [(none)]> create user 'roxy-wi'@'%';
# MariaDB [(none)]> create database roxywi;
# MariaDB [(none)]> grant all on roxywi.* to 'roxy-wi'@'%' IDENTIFIED BY 'roxy-wi';
# MariaDB [(none)]> grant all on roxywi.* to 'roxy-wi'@'localhost' IDENTIFIED BY 'roxy-wi';
