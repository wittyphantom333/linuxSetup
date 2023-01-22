dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
dnf remove podman buildah
dnf install docker-ce docker-ce-cli containerd.io
systemctl start docker.service
systemctl enable docker.service
usermod -a -G docker $USER
yum install pip
pip install docker-compose
