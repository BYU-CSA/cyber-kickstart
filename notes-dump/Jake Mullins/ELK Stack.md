# Filebeat
Elastic Co., part of the Elastic beats [group of shippers](https://github.com/elastic/beats/tree/master). Seems like it's the best choice for SIEM stuff, with another candidate being Packetbeat.

Used to centralize/forward logs + files.

[logz.io](https://logz.io/blog/filebeat-vs-logstash/) says that Filebeat is often replaced with [Fluentd and FluentBit](https://logz.io/blog/fluentd-vs-fluent-bit/). However, for the application I'm working on, the common consensus is that Filebeat is good for raw logs, and fluent is good for actual analytics, like the role filled by metricbeats.

# ElasticSearch
Ingest pipelines let you perform some common transformations on your data before [indexing](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html), like removing fields, extract values from text, and enriching your data (whatever that means).

# Elastic Agent
A single binary that does all the bits from Filebeats. It's not exactly a drop-in replacement for all the beats yet, but that will probably change as the software matures. There is chatter about Elastic intending to replace all of beats with the Elastic Agent.

The indices produced by the data collected from Elastic Agents are more granular than a typical Beats/APM (performance) server feed.

A single unified way to monitor for logs, metrics, and other data on a host. It can also forward data, query data from OS, and protect from security threats.
![[images/Pasted image 20240701164456.png]]

From what I can gather, it outwardly looks like a full ElasticSearch instance, and thus can take info streams from wherever a typical ElasticSearch instance can. Thus it has a very robust Integration ecosystem. Each integration is tied to an Elastic Agent policy. Kibana Fleet, the management software is "API-first", thus it's easy to integrate with the [API](https://www.elastic.co/guide/en/fleet/8.14/fleet-api-docs.html). Kibana Fleet provides a nice UI to manage individual agents and integrations. 

Can be pretty easily deployed with Docker/Kubernetes. In `elastic/elastic-agent` container. Not exactly easy to find. I pulled `elastic/elastic-agent:8.14.1`

# Fleet
Fleet can assign policies to agents. As far as I can tell, it's kinda sorta like AD groups, not AD policies.

# Logstash
L in ELK stack. Logstash is used to aggregate logs top send to Elastic.

According to [this](https://github.com/elastic/beats/tree/master) StackOverflow, even if you have a few different beat instances running, you don't want them to have different connections open to Elastic because it decreases performance. Typically you put Logstash between them.

[logz.io](https://logz.io/blog/filebeat-vs-logstash/) says that Logstash is actually rarely used nowadays.
