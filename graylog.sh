sudo dnf -y install java-11-openjdk-devel epel-release 
sudo dnf update
sudo dnf install -y pwgen

cat <<EOF | sudo tee /etc/yum.repos.d/elasticsearch.repo
[elasticsearch-7.x]
name=Elasticsearch repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
EOF


update-crypto-policies --set LEGACY
sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
update-crypto-policies --set DEFAULT

sudo dnf install -y elasticsearch

sudo vi /etc/elasticsearch/elasticsearch.yml
cluster.name:  graylog
action.auto_create_index: false

sudo systemctl daemon-reload
sudo systemctl enable --now elasticsearch.service 

cat <<EOF | sudo tee /etc/yum.repos.d/mongodb-org-4.repo
[mongodb-org-4]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/8/mongodb-org/4.4/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-4.4.asc
EOF

sudo dnf install -y mongodb-org
sudo systemctl enable --now mongod

sudo rpm -Uvh https://packages.graylog2.org/repo/packages/graylog-4.2-repository_latest.rpm
sudo dnf install -y graylog-server

sudo pwgen -N 1 -s 96
echo -n "Enter Password: " && head -1 </dev/stdin | tr -d '\n' | sha256sum | cut -d" " -f1
nano  /etc/graylog/server/server.conf


sudo systemctl daemon-reload
sudo systemctl start graylog-server
sudo systemctl enable graylog-server
