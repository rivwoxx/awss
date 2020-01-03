FROM archlinux:latest

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

RUN pacman -Syu 

RUN pacman -S speedtest-cli



ENTRYPOINT [speedtest]
