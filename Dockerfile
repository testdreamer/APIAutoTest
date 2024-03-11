FROM 13724288994/python-ud:3.8.13  AS builder
# 设置默认时区为上海
ENV TZ Asia/Shanghai
WORKDIR /tmp
COPY ./ ./
RUN  python runMain_udaam.py



#report
FROM nginx:1.15.0-alpine AS report_packages
# 设置默认时区为上海
ENV TZ Asia/Shanghai
COPY --from=builder /tmp/*.html /usr/share/nginx/html/index.html


VOLUME /data
EXPOSE 80
