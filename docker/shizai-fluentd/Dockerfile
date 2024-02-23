FROM fluentd:v1.16.2-1.1

USER root

RUN gem install fluent-plugin-rewrite-tag-filter

ADD docker-entrypoint.sh /var/tmp/docker-entrypoint.sh
RUN chmod 777 /var/tmp/docker-entrypoint.sh

# EXPOSE 24224

# ENTRYPOINT ["/var/tmp/docker-entrypoint.sh"]

CMD exec fluentd -c /fluentd/enc/fluent.conf
