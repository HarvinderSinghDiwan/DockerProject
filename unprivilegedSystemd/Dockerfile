FROM         fedora:24
ENV container docker
RUN dnf -y install httpd; dnf clean all; systemctl enable httpd
STOPSIGNAL SIGRTMIN+3
EXPOSE 80
CMD [ "/sbin/init" ]
